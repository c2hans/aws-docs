---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-eventbridgeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket EventBridgeConfiguration
<a name="aws-properties-s3-bucket-eventbridgeconfiguration"></a>

Amazon S3 can send events to Amazon EventBridge whenever certain events happen in your bucket, see [Using EventBridge](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventBridge.html) in the *Amazon S3 User Guide*.

Unlike other destinations, delivery of events to EventBridge can be either enabled or disabled for a bucket. If enabled, all events will be sent to EventBridge and you can use EventBridge rules to route events to additional targets. For more information, see [What Is Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) in the *Amazon EventBridge User Guide*

## Syntax
<a name="aws-properties-s3-bucket-eventbridgeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-eventbridgeconfiguration-syntax.json"></a>

```
{
  "[EventBridgeEnabled](#cfn-s3-bucket-eventbridgeconfiguration-eventbridgeenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-s3-bucket-eventbridgeconfiguration-syntax.yaml"></a>

```
  [EventBridgeEnabled](#cfn-s3-bucket-eventbridgeconfiguration-eventbridgeenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-s3-bucket-eventbridgeconfiguration-properties"></a>

`EventBridgeEnabled`  <a name="cfn-s3-bucket-eventbridgeconfiguration-eventbridgeenabled"></a>
Enables delivery of events to Amazon EventBridge.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3-bucket-eventbridgeconfiguration--examples"></a>

### Enable EventBridgeConfiguration
<a name="aws-properties-s3-bucket-eventbridgeconfiguration--examples--Enable_EventBridgeConfiguration"></a>

The following example template shows an Amazon S3 bucket with a notification configuration with EventBridge enabled.

#### JSON
<a name="aws-properties-s3-bucket-eventbridgeconfiguration--examples--Enable_EventBridgeConfiguration--json"></a>

```
{
"Resources": {
  "S3Bucket": {
    "Type": "AWS::S3::Bucket",
    "Properties": {
      "NotificationConfiguration": {
        "EventBridgeConfiguration": {
          "EventBridgeEnabled": true
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-properties-s3-bucket-eventbridgeconfiguration--examples--Enable_EventBridgeConfiguration--yaml"></a>

```
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      NotificationConfiguration:
        EventBridgeConfiguration:
          EventBridgeEnabled: true
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
