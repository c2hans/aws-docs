---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-appspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob AppSpecification
<a name="aws-properties-sagemaker-processingjob-appspecification"></a>

Configuration to run a processing job in a specified container image.

## Syntax
<a name="aws-properties-sagemaker-processingjob-appspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-appspecification-syntax.json"></a>

```
{
  "[ContainerArguments](#cfn-sagemaker-processingjob-appspecification-containerarguments)" : {{[ String, ... ]}},
  "[ContainerEntrypoint](#cfn-sagemaker-processingjob-appspecification-containerentrypoint)" : {{[ String, ... ]}},
  "[ImageUri](#cfn-sagemaker-processingjob-appspecification-imageuri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-appspecification-syntax.yaml"></a>

```
  [ContainerArguments](#cfn-sagemaker-processingjob-appspecification-containerarguments): {{
    - String}}
  [ContainerEntrypoint](#cfn-sagemaker-processingjob-appspecification-containerentrypoint): {{
    - String}}
  [ImageUri](#cfn-sagemaker-processingjob-appspecification-imageuri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-appspecification-properties"></a>

`ContainerArguments`  <a name="cfn-sagemaker-processingjob-appspecification-containerarguments"></a>
The arguments for a container used to run a processing job.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `256 | 100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerEntrypoint`  <a name="cfn-sagemaker-processingjob-appspecification-containerentrypoint"></a>
The entrypoint for a container used to run a processing job.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `256 | 100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageUri`  <a name="cfn-sagemaker-processingjob-appspecification-imageuri"></a>
The container image to be run by the processing job.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
