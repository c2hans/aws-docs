---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SequentialExecutorConfiguration.html
---

# SequentialExecutorConfiguration
<a name="API_SequentialExecutorConfiguration"></a>

The configuration for a `SEQUENTIAL_EXECUTOR` function. A `SEQUENTIAL_EXECUTOR` runs a sequence of child functions in order, passing data between steps through temporary data. For more information, see [SEQUENTIAL\_EXECUTOR](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types-sequential-executor.html) in the *MediaTailor User Guide*.

## Contents
<a name="API_SequentialExecutorConfiguration_Contents"></a>

 ** FunctionList **   <a name="mediatailor-Type-SequentialExecutorConfiguration-FunctionList"></a>
An ordered list of 1 to 10 steps. Each step specifies a child function to execute and an optional run condition expression that controls whether the step runs. MediaTailor executes steps in order, passing data between steps through temporary data.
Type: Array of [FunctionRef](API_FunctionRef.md) objects
Required: Yes

 ** Runtime **   <a name="mediatailor-Type-SequentialExecutorConfiguration-Runtime"></a>
The expression language used to evaluate expressions in the function configuration. Set this to `JSONata`.
Type: String
Valid Values: `JSONATA`
Required: Yes

 ** TimeoutMilliseconds **   <a name="mediatailor-Type-SequentialExecutorConfiguration-TimeoutMilliseconds"></a>
The maximum time, in milliseconds, for the entire sequence to complete. This timeout covers all steps, including any HTTP calls made by child functions. If the sequence exceeds this timeout, MediaTailor discards all output from the sequence and proceeds with default behavior.
Type: Integer
Required: Yes

 ** Output **   <a name="mediatailor-Type-SequentialExecutorConfiguration-Output"></a>
An optional map of output bindings that controls which bindings the sequence commits to the session state after all steps complete. If omitted, MediaTailor commits all accumulated output bindings from all child steps.
Type: String to string map
Required: No

## See Also
<a name="API_SequentialExecutorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/SequentialExecutorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/SequentialExecutorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/SequentialExecutorConfiguration)
