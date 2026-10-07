---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-rcsagent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::RcsAgent
<a name="aws-resource-smsvoice-rcsagent"></a>

Creates a new RCS agent for sending rich messages through the RCS channel. The RCS agent serves as an origination identity for sending RCS messages to your recipients.

## Syntax
<a name="aws-resource-smsvoice-rcsagent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-rcsagent-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::RcsAgent",
  "Properties" : {
      "[DeletionProtectionEnabled](#cfn-smsvoice-rcsagent-deletionprotectionenabled)" : {{Boolean}},
      "[OptOutListName](#cfn-smsvoice-rcsagent-optoutlistname)" : {{String}},
      "[SelfManagedOptOutsEnabled](#cfn-smsvoice-rcsagent-selfmanagedoptoutsenabled)" : {{Boolean}},
      "[Tags](#cfn-smsvoice-rcsagent-tags)" : {{[ Tag, ... ]}},
      "[TwoWayChannelArn](#cfn-smsvoice-rcsagent-twowaychannelarn)" : {{String}},
      "[TwoWayChannelRole](#cfn-smsvoice-rcsagent-twowaychannelrole)" : {{String}},
      "[TwoWayEnabled](#cfn-smsvoice-rcsagent-twowayenabled)" : {{Boolean}},
      "[TwoWayMediaS3BucketName](#cfn-smsvoice-rcsagent-twowaymedias3bucketname)" : {{String}},
      "[TwoWayMediaS3KeyPrefix](#cfn-smsvoice-rcsagent-twowaymedias3keyprefix)" : {{String}},
      "[TwoWayMediaS3Role](#cfn-smsvoice-rcsagent-twowaymedias3role)" : {{String}},
      "[TwoWayRcsEventsEnabled](#cfn-smsvoice-rcsagent-twowayrcseventsenabled)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-rcsagent-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::RcsAgent
Properties:
  [DeletionProtectionEnabled](#cfn-smsvoice-rcsagent-deletionprotectionenabled): {{Boolean}}
  [OptOutListName](#cfn-smsvoice-rcsagent-optoutlistname): {{String}}
  [SelfManagedOptOutsEnabled](#cfn-smsvoice-rcsagent-selfmanagedoptoutsenabled): {{Boolean}}
  [Tags](#cfn-smsvoice-rcsagent-tags): {{
    - Tag}}
  [TwoWayChannelArn](#cfn-smsvoice-rcsagent-twowaychannelarn): {{String}}
  [TwoWayChannelRole](#cfn-smsvoice-rcsagent-twowaychannelrole): {{String}}
  [TwoWayEnabled](#cfn-smsvoice-rcsagent-twowayenabled): {{Boolean}}
  [TwoWayMediaS3BucketName](#cfn-smsvoice-rcsagent-twowaymedias3bucketname): {{String}}
  [TwoWayMediaS3KeyPrefix](#cfn-smsvoice-rcsagent-twowaymedias3keyprefix): {{String}}
  [TwoWayMediaS3Role](#cfn-smsvoice-rcsagent-twowaymedias3role): {{String}}
  [TwoWayRcsEventsEnabled](#cfn-smsvoice-rcsagent-twowayrcseventsenabled): {{
    - String}}
```

## Properties
<a name="aws-resource-smsvoice-rcsagent-properties"></a>

`DeletionProtectionEnabled`  <a name="cfn-smsvoice-rcsagent-deletionprotectionenabled"></a>
When set to true the RCS agent can't be deleted.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OptOutListName`  <a name="cfn-smsvoice-rcsagent-optoutlistname"></a>
The name of the OptOutList associated with the RCS agent.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfManagedOptOutsEnabled`  <a name="cfn-smsvoice-rcsagent-selfmanagedoptoutsenabled"></a>
When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-smsvoice-rcsagent-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-smsvoice-rcsagent-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TwoWayChannelArn`  <a name="cfn-smsvoice-rcsagent-twowaychannelarn"></a>
The Amazon Resource Name (ARN) of the two way channel.
*Required*: No
*Type*: String
*Pattern*: `^\S+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TwoWayChannelRole`  <a name="cfn-smsvoice-rcsagent-twowaychannelrole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
*Required*: No
*Type*: String
*Pattern*: `^arn:\S+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TwoWayEnabled`  <a name="cfn-smsvoice-rcsagent-twowayenabled"></a>
When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TwoWayMediaS3BucketName`  <a name="cfn-smsvoice-rcsagent-twowaymedias3bucketname"></a>
The name of the S3 bucket where inbound RCS media files are stored.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9][a-z0-9.-]*[a-z0-9]$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TwoWayMediaS3KeyPrefix`  <a name="cfn-smsvoice-rcsagent-twowaymedias3keyprefix"></a>
The key prefix used for inbound RCS media objects in the S3 bucket.
*Required*: No
*Type*: String
*Pattern*: `^[\S]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TwoWayMediaS3Role`  <a name="cfn-smsvoice-rcsagent-twowaymedias3role"></a>
The ARN of the IAM role used to write inbound RCS media files to the S3 bucket.
*Required*: No
*Type*: String
*Pattern*: `^arn:\S+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TwoWayRcsEventsEnabled`  <a name="cfn-smsvoice-rcsagent-twowayrcseventsenabled"></a>
The list of RCS event types enabled for two-way messaging on the agent.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `50 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-smsvoice-rcsagent-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-rcsagent-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-smsvoice-rcsagent-return-values-fn--getatt"></a>

####
<a name="aws-resource-smsvoice-rcsagent-return-values-fn--getatt-fn--getatt"></a>

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
The time when the RCS agent was created, in [UNIX epoch time](https://www.epochconverter.com/) format.

`PoolId`  <a name="PoolId-fn::getatt"></a>
The unique identifier of the pool associated with the RCS agent.

`RcsAgentArn`  <a name="RcsAgentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the RCS agent.

`RcsAgentId`  <a name="RcsAgentId-fn::getatt"></a>
The unique identifier for the RCS agent.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the RCS agent.
