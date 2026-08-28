---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PrefixAwareRoutingConfig.html
---

# PrefixAwareRoutingConfig
<a name="API_PrefixAwareRoutingConfig"></a>

The configuration for prefix-aware routing on a SageMaker real-time inference endpoint. Specify `PrefixLength` and `ConcurrencyThreshold` to control routing behavior.

## Contents
<a name="API_PrefixAwareRoutingConfig_Contents"></a>

 ** ConcurrencyThreshold **   <a name="sagemaker-Type-PrefixAwareRoutingConfig-ConcurrencyThreshold"></a>
The maximum number of in-flight requests on the target instance before the endpoint routes to another instance. Required when `RoutingStrategy` is `PREFIX_AWARE`. When in-flight requests on the prefix-selected instance reach this threshold, the endpoint routes the request to an instance with more available capacity.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** PrefixLength **   <a name="sagemaker-Type-PrefixAwareRoutingConfig-PrefixLength"></a>
The maximum length of the prefix used for routing decisions. Required when `RoutingStrategy` is `PREFIX_AWARE`.
+ For the SageMaker Runtime `InvokeEndpoint` and `InvokeEndpointWithResponseStream` APIs, this value specifies the number of bytes from the beginning of the request body.
+ For OpenAI-compatible API, this value specifies the number of characters from the text content of the messages array.
The endpoint routes requests that share the same prefix to the same instance. Set this value to cover shared content (such as system prompts) plus enough unique content to distribute workloads across instances.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65536.
Required: No

## See Also
<a name="API_PrefixAwareRoutingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PrefixAwareRoutingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PrefixAwareRoutingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PrefixAwareRoutingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
