---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodelsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ApplicationInferenceProfile InferenceProfileModelSource
<a name="aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodelsource"></a>

Contains information about the model or system-defined inference profile that is the source for an inference profile..

## Syntax
<a name="aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodelsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodelsource-syntax.json"></a>

```
{
  "[CopyFrom](#cfn-bedrock-applicationinferenceprofile-inferenceprofilemodelsource-copyfrom)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodelsource-syntax.yaml"></a>

```
  [CopyFrom](#cfn-bedrock-applicationinferenceprofile-inferenceprofilemodelsource-copyfrom): {{String}}
```

## Properties
<a name="aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodelsource-properties"></a>

`CopyFrom`  <a name="cfn-bedrock-applicationinferenceprofile-inferenceprofilemodelsource-copyfrom"></a>
The ARN of the model or system-defined inference profile that is the source for the inference profile.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|foundation-model)/[a-zA-Z0-9-:.]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
