---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budget-notification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::Budget Notification
<a name="aws-properties-budgets-budget-notification"></a>

A notification that's associated with a budget. A budget can have up to ten notifications.

Each notification must have at least one subscriber. A notification can have one SNS subscriber and up to 10 email subscribers, for a total of 11 subscribers.

For example, if you have a budget for 200 dollars and you want to be notified when you go over 160 dollars, create a notification with the following parameters:
+ A notificationType of `ACTUAL`
+ A `thresholdType` of `PERCENTAGE`
+ A `comparisonOperator` of `GREATER_THAN`
+ A notification `threshold` of `80`

## Syntax
<a name="aws-properties-budgets-budget-notification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budget-notification-syntax.json"></a>

```
{
  "[ComparisonOperator](#cfn-budgets-budget-notification-comparisonoperator)" : {{String}},
  "[NotificationType](#cfn-budgets-budget-notification-notificationtype)" : {{String}},
  "[Threshold](#cfn-budgets-budget-notification-threshold)" : {{Number}},
  "[ThresholdType](#cfn-budgets-budget-notification-thresholdtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-budgets-budget-notification-syntax.yaml"></a>

```
  [ComparisonOperator](#cfn-budgets-budget-notification-comparisonoperator): {{String}}
  [NotificationType](#cfn-budgets-budget-notification-notificationtype): {{String}}
  [Threshold](#cfn-budgets-budget-notification-threshold): {{Number}}
  [ThresholdType](#cfn-budgets-budget-notification-thresholdtype): {{String}}
```

## Properties
<a name="aws-properties-budgets-budget-notification-properties"></a>

`ComparisonOperator`  <a name="cfn-budgets-budget-notification-comparisonoperator"></a>
The comparison that's used for this notification.
*Required*: Yes
*Type*: String
*Allowed values*: `GREATER_THAN | LESS_THAN | EQUAL_TO`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NotificationType`  <a name="cfn-budgets-budget-notification-notificationtype"></a>
Specifies whether the notification is for how much you have spent (`ACTUAL`) or for how much that you're forecasted to spend (`FORECASTED`).
*Required*: Yes
*Type*: String
*Allowed values*: `ACTUAL | FORECASTED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Threshold`  <a name="cfn-budgets-budget-notification-threshold"></a>
The threshold that's associated with a notification. Thresholds are always a percentage, and many customers find value being alerted between 50% - 200% of the budgeted amount. The maximum limit for your threshold is 1,000,000% above the budgeted amount.
*Required*: Yes
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ThresholdType`  <a name="cfn-budgets-budget-notification-thresholdtype"></a>
The type of threshold for a notification. For `ABSOLUTE_VALUE` thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For `PERCENTAGE` thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a `PERCENTAGE` threshold of 80%, AWS notifies you when you go over 160 dollars.
*Required*: No
*Type*: String
*Allowed values*: `PERCENTAGE | ABSOLUTE_VALUE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-budgets-budget-notification--seealso"></a>
+ [Notification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Notification.html) in the *AWS Cost Explorer Service Cost Management APIs*
