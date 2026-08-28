---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::DataQualityJobDefinition DataQualityJobInput
<a name="aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput"></a>

The input for the data quality monitoring job. Currently endpoints are supported for input.

## Syntax
<a name="aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput-syntax.json"></a>

```
{
  "[BatchTransformInput](#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput-batchtransforminput)" : {{BatchTransformInput}},
  "[EndpointInput](#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput-endpointinput)" : {{EndpointInput}}
}
```

### YAML
<a name="aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput-syntax.yaml"></a>

```
  [BatchTransformInput](#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput-batchtransforminput): {{
    BatchTransformInput}}
  [EndpointInput](#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput-endpointinput): {{
    EndpointInput}}
```

## Properties
<a name="aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput-properties"></a>

`BatchTransformInput`  <a name="cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput-batchtransforminput"></a>
Input object for the batch transform job.
*Required*: No
*Type*: [BatchTransformInput](aws-properties-sagemaker-dataqualityjobdefinition-batchtransforminput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointInput`  <a name="cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput-endpointinput"></a>
Input object for the endpoint
*Required*: No
*Type*: [EndpointInput](aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
