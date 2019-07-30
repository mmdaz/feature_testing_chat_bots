from unittest.mock import Mock

from behave import given, when, then
from bot.test_controller import TestController


@given('a bot and update from server')
def step_impl(context):
    context.bot = Mock()
    context.update = Mock()
    context.dispatcher = Mock()
    # context.dbhandler = Mock()
    # context.dbhandler.add_user.return_value = context.user
    context.test_controller = TestController(dispatcher=context.dispatcher)


@when('user send /start')
def step_impl(context):
    context.first_step = context.test_controller.main_menu(context.bot, context.update)


@then('send main menu')
def step_impl(context):
    assert context.first_step == context.test_controller.states_dict["step_1"]


@then('user send me text')
def step_impl(context):
    context.second_state = context.test_controller.first_step(context.bot, context.update)


@then('bot send user text')
def step_impl(context):
    assert context.second_state == context.test_controller.states_dict["step_2"]
