---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationIndicator.html
---

# InvestigationIndicator
<a name="API_InvestigationIndicator"></a>

Contains a threat indicator, such as an IP address, a domain, or a file hash.

## Contents
<a name="API_InvestigationIndicator_Contents"></a>

 ** value **   <a name="guardduty-Type-InvestigationIndicator-value"></a>
The value of the indicator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** type **   <a name="guardduty-Type-InvestigationIndicator-type"></a>
The type of the indicator. Possible values are `IP`, `DOMAIN`, and `FILE`.
Type: String
Valid Values: `IP | DOMAIN | FILE`
Required: No

## See Also
<a name="API_InvestigationIndicator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationIndicator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationIndicator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationIndicator)
