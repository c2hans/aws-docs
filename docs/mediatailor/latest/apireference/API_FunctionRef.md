---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_FunctionRef.html
---

# FunctionRef
<a name="API_FunctionRef"></a>

A reference to a child function within a `SEQUENTIAL_EXECUTOR` function.

## Contents
<a name="API_FunctionRef_Contents"></a>

 ** Alias **   <a name="mediatailor-Type-FunctionRef-Alias"></a>
An optional alternate name for the function within the executor. If omitted, MediaTailor uses the function identifier.
Type: String
Required: No

 ** FunctionId **   <a name="mediatailor-Type-FunctionRef-FunctionId"></a>
The identifier of the child function to execute in this step.
Type: String
Required: No

 ** RunCondition **   <a name="mediatailor-Type-FunctionRef-RunCondition"></a>
An optional expression that evaluates to a boolean. MediaTailor evaluates this expression immediately before running the step, using the accumulated state at that point in the sequence. If the expression evaluates to `false`, MediaTailor skips the step and moves to the next one. If omitted, the step always runs.
Type: String
Required: No

## See Also
<a name="API_FunctionRef_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/FunctionRef)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/FunctionRef)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/FunctionRef)
