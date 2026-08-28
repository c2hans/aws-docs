---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CodeReviewJobSummary.html
---

# CodeReviewJobSummary
<a name="API_CodeReviewJobSummary"></a>

Contains summary information about a code review job.

## Contents
<a name="API_CodeReviewJobSummary_Contents"></a>

 ** codeReviewId **   <a name="securityagent-Type-CodeReviewJobSummary-codeReviewId"></a>
The unique identifier of the code review associated with the job.
Type: String
Required: Yes

 ** codeReviewJobId **   <a name="securityagent-Type-CodeReviewJobSummary-codeReviewJobId"></a>
The unique identifier of the code review job.
Type: String
Required: Yes

 ** createdAt **   <a name="securityagent-Type-CodeReviewJobSummary-createdAt"></a>
The date and time the code review job was created, in UTC format.
Type: Timestamp
Required: No

 ** status **   <a name="securityagent-Type-CodeReviewJobSummary-status"></a>
The current status of the code review job.
Type: String
Valid Values: `IN_PROGRESS | STOPPING | STOPPED | FAILED | COMPLETED`
Required: No

 ** title **   <a name="securityagent-Type-CodeReviewJobSummary-title"></a>
The title of the code review job.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-CodeReviewJobSummary-updatedAt"></a>
The date and time the code review job was last updated, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_CodeReviewJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CodeReviewJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CodeReviewJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CodeReviewJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
