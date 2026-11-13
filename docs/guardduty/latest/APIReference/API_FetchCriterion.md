---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FetchCriterion.html
---

# FetchCriterion
<a name="API_FetchCriterion"></a>

Contains a filter condition that GuardDuty applied when it retrieved data.

## Contents
<a name="API_FetchCriterion_Contents"></a>

 ** condition **   <a name="guardduty-Type-FetchCriterion-condition"></a>
The comparison operator of the condition. Possible values are `EQUALS`, `NOT_EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL`, `LESS_THAN`, and `LESS_THAN_OR_EQUAL`.
Type: String
Valid Values: `EQUALS | NOT_EQUALS | GREATER_THAN | GREATER_THAN_OR_EQUAL | LESS_THAN | LESS_THAN_OR_EQUAL`
Required: Yes

 ** field **   <a name="guardduty-Type-FetchCriterion-field"></a>
The name of the field that the condition applies to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** values **   <a name="guardduty-Type-FetchCriterion-values"></a>
The values that the field is compared against. Numeric and Boolean values are represented as strings.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_FetchCriterion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FetchCriterion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FetchCriterion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FetchCriterion)
