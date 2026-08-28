---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_RescoreExecutionPlanSummary.html
---

# RescoreExecutionPlanSummary
<a name="API_Ranking_RescoreExecutionPlanSummary"></a>

Summary information for a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the `Rescore` API.

## Contents
<a name="API_Ranking_RescoreExecutionPlanSummary_Contents"></a>

 ** CreatedAt **   <a name="kendra-Type-Ranking_RescoreExecutionPlanSummary-CreatedAt"></a>
The Unix timestamp when the rescore execution plan was created.
Type: Timestamp
Required: No

 ** Id **   <a name="kendra-Type-Ranking_RescoreExecutionPlanSummary-Id"></a>
The identifier of the rescore execution plan.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`
Required: No

 ** Name **   <a name="kendra-Type-Ranking_RescoreExecutionPlanSummary-Name"></a>
The name of the rescore execution plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** Status **   <a name="kendra-Type-Ranking_RescoreExecutionPlanSummary-Status"></a>
The current status of the rescore execution plan. When the value is `ACTIVE`, the rescore execution plan is ready for use.
Type: String
Valid Values: `CREATING | UPDATING | ACTIVE | DELETING | FAILED`
Required: No

 ** UpdatedAt **   <a name="kendra-Type-Ranking_RescoreExecutionPlanSummary-UpdatedAt"></a>
The Unix timestamp when the rescore execution plan was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Ranking_RescoreExecutionPlanSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-ranking-2022-10-19/RescoreExecutionPlanSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-ranking-2022-10-19/RescoreExecutionPlanSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-ranking-2022-10-19/RescoreExecutionPlanSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
