from behave import given, when, then


@given("a synced and ticking clock")
def step_given_synced_ticking_clock(context):
    raise NotImplementedError("Step not yet implemented")


@when("the parent board requests data over I2C")
def step_when_parent_requests_i2c(context):
    raise NotImplementedError("Step not yet implemented")


@then("the clock should respond with the current Unix timestamp")
def step_then_clock_responds_with_unix_timestamp(context):
    raise NotImplementedError("Step not yet implemented")


@given("a clock with light show slot {slot:d} active")
def step_given_clock_with_light_show_slot(context, slot):
    raise NotImplementedError("Step not yet implemented")


@then("the clock should respond with light show slot {slot:d}")
def step_then_clock_responds_with_slot(context, slot):
    raise NotImplementedError("Step not yet implemented")


@given("a clock receiving a light show slot assignment")
def step_given_clock_receiving_slot_assignment(context):
    raise NotImplementedError("Step not yet implemented")


@when("the slot value is outside the range of 0 to 255")
def step_when_slot_out_of_range(context):
    raise NotImplementedError("Step not yet implemented")


@then("the clock should reject the assignment")
def step_then_clock_rejects_assignment(context):
    raise NotImplementedError("Step not yet implemented")


@then("retain the previous valid slot value")
def step_then_clock_retains_previous_slot(context):
    raise NotImplementedError("Step not yet implemented")
