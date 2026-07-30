---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budget-expressiondimensionvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::Budget ExpressionDimensionValues
<a name="aws-properties-budgets-budget-expressiondimensionvalues"></a>

Contains the specifications for the filters to use for your request.

## Syntax
<a name="aws-properties-budgets-budget-expressiondimensionvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budget-expressiondimensionvalues-syntax.json"></a>

```
{
  "[Key](#cfn-budgets-budget-expressiondimensionvalues-key)" : {{String}},
  "[MatchOptions](#cfn-budgets-budget-expressiondimensionvalues-matchoptions)" : {{[ String, ... ]}},
  "[Values](#cfn-budgets-budget-expressiondimensionvalues-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-budgets-budget-expressiondimensionvalues-syntax.yaml"></a>

```
  [Key](#cfn-budgets-budget-expressiondimensionvalues-key): {{String}}
  [MatchOptions](#cfn-budgets-budget-expressiondimensionvalues-matchoptions): {{
    - String}}
  [Values](#cfn-budgets-budget-expressiondimensionvalues-values): {{
    - String}}
```

## Properties
<a name="aws-properties-budgets-budget-expressiondimensionvalues-properties"></a>

`Key`  <a name="cfn-budgets-budget-expressiondimensionvalues-key"></a>
The name of the dimension that you want to filter on.
*Required*: No
*Type*: String
*Allowed values*: `AZ | INSTANCE_TYPE | LINKED_ACCOUNT | LINKED_ACCOUNT_NAME | OPERATION | PURCHASE_TYPE | REGION | SERVICE | SERVICE_CODE | USAGE_TYPE | USAGE_TYPE_GROUP | RECORD_TYPE | OPERATING_SYSTEM | TENANCY | SCOPE | PLATFORM | SUBSCRIPTION_ID | LEGAL_ENTITY_NAME | INVOICING_ENTITY | DEPLOYMENT_OPTION | DATABASE_ENGINE | CACHE_ENGINE | INSTANCE_TYPE_FAMILY | BILLING_ENTITY | RESERVATION_ID | RESOURCE_ID | RIGHTSIZING_TYPE | SAVINGS_PLANS_TYPE | SAVINGS_PLAN_ARN | PAYMENT_OPTION | RESERVATION_MODIFIED | TAG_KEY | COST_CATEGORY_NAME`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchOptions`  <a name="cfn-budgets-budget-expressiondimensionvalues-matchoptions"></a>
The match options that you can use to filter your results. You can specify only one of these values in the array.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-budgets-budget-expressiondimensionvalues-values"></a>
The metadata values you can specify to filter upon, so that the results all match at least one of the specified values.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
