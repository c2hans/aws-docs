---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentContainerSpecificationForInstanceType
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype"></a>

<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-description"></a>The `InferenceComponentContainerSpecificationForInstanceType` property type specifies Property description not available. for an [AWS::SageMaker::InferenceComponent](aws-resource-sagemaker-inferencecomponent.md).

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-syntax.json"></a>

```
{
  "[ArtifactUrl](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-artifacturl)" : {{String}},
  "[ContainerMetricsConfig](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-containermetricsconfig)" : {{ContainerMetricsConfig}},
  "[Environment](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-environment)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Image](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-image)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-syntax.yaml"></a>

```
  [ArtifactUrl](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-artifacturl): {{String}}
  [ContainerMetricsConfig](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-containermetricsconfig): {{
    ContainerMetricsConfig}}
  [Environment](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-environment): {{
    {{Key}}: {{Value}}}}
  [Image](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-image): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-properties"></a>

`ArtifactUrl`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-artifacturl"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerMetricsConfig`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-containermetricsconfig"></a>
Property description not available.
*Required*: No
*Type*: [ContainerMetricsConfig](aws-properties-sagemaker-inferencecomponent-containermetricsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-environment"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z_][a-zA-Z0-9_]{1,1024}$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Image`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype-image"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `[\S]+`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
