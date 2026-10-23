---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_FlowVerdict.html
---

# FlowVerdict
<a name="API_FlowVerdict"></a>

Validation's verdict for one attack flow.

## Contents
<a name="API_FlowVerdict_Contents"></a>

 ** flowId **   <a name="continuum-Type-FlowVerdict-flowId"></a>
The identifier of the flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** verdict **   <a name="continuum-Type-FlowVerdict-verdict"></a>
The verdict.
Type: String
Valid Values: `CONFIRMED | DENIED | INCONCLUSIVE`
Required: Yes

 ** confidence **   <a name="continuum-Type-FlowVerdict-confidence"></a>
The confidence.
Type: Double
Required: No

 ** evidence **   <a name="continuum-Type-FlowVerdict-evidence"></a>
The evidence.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_FlowVerdict_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/FlowVerdict)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/FlowVerdict)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/FlowVerdict)
