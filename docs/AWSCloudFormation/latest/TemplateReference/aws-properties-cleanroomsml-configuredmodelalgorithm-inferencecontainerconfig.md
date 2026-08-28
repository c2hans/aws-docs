---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithm InferenceContainerConfig
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig"></a>

Provides configuration information for the inference container that is used when you run an inference job on a configured model algorithm.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig-syntax.json"></a>

```
{
  "[ImageUri](#cfn-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig-imageuri)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig-syntax.yaml"></a>

```
  [ImageUri](#cfn-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig-imageuri): {{String}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig-properties"></a>

`ImageUri`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig-imageuri"></a>
The registry path of the docker image that contains the inference algorithm. Clean Rooms ML currently only supports the `registry/repository[:tag]` image path format. For more information about using images in Clean Rooms ML, see the [Sagemaker API reference](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html#sagemaker-Type-AlgorithmSpecification-TrainingImage).
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
