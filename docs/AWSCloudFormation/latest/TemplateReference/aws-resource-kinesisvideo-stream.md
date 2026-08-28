---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisvideo-stream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisVideo::Stream
<a name="aws-resource-kinesisvideo-stream"></a>

Specifies a new Kinesis video stream.

When you create a new stream, Kinesis Video Streams assigns it a version number. When you change the stream's metadata, Kinesis Video Streams updates the version.

`CreateStream` is an asynchronous operation.

For information about how the service works, see [How it Works](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-works.html).

You must have permissions for the `KinesisVideo:CreateStream` action.

## Syntax
<a name="aws-resource-kinesisvideo-stream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kinesisvideo-stream-syntax.json"></a>

```
{
  "Type" : "AWS::KinesisVideo::Stream",
  "Properties" : {
      "[DataRetentionInHours](#cfn-kinesisvideo-stream-dataretentioninhours)" : {{Integer}},
      "[DeviceName](#cfn-kinesisvideo-stream-devicename)" : {{String}},
      "[KmsKeyId](#cfn-kinesisvideo-stream-kmskeyid)" : {{String}},
      "[MediaType](#cfn-kinesisvideo-stream-mediatype)" : {{String}},
      "[Name](#cfn-kinesisvideo-stream-name)" : {{String}},
      "[StreamStorageConfiguration](#cfn-kinesisvideo-stream-streamstorageconfiguration)" : {{StreamStorageConfiguration}},
      "[Tags](#cfn-kinesisvideo-stream-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kinesisvideo-stream-syntax.yaml"></a>

```
Type: AWS::KinesisVideo::Stream
Properties:
  [DataRetentionInHours](#cfn-kinesisvideo-stream-dataretentioninhours): {{Integer}}
  [DeviceName](#cfn-kinesisvideo-stream-devicename): {{String}}
  [KmsKeyId](#cfn-kinesisvideo-stream-kmskeyid): {{String}}
  [MediaType](#cfn-kinesisvideo-stream-mediatype): {{String}}
  [Name](#cfn-kinesisvideo-stream-name): {{String}}
  [StreamStorageConfiguration](#cfn-kinesisvideo-stream-streamstorageconfiguration): {{
    StreamStorageConfiguration}}
  [Tags](#cfn-kinesisvideo-stream-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kinesisvideo-stream-properties"></a>

`DataRetentionInHours`  <a name="cfn-kinesisvideo-stream-dataretentioninhours"></a>
How long the stream retains data, in hours.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `87600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceName`  <a name="cfn-kinesisvideo-stream-devicename"></a>
The name of the device that is associated with the stream.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_.-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-kinesisvideo-stream-kmskeyid"></a>
The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to encrypt data on the stream.
*Required*: No
*Type*: String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaType`  <a name="cfn-kinesisvideo-stream-mediatype"></a>
The `MediaType` of the stream.
*Required*: No
*Type*: String
*Pattern*: `[\w\-\.\+]+/[\w\-\.\+]+(,[\w\-\.\+]+/[\w\-\.\+]+)*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-kinesisvideo-stream-name"></a>
The name of the stream.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_.-]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StreamStorageConfiguration`  <a name="cfn-kinesisvideo-stream-streamstorageconfiguration"></a>
The configuration for stream storage, including the default storage tier for stream data. This configuration determines how stream data is stored and accessed, with different tiers offering varying levels of performance and cost optimization.
*Required*: No
*Type*: [StreamStorageConfiguration](aws-properties-kinesisvideo-stream-streamstorageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-kinesisvideo-stream-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-kinesisvideo-stream-tag.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kinesisvideo-stream-return-values"></a>

### Ref
<a name="aws-resource-kinesisvideo-stream-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-kinesisvideo-stream-return-values-fn--getatt"></a>

####
<a name="aws-resource-kinesisvideo-stream-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the stream.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
