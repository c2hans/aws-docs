---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_Function.html
---

# Function
<a name="API_Function"></a>

Defines reusable logic that MediaTailor executes at lifecycle hooks during ad insertion. The `FunctionType` determines the function's runtime behavior. For more information about functions, see [Working with functions](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the *MediaTailor User Guide*.

## Contents
<a name="API_Function_Contents"></a>

 ** FunctionId **   <a name="mediatailor-Type-Function-FunctionId"></a>
The identifier of the function.
Type: String
Required: Yes

 ** FunctionType **   <a name="mediatailor-Type-Function-FunctionType"></a>
The type of the function.
Type: String
Valid Values: `HTTP_REQUEST | CUSTOM_OUTPUT | CONCURRENT_EXECUTOR | SEQUENTIAL_EXECUTOR`
Required: Yes

 ** Arn **   <a name="mediatailor-Type-Function-Arn"></a>
The Amazon Resource Name (ARN) of the function.
Type: String
Required: No

 ** ConcurrentExecutorConfiguration **   <a name="mediatailor-Type-Function-ConcurrentExecutorConfiguration"></a>
The configuration for a `CONCURRENT_EXECUTOR` function.
Type: [ConcurrentExecutorConfiguration](API_ConcurrentExecutorConfiguration.md) object
Required: No

 ** CustomOutputConfiguration **   <a name="mediatailor-Type-Function-CustomOutputConfiguration"></a>
The configuration for a `CUSTOM_OUTPUT` function.
Type: [CustomOutputConfiguration](API_CustomOutputConfiguration.md) object
Required: No

 ** Description **   <a name="mediatailor-Type-Function-Description"></a>
A description of the function.
Type: String
Required: No

 ** HttpRequestConfiguration **   <a name="mediatailor-Type-Function-HttpRequestConfiguration"></a>
The configuration for an `HTTP_REQUEST` function.
Type: [HttpRequestConfiguration](API_HttpRequestConfiguration.md) object
Required: No

 ** SequentialExecutorConfiguration **   <a name="mediatailor-Type-Function-SequentialExecutorConfiguration"></a>
The configuration for a `SEQUENTIAL_EXECUTOR` function.
Type: [SequentialExecutorConfiguration](API_SequentialExecutorConfiguration.md) object
Required: No

 ** tags **   <a name="mediatailor-Type-Function-tags"></a>
The tags assigned to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

## See Also
<a name="API_Function_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/Function)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/Function)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/Function)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
