from behave import given, when, then


@given("a clock with signed firmware installed")
def step_given_signed_firmware(context):
    raise NotImplementedError("Step not yet implemented")


@when("the device powers on")
def step_when_device_powers_on(context):
    raise NotImplementedError("Step not yet implemented")


@then("secure boot should verify the firmware signature")
def step_then_secure_boot_verifies_signature(context):
    raise NotImplementedError("Step not yet implemented")


@then("the device should proceed to normal operation")
def step_then_device_proceeds_normally(context):
    raise NotImplementedError("Step not yet implemented")


@given("a clock with modified unsigned firmware")
def step_given_unsigned_firmware(context):
    raise NotImplementedError("Step not yet implemented")


@then("secure boot should detect the invalid signature")
def step_then_secure_boot_detects_invalid_signature(context):
    raise NotImplementedError("Step not yet implemented")


@then("the device should halt and not execute the firmware")
def step_then_device_halts(context):
    raise NotImplementedError("Step not yet implemented")
