---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-snapshot-sourceapplicationdescription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Snapshot SourceApplicationDescription
<a name="aws-properties-kinesisanalyticsv2-snapshot-sourceapplicationdescription"></a>

Describes the application that an enhanced snapshot was created from.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-snapshot-sourceapplicationdescription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-snapshot-sourceapplicationdescription-syntax.json"></a>

```
{
  "[ApplicationCreationTimestamp](#cfn-kinesisanalyticsv2-snapshot-sourceapplicationdescription-applicationcreationtimestamp)" : {{String}},
  "[ApplicationName](#cfn-kinesisanalyticsv2-snapshot-sourceapplicationdescription-applicationname)" : {{String}},
  "[ApplicationVersionId](#cfn-kinesisanalyticsv2-snapshot-sourceapplicationdescription-applicationversionid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-snapshot-sourceapplicationdescription-syntax.yaml"></a>

```
  [ApplicationCreationTimestamp](#cfn-kinesisanalyticsv2-snapshot-sourceapplicationdescription-applicationcreationtimestamp): {{String}}
  [ApplicationName](#cfn-kinesisanalyticsv2-snapshot-sourceapplicationdescription-applicationname): {{String}}
  [ApplicationVersionId](#cfn-kinesisanalyticsv2-snapshot-sourceapplicationdescription-applicationversionid): {{Integer}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-snapshot-sourceapplicationdescription-properties"></a>

`ApplicationCreationTimestamp`  <a name="cfn-kinesisanalyticsv2-snapshot-sourceapplicationdescription-applicationcreationtimestamp"></a>
The timestamp that indicates when the source application was created.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationName`  <a name="cfn-kinesisanalyticsv2-snapshot-sourceapplicationdescription-applicationname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationVersionId`  <a name="cfn-kinesisanalyticsv2-snapshot-sourceapplicationdescription-applicationversionid"></a>
The version ID of the source application when the snapshot was created.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `999999999`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
