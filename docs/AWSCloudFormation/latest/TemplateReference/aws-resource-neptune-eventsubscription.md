---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-neptune-eventsubscription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Neptune::EventSubscription
<a name="aws-resource-neptune-eventsubscription"></a>

Creates an event notification subscription. This action requires a topic ARN (Amazon Resource Name) created by either the Neptune console, the SNS console, or the SNS API. To obtain an ARN with SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.

You can specify the type of source (SourceType) you want to be notified of, provide a list of Neptune sources (SourceIds) that triggers the events, and provide a list of event categories (EventCategories) for events you want to be notified of. For example, you can specify SourceType = db-instance, SourceIds = mydbinstance1, mydbinstance2 and EventCategories = Availability, Backup.

If you specify both the SourceType and SourceIds, such as SourceType = db-instance and SourceIdentifier = myDBInstance1, you are notified of all the db-instance events for the specified source. If you specify a SourceType but do not specify a SourceIdentifier, you receive notice of the events for that source type for all your Neptune sources. If you do not specify either the SourceType nor the SourceIdentifier, you are notified of events generated from all Neptune sources belonging to your customer account.

## Syntax
<a name="aws-resource-neptune-eventsubscription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-neptune-eventsubscription-syntax.json"></a>

```
{
  "Type" : "AWS::Neptune::EventSubscription",
  "Properties" : {
      "[Enabled](#cfn-neptune-eventsubscription-enabled)" : {{Boolean}},
      "[EventCategories](#cfn-neptune-eventsubscription-eventcategories)" : {{[ String, ... ]}},
      "[SnsTopicArn](#cfn-neptune-eventsubscription-snstopicarn)" : {{String}},
      "[SourceIds](#cfn-neptune-eventsubscription-sourceids)" : {{[ String, ... ]}},
      "[SourceType](#cfn-neptune-eventsubscription-sourcetype)" : {{String}},
      "[SubscriptionName](#cfn-neptune-eventsubscription-subscriptionname)" : {{String}},
      "[Tags](#cfn-neptune-eventsubscription-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-neptune-eventsubscription-syntax.yaml"></a>

```
Type: AWS::Neptune::EventSubscription
Properties:
  [Enabled](#cfn-neptune-eventsubscription-enabled): {{Boolean}}
  [EventCategories](#cfn-neptune-eventsubscription-eventcategories): {{
    - String}}
  [SnsTopicArn](#cfn-neptune-eventsubscription-snstopicarn): {{String}}
  [SourceIds](#cfn-neptune-eventsubscription-sourceids): {{
    - String}}
  [SourceType](#cfn-neptune-eventsubscription-sourcetype): {{String}}
  [SubscriptionName](#cfn-neptune-eventsubscription-subscriptionname): {{String}}
  [Tags](#cfn-neptune-eventsubscription-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-neptune-eventsubscription-properties"></a>

`Enabled`  <a name="cfn-neptune-eventsubscription-enabled"></a>
A Boolean value indicating if the subscription is enabled. True indicates the subscription is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventCategories`  <a name="cfn-neptune-eventsubscription-eventcategories"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsTopicArn`  <a name="cfn-neptune-eventsubscription-snstopicarn"></a>
The topic ARN of the event notification subscription.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceIds`  <a name="cfn-neptune-eventsubscription-sourceids"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceType`  <a name="cfn-neptune-eventsubscription-sourcetype"></a>
The source type for the event notification subscription.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscriptionName`  <a name="cfn-neptune-eventsubscription-subscriptionname"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-neptune-eventsubscription-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-neptune-eventsubscription-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-neptune-eventsubscription-return-values"></a>

### Ref
<a name="aws-resource-neptune-eventsubscription-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
