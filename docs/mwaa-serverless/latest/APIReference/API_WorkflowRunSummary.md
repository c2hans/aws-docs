---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_WorkflowRunSummary.html
---

# WorkflowRunSummary
<a name="API_WorkflowRunSummary"></a>

Summary information about a workflow run, including basic identification and status information.

## Contents
<a name="API_WorkflowRunSummary_Contents"></a>

 ** RunDetailSummary **   <a name="mwaaserverless-Type-WorkflowRunSummary-RunDetailSummary"></a>
Summary details about the workflow run execution.
Type: [RunDetailSummary](API_RunDetailSummary.md) object
Required: No

 ** RunId **   <a name="mwaaserverless-Type-WorkflowRunSummary-RunId"></a>
The unique identifier of the workflow run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`
Required: No

 ** RunType **   <a name="mwaaserverless-Type-WorkflowRunSummary-RunType"></a>
The type of workflow run.
Type: String
Valid Values: `ON_DEMAND | SCHEDULED`
Required: No

 ** WorkflowArn **   <a name="mwaaserverless-Type-WorkflowRunSummary-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow that contains this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`
Required: No

 ** WorkflowVersion **   <a name="mwaaserverless-Type-WorkflowRunSummary-WorkflowVersion"></a>
The version of the workflow used for this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.+`
Required: No

## See Also
<a name="API_WorkflowRunSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/WorkflowRunSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/WorkflowRunSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/WorkflowRunSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
