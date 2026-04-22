Feature: Radio Time Synchronization
  As a clock owner
  I want my clock to receive time pulses from an authoritative source
  So that all clocks remain in millisecond-level lockstep

  Scenario: Clock syncs to authoritative time leader
    Given a clock that is ticking independently
    And an authenticated authoritative time source is broadcasting
    When the clock receives a valid time pulse
    Then the clock should snap its tick to match the authoritative time
    And the offset should be within 1 millisecond

  Scenario: Clock ignores unauthenticated time broadcasts
    Given a clock that is ticking independently
    And an unauthenticated device is broadcasting time
    When the clock receives the unauthenticated time pulse
    Then the clock should ignore the broadcast
    And continue ticking at its current time

  Scenario: 500 clocks sync within tolerance
    Given 500 initialized clocks in range of an authoritative time source
    When the authoritative source broadcasts a sync pulse
    Then all 500 clocks should be within 1 millisecond of each other
