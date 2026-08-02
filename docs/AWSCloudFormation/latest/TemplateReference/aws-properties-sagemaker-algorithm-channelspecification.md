---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-channelspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm ChannelSpecification
<a name="aws-properties-sagemaker-algorithm-channelspecification"></a>

Defines a named input source, called a channel, to be used by an algorithm.

## Syntax
<a name="aws-properties-sagemaker-algorithm-channelspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-channelspecification-syntax.json"></a>

```
{
  "[Description](#cfn-sagemaker-algorithm-channelspecification-description)" : {{String}},
  "[IsRequired](#cfn-sagemaker-algorithm-channelspecification-isrequired)" : {{Boolean}},
  "[Name](#cfn-sagemaker-algorithm-channelspecification-name)" : {{String}},
  "[SupportedCompressionTypes](#cfn-sagemaker-algorithm-channelspecification-supportedcompressiontypes)" : {{[ String, ... ]}},
  "[SupportedContentTypes](#cfn-sagemaker-algorithm-channelspecification-supportedcontenttypes)" : {{[ String, ... ]}},
  "[SupportedInputModes](#cfn-sagemaker-algorithm-channelspecification-supportedinputmodes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-channelspecification-syntax.yaml"></a>

```
  [Description](#cfn-sagemaker-algorithm-channelspecification-description): {{String}}
  [IsRequired](#cfn-sagemaker-algorithm-channelspecification-isrequired): {{Boolean}}
  [Name](#cfn-sagemaker-algorithm-channelspecification-name): {{String}}
  [SupportedCompressionTypes](#cfn-sagemaker-algorithm-channelspecification-supportedcompressiontypes): {{
    - String}}
  [SupportedContentTypes](#cfn-sagemaker-algorithm-channelspecification-supportedcontenttypes): {{
    - String}}
  [SupportedInputModes](#cfn-sagemaker-algorithm-channelspecification-supportedinputmodes): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-channelspecification-properties"></a>

`Description`  <a name="cfn-sagemaker-algorithm-channelspecification-description"></a>
A brief description of the channel.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsRequired`  <a name="cfn-sagemaker-algorithm-channelspecification-isrequired"></a>
Indicates whether the channel is required by the algorithm.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-sagemaker-algorithm-channelspecification-name"></a>
The name of the channel.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9\.\-_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportedCompressionTypes`  <a name="cfn-sagemaker-algorithm-channelspecification-supportedcompressiontypes"></a>
The allowed compression types, if data compression is used.
*Required*: No
*Type*: Array of String
*Allowed values*: `None | Gzip`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportedContentTypes`  <a name="cfn-sagemaker-algorithm-channelspecification-supportedcontenttypes"></a>
The supported MIME types for the data.
*Required*: Yes
*Type*: Array of String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportedInputModes`  <a name="cfn-sagemaker-algorithm-channelspecification-supportedinputmodes"></a>
The allowed input mode, either FILE or PIPE.
In FILE mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode.
In PIPE mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `Pipe | File | FastFile`
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
