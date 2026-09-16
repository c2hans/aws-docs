---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AIWorkloadConfig AIWorkloadInputDataConfig
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig"></a>

A channel of input data for an AI workload configuration. Each channel has a name and a data source.

## Syntax
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig-syntax.json"></a>

```
{
  "[ChannelName](#cfn-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig-channelname)" : {{String}},
  "[DataSource](#cfn-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig-datasource)" : {{AIWorkloadDataSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig-syntax.yaml"></a>

```
  [ChannelName](#cfn-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig-channelname): {{String}}
  [DataSource](#cfn-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig-datasource): {{
    AIWorkloadDataSource}}
```

## Properties
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig-properties"></a>

`ChannelName`  <a name="cfn-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig-channelname"></a>
The logical name for the data channel.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9\.\-_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataSource`  <a name="cfn-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig-datasource"></a>
The data source for this channel.
*Required*: Yes
*Type*: [AIWorkloadDataSource](aws-properties-sagemaker-aiworkloadconfig-aiworkloaddatasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
