from behave import given, when, then


@given("a clock that has not received an authoritative sync pulse")
def step_given_clock_no_sync_pulse(context):
    raise NotImplementedError("Step not yet implemented")


@given("no other leader is present in radio range")
def step_given_no_leader_in_range(context):
    raise NotImplementedError("Step not yet implemented")


@when("the timeout threshold elapses")
def step_when_timeout_elapses(context):
    raise NotImplementedError("Step not yet implemented")


@then("the clock should promote itself to a local leader")
def step_then_clock_promotes_to_leader(context):
    raise NotImplementedError("Step not yet implemented")


@then("begin broadcasting time pulses")
def step_then_clock_begins_broadcasting(context):
    raise NotImplementedError("Step not yet implemented")


@given("a self-promoted leader clock")
def step_given_self_promoted_leader(context):
    raise NotImplementedError("Step not yet implemented")


@when("an authenticated authoritative time source comes into radio range")
def step_when_authoritative_source_in_range(context):
    raise NotImplementedError("Step not yet implemented")


@then("the clock should demote itself from leader")
def step_then_clock_demotes_from_leader(context):
    raise NotImplementedError("Step not yet implemented")


@given("a clock following a self-promoted leader")
def step_given_clock_following_self_promoted_leader(context):
    raise NotImplementedError("Step not yet implemented")


@then("the self-promoted leader should also snap and demote")
def step_then_self_promoted_leader_snaps_and_demotes(context):
    raise NotImplementedError("Step not yet implemented")
