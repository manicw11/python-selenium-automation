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