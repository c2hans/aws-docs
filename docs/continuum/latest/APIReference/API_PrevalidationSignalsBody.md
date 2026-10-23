---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_PrevalidationSignalsBody.html
---

# PrevalidationSignalsBody
<a name="API_PrevalidationSignalsBody"></a>

Projected content for an EVIDENCE artifact carrying prioritization's prevalidation signals.

## Contents
<a name="API_PrevalidationSignalsBody_Contents"></a>

 ** producedBy **   <a name="continuum-Type-PrevalidationSignalsBody-producedBy"></a>
The produced By.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_.-]{0,127}`
Required: No

 ** signals **   <a name="continuum-Type-PrevalidationSignalsBody-signals"></a>
The signals.
Type: Array of [PrevalidationSignal](API_PrevalidationSignal.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_PrevalidationSignalsBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/PrevalidationSignalsBody)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/PrevalidationSignalsBody)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/PrevalidationSignalsBody)
