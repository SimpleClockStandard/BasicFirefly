Define: Grandfather Clock: authoritative clock
Define: NAClock: Non-authoritative clock

For ALL scenarios: I NEVER reset my RTC from the factory.

Cycle of waking: NAClock WITH a parent board
1. I wake up on my interval. Because I have a parent board, I wake up MORE OFTEN than a standalone clock.
2. I listen for a Grandfather Clock.
   1. If I hear a Grandfather Clock, I check my drift and apply my offset if I have drifted more than the tested drift allowance variable. Done. Go back to sleep.
   2. If I DO NOT hear a Grandfather Clock, I go back to sleep for a short RAND amt of time and listen again.
      1. If I hear a Grandfather Clock on the retry, I set my clock accordingly and finish processing from step 2.1.
      2. If I STILL do not hear a Grandfather Clock, I promote myself to Step-Grandfather Clock and begin broadcasting. Go to "Cycle of waking: Step-Grandfather Clock" below.

Cycle of waking: NAClock WITHOUT a parent board (or parent board not providing 3.3v)
1. I wake up on my interval.
2. I listen for a Grandfather Clock.
   1. If I hear a Grandfather Clock, I check my drift and apply my offset if I have drifted more than the tested drift allowance variable. Done. Go back to sleep.
   2. If I DO NOT hear a Grandfather Clock, I go back to sleep for a short RAND amt of time and listen again.
      1. If I hear a Grandfather Clock on the retry, I set my clock accordingly and finish processing from step 2.1.
      2. If I STILL do not hear a Grandfather Clock, I go back to DEEP SLEEP. I do NOT broadcast. I have no parent board, so no one is listening to me anyway.

Cycle of waking: Step-Grandfather Clock (NAClock WITH parent, promoted)
1. I wake up. The FIRST thing I do is listen for a true Grandfather Clock.
   1. If I hear a Grandfather Clock, I IMMEDIATELY stop broadcasting, snap to its time, demote myself back to NAClock WITH parent, and go back to sleep.
   2. If I do NOT hear a Grandfather Clock, I broadcast my current time and go back to sleep. I will check again next wake.

Cycle of waking for a Grandfather Clock (authoritative clock)
1. I wake up and I broadcast my current time, signed so other clocks know I am authoritative.
2. I go back to sleep. That's it. I am the source of truth. I do not listen. I do not drift-check. I just broadcast.

Drift rules for ALL clocks
1. I know I drift at most +/- 3 seconds per year. So if I have been offline for N years, the most I could have drifted is N * 3 seconds.
2. When I receive a sync signal, I calculate my delta against the received time.
   1. If abs(delta) <= N * 3 seconds: I trust it. I snap. I update my offset.
   2. If abs(delta) > N * 3 seconds: I do NOT trust it. I do not update. I do not broadcast. I wait for a signal I CAN trust.

I2C behavior (when connected to a parent board)
1. THE PARENT ASKS ME. I do not push. I respond to I2C reads.
2. I always respond with two things: current Unix timestamp, and current light show slot (0-255).
3. If I am not yet synced, I still report my local RTC time and I flag it as unsynced in the response.
4. If I receive a light show slot outside of 0-255, I throw it away and keep the last valid one.

LED behavior
1. My LED fades up and fades down once per minute, locked to the top of the minute from my RTC.
2. If I re-sync and my time jumps, my LED phase jumps with it immediately. No smoothing. Hard snap.
