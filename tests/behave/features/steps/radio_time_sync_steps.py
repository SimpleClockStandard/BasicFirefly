from behave import given, when, then


@given("a clock that is ticking independently")
def step_given_clock_ticking_independently(context):
    raise NotImplementedError("Step not yet implemented")


@given("an authenticated authoritative time source is broadcasting")
def step_given_authenticated_source_broadcasting(context):
    raise NotImplementedError("Step not yet implemented")


@when("the clock receives a valid time pulse")
def step_when_clock_receives_valid_pulse(context):
    raise NotImplementedError("Step not yet implemented")


@then("the clock should snap its tick to match the authoritative time")
def step_then_clock_snaps_to_authoritative_time(context):
    raise NotImplementedError("Step not yet implemented")


@then("the offset should be within 1 millisecond")
def step_then_offset_within_1ms(context):
    raise NotImplementedError("Step not yet implemented")


@given("an unauthenticated device is broadcasting time")
def step_given_unauthenticated_device_broadcasting(context):
    raise NotImplementedError("Step not yet implemented")


@when("the clock receives the unauthenticated time pulse")
def step_when_clock_receives_unauthenticated_pulse(context):
    raise NotImplementedError("Step not yet implemented")


@then("the clock should ignore the broadcast")
def step_then_clock_ignores_broadcast(context):
    raise NotImplementedError("Step not yet implemented")


@then("continue ticking at its current time")
def step_then_clock_continues_at_current_time(context):
    raise NotImplementedError("Step not yet implemented")


@given("{count:d} initialized clocks in range of an authoritative time source")
def step_given_n_clocks_in_range(context, count):
    raise NotImplementedError("Step not yet implemented")


@when("the authoritative source broadcasts a sync pulse")
def step_when_authoritative_source_broadcasts(context):
    raise NotImplementedError("Step not yet implemented")


@then("all {count:d} clocks should be within 1 millisecond of each other")
def step_then_all_clocks_within_1ms(context, count):
    raise NotImplementedError("Step not yet implemented")
