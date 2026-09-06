---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-instancestorageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::InstanceStorageConfig
<a name="aws-resource-connect-instancestorageconfig"></a>

The storage configuration for the instance.

## Syntax
<a name="aws-resource-connect-instancestorageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-instancestorageconfig-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::InstanceStorageConfig",
  "Properties" : {
      "[InstanceArn](#cfn-connect-instancestorageconfig-instancearn)" : {{String}},
      "[KinesisFirehoseConfig](#cfn-connect-instancestorageconfig-kinesisfirehoseconfig)" : {{KinesisFirehoseConfig}},
      "[KinesisStreamConfig](#cfn-connect-instancestorageconfig-kinesisstreamconfig)" : {{KinesisStreamConfig}},
      "[KinesisVideoStreamConfig](#cfn-connect-instancestorageconfig-kinesisvideostreamconfig)" : {{KinesisVideoStreamConfig}},
      "[ResourceType](#cfn-connect-instancestorageconfig-resourcetype)" : {{String}},
      "[S3Config](#cfn-connect-instancestorageconfig-s3config)" : {{S3Config}},
      "[StorageType](#cfn-connect-instancestorageconfig-storagetype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-instancestorageconfig-syntax.yaml"></a>

```
Type: AWS::Connect::InstanceStorageConfig
Properties:
  [InstanceArn](#cfn-connect-instancestorageconfig-instancearn): {{String}}
  [KinesisFirehoseConfig](#cfn-connect-instancestorageconfig-kinesisfirehoseconfig): {{
    KinesisFirehoseConfig}}
  [KinesisStreamConfig](#cfn-connect-instancestorageconfig-kinesisstreamconfig): {{
    KinesisStreamConfig}}
  [KinesisVideoStreamConfig](#cfn-connect-instancestorageconfig-kinesisvideostreamconfig): {{
    KinesisVideoStreamConfig}}
  [ResourceType](#cfn-connect-instancestorageconfig-resourcetype): {{String}}
  [S3Config](#cfn-connect-instancestorageconfig-s3config): {{
    S3Config}}
  [StorageType](#cfn-connect-instancestorageconfig-storagetype): {{String}}
```

## Properties
<a name="aws-resource-connect-instancestorageconfig-properties"></a>

`InstanceArn`  <a name="cfn-connect-instancestorageconfig-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KinesisFirehoseConfig`  <a name="cfn-connect-instancestorageconfig-kinesisfirehoseconfig"></a>
The configuration of the Kinesis Firehose delivery stream.
*Required*: No
*Type*: [KinesisFirehoseConfig](aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KinesisStreamConfig`  <a name="cfn-connect-instancestorageconfig-kinesisstreamconfig"></a>
The configuration of the Kinesis data stream.
*Required*: No
*Type*: [KinesisStreamConfig](aws-properties-connect-instancestorageconfig-kinesisstreamconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KinesisVideoStreamConfig`  <a name="cfn-connect-instancestorageconfig-kinesisvideostreamconfig"></a>
The configuration of the Kinesis video stream.
*Required*: No
*Type*: [KinesisVideoStreamConfig](aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-connect-instancestorageconfig-resourcetype"></a>
A valid resource type. Following are the valid resource types: `CHAT_TRANSCRIPTS` \| `CALL_RECORDINGS` \| `SCHEDULED_REPORTS` \| `MEDIA_STREAMS` \| `CONTACT_TRACE_RECORDS` \| `AGENT_EVENTS`
*Required*: Yes
*Type*: String
*Allowed values*: `CHAT_TRANSCRIPTS | CALL_RECORDINGS | SCHEDULED_REPORTS | MEDIA_STREAMS | CONTACT_TRACE_RECORDS | AGENT_EVENTS | REAL_TIME_CONTACT_ANALYSIS_SEGMENTS | ATTACHMENTS | CONTACT_EVALUATIONS | SCREEN_RECORDINGS | REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS | REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS | EMAIL_MESSAGES`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Config`  <a name="cfn-connect-instancestorageconfig-s3config"></a>
The S3 bucket configuration.
*Required*: No
*Type*: [S3Config](aws-properties-connect-instancestorageconfig-s3config.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageType`  <a name="cfn-connect-instancestorageconfig-storagetype"></a>
A valid storage type.
*Required*: Yes
*Type*: String
*Allowed values*: `S3 | KINESIS_VIDEO_STREAM | KINESIS_STREAM | KINESIS_FIREHOSE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-instancestorageconfig-return-values"></a>

### Ref
<a name="aws-resource-connect-instancestorageconfig-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the instance storage configuration. For example:

 `{ "Ref": "myInstanceStorageConfig" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-instancestorageconfig-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-instancestorageconfig-return-values-fn--getatt-fn--getatt"></a>

`AssociationId`  <a name="AssociationId-fn::getatt"></a>
The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
