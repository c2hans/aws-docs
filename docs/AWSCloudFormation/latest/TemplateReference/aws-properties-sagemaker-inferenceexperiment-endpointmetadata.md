---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferenceexperiment-endpointmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceExperiment EndpointMetadata
<a name="aws-properties-sagemaker-inferenceexperiment-endpointmetadata"></a>

The metadata of the endpoint.

## Syntax
<a name="aws-properties-sagemaker-inferenceexperiment-endpointmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferenceexperiment-endpointmetadata-syntax.json"></a>

```
{
  "[EndpointConfigName](#cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointconfigname)" : {{String}},
  "[EndpointName](#cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointname)" : {{String}},
  "[EndpointStatus](#cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferenceexperiment-endpointmetadata-syntax.yaml"></a>

```
  [EndpointConfigName](#cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointconfigname): {{String}}
  [EndpointName](#cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointname): {{String}}
  [EndpointStatus](#cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointstatus): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferenceexperiment-endpointmetadata-properties"></a>

`EndpointConfigName`  <a name="cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointconfigname"></a>
The name of the endpoint configuration.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointName`  <a name="cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointname"></a>
The name of the endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointStatus`  <a name="cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointstatus"></a>
 The status of the endpoint. For possible values of the status of an endpoint, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-endpointmetadata.html#cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointstatus](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-endpointmetadata.html#cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointstatus).
*Required*: No
*Type*: String
*Allowed values*: `Creating | Updating | SystemUpdating | RollingBack | InService | OutOfService | Deleting | Failed`
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
