---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ModelSummary.html
---

# ModelSummary
<a name="API_ModelSummary"></a>

Summary information about an available AI model.

## Contents
<a name="API_ModelSummary_Contents"></a>

 ** minimumCompatibilityVersion **   <a name="novaact-Type-ModelSummary-minimumCompatibilityVersion"></a>
The minimum client compatibility version required to use this model.
Type: Integer
Required: Yes

 ** modelId **   <a name="novaact-Type-ModelSummary-modelId"></a>
The unique identifier of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** modelLifecycle **   <a name="novaact-Type-ModelSummary-modelLifecycle"></a>
The lifecycle information for the model.
Type: [ModelLifecycle](API_ModelLifecycle.md) object
Required: Yes

## See Also
<a name="API_ModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/ModelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/ModelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ModelSummary)
