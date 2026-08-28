---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelExplainabilityJobDefinition ModelExplainabilityJobInput
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput"></a>

Inputs for the model explainability job.

## Syntax
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-syntax.json"></a>

```
{
  "[BatchTransformInput](#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-batchtransforminput)" : {{BatchTransformInput}},
  "[EndpointInput](#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-endpointinput)" : {{EndpointInput}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-syntax.yaml"></a>

```
  [BatchTransformInput](#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-batchtransforminput): {{
    BatchTransformInput}}
  [EndpointInput](#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-endpointinput): {{
    EndpointInput}}
```

## Properties
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-properties"></a>

`BatchTransformInput`  <a name="cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-batchtransforminput"></a>
Input object for the batch transform job.
*Required*: No
*Type*: [BatchTransformInput](aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointInput`  <a name="cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-endpointinput"></a>
Input object for the endpoint
*Required*: No
*Type*: [EndpointInput](aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
