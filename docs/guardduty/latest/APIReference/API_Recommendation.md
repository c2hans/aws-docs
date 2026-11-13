---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Recommendation.html
---

# Recommendation
<a name="API_Recommendation"></a>

Contains a recommended action.

## Contents
<a name="API_Recommendation_Contents"></a>

 ** category **   <a name="guardduty-Type-Recommendation-category"></a>
The category of the recommendation. Possible values are `ENABLE_PROTECTION`, `FURTHER_INVESTIGATION`, `SUPPRESSION_RULE`, `HARDENING`, and `MONITORING`.
Type: String
Valid Values: `ENABLE_PROTECTION | FURTHER_INVESTIGATION | SUPPRESSION_RULE | HARDENING | MONITORING`
Required: No

 ** cliCommands **   <a name="guardduty-Type-Recommendation-cliCommands"></a>
 AWS CLI commands that you can run to carry out the recommendation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** priority **   <a name="guardduty-Type-Recommendation-priority"></a>
The priority of the recommendation. Possible values are `IMMEDIATE`, `SHORT_TERM`, and `STRATEGIC`.
Type: String
Valid Values: `IMMEDIATE | SHORT_TERM | STRATEGIC`
Required: No

 ** rationale **   <a name="guardduty-Type-Recommendation-rationale"></a>
The reason for the recommendation.
Type: String
Required: No

 ** title **   <a name="guardduty-Type-Recommendation-title"></a>
A short title for the recommendation.
Type: String
Required: No

## See Also
<a name="API_Recommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Recommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Recommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Recommendation)
