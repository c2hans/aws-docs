---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budget-subscriber.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::Budget Subscriber
<a name="aws-properties-budgets-budget-subscriber"></a>

The `Subscriber` property type specifies who to notify for a Billing and Cost Management budget notification. The subscriber consists of a subscription type, and either an Amazon SNS topic or an email address.

For example, an email subscriber would have the following parameters:
+ A `subscriptionType` of `EMAIL`
+ An `address` of `example@example.com`

## Syntax
<a name="aws-properties-budgets-budget-subscriber-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budget-subscriber-syntax.json"></a>

```
{
  "[Address](#cfn-budgets-budget-subscriber-address)" : {{String}},
  "[SubscriptionType](#cfn-budgets-budget-subscriber-subscriptiontype)" : {{String}}
}
```

### YAML
<a name="aws-properties-budgets-budget-subscriber-syntax.yaml"></a>

```
  [Address](#cfn-budgets-budget-subscriber-address): {{String}}
  [SubscriptionType](#cfn-budgets-budget-subscriber-subscriptiontype): {{String}}
```

## Properties
<a name="aws-properties-budgets-budget-subscriber-properties"></a>

`Address`  <a name="cfn-budgets-budget-subscriber-address"></a>
The address that AWS sends budget notifications to, either an SNS topic or an email.
When you create a subscriber, the value of `Address` can't contain line breaks.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubscriptionType`  <a name="cfn-budgets-budget-subscriber-subscriptiontype"></a>
The type of notification that AWS sends to a subscriber.
*Required*: Yes
*Type*: String
*Allowed values*: `SNS | EMAIL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-budgets-budget-subscriber--seealso"></a>
+ [Subscriber](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Subscriber.html) in the *AWS Cost Explorer Service Cost Management APIs*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
