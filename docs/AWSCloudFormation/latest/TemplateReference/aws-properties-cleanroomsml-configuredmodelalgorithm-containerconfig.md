---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithm ContainerConfig
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig"></a>

Provides configuration information for the training container, including entrypoints and arguments.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig-syntax.json"></a>

```
{
  "[Arguments](#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-arguments)" : {{[ String, ... ]}},
  "[Entrypoint](#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-entrypoint)" : {{[ String, ... ]}},
  "[ImageUri](#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-imageuri)" : {{String}},
  "[MetricDefinitions](#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-metricdefinitions)" : {{[ MetricDefinition, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig-syntax.yaml"></a>

```
  [Arguments](#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-arguments): {{
    - String}}
  [Entrypoint](#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-entrypoint): {{
    - String}}
  [ImageUri](#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-imageuri): {{String}}
  [MetricDefinitions](#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-metricdefinitions): {{
    - MetricDefinition}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig-properties"></a>

`Arguments`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-arguments"></a>
The arguments for a container used to run a training job. See How Amazon SageMaker Runs Your Training Image for additional information. For more information, see [How Sagemaker runs your training image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html).
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `256 | 100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Entrypoint`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-entrypoint"></a>
The entrypoint script for a Docker container used to run a training job. This script takes precedence over the default train processing instructions. See How Amazon SageMaker Runs Your Training Image for additional information. For more information, see [How Sagemaker runs your training image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html).
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `256 | 100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageUri`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-imageuri"></a>
The registry path of the docker image that contains the algorithm. Clean Rooms ML currently only supports the `registry/repository[:tag]` image path format. For more information about using images in Clean Rooms ML, see the [Sagemaker API reference](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html#sagemaker-Type-AlgorithmSpecification-TrainingImage).
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricDefinitions`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-metricdefinitions"></a>
A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. AWS Clean Rooms ML publishes each metric to all members' Amazon CloudWatch using IAM role configured in [PutMLConfiguration](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_PutMLConfiguration.html).
*Required*: No
*Type*: Array of [MetricDefinition](aws-properties-cleanroomsml-configuredmodelalgorithm-metricdefinition.md)
*Minimum*: `0`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
