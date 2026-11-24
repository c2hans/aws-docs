---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencerouter-routingtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceRouter RoutingTarget

A model that an inference router serves, and the destinations that can serve it. When you invoke the router, you name the routing target, and the router sends the request to one of its destinations.

Every destination in a routing target must serve the same model, with the same request and response format.

## Syntax
<a name="aws-properties-sagemaker-inferencerouter-routingtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencerouter-routingtarget-syntax.json"></a>

```json
{
  "[AsyncInferenceConfig](#cfn-sagemaker-inferencerouter-routingtarget-asyncinferenceconfig)" : {{AsyncInferenceConfig}},
  "[Destinations](#cfn-sagemaker-inferencerouter-routingtarget-destinations)" : {{[ Destination, ... ]}},
  "[Name](#cfn-sagemaker-inferencerouter-routingtarget-name)" : {{String}},
  "[RoutingPreference](#cfn-sagemaker-inferencerouter-routingtarget-routingpreference)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencerouter-routingtarget-syntax.yaml"></a>

```yaml
  [AsyncInferenceConfig](#cfn-sagemaker-inferencerouter-routingtarget-asyncinferenceconfig): {{
    AsyncInferenceConfig}}
  [Destinations](#cfn-sagemaker-inferencerouter-routingtarget-destinations): {{
    - Destination}}
  [Name](#cfn-sagemaker-inferencerouter-routingtarget-name): {{String}}
  [RoutingPreference](#cfn-sagemaker-inferencerouter-routingtarget-routingpreference): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferencerouter-routingtarget-properties"></a>

`AsyncInferenceConfig`  <a name="cfn-sagemaker-inferencerouter-routingtarget-asyncinferenceconfig"></a>
The asynchronous inference settings of the routing target. Specify this setting to make the routing target asynchronous. If you omit it, the routing target serves real-time requests.
Asynchronous routing targets aren't available in all AWS Regions. For information about asynchronous routing targets and Region availability, see [Send asynchronous requests through an inference router](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-async.html).
Because `UpdateInferenceRouter` replaces all routing targets, include this setting in every update of an asynchronous routing target.
For information about asynchronous routing targets, see [Send asynchronous requests through an inference router](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-async.html).
*Required*: No
*Type*: [AsyncInferenceConfig](aws-properties-sagemaker-inferencerouter-asyncinferenceconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destinations`  <a name="cfn-sagemaker-inferencerouter-routingtarget-destinations"></a>
The endpoints and inference components that serve the routing target. Each destination can appear only once in a routing target.
In an asynchronous routing target, every destination must be an asynchronous inference endpoint. In a real-time routing target, no destination can be one. SageMaker AI checks an endpoint in another account with your credentials, so both your IAM policy and the endpoint policy must allow `sagemaker:DescribeEndpoint`. If an endpoint can't be checked, for example because it isn't found or can't be read in time, it's accepted, and requests to it fail if it's the wrong mode.
*Required*: Yes
*Type*: Array of [Destination](aws-properties-sagemaker-inferencerouter-destination.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-inferencerouter-routingtarget-name"></a>
The name of the routing target. Callers specify this name in the `RoutingTargetName` parameter when they invoke the inference router. The name must be unique within the router.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoutingPreference`  <a name="cfn-sagemaker-inferencerouter-routingtarget-routingpreference"></a>
How the inference router chooses among the routing target's destinations. The default is `LocalRegionFirst`.
LocalRegionFirst
The router uses destinations in its own Region first. When the request leaves the Region, the router spreads it across healthy destinations in other Regions.
InstancePoolOrder
The router prefers destinations by instance type first and by Region second. Every destination must be an endpoint that lists the same two or more instance types, each with a different priority, in the same priority order. This value is supported only for asynchronous routing targets.
With either value, the router uses destinations whose health or capacity is reduced after the others, but doesn't exclude them.
*Required*: No
*Type*: String
*Allowed values*: `LocalRegionFirst | InstancePoolOrder`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
