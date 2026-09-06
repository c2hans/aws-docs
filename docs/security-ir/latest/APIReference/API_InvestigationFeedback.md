---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_InvestigationFeedback.html
---

# InvestigationFeedback
<a name="API_InvestigationFeedback"></a>

Contains user feedback about an investigation action, including ratings and comments to help improve investigation quality.

## Contents
<a name="API_InvestigationFeedback_Contents"></a>

 ** comment **   <a name="securityir-Type-InvestigationFeedback-comment"></a>
Optional text feedback providing additional details about the usefulness rating or suggestions for improvement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** submittedAt **   <a name="securityir-Type-InvestigationFeedback-submittedAt"></a>
The timestamp when the feedback was submitted.
Type: Timestamp
Required: No

 ** usefulness **   <a name="securityir-Type-InvestigationFeedback-usefulness"></a>
A rating indicating how useful the investigation action was to the user.
Type: String
Valid Values: `USEFUL | NOT_USEFUL`
Required: No

## See Also
<a name="API_InvestigationFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/InvestigationFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/InvestigationFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/InvestigationFeedback)
