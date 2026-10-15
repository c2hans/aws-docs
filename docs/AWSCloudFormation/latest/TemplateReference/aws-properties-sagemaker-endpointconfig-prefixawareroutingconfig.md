---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-prefixawareroutingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig PrefixAwareRoutingConfig
<a name="aws-properties-sagemaker-endpointconfig-prefixawareroutingconfig"></a>

The configuration for prefix-aware routing on a SageMaker real-time inference endpoint. Specify `PrefixLength` and `ConcurrencyThreshold` to control routing behavior.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-prefixawareroutingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-prefixawareroutingconfig-syntax.json"></a>

```
{
  "[ConcurrencyThreshold](#cfn-sagemaker-endpointconfig-prefixawareroutingconfig-concurrencythreshold)" : {{Integer}},
  "[PrefixLength](#cfn-sagemaker-endpointconfig-prefixawareroutingconfig-prefixlength)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-prefixawareroutingconfig-syntax.yaml"></a>

```
  [ConcurrencyThreshold](#cfn-sagemaker-endpointconfig-prefixawareroutingconfig-concurrencythreshold): {{Integer}}
  [PrefixLength](#cfn-sagemaker-endpointconfig-prefixawareroutingconfig-prefixlength): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-prefixawareroutingconfig-properties"></a>

`ConcurrencyThreshold`  <a name="cfn-sagemaker-endpointconfig-prefixawareroutingconfig-concurrencythreshold"></a>
The number of in-flight requests on the selected instance or inference component copy at which the endpoint routes a request to another copy or instance. Required when `RoutingStrategy` is `PREFIX_AWARE`.
On an endpoint without inference components, the endpoint compares this threshold with the number of in-flight requests on the selected instance. When that number reaches the threshold, the endpoint routes the request to another instance.
On an endpoint with inference components, the endpoint compares this threshold with the number of in-flight requests on the selected copy of the invoked inference component. Requests to other inference components on the same instance don't count. When the instance hosts more than one copy of the inference component, the endpoint routes requests that share a prefix to the same copy and, while that copy has reached the threshold, to another copy on the instance that is under the threshold. When every copy on the instance has reached the threshold, the endpoint routes the request to another instance.
The threshold applies to every instance and every copy of every inference component in the production variant, so choose a value that suits the instance or copy that can serve the fewest concurrent requests.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrefixLength`  <a name="cfn-sagemaker-endpointconfig-prefixawareroutingconfig-prefixlength"></a>
The maximum length of the prefix used for routing decisions. Required when `RoutingStrategy` is `PREFIX_AWARE`.
+ For the SageMaker Runtime `InvokeEndpoint` and `InvokeEndpointWithResponseStream` APIs, this value specifies the number of bytes from the beginning of the request body.
+ For OpenAI-compatible API, this value specifies the number of characters from the text content of the messages array.
The endpoint routes requests that share the same prefix to the same instance and, when that instance hosts more than one copy of the invoked inference component, to the same copy. Set this value to cover shared content (such as system prompts) plus enough unique content to distribute workloads across instances and copies.
*Required*: No
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65536`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
