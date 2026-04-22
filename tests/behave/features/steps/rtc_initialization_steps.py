from behave import given, when, then


@given("a new unprogrammed clock")
def step_given_new_unprogrammed_clock(context):
    raise NotImplementedError("Step not yet implemented")


@when("the clock undergoes the birth process")
def step_when_clock_undergoes_birth_process(context):
    raise NotImplementedError("Step not yet implemented")


@then("the RTC should be set to the current Unix time")
def step_then_rtc_set_to_unix_time(context):
    raise NotImplementedError("Step not yet implemented")


@then("the RTC should begin ticking")
def step_then_rtc_begins_ticking(context):
    raise NotImplementedError("Step not yet implemented")


@given("a clock that has already been initialized")
def step_given_clock_already_initialized(context):
    raise NotImplementedError("Step not yet implemented")


@when("the clock powers on")
def step_when_clock_powers_on(context):
    raise NotImplementedError("Step not yet implemented")


@then("the RTC should retain its previously set time")
def step_then_rtc_retains_time(context):
    raise NotImplementedError("Step not yet implemented")


@then("the birth process should not run again")
def step_then_birth_process_not_repeated(context):
    raise NotImplementedError("Step not yet implemented")
