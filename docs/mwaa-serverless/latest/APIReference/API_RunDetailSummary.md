---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_RunDetailSummary.html
---

# RunDetailSummary
<a name="API_RunDetailSummary"></a>

Summary information about a workflow run's execution details, including status and timing information.

## Contents
<a name="API_RunDetailSummary_Contents"></a>

 ** CreatedOn **   <a name="mwaaserverless-Type-RunDetailSummary-CreatedOn"></a>
The timestamp when the workflow run was created, in ISO 8601 date-time format.
Type: Timestamp
Required: No

 ** EndedAt **   <a name="mwaaserverless-Type-RunDetailSummary-EndedAt"></a>
The timestamp when the workflow run completed execution, in ISO 8601 date-time format. This value is null if the run is not complete.
Type: Timestamp
Required: No

 ** StartedAt **   <a name="mwaaserverless-Type-RunDetailSummary-StartedAt"></a>
The timestamp when the workflow run started execution, in ISO 8601 date-time format.
Type: Timestamp
Required: No

 ** Status **   <a name="mwaaserverless-Type-RunDetailSummary-Status"></a>
The current status of the workflow run.
Type: String
Valid Values: `STARTING | QUEUED | RUNNING | SUCCESS | FAILED | TIMEOUT | STOPPING | STOPPED`
Required: No

## See Also
<a name="API_RunDetailSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/RunDetailSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/RunDetailSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/RunDetailSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
