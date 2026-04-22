Feature: RTC Drift Management
  As a clock operator
  I want drift to be within acceptable bounds before re-sync
  So that clocks remain useful even without radio contact

  # Drift is bounded at +/- 3 seconds per year. A clock offline for N years
  # may have drifted up to N * 3 seconds in either direction.
  # Clocks within that window are accepted and snapped. Clocks outside it
  # are rejected as untrustworthy.

  Scenario Outline: Clock drift stays within spec after <years> year(s) without sync
    Given a clock initialized with accurate time
    And no radio sync pulses are received
    When <years> year(s) of simulated time elapses
    Then the RTC drift should be no more than <max_drift_seconds> seconds in either direction

    Examples:
      | years | max_drift_seconds |
      | 1     | 3                 |
      | 2     | 6                 |
      | 5     | 15                |

  Scenario Outline: Clock re-syncs correctly after being offline for <years> year(s)
    Given a clock that has drifted <drift_seconds> seconds from true time
    And the drift is within the expected window of <years> year(s)
    When a valid beacon sync pulse is received
    Then the clock should correct to within 1 millisecond of true time
    And the clock should be marked as trusted

    Examples:
      | years | drift_seconds |
      | 1     | 2             |
      | 2     | 5             |
      | 5     | 14            |

  Scenario Outline: Clock with drift exceeding the <years>-year window is rejected
    Given a clock that has drifted <drift_seconds> seconds from true time
    And the drift exceeds the expected window of <years> year(s)
    When a valid beacon sync pulse is received
    Then the clock should be rejected as untrustworthy
    And the beacon should not snap to the drifted clock's time

    Examples:
      | years | drift_seconds |
      | 1     | 4             |
      | 2     | 7             |
      | 5     | 16            |

  Scenario: Beacon pulse corrects a clock drifted fast (positive)
    Given a clock that has drifted +2 seconds from true time
    When a valid beacon sync pulse is received
    Then the clock should correct to within 1 millisecond of true time

  Scenario: Beacon pulse corrects a clock drifted slow (negative)
    Given a clock that has drifted -2 seconds from true time
    When a valid beacon sync pulse is received
    Then the clock should correct to within 1 millisecond of true time
