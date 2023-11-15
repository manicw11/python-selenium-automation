# Created by manic at 11/14/2023
Feature: Verify Product in Cart
  # Enter feature description here

  Scenario: Verify Product in Cart
    Given Open Target main page
    When Search for air fryer
    And Add air fryer to cart
    Then Verify air fryer in cart