---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::EventDataStore AdvancedEventSelector
<a name="aws-properties-cloudtrail-eventdatastore-advancedeventselector"></a>

Advanced event selectors let you create fine-grained selectors for AWS CloudTrail management, data, and network activity events. They help you control costs by logging only those events that are important to you. For more information about configuring advanced event selectors, see the [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html), [Logging network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html), and [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) topics in the *AWS CloudTrail User Guide*.

You cannot apply both event selectors and advanced event selectors to a trail.

 **Supported CloudTrail event record fields for management events**
+ `eventCategory` (required)
+  `eventSource`
+  `readOnly`

The following additional fields are available for event data stores:
+  `eventName`
+  `eventType`
+  `sessionCredentialFromConsole`
+  `userIdentity.arn`

 **Supported CloudTrail event record fields for data events**
+ `eventCategory` (required)
+  `eventName`
+  `eventSource`
+  `eventType`
+  `resources.ARN`
+ `resources.type` (required)
+  `readOnly`
+  `sessionCredentialFromConsole`
+  `userIdentity.arn`

 **Supported CloudTrail event record fields for network activity events**
+ `eventCategory` (required)
+ `eventSource` (required)
+  `eventName`
+ `errorCode` - The only valid value for `errorCode` is `VpceAccessDenied`.
+  `vpcEndpointId`

The following additional field is available for trails:
+  `userIdentity.arn`

**Note**
For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS, the only supported field is `eventCategory`.

## Syntax
<a name="aws-properties-cloudtrail-eventdatastore-advancedeventselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudtrail-eventdatastore-advancedeventselector-syntax.json"></a>

```
{
  "[FieldSelectors](#cfn-cloudtrail-eventdatastore-advancedeventselector-fieldselectors)" : {{[ AdvancedFieldSelector, ... ]}},
  "[Name](#cfn-cloudtrail-eventdatastore-advancedeventselector-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudtrail-eventdatastore-advancedeventselector-syntax.yaml"></a>

```
  [FieldSelectors](#cfn-cloudtrail-eventdatastore-advancedeventselector-fieldselectors): {{
    - AdvancedFieldSelector}}
  [Name](#cfn-cloudtrail-eventdatastore-advancedeventselector-name): {{String}}
```

## Properties
<a name="aws-properties-cloudtrail-eventdatastore-advancedeventselector-properties"></a>

`FieldSelectors`  <a name="cfn-cloudtrail-eventdatastore-advancedeventselector-fieldselectors"></a>
Contains all selector statements in an advanced event selector.
*Required*: Yes
*Type*: Array of [AdvancedFieldSelector](aws-properties-cloudtrail-eventdatastore-advancedfieldselector.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudtrail-eventdatastore-advancedeventselector-name"></a>
An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
