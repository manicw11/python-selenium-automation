# Created by manic at 11/9/2023
Feature: Verification tests
  # Enter feature description here

  Scenario: Verify empty cart presence
      Given Open target main page
      When Click on cart icon
      Then Verify cart is empty message shown


  Scenario: Verify Sign in
      Given Open target main page
      When Click on Sign In
      When Click on Menu Sign In
      Then Verify Sign In page opens


  Scenario: Verify Product in Cart
    Given Open Target main page
    When Search for Air Fryer
    And Add product to cart
    Then Verify Air Fryer in cart


  Scenario: Verify Benefit Boxes
    Given Open Target Circle page
    Then Verify 5 Benefit Boxes are present