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
The maximum number of in-flight requests on the target instance before the endpoint routes to another instance. Required when `RoutingStrategy` is `PREFIX_AWARE`. When in-flight requests on the prefix-selected instance reach this threshold, the endpoint routes the request to an instance with more available capacity.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrefixLength`  <a name="cfn-sagemaker-endpointconfig-prefixawareroutingconfig-prefixlength"></a>
The maximum length of the prefix used for routing decisions. Required when `RoutingStrategy` is `PREFIX_AWARE`.
+ For the SageMaker Runtime `InvokeEndpoint` and `InvokeEndpointWithResponseStream` APIs, this value specifies the number of bytes from the beginning of the request body.
+ For OpenAI-compatible API, this value specifies the number of characters from the text content of the messages array.
The endpoint routes requests that share the same prefix to the same instance. Set this value to cover shared content (such as system prompts) plus enough unique content to distribute workloads across instances.
*Required*: No
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65536`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
