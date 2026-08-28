---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-inferencecomponent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent
<a name="aws-resource-sagemaker-inferencecomponent"></a>

Creates an inference component, which is a SageMaker AI hosting object that you can use to deploy a model to an endpoint. In the inference component settings, you specify the model, the endpoint, and how the model utilizes the resources that the endpoint hosts. You can optimize resource utilization by tailoring how the required CPU cores, accelerators, and memory are allocated. You can deploy multiple inference components to an endpoint, where each inference component contains one model and the resource utilization needs for that individual model. After you deploy an inference component, you can directly invoke the associated model when you use the InvokeEndpoint API action.

## Syntax
<a name="aws-resource-sagemaker-inferencecomponent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-inferencecomponent-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::InferenceComponent",
  "Properties" : {
      "[DeploymentConfig](#cfn-sagemaker-inferencecomponent-deploymentconfig)" : {{InferenceComponentDeploymentConfig}},
      "[EndpointArn](#cfn-sagemaker-inferencecomponent-endpointarn)" : {{String}},
      "[EndpointName](#cfn-sagemaker-inferencecomponent-endpointname)" : {{String}},
      "[InferenceComponentName](#cfn-sagemaker-inferencecomponent-inferencecomponentname)" : {{String}},
      "[RuntimeConfig](#cfn-sagemaker-inferencecomponent-runtimeconfig)" : {{InferenceComponentRuntimeConfig}},
      "[Specification](#cfn-sagemaker-inferencecomponent-specification)" : {{InferenceComponentSpecification}},
      "[Tags](#cfn-sagemaker-inferencecomponent-tags)" : {{[ Tag, ... ]}},
      "[VariantName](#cfn-sagemaker-inferencecomponent-variantname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-inferencecomponent-syntax.yaml"></a>

```
Type: AWS::SageMaker::InferenceComponent
Properties:
  [DeploymentConfig](#cfn-sagemaker-inferencecomponent-deploymentconfig): {{
    InferenceComponentDeploymentConfig}}
  [EndpointArn](#cfn-sagemaker-inferencecomponent-endpointarn): {{String}}
  [EndpointName](#cfn-sagemaker-inferencecomponent-endpointname): {{String}}
  [InferenceComponentName](#cfn-sagemaker-inferencecomponent-inferencecomponentname): {{String}}
  [RuntimeConfig](#cfn-sagemaker-inferencecomponent-runtimeconfig): {{
    InferenceComponentRuntimeConfig}}
  [Specification](#cfn-sagemaker-inferencecomponent-specification): {{
    InferenceComponentSpecification}}
  [Tags](#cfn-sagemaker-inferencecomponent-tags): {{
    - Tag}}
  [VariantName](#cfn-sagemaker-inferencecomponent-variantname): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-inferencecomponent-properties"></a>

`DeploymentConfig`  <a name="cfn-sagemaker-inferencecomponent-deploymentconfig"></a>
The deployment configuration for an endpoint, which contains the desired deployment strategy and rollback configurations.
*Required*: No
*Type*: [InferenceComponentDeploymentConfig](aws-properties-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointArn`  <a name="cfn-sagemaker-inferencecomponent-endpointarn"></a>
The Amazon Resource Name (ARN) of the endpoint that hosts the inference component.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointName`  <a name="cfn-sagemaker-inferencecomponent-endpointname"></a>
The name of the endpoint that hosts the inference component.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InferenceComponentName`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentname"></a>
The name of the inference component.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeConfig`  <a name="cfn-sagemaker-inferencecomponent-runtimeconfig"></a>
Runtime settings for the inference component, including the number of copies to deploy.
*Required*: No
*Type*: [InferenceComponentRuntimeConfig](aws-properties-sagemaker-inferencecomponent-inferencecomponentruntimeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Specification`  <a name="cfn-sagemaker-inferencecomponent-specification"></a>
The specification for the inference component, including the model and container configuration.
*Required*: Yes
*Type*: [InferenceComponentSpecification](aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-inferencecomponent-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-inferencecomponent-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VariantName`  <a name="cfn-sagemaker-inferencecomponent-variantname"></a>
The name of the production variant that hosts the inference component.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-inferencecomponent-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-inferencecomponent-return-values-ref"></a>

 When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the inference component.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-inferencecomponent-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-inferencecomponent-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time when the inference component was created.

`FailureReason`  <a name="FailureReason-fn::getatt"></a>
The reason why the inference component failed, if applicable.

`InferenceComponentArn`  <a name="InferenceComponentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the inference component.

`InferenceComponentStatus`  <a name="InferenceComponentStatus-fn::getatt"></a>
The status of the inference component.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time when the inference component was last updated.

`RuntimeConfig.CurrentCopyCount`  <a name="RuntimeConfig.CurrentCopyCount-fn::getatt"></a>
The number of runtime copies of the model container that are currently deployed.

`RuntimeConfig.DesiredCopyCount`  <a name="RuntimeConfig.DesiredCopyCount-fn::getatt"></a>
The number of runtime copies of the model container that you requested to deploy with the inference component.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
