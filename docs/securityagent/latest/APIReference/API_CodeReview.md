---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CodeReview.html
---

# CodeReview
<a name="API_CodeReview"></a>

Represents a code review configuration that defines the parameters for automated security-focused code analysis, including target assets and logging configuration.

## Contents
<a name="API_CodeReview_Contents"></a>

 ** agentSpaceId **   <a name="securityagent-Type-CodeReview-agentSpaceId"></a>
The unique identifier of the agent space that contains the code review.
Type: String
Required: Yes

 ** assets **   <a name="securityagent-Type-CodeReview-assets"></a>
The assets included in the code review.
Type: [Assets](API_Assets.md) object
Required: Yes

 ** codeReviewId **   <a name="securityagent-Type-CodeReview-codeReviewId"></a>
The unique identifier of the code review.
Type: String
Required: Yes

 ** title **   <a name="securityagent-Type-CodeReview-title"></a>
The title of the code review.
Type: String
Required: Yes

 ** codeRemediationStrategy **   <a name="securityagent-Type-CodeReview-codeRemediationStrategy"></a>
The code remediation strategy for the code review.
Type: String
Valid Values: `AUTOMATIC | DISABLED`
Required: No

 ** createdAt **   <a name="securityagent-Type-CodeReview-createdAt"></a>
The date and time the code review was created, in UTC format.
Type: Timestamp
Required: No

 ** logConfig **   <a name="securityagent-Type-CodeReview-logConfig"></a>
The CloudWatch Logs configuration for the code review.
Type: [CloudWatchLog](API_CloudWatchLog.md) object
Required: No

 ** serviceRole **   <a name="securityagent-Type-CodeReview-serviceRole"></a>
The IAM service role used for the code review.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-CodeReview-updatedAt"></a>
The date and time the code review was last updated, in UTC format.
Type: Timestamp
Required: No

 ** validationMode **   <a name="securityagent-Type-CodeReview-validationMode"></a>
The validation mode for the code review. Valid values are SIMULATED and DISABLED.
Type: String
Valid Values: `DISABLED | SIMULATED`
Required: No

## See Also
<a name="API_CodeReview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CodeReview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CodeReview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CodeReview)
