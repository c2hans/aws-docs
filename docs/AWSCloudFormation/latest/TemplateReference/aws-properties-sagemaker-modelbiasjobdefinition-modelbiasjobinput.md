---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelBiasJobDefinition ModelBiasJobInput
<a name="aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput"></a>

Inputs for the model bias job.

## Syntax
<a name="aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput-syntax.json"></a>

```
{
  "[BatchTransformInput](#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-batchtransforminput)" : {{BatchTransformInput}},
  "[EndpointInput](#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-endpointinput)" : {{EndpointInput}},
  "[GroundTruthS3Input](#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-groundtruths3input)" : {{MonitoringGroundTruthS3Input}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput-syntax.yaml"></a>

```
  [BatchTransformInput](#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-batchtransforminput): {{
    BatchTransformInput}}
  [EndpointInput](#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-endpointinput): {{
    EndpointInput}}
  [GroundTruthS3Input](#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-groundtruths3input): {{
    MonitoringGroundTruthS3Input}}
```

## Properties
<a name="aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput-properties"></a>

`BatchTransformInput`  <a name="cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-batchtransforminput"></a>
Input object for the batch transform job.
*Required*: No
*Type*: [BatchTransformInput](aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointInput`  <a name="cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-endpointinput"></a>
Input object for the endpoint
*Required*: No
*Type*: [EndpointInput](aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroundTruthS3Input`  <a name="cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-groundtruths3input"></a>
Location of ground truth labels to use in model bias job.
*Required*: Yes
*Type*: [MonitoringGroundTruthS3Input](aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
