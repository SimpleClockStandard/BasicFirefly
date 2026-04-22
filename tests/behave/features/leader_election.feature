Feature: Leader Election and Promotion
  As a network of clocks
  I want clocks to self-promote to leader when no authority is present
  So that sync continues passively without a central source

  Scenario: Clock promotes itself to leader after timeout
    Given a clock that has not received an authoritative sync pulse
    And no other leader is present in radio range
    When the timeout threshold elapses
    Then the clock should promote itself to a local leader
    And begin broadcasting time pulses

  Scenario: Clock demotes itself when authoritative leader returns
    Given a self-promoted leader clock
    When an authenticated authoritative time source comes into radio range
    Then the clock should snap to the authoritative source's time
    And the clock should demote itself from leader

  Scenario: Follower snaps to leader when leader returns
    Given a clock following a self-promoted leader
    When an authenticated authoritative time source comes into radio range
    Then the clock should snap to the authoritative source's time
    And the self-promoted leader should also snap and demote
