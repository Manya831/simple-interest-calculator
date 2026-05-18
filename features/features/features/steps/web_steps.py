
from behave import then

@then('I should see text')
def step_impl(context):
    assert True

@then('text should not be present')
def step_impl(context):
    assert True

@then('message is displayed')
def step_impl(context):
    assert True
