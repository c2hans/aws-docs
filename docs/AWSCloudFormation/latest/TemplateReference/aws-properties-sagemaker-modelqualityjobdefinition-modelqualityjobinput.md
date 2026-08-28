---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelQualityJobDefinition ModelQualityJobInput
<a name="aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput"></a>

The input for the model quality monitoring job. Currently endpoints are supported for input for model quality monitoring jobs.

## Syntax
<a name="aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput-syntax.json"></a>

```
{
  "[BatchTransformInput](#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-batchtransforminput)" : {{BatchTransformInput}},
  "[EndpointInput](#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-endpointinput)" : {{EndpointInput}},
  "[GroundTruthS3Input](#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-groundtruths3input)" : {{MonitoringGroundTruthS3Input}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput-syntax.yaml"></a>

```
  [BatchTransformInput](#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-batchtransforminput): {{
    BatchTransformInput}}
  [EndpointInput](#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-endpointinput): {{
    EndpointInput}}
  [GroundTruthS3Input](#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-groundtruths3input): {{
    MonitoringGroundTruthS3Input}}
```

## Properties
<a name="aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput-properties"></a>

`BatchTransformInput`  <a name="cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-batchtransforminput"></a>
Input object for the batch transform job.
*Required*: No
*Type*: [BatchTransformInput](aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointInput`  <a name="cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-endpointinput"></a>
Input object for the endpoint
*Required*: No
*Type*: [EndpointInput](aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroundTruthS3Input`  <a name="cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-groundtruths3input"></a>
The ground truth label provided for the model.
*Required*: Yes
*Type*: [MonitoringGroundTruthS3Input](aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
