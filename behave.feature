Feature: send final message
  Scenario: test scenario
    Given a bot and update from server
    When user send /start
    Then send main menu
    And user send me text
    And bot send user text

