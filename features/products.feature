
Feature: Products API

Scenario: Read product
  Given a product exists
  When I request the product
  Then I should receive the product

Scenario: Update product
  When I update a product
  Then product should be updated

Scenario: Delete product
  When I delete a product
  Then product should be removed

Scenario: List all products
  When I request all products
  Then I should see product list

Scenario: Search by category
  When I search by category
  Then matching products are returned

Scenario: Search by availability
  When I search by availability
  Then available products are returned

Scenario: Search by name
  When I search by name
  Then matching product is returned
