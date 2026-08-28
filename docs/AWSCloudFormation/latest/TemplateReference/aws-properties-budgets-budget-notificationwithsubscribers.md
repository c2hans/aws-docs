---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budget-notificationwithsubscribers.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::Budget NotificationWithSubscribers
<a name="aws-properties-budgets-budget-notificationwithsubscribers"></a>

A notification with subscribers. A notification can have one SNS subscriber and up to 10 email subscribers, for a total of 11 subscribers.

## Syntax
<a name="aws-properties-budgets-budget-notificationwithsubscribers-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budget-notificationwithsubscribers-syntax.json"></a>

```
{
  "[Notification](#cfn-budgets-budget-notificationwithsubscribers-notification)" : {{Notification}},
  "[Subscribers](#cfn-budgets-budget-notificationwithsubscribers-subscribers)" : {{[ Subscriber, ... ]}}
}
```

### YAML
<a name="aws-properties-budgets-budget-notificationwithsubscribers-syntax.yaml"></a>

```
  [Notification](#cfn-budgets-budget-notificationwithsubscribers-notification): {{
    Notification}}
  [Subscribers](#cfn-budgets-budget-notificationwithsubscribers-subscribers): {{
    - Subscriber}}
```

## Properties
<a name="aws-properties-budgets-budget-notificationwithsubscribers-properties"></a>

`Notification`  <a name="cfn-budgets-budget-notificationwithsubscribers-notification"></a>
The notification that's associated with a budget.
*Required*: Yes
*Type*: [Notification](aws-properties-budgets-budget-notification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subscribers`  <a name="cfn-budgets-budget-notificationwithsubscribers-subscribers"></a>
A list of subscribers who are subscribed to this notification.
*Required*: Yes
*Type*: Array of [Subscriber](aws-properties-budgets-budget-subscriber.md)
*Minimum*: `1`
*Maximum*: `11`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-budgets-budget-notificationwithsubscribers--seealso"></a>
+ [NotificationWithSubscribers](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_NotificationWithSubscribers.html) in the *AWS Cost Explorer Service Cost Management APIs*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
