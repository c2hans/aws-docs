---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentSpecificationForInstanceType
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype"></a>

<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-description"></a>The `InferenceComponentSpecificationForInstanceType` property type specifies Property description not available. for an [AWS::SageMaker::InferenceComponent](aws-resource-sagemaker-inferencecomponent.md).

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-syntax.json"></a>

```
{
  "[ComputeResourceRequirements](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-computeresourcerequirements)" : {{InferenceComponentComputeResourceRequirements}},
  "[Container](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-container)" : {{InferenceComponentContainerSpecificationForInstanceType}},
  "[CurrentDataCacheConfig](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-currentdatacacheconfig)" : {{InferenceComponentDataCacheConfig}},
  "[DataCacheConfig](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-datacacheconfig)" : {{InferenceComponentDataCacheConfig}},
  "[InstanceType](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-instancetype)" : {{String}},
  "[ModelName](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-modelname)" : {{String}},
  "[SchedulingConfig](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-schedulingconfig)" : {{InferenceComponentSchedulingConfig}},
  "[StartupParameters](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-startupparameters)" : {{InferenceComponentStartupParameters}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-syntax.yaml"></a>

```
  [ComputeResourceRequirements](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-computeresourcerequirements): {{
    InferenceComponentComputeResourceRequirements}}
  [Container](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-container): {{
    InferenceComponentContainerSpecificationForInstanceType}}
  [CurrentDataCacheConfig](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-currentdatacacheconfig): {{
    InferenceComponentDataCacheConfig}}
  [DataCacheConfig](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-datacacheconfig): {{
    InferenceComponentDataCacheConfig}}
  [InstanceType](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-instancetype): {{String}}
  [ModelName](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-modelname): {{String}}
  [SchedulingConfig](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-schedulingconfig): {{
    InferenceComponentSchedulingConfig}}
  [StartupParameters](#cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-startupparameters): {{
    InferenceComponentStartupParameters}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-properties"></a>

`ComputeResourceRequirements`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-computeresourcerequirements"></a>
Property description not available.
*Required*: No
*Type*: [InferenceComponentComputeResourceRequirements](aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Container`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-container"></a>
Property description not available.
*Required*: No
*Type*: [InferenceComponentContainerSpecificationForInstanceType](aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecificationforinstancetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CurrentDataCacheConfig`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-currentdatacacheconfig"></a>
Property description not available.
*Required*: No
*Type*: [InferenceComponentDataCacheConfig](aws-properties-sagemaker-inferencecomponent-inferencecomponentdatacacheconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataCacheConfig`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-datacacheconfig"></a>
Property description not available.
*Required*: No
*Type*: [InferenceComponentDataCacheConfig](aws-properties-sagemaker-inferencecomponent-inferencecomponentdatacacheconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-instancetype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^ml\..*`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelName`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-modelname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchedulingConfig`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-schedulingconfig"></a>
Property description not available.
*Required*: No
*Type*: [InferenceComponentSchedulingConfig](aws-properties-sagemaker-inferencecomponent-inferencecomponentschedulingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartupParameters`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecificationforinstancetype-startupparameters"></a>
Property description not available.
*Required*: No
*Type*: [InferenceComponentStartupParameters](aws-properties-sagemaker-inferencecomponent-inferencecomponentstartupparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
