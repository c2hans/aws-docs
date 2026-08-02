---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-msk-channel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Channel
<a name="aws-resource-msk-channel"></a>

<a name="aws-resource-msk-channel-description"></a>The `AWS::MSK::Channel` resource Property description not available. for MSK.

## Syntax
<a name="aws-resource-msk-channel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-msk-channel-syntax.json"></a>

```
{
  "Type" : "AWS::MSK::Channel",
  "Properties" : {
      "[ChannelName](#cfn-msk-channel-channelname)" : {{String}},
      "[ClusterArn](#cfn-msk-channel-clusterarn)" : {{String}},
      "[EncryptionConfiguration](#cfn-msk-channel-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[IcebergDestinationConfiguration](#cfn-msk-channel-icebergdestinationconfiguration)" : {{IcebergDestinationConfiguration}},
      "[LoggingInfo](#cfn-msk-channel-logginginfo)" : {{ChannelLoggingInfo}},
      "[S3DestinationConfiguration](#cfn-msk-channel-s3destinationconfiguration)" : {{S3DestinationConfiguration}},
      "[Tags](#cfn-msk-channel-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TopicConfigurationList](#cfn-msk-channel-topicconfigurationlist)" : {{[ TopicConfiguration, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-msk-channel-syntax.yaml"></a>

```
Type: AWS::MSK::Channel
Properties:
  [ChannelName](#cfn-msk-channel-channelname): {{String}}
  [ClusterArn](#cfn-msk-channel-clusterarn): {{String}}
  [EncryptionConfiguration](#cfn-msk-channel-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [IcebergDestinationConfiguration](#cfn-msk-channel-icebergdestinationconfiguration): {{
    IcebergDestinationConfiguration}}
  [LoggingInfo](#cfn-msk-channel-logginginfo): {{
    ChannelLoggingInfo}}
  [S3DestinationConfiguration](#cfn-msk-channel-s3destinationconfiguration): {{
    S3DestinationConfiguration}}
  [Tags](#cfn-msk-channel-tags): {{
    {{Key}}: {{Value}}}}
  [TopicConfigurationList](#cfn-msk-channel-topicconfigurationlist): {{
    - TopicConfiguration}}
```

## Properties
<a name="aws-resource-msk-channel-properties"></a>

`ChannelName`  <a name="cfn-msk-channel-channelname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClusterArn`  <a name="cfn-msk-channel-clusterarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w-]+:kafka:[\w-]+:\d+:cluster.*\Z`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionConfiguration`  <a name="cfn-msk-channel-encryptionconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-msk-channel-encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IcebergDestinationConfiguration`  <a name="cfn-msk-channel-icebergdestinationconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [IcebergDestinationConfiguration](aws-properties-msk-channel-icebergdestinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoggingInfo`  <a name="cfn-msk-channel-logginginfo"></a>
Property description not available.
*Required*: No
*Type*: [ChannelLoggingInfo](aws-properties-msk-channel-channellogginginfo.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3DestinationConfiguration`  <a name="cfn-msk-channel-s3destinationconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [S3DestinationConfiguration](aws-properties-msk-channel-s3destinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-msk-channel-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicConfigurationList`  <a name="cfn-msk-channel-topicconfigurationlist"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [TopicConfiguration](aws-properties-msk-channel-topicconfiguration.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-msk-channel-return-values"></a>

### Ref
<a name="aws-resource-msk-channel-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-msk-channel-return-values-fn--getatt"></a>

####
<a name="aws-resource-msk-channel-return-values-fn--getatt-fn--getatt"></a>

`ChannelArn`  <a name="ChannelArn-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.
