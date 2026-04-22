Feature: RTC Initialization at Birth
  As a manufacturer
  I want each clock to have its RTC set at the factory
  So that it starts with accurate time from the moment it powers on

  Scenario: Clock sets RTC on first boot
    Given a new unprogrammed clock
    When the clock undergoes the birth process
    Then the RTC should be set to the current Unix time
    And the RTC should begin ticking

  Scenario: Clock does not re-run birth process on subsequent boots
    Given a clock that has already been initialized
    When the clock powers on
    Then the RTC should retain its previously set time
    And the birth process should not run again
