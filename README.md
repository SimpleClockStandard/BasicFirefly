# BasicFirefly — Smarter Clock Standard

> *Inspired by Destin Sandlin / SmarterEveryDay and his video on firefly synchronization. We're doing that. But with clocks. Indoors. At conferences. No GPS.*

---

## What is this thing

It's a clock. A really good one. 2 cm × 2 cm, backup battery, and one job: **keep accurate time to within 1 ms and tell its parent board about it over I2C**.

That's it. That's the whole product.

The fanciest thing this clock does is expose a 13-byte I2C response. It does not run a web server. It does not do OTA updates. It is not a microcontroller platform. It is a clock. A very disciplined, very paranoid clock that was born at the factory with a set time and has been ticking ever since.

The magic is that 500 of these can be in the same room and every single one of them is ticking on the same millisecond - passively, with zero configuration - because they all trust the same authenticated radio signal from the same factory-provisioned source of truth.

Think windmill farms in NorCal at night, all pulsing in unison because they're GPS-locked. That's the vibe. Except we can't use GPS indoors (attenuation, multipath, crowding - you're not getting ms accuracy across hundreds of devices that way). So we built our own.

---

## The one-line pitch

> A firefly, already programmed, that blinks every minute in time with every other firefly in the room.

---

## Hardware

| Part | What | Why |
|---|---|---|
| TI CC1352R | Radio MCU | The radio and the brains. Sub-GHz LF radio for the beacon protocol. Datasheets in `datasheets/cc1352r/`. |
| Micro Crystal RV-3028-C7 | RTC | Extremely low drift, backup battery support, I2C native. Datasheet in `datasheets/rv3028c7/`. |

The RTC is the clock. The MCU is the manager. They have a strict relationship: **the MCU reads the RTC, it does not write to it. Ever. After birth, the RTC registers are locked.**

---

## Device Roles

There are four roles a device can be in at any moment:

| Role | Broadcasts | Listens to |
|---|---|---|
| **Grandfather Clock (GC)** | Always, signed with factory key | Peer GCs only |
| **Step-Grandfather Clock** | While promoted, signed | GC (always first) |
| **NAClock w/ parent board** | Never | GC or Step-GC |
| **NAClock w/o parent board** | Never | GC or Step-GC, then deep sleep |

The hierarchy is simple: GCs are the source of truth. NAClocks listen. If a NAClock with a parent board hasn't heard a GC in too long, it promotes itself to Step-GC and keeps the chain alive until a real GC comes back — at which point it immediately stands down. No ego.

A NAClock without a parent board never promotes. Nobody's listening to it anyway. It just deep sleeps and waits.

---

## The Birth

Every device is born at the factory. A Birth Jig — a standalone external computer with a traceable time source — connects directly to the RTC chip via dedicated PCB pads (bypassing the MCU entirely), sets the time once, and locks it:

1. MCU is held in reset so it can't interfere with the I2C bus
2. RTC time registers are written directly by the Birth Jig
3. Written value is read back and verified (≤ 50 ms tolerance)
4. HMAC factory key and provisioning data are flashed to the MCU via JTAG/SWD
5. Debug interface (JTAG/SWD) is locked at the highest irreversible protection level
6. RTC write protection is engaged — requires manufacturer credential to undo
7. MCU reset is released

After step 6, **nobody can reset that RTC**. Not the MCU, not a curious engineer with a debugger, not someone who stole a device. The write-protection credential lives only on authorized Birth Jig systems.

The MCU firmware does not contain any code path that writes to RTC time registers. This is audited before production. Presence of such a routine is a production stop condition.

---

## Drift and Trust

RTC crystals drift. That's fine — we budget for it. The RV-3028-C7 drifts at most ~3 seconds per year (check the datasheet for exact figures). So if a device has been offline for N years, the most it could have drifted is `N × 3 seconds`.

When a device receives a beacon:
- `delta = abs(received_time - local_rtc_time)`
- If `delta ≤ N × MAX_DRIFT_RATE`: trust it, update the Drift Offset, go back to sleep
- If `delta > N × MAX_DRIFT_RATE`: **enter Dead State immediately**

Dead State is permanent. No retry, no grace period, no operator override in the field. A device that can't be trusted is a device that must not operate. Factory re-provisioning only.

Critically: **we never write to the RTC register**. All correction is accumulated in a non-volatile Drift Offset field. The birth-set RTC is the immutable baseline, forever.

---

## I2C Interface (13 bytes)

The parent board is I2C master. The clock is I2C slave. The clock never initiates.

```
Field 1: Unix timestamp     (uint32, seconds)
Field 2: Light show slot    (uint8, 0–255)
Field 3: BPM                (uint8, 0–255)
Field 4: Beat Modulus       (uint16, prime, 257–65521)
Field 5: Beat phase         (uint8, unix_time_seconds mod Beat_Modulus)
Field 6: Drift Offset       (int16, milliseconds)
Field 7: Status byte        (bit 0: synced, bit 1: dead, bits 2–7: reserved=0)
```

The light show slot and BPM are how the clock coordinates visual behavior across the room. 255 operator-defined patterns available. The parent board drives its own output based on whatever slot the clock is reporting — the clock doesn't know or care what the pattern looks like, it just keeps the slot in sync.

There's also an optional TICK pin — pulses HIGH for 1 ms at every RTC second boundary — so parent boards that want tight timestamp accuracy can interrupt on it instead of polling.

---

## LED Behavior

One LED, onboard. Fades up and down once per 60-second period. Phase derived from `unix_time mod 60`. On re-sync, the phase snaps hard to the corrected time. No smoothing, no interpolation — just snap.

This is the firefly. 500 of them in a room, all fading in and out on the same second. Zero configuration. Zero coordination at runtime. Just math on a shared clock.

---

## The WAG (Wildly Ambitious Goal)

Section 13 of the RFC describes synchronized PWM duty cycle across devices using a raised cosine waveform derived from the same `t_eff_ms` all devices share. Non-normative. Not required for base compliance. Probably version 4 or 5 material — you'd need either a POT onboard or an AutoPOT to tune carrier frequency, which is out of scope for v1. But the math is in the RFC and it's beautiful.

---

## Security Model (summary)

- Beacons are HMAC-SHA-256 authenticated minimum. Unsigned beacons are silently discarded.
- Secure Boot is enabled. You can't extract the key by replacing firmware.
- JTAG/SWD debug interfaces are locked post-provisioning at the highest irreversible level.
- RTC write protection is credential-gated and lives only on authorized Birth Jig systems.
- The drift trust window bounds time-injection attacks: you can't shift a device's clock by more than its accumulated drift envelope without killing it.
- Dead State is the security boundary of last resort. A compromised clock is a dead clock.

---

## Repo Structure

```
RFC-XXXX-clock-sync-protocol.md   ← The full protocol spec (LFRTS/1.0)
clock_outline.md                  ← Original design outline / working notes
datasheets/
  cc1352r/
    cc1352r.pdf                   ← TI CC1352R datasheet
    swra651.pdf                   ← TI CC1352R application note
  rv3028c7/
    RV-3028-C7_App-Manual.pdf     ← RV-3028-C7 application manual
tests/
  behave/
    features/                     ← Behave BDD feature files (stubs, need filling out)
      drift_tolerance.feature
      leader_election.feature
      radio_time_sync.feature
      rtc_initialization.feature
      secure_boot.feature
      i2c_communication.feature.rsls
      led_sync.feature.rsls
    features/steps/               ← Step implementations (stubs)
README.old.md                     ← Previous README, kept for reference
```

---

## What's Left To Do

- [ ] **Fill in the Behave test stubs** — every `.feature` file is currently empty. This is the most urgent gap between the RFC and something shippable.
- [ ] **RTC chip confirmation** — the RFC says "Alex Chosen Chip" in places. RV-3028-C7 is the working assumption. Confirm and lock in.
- [ ] **Radio protocol detail** — the RFC defines the beacon payload and authentication requirements but does not specify the wire format, channel, modulation scheme, or CC1352R register config. That's a necessary artifact before firmware.
- [ ] **Birth Jig implementation** — the provisioning process is fully specced in RFC §12 but the Birth Jig software does not exist yet.
- [ ] **Step-GC authentication gap** — RFC §6 mandates HMAC on GC beacons but doesn't explicitly require Step-GC beacons to be signed. The intent is clear from §10 but the normative language needs tightening.
- [ ] **`clock_outline.md` drift rule discrepancy** — the outline says a device waits for a signal it can trust if delta is too large; the RFC says it enters Dead State immediately. The RFC wins. The outline should be updated or retired.

---

## Dev Environment

**PlatformIO** is the primary IDE. See the CC1352R datasheets in `datasheets/cc1352r/` for register maps and radio configuration reference.
