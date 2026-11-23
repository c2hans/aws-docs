---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_ContextFilter.html
---

# ContextFilter

A filter that matches revenue attributions by a context key and, optionally, a set of values.

## Contents
<a name="API_prm_ContextFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="AWSPartnerCentral-Type-prm_ContextFilter-Key"></a>
The context key to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: Yes

 ** Values **   <a name="AWSPartnerCentral-Type-prm_ContextFilter-Values"></a>
The context values to match. A revenue attribution matches when its value for the key equals any of these values. If omitted, a revenue attribution matches when the key is present.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\x20-\x7E]+`
Required: No

## See Also
<a name="API_prm_ContextFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/ContextFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/ContextFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/ContextFilter)
