---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentSpecification
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification"></a>

Details about the resources to deploy with this inference component, including the model, container, and compute resources.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification-syntax.json"></a>

```
{
  "[BaseInferenceComponentName](#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-baseinferencecomponentname)" : {{String}},
  "[ComputeResourceRequirements](#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-computeresourcerequirements)" : {{InferenceComponentComputeResourceRequirements}},
  "[Container](#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-container)" : {{InferenceComponentContainerSpecification}},
  "[ModelName](#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-modelname)" : {{String}},
  "[StartupParameters](#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-startupparameters)" : {{InferenceComponentStartupParameters}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification-syntax.yaml"></a>

```
  [BaseInferenceComponentName](#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-baseinferencecomponentname): {{String}}
  [ComputeResourceRequirements](#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-computeresourcerequirements): {{
    InferenceComponentComputeResourceRequirements}}
  [Container](#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-container): {{
    InferenceComponentContainerSpecification}}
  [ModelName](#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-modelname): {{String}}
  [StartupParameters](#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-startupparameters): {{
    InferenceComponentStartupParameters}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification-properties"></a>

`BaseInferenceComponentName`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecification-baseinferencecomponentname"></a>
The name of an existing inference component that is to contain the inference component that you're creating with your request.
Specify this parameter only if your request is meant to create an adapter inference component. An adapter inference component contains the path to an adapter model. The purpose of the adapter model is to tailor the inference output of a base foundation model, which is hosted by the base inference component. The adapter inference component uses the compute resources that you assigned to the base inference component.
When you create an adapter inference component, use the `Container` parameter to specify the location of the adapter artifacts. In the parameter value, use the `ArtifactUrl` parameter of the `InferenceComponentContainerSpecification` data type.
Before you can create an adapter inference component, you must have an existing inference component that contains the foundation model that you want to adapt.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputeResourceRequirements`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecification-computeresourcerequirements"></a>
The compute resources allocated to run the model, plus any adapter models, that you assign to the inference component.
Omit this parameter if your request is meant to create an adapter inference component. An adapter inference component is loaded by a base inference component, and it uses the compute resources of the base inference component.
*Required*: No
*Type*: [InferenceComponentComputeResourceRequirements](aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Container`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecification-container"></a>
Defines a container that provides the runtime environment for a model that you deploy with an inference component.
*Required*: No
*Type*: [InferenceComponentContainerSpecification](aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelName`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecification-modelname"></a>
The name of an existing SageMaker AI model object in your account that you want to deploy with the inference component.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartupParameters`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentspecification-startupparameters"></a>
Settings that take effect while the model container starts up.
*Required*: No
*Type*: [InferenceComponentStartupParameters](aws-properties-sagemaker-inferencecomponent-inferencecomponentstartupparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
