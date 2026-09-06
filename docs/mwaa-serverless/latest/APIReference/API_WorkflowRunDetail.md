---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_WorkflowRunDetail.html
---

# WorkflowRunDetail
<a name="API_WorkflowRunDetail"></a>

Detailed information about a workflow run execution, including timing, status, error information, and associated task instances. This structure provides comprehensive visibility into the workflow execution lifecycle within the Amazon Managed Workflows for Apache Airflow Serverless serverless environment. The service tracks execution across distributed ECS worker tasks and provides detailed timing information, error diagnostics, and task instance relationships to support effective monitoring and troubleshooting of complex workflow executions.

## Contents
<a name="API_WorkflowRunDetail_Contents"></a>

 ** CompletedOn **   <a name="mwaaserverless-Type-WorkflowRunDetail-CompletedOn"></a>
The timestamp when the workflow run completed execution, in ISO 8601 date-time format. This value is null if the run is not complete.
Type: Timestamp
Required: No

 ** CreatedAt **   <a name="mwaaserverless-Type-WorkflowRunDetail-CreatedAt"></a>
The timestamp when the workflow run was created, in ISO 8601 date-time format.
Type: Timestamp
Required: No

 ** Duration **   <a name="mwaaserverless-Type-WorkflowRunDetail-Duration"></a>
The total duration of the workflow run execution in seconds. This value is null if the run is not complete.
Type: Integer
Required: No

 ** ErrorMessage **   <a name="mwaaserverless-Type-WorkflowRunDetail-ErrorMessage"></a>
The error message if the workflow run failed. This value is null if the run completed successfully.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** ModifiedAt **   <a name="mwaaserverless-Type-WorkflowRunDetail-ModifiedAt"></a>
The timestamp when the workflow run was last modified, in ISO 8601 date-time format.
Type: Timestamp
Required: No

 ** RunId **   <a name="mwaaserverless-Type-WorkflowRunDetail-RunId"></a>
The unique identifier of this workflow run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`
Required: No

 ** RunState **   <a name="mwaaserverless-Type-WorkflowRunDetail-RunState"></a>
The current execution state of the workflow run.
Type: String
Valid Values: `STARTING | QUEUED | RUNNING | SUCCESS | FAILED | TIMEOUT | STOPPING | STOPPED`
Required: No

 ** RunType **   <a name="mwaaserverless-Type-WorkflowRunDetail-RunType"></a>
The type of workflow run.
Type: String
Valid Values: `ON_DEMAND | SCHEDULED`
Required: No

 ** StartedOn **   <a name="mwaaserverless-Type-WorkflowRunDetail-StartedOn"></a>
The timestamp when the workflow run started execution, in ISO 8601 date-time format.
Type: Timestamp
Required: No

 ** TaskInstances **   <a name="mwaaserverless-Type-WorkflowRunDetail-TaskInstances"></a>
A list of task instance IDs that are part of this workflow run.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`
Required: No

 ** WorkflowArn **   <a name="mwaaserverless-Type-WorkflowRunDetail-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow that contains this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`
Required: No

 ** WorkflowVersion **   <a name="mwaaserverless-Type-WorkflowRunDetail-WorkflowVersion"></a>
The version of the workflow used for this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.+`
Required: No

## See Also
<a name="API_WorkflowRunDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/WorkflowRunDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/WorkflowRunDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/WorkflowRunDetail)
