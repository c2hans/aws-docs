---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_InvestigationAction.html
---

# InvestigationAction
<a name="API_InvestigationAction"></a>

Represents a specific action or recommendation generated during a security investigation. Investigation actions provide guidance on steps to take in response to security incidents.

## Contents
<a name="API_InvestigationAction_Contents"></a>

 ** actionType **   <a name="securityir-Type-InvestigationAction-actionType"></a>
The type or category of the investigation action, indicating the nature of the recommended step (e.g., containment, remediation, analysis).
Type: String
Valid Values: `Evidence | Investigation | Summarization`
Required: Yes

 ** content **   <a name="securityir-Type-InvestigationAction-content"></a>
Detailed information about the investigation action, including specific steps, context, and guidance for implementation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Required: Yes

 ** investigationId **   <a name="securityir-Type-InvestigationAction-investigationId"></a>
The unique identifier of the investigation to which this action belongs.
Type: String
Pattern: `inv-[a-z0-9]{10,32}`
Required: Yes

 ** lastUpdated **   <a name="securityir-Type-InvestigationAction-lastUpdated"></a>
The timestamp when the investigation action was last modified or updated.
Type: Timestamp
Required: Yes

 ** status **   <a name="securityir-Type-InvestigationAction-status"></a>
The current status of the investigation action (e.g., pending, in progress, completed, dismissed).
Type: String
Valid Values: `Pending | InProgress | Waiting | Completed | Failed | Cancelled`
Required: Yes

 ** title **   <a name="securityir-Type-InvestigationAction-title"></a>
A brief, descriptive title summarizing the investigation action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** feedback **   <a name="securityir-Type-InvestigationAction-feedback"></a>
User feedback associated with this investigation action, including usefulness ratings and comments.
Type: [InvestigationFeedback](API_InvestigationFeedback.md) object
Required: No

## See Also
<a name="API_InvestigationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/InvestigationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/InvestigationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/InvestigationAction)
