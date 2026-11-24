---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-inferencerouter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceRouter

Creates an inference router. An inference router is a Regional SageMaker AI resource that sends each inference request to one of the endpoints or inference components that you list for a routing target. These destinations can be in any AWS account, and in any AWS Region in the same partition as the router.

The router's status is `Creating` until it's ready to use. SageMaker AI checks that each endpoint is a real-time or asynchronous endpoint, as the routing target requires, and rejects one of the wrong type. It checks endpoints in other accounts with your credentials, so the endpoint policy must allow `sagemaker:DescribeEndpoint`. SageMaker AI accepts an endpoint that it can't check, for example one that doesn't exist. Requests to it fail if it's the wrong type or doesn't exist. To see the status of each destination, call [DescribeInferenceRouter](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceRouter.html) and see the `RoutingStatus` of each destination.

To invoke the router, use `InvokeInferenceRouter` or `InvokeInferenceRouterAsync`. For information about inference routers, see [Route requests across Regions with inference routers](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router.html).

## Syntax
<a name="aws-resource-sagemaker-inferencerouter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-inferencerouter-syntax.json"></a>

```json
{
  "Type" : "AWS::SageMaker::InferenceRouter",
  "Properties" : {
      "[InferenceRouterName](#cfn-sagemaker-inferencerouter-inferenceroutername)" : {{String}},
      "[RoutingTargets](#cfn-sagemaker-inferencerouter-routingtargets)" : {{[ RoutingTarget, ... ]}},
      "[Tags](#cfn-sagemaker-inferencerouter-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-inferencerouter-syntax.yaml"></a>

```yaml
Type: AWS::SageMaker::InferenceRouter
Properties:
  [InferenceRouterName](#cfn-sagemaker-inferencerouter-inferenceroutername): {{String}}
  [RoutingTargets](#cfn-sagemaker-inferencerouter-routingtargets): {{
    - RoutingTarget}}
  [Tags](#cfn-sagemaker-inferencerouter-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-inferencerouter-properties"></a>

`InferenceRouterName`  <a name="cfn-sagemaker-inferencerouter-inferenceroutername"></a>
The name of the inference router.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoutingTargets`  <a name="cfn-sagemaker-inferencerouter-routingtargets"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [RoutingTarget](aws-properties-sagemaker-inferencerouter-routingtarget.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-inferencerouter-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-inferencerouter-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-inferencerouter-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-inferencerouter-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-inferencerouter-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-inferencerouter-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The date and time that the inference router was created.

`InferenceRouterArn`  <a name="InferenceRouterArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the inference router.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The date and time that the inference router was last updated.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.
