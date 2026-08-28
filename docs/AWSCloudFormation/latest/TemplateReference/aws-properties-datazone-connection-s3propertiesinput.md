---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-s3propertiesinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection S3PropertiesInput
<a name="aws-properties-datazone-connection-s3propertiesinput"></a>

The Amazon S3 properties of a connection.

## Syntax
<a name="aws-properties-datazone-connection-s3propertiesinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-s3propertiesinput-syntax.json"></a>

```
{
  "[RegisterS3AccessGrantLocation](#cfn-datazone-connection-s3propertiesinput-registers3accessgrantlocation)" : {{Boolean}},
  "[S3AccessGrantLocationId](#cfn-datazone-connection-s3propertiesinput-s3accessgrantlocationid)" : {{String}},
  "[S3Uri](#cfn-datazone-connection-s3propertiesinput-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-s3propertiesinput-syntax.yaml"></a>

```
  [RegisterS3AccessGrantLocation](#cfn-datazone-connection-s3propertiesinput-registers3accessgrantlocation): {{Boolean}}
  [S3AccessGrantLocationId](#cfn-datazone-connection-s3propertiesinput-s3accessgrantlocationid): {{String}}
  [S3Uri](#cfn-datazone-connection-s3propertiesinput-s3uri): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-s3propertiesinput-properties"></a>

`RegisterS3AccessGrantLocation`  <a name="cfn-datazone-connection-s3propertiesinput-registers3accessgrantlocation"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3AccessGrantLocationId`  <a name="cfn-datazone-connection-s3propertiesinput-s3accessgrantlocationid"></a>
The Amazon S3 Access Grant location ID that's part of the Amazon S3 properties of a connection.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9\-]+`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Uri`  <a name="cfn-datazone-connection-s3propertiesinput-s3uri"></a>
The Amazon S3 URI that's part of the Amazon S3 properties of a connection.
*Required*: Yes
*Type*: String
*Pattern*: `s3://.+`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
