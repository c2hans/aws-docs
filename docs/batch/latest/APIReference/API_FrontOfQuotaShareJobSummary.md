---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_FrontOfQuotaShareJobSummary.html
---

# FrontOfQuotaShareJobSummary
<a name="API_FrontOfQuotaShareJobSummary"></a>

An object that represents summary details for the first `RUNNABLE` job in a quota share.

## Contents
<a name="API_FrontOfQuotaShareJobSummary_Contents"></a>

 ** earliestTimeAtPosition **   <a name="Batch-Type-FrontOfQuotaShareJobSummary-earliestTimeAtPosition"></a>
The Unix timestamp (in milliseconds) for when the job transitioned to its current position in the quota share.
Type: Long
Required: No

 ** jobArn **   <a name="Batch-Type-FrontOfQuotaShareJobSummary-jobArn"></a>
The ARN for a job in a named quota share.
Type: String
Required: No

## See Also
<a name="API_FrontOfQuotaShareJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FrontOfQuotaShareJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FrontOfQuotaShareJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FrontOfQuotaShareJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
