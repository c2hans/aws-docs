---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-docdb-eventsubscription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DocDB::EventSubscription
<a name="aws-resource-docdb-eventsubscription"></a>

Creates an Amazon DocumentDB event notification subscription. This action requires a topic Amazon Resource Name (ARN) created by using the Amazon DocumentDB console, the Amazon SNS console, or the Amazon SNS API. To obtain an ARN with Amazon SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the Amazon SNS console.

You can specify the type of source (`SourceType`) that you want to be notified of. You can also provide a list of Amazon DocumentDB sources (`SourceIds`) that trigger the events, and you can provide a list of event categories (`EventCategories`) for events that you want to be notified of. For example, you can specify `SourceType = db-instance`, `SourceIds = mydbinstance1, mydbinstance2` and `EventCategories = Availability, Backup`.

If you specify both the `SourceType` and `SourceIds` (such as `SourceType = db-instance` and `SourceIdentifier = myDBInstance1`), you are notified of all the `db-instance` events for the specified source. If you specify a `SourceType` but do not specify a `SourceIdentifier`, you receive notice of the events for that source type for all your Amazon DocumentDB sources. If you do not specify either the `SourceType` or the `SourceIdentifier`, you are notified of events generated from all Amazon DocumentDB sources belonging to your customer account.

## Syntax
<a name="aws-resource-docdb-eventsubscription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-docdb-eventsubscription-syntax.json"></a>

```
{
  "Type" : "AWS::DocDB::EventSubscription",
  "Properties" : {
      "[Enabled](#cfn-docdb-eventsubscription-enabled)" : {{Boolean}},
      "[EventCategories](#cfn-docdb-eventsubscription-eventcategories)" : {{[ String, ... ]}},
      "[SnsTopicArn](#cfn-docdb-eventsubscription-snstopicarn)" : {{String}},
      "[SourceIds](#cfn-docdb-eventsubscription-sourceids)" : {{[ String, ... ]}},
      "[SourceType](#cfn-docdb-eventsubscription-sourcetype)" : {{String}},
      "[SubscriptionName](#cfn-docdb-eventsubscription-subscriptionname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-docdb-eventsubscription-syntax.yaml"></a>

```
Type: AWS::DocDB::EventSubscription
Properties:
  [Enabled](#cfn-docdb-eventsubscription-enabled): {{Boolean}}
  [EventCategories](#cfn-docdb-eventsubscription-eventcategories): {{
    - String}}
  [SnsTopicArn](#cfn-docdb-eventsubscription-snstopicarn): {{String}}
  [SourceIds](#cfn-docdb-eventsubscription-sourceids): {{
    - String}}
  [SourceType](#cfn-docdb-eventsubscription-sourcetype): {{String}}
  [SubscriptionName](#cfn-docdb-eventsubscription-subscriptionname): {{String}}
```

## Properties
<a name="aws-resource-docdb-eventsubscription-properties"></a>

`Enabled`  <a name="cfn-docdb-eventsubscription-enabled"></a>
 A Boolean value; set to `true` to activate the subscription, set to `false` to create the subscription but not active it.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventCategories`  <a name="cfn-docdb-eventsubscription-eventcategories"></a>
 A list of event categories for a `SourceType` that you want to subscribe to.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsTopicArn`  <a name="cfn-docdb-eventsubscription-snstopicarn"></a>
The Amazon Resource Name (ARN) of the SNS topic created for event notification. Amazon SNS creates the ARN when you create a topic and subscribe to it.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceIds`  <a name="cfn-docdb-eventsubscription-sourceids"></a>
The list of identifiers of the event sources for which events are returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.
Constraints:
+ If `SourceIds` are provided, `SourceType` must also be provided.
+ If the source type is an instance, a `DBInstanceIdentifier` must be provided.
+ If the source type is a security group, a `DBSecurityGroupName` must be provided.
+ If the source type is a parameter group, a `DBParameterGroupName` must be provided.
+ If the source type is a snapshot, a `DBSnapshotIdentifier` must be provided.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceType`  <a name="cfn-docdb-eventsubscription-sourcetype"></a>
The type of source that is generating the events. For example, if you want to be notified of events generated by an instance, you would set this parameter to `db-instance`. If this value is not specified, all events are returned.
Valid values: `db-instance`, `db-cluster`, `db-parameter-group`, `db-security-group`, `db-cluster-snapshot`
*Required*: No
*Type*: String
*Allowed values*: `db-instance | db-cluster | db-parameter-group | db-security-group | db-cluster-snapshot`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscriptionName`  <a name="cfn-docdb-eventsubscription-subscriptionname"></a>
The name of the subscription.
Constraints: The name must be fewer than 255 characters.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-docdb-eventsubscription-return-values"></a>

### Ref
<a name="aws-resource-docdb-eventsubscription-return-values-ref"></a>
