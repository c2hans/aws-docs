---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-automljob-automlchannel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob AutoMLChannel
<a name="aws-properties-sagemaker-automljob-automlchannel"></a>

A channel is a named input source that training algorithms can consume. The validation dataset size is limited to less than 2 GB. The training dataset size must be less than 100 GB. For more information, see [ Channel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html).

**Note**
A validation dataset must contain the same headers as the training dataset.

## Syntax
<a name="aws-properties-sagemaker-automljob-automlchannel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-automljob-automlchannel-syntax.json"></a>

```
{
  "[ChannelType](#cfn-sagemaker-automljob-automlchannel-channeltype)" : {{String}},
  "[CompressionType](#cfn-sagemaker-automljob-automlchannel-compressiontype)" : {{String}},
  "[ContentType](#cfn-sagemaker-automljob-automlchannel-contenttype)" : {{String}},
  "[DataSource](#cfn-sagemaker-automljob-automlchannel-datasource)" : {{AutoMLDataSource}},
  "[TargetAttributeName](#cfn-sagemaker-automljob-automlchannel-targetattributename)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-automljob-automlchannel-syntax.yaml"></a>

```
  [ChannelType](#cfn-sagemaker-automljob-automlchannel-channeltype): {{String}}
  [CompressionType](#cfn-sagemaker-automljob-automlchannel-compressiontype): {{String}}
  [ContentType](#cfn-sagemaker-automljob-automlchannel-contenttype): {{String}}
  [DataSource](#cfn-sagemaker-automljob-automlchannel-datasource): {{
    AutoMLDataSource}}
  [TargetAttributeName](#cfn-sagemaker-automljob-automlchannel-targetattributename): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-automljob-automlchannel-properties"></a>

`ChannelType`  <a name="cfn-sagemaker-automljob-automlchannel-channeltype"></a>
The channel type (optional) is an `enum` string. The default value is `training`. Channels for training and validation must share the same `ContentType` and `TargetAttributeName`. For information on specifying training and validation channel types, see [How to specify training and validation datasets](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-data-sources-training-or-validation).
*Required*: No
*Type*: String
*Allowed values*: `training | validation`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CompressionType`  <a name="cfn-sagemaker-automljob-automlchannel-compressiontype"></a>
You can use `Gzip` or `None`. The default value is `None`.
*Required*: No
*Type*: String
*Allowed values*: `None | Gzip`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContentType`  <a name="cfn-sagemaker-automljob-automlchannel-contenttype"></a>
The content type of the data from the input source. You can use `text/csv;header=present` or `x-application/vnd.amazon+parquet`. The default value is `text/csv;header=present`.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataSource`  <a name="cfn-sagemaker-automljob-automlchannel-datasource"></a>
The data source for an AutoML channel.
*Required*: No
*Type*: [AutoMLDataSource](aws-properties-sagemaker-automljob-automldatasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetAttributeName`  <a name="cfn-sagemaker-automljob-automlchannel-targetattributename"></a>
The name of the target variable in supervised learning, usually represented by 'y'.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
