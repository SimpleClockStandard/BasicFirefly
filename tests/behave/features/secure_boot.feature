Feature: Secure Boot
  As a manufacturer
  I want the firmware to be protected from unauthorized access
  So that our code cannot be extracted or cloned

  Scenario: Device boots with verified firmware
    Given a clock with signed firmware installed
    When the device powers on
    Then secure boot should verify the firmware signature
    And the device should proceed to normal operation

  Scenario: Device refuses to boot with tampered firmware
    Given a clock with modified unsigned firmware
    When the device powers on
    Then secure boot should detect the invalid signature
    And the device should halt and not execute the firmware
