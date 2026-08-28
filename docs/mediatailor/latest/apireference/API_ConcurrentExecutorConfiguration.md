---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ConcurrentExecutorConfiguration.html
---

# ConcurrentExecutorConfiguration
<a name="API_ConcurrentExecutorConfiguration"></a>

The configuration for a `CONCURRENT_EXECUTOR` function. A `CONCURRENT_EXECUTOR` runs a set of child functions in parallel, up to a maximum concurrency, and combines their output when all functions complete. For more information about functions, see [Working with functions](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the *MediaTailor User Guide*.

## Contents
<a name="API_ConcurrentExecutorConfiguration_Contents"></a>

 ** FunctionList **   <a name="mediatailor-Type-ConcurrentExecutorConfiguration-FunctionList"></a>
The list of child functions that MediaTailor runs in parallel. Each entry specifies a child function to execute and an optional run condition expression that controls whether the function runs.
Type: Array of [FunctionRef](API_FunctionRef.md) objects
Required: Yes

 ** MaxConcurrency **   <a name="mediatailor-Type-ConcurrentExecutorConfiguration-MaxConcurrency"></a>
The maximum number of child functions that MediaTailor runs simultaneously. When the list contains more functions than `MaxConcurrency`, MediaTailor starts additional functions as running ones complete, so that no more than `MaxConcurrency` functions run at the same time.
Type: Integer
Required: Yes

 ** Output **   <a name="mediatailor-Type-ConcurrentExecutorConfiguration-Output"></a>
A map of output bindings that controls which bindings the executor commits to the session state after all child functions complete. Each key is a namespaced output path, and each value is an expression that MediaTailor evaluates against the combined results of the child functions.
Type: String to string map
Required: Yes

 ** Runtime **   <a name="mediatailor-Type-ConcurrentExecutorConfiguration-Runtime"></a>
The expression language used to evaluate expressions in the function configuration. Set this to `JSONata`.
Type: String
Valid Values: `JSONATA`
Required: Yes

 ** TimeoutMilliseconds **   <a name="mediatailor-Type-ConcurrentExecutorConfiguration-TimeoutMilliseconds"></a>
The maximum time, in milliseconds, for all child functions to complete. This timeout covers every function in the list, including any HTTP calls the child functions make. If the executor exceeds this timeout, MediaTailor discards all output from the executor and proceeds with default behavior.
Type: Integer
Required: Yes

## See Also
<a name="API_ConcurrentExecutorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ConcurrentExecutorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ConcurrentExecutorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ConcurrentExecutorConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
