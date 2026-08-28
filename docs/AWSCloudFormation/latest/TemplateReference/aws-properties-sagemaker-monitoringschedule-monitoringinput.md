---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedule-monitoringinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringSchedule MonitoringInput
<a name="aws-properties-sagemaker-monitoringschedule-monitoringinput"></a>

The inputs for a monitoring job.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedule-monitoringinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedule-monitoringinput-syntax.json"></a>

```
{
  "[BatchTransformInput](#cfn-sagemaker-monitoringschedule-monitoringinput-batchtransforminput)" : {{BatchTransformInput}},
  "[EndpointInput](#cfn-sagemaker-monitoringschedule-monitoringinput-endpointinput)" : {{EndpointInput}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedule-monitoringinput-syntax.yaml"></a>

```
  [BatchTransformInput](#cfn-sagemaker-monitoringschedule-monitoringinput-batchtransforminput): {{
    BatchTransformInput}}
  [EndpointInput](#cfn-sagemaker-monitoringschedule-monitoringinput-endpointinput): {{
    EndpointInput}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedule-monitoringinput-properties"></a>

`BatchTransformInput`  <a name="cfn-sagemaker-monitoringschedule-monitoringinput-batchtransforminput"></a>
Input object for the batch transform job.
*Required*: No
*Type*: [BatchTransformInput](aws-properties-sagemaker-monitoringschedule-batchtransforminput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointInput`  <a name="cfn-sagemaker-monitoringschedule-monitoringinput-endpointinput"></a>
The endpoint for a monitoring job.
*Required*: No
*Type*: [EndpointInput](aws-properties-sagemaker-monitoringschedule-endpointinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
