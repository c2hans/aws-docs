---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormAIVersionLifecycle.html
---

# EvaluationFormAIVersionLifecycle
<a name="API_EvaluationFormAIVersionLifecycle"></a>

Contains the status and availability dates for an AI version, indicating when the version became active and when it reaches end of life.

## Contents
<a name="API_EvaluationFormAIVersionLifecycle_Contents"></a>

 ** StartOfLifeTime **   <a name="connect-Type-EvaluationFormAIVersionLifecycle-StartOfLifeTime"></a>
The timestamp for when this AI version became available.
Type: Timestamp
Required: Yes

 ** Status **   <a name="connect-Type-EvaluationFormAIVersionLifecycle-Status"></a>
The status of the AI version. Valid values:
+  `Latest` - The most recent AI version.
+  `Preview` - An AI version available for preview.
+  `Active` - An AI version that is currently available.
+  `Deprecated` - An AI version that is no longer recommended for use.
+  `Removed` - An AI version that is no longer available.
Type: String
Valid Values: `LATEST | PREVIEW | ACTIVE | DEPRECATED`
Required: Yes

 ** EndOfLifeTime **   <a name="connect-Type-EvaluationFormAIVersionLifecycle-EndOfLifeTime"></a>
The timestamp when this AI version reaches or reached end of life.
Type: Timestamp
Required: No

## See Also
<a name="API_EvaluationFormAIVersionLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormAIVersionLifecycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormAIVersionLifecycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormAIVersionLifecycle)
