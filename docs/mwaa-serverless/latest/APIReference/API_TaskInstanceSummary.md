---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_TaskInstanceSummary.html
---

# TaskInstanceSummary
<a name="API_TaskInstanceSummary"></a>

Summary information about a task instance within a workflow run, including its status and execution details.

## Contents
<a name="API_TaskInstanceSummary_Contents"></a>

 ** DurationInSeconds **   <a name="mwaaserverless-Type-TaskInstanceSummary-DurationInSeconds"></a>
The duration of the task instance execution in seconds. This value is null if the task is not complete.
Type: Integer
Required: No

 ** OperatorName **   <a name="mwaaserverless-Type-TaskInstanceSummary-OperatorName"></a>
The name of the Apache Airflow operator used for this task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** RunId **   <a name="mwaaserverless-Type-TaskInstanceSummary-RunId"></a>
The unique identifier of the workflow run that contains this task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`
Required: No

 ** Status **   <a name="mwaaserverless-Type-TaskInstanceSummary-Status"></a>
The current status of the task instance.
Type: String
Valid Values: `QUEUED | FAILED | SCHEDULED | RUNNING | SUCCESS | UP_FOR_RESCHEDULE | UP_FOR_RETRY | UPSTREAM_FAILED | REMOVED | RESTARTING | DEFERRED | NONE | CANCELLED | TIMEOUT`
Required: No

 ** TaskInstanceId **   <a name="mwaaserverless-Type-TaskInstanceSummary-TaskInstanceId"></a>
The unique identifier of this task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`
Required: No

 ** WorkflowArn **   <a name="mwaaserverless-Type-TaskInstanceSummary-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow that contains this task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`
Required: No

 ** WorkflowVersion **   <a name="mwaaserverless-Type-TaskInstanceSummary-WorkflowVersion"></a>
The version of the workflow that contains this task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.+`
Required: No

## See Also
<a name="API_TaskInstanceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/TaskInstanceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/TaskInstanceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/TaskInstanceSummary)
