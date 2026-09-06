---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-budgets-budget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::Budget
<a name="aws-resource-budgets-budget"></a>

The `AWS::Budgets::Budget` resource allows customers to take pre-defined actions that will trigger once a budget threshold has been exceeded. creates, replaces, or deletes budgets for Billing and Cost Management. For more information, see [Managing Your Costs with Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html) in the *AWS Billing and Cost Management User Guide*.

## Syntax
<a name="aws-resource-budgets-budget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-budgets-budget-syntax.json"></a>

```
{
  "Type" : "AWS::Budgets::Budget",
  "Properties" : {
      "[Budget](#cfn-budgets-budget-budget)" : {{BudgetData}},
      "[NotificationsWithSubscribers](#cfn-budgets-budget-notificationswithsubscribers)" : {{[ NotificationWithSubscribers, ... ]}},
      "[ResourceTags](#cfn-budgets-budget-resourcetags)" : {{[ ResourceTag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-budgets-budget-syntax.yaml"></a>

```
Type: AWS::Budgets::Budget
Properties:
  [Budget](#cfn-budgets-budget-budget): {{
    BudgetData}}
  [NotificationsWithSubscribers](#cfn-budgets-budget-notificationswithsubscribers): {{
    - NotificationWithSubscribers}}
  [ResourceTags](#cfn-budgets-budget-resourcetags): {{
    - ResourceTag}}
```

## Properties
<a name="aws-resource-budgets-budget-properties"></a>

`Budget`  <a name="cfn-budgets-budget-budget"></a>
The budget object that you want to create.
*Required*: Yes
*Type*: [BudgetData](aws-properties-budgets-budget-budgetdata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationsWithSubscribers`  <a name="cfn-budgets-budget-notificationswithsubscribers"></a>
A notification that you want to associate with a budget. A budget can have up to five notifications, and each notification can have one SNS subscriber and up to 10 email subscribers. If you include notifications and subscribers in your `CreateBudget` call, AWS creates the notifications and subscribers for you.
*Required*: No
*Type*: Array of [NotificationWithSubscribers](aws-properties-budgets-budget-notificationwithsubscribers.md)
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceTags`  <a name="cfn-budgets-budget-resourcetags"></a>
An optional list of tags to associate with the specified budget. Each tag consists of a key and a value, and each key must be unique for the resource.
*Required*: No
*Type*: Array of [ResourceTag](aws-properties-budgets-budget-resourcetag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-budgets-budget-return-values"></a>

### Ref
<a name="aws-resource-budgets-budget-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the budget that is created by the template.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-budgets-budget-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

## Examples
<a name="aws-resource-budgets-budget--examples"></a>

### Budget for 100 USD with two notifications
<a name="aws-resource-budgets-budget--examples--Budget_for_100_USD_with_two_notifications"></a>

The following example creates a budget for 100 USD amount of costs, with notifications for when you have spent over 80 USD or over 99 USD. The notifications are sent to the subscribers `email@example.com` and `email2@example.com`.

#### JSON
<a name="aws-resource-budgets-budget--examples--Budget_for_100_USD_with_two_notifications--json"></a>

```
{
  "Description": "Basic Budget test",
  "Resources": {
    "Budget": {
      "Type": "AWS::Budgets::Budget",
      "Properties": {
        "Budget": {
          "BudgetLimit": {
            "Amount": "100",
            "Unit": "USD"
          },
          "TimeUnit": "MONTHLY",
          "TimePeriod": {
            "Start": "1225864800",
            "End": "1926864800"
          },
          "BudgetType": "COST",
          "CostFilters": {
            "AZ": [
              "us-east-1",
              "us-west-1",
              "us-east-2"
            ]
          }
        },
        "NotificationsWithSubscribers": [
          {
            "Notification": {
              "NotificationType": "ACTUAL",
              "ComparisonOperator": "GREATER_THAN",
              "Threshold": 99
            },
            "Subscribers": [
              {
                "SubscriptionType": "EMAIL",
                "Address": "email@example.com"
              },
              {
                "SubscriptionType": "EMAIL",
                "Address": "email2@example.com"
              }
            ]
          },
          {
            "Notification": {
              "NotificationType": "ACTUAL",
              "ComparisonOperator": "GREATER_THAN",
              "Threshold": 80
            },
            "Subscribers": [
              {
                "SubscriptionType": "EMAIL",
                "Address": "email@example.com"
              }
            ]
          }
        ]
      }
    }
  },
  "Outputs": {
    "BudgetId": {
      "Value": "BudgetExample"
    }
  }
}
```

#### YAML
<a name="aws-resource-budgets-budget--examples--Budget_for_100_USD_with_two_notifications--yaml"></a>

```
---
Description: "Basic Budget test"
Resources:
  BudgetExample:
    Type: "AWS::Budgets::Budget"
    Properties:
      Budget:
        BudgetLimit:
          Amount: 100
          Unit: USD
        TimeUnit: MONTHLY
        TimePeriod:
          Start: 1225864800
          End: 1926864800
        BudgetType: COST
        CostFilters:
          AZ:
            - us-east-1
            - us-west-1
            - us-east-2
      NotificationsWithSubscribers:
        - Notification:
            NotificationType: ACTUAL
            ComparisonOperator: GREATER_THAN
            Threshold: 99
          Subscribers:
            - SubscriptionType: EMAIL
              Address: email@example.com
            - SubscriptionType: EMAIL
              Address: email2@example.com
        - Notification:
            NotificationType: ACTUAL
            ComparisonOperator: GREATER_THAN
            Threshold: 80
          Subscribers:
          - SubscriptionType: EMAIL
            Address: email@example.com
Outputs:
  BudgetId:
    Value: !Ref BudgetExample
```

## See also
<a name="aws-resource-budgets-budget--seealso"></a>
+ [CreateBudget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateBudget.html) in the *AWS Cost Explorer Service Cost Management APIs*
