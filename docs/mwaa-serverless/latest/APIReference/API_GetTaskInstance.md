---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_GetTaskInstance.html
---

# GetTaskInstance
<a name="API_GetTaskInstance"></a>

Retrieves detailed information about a specific task instance within a workflow run. Task instances represent individual tasks that are executed as part of a workflow in the Amazon Managed Workflows for Apache Airflow Serverless environment. Each task instance runs in an isolated ECS container with dedicated resources and security boundaries. The service tracks task execution state, retry attempts, and provides detailed timing and error information for troubleshooting and monitoring purposes.

## Request Syntax
<a name="API_GetTaskInstance_RequestSyntax"></a>

```
{
   "RunId": "{{string}}",
   "TaskInstanceId": "{{string}}",
   "WorkflowArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTaskInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RunId](#API_GetTaskInstance_RequestSyntax) **   <a name="mwaaserverless-GetTaskInstance-request-RunId"></a>
The unique identifier of the workflow run that contains the task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [TaskInstanceId](#API_GetTaskInstance_RequestSyntax) **   <a name="mwaaserverless-GetTaskInstance-request-TaskInstanceId"></a>
The unique identifier of the task instance to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [WorkflowArn](#API_GetTaskInstance_RequestSyntax) **   <a name="mwaaserverless-GetTaskInstance-request-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow that contains the task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`
Required: Yes

## Response Syntax
<a name="API_GetTaskInstance_ResponseSyntax"></a>

```
{
   "AttemptNumber": number,
   "DurationInSeconds": number,
   "EndedAt": "string",
   "ErrorMessage": "string",
   "LogStream": "string",
   "ModifiedAt": "string",
   "OperatorName": "string",
   "RunId": "string",
   "StartedAt": "string",
   "Status": "string",
   "TaskId": "string",
   "TaskInstanceId": "string",
   "WorkflowArn": "string",
   "WorkflowVersion": "string",
   "Xcom": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetTaskInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttemptNumber](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-AttemptNumber"></a>
The attempt number for this task instance.
Type: Integer

 ** [DurationInSeconds](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-DurationInSeconds"></a>
The duration of the task instance execution in seconds. This value is null if the task is not complete.
Type: Integer

 ** [EndedAt](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-EndedAt"></a>
The timestamp when the task instance completed execution, in ISO 8601 date-time format. This value is null if the task is not complete.
Type: Timestamp

 ** [ErrorMessage](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-ErrorMessage"></a>
The error message if the task instance failed. This value is null if the task completed successfully.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`

 ** [LogStream](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-LogStream"></a>
The CloudWatch log stream name for this task instance execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`

 ** [ModifiedAt](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-ModifiedAt"></a>
The timestamp when the task instance was last modified, in ISO 8601 date-time format.
Type: Timestamp

 ** [OperatorName](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-OperatorName"></a>
The name of the Apache Airflow operator used for this task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`

 ** [RunId](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-RunId"></a>
The unique identifier of the workflow run that contains this task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`

 ** [StartedAt](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-StartedAt"></a>
The timestamp when the task instance started execution, in ISO 8601 date-time format. This value is null if the task has not started.
Type: Timestamp

 ** [Status](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-Status"></a>
The current status of the task instance.
Type: String
Valid Values: `QUEUED | FAILED | SCHEDULED | RUNNING | SUCCESS | UP_FOR_RESCHEDULE | UP_FOR_RETRY | UPSTREAM_FAILED | REMOVED | RESTARTING | DEFERRED | NONE | CANCELLED | TIMEOUT`

 ** [TaskId](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-TaskId"></a>
The unique identifier of the task definition within the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`

 ** [TaskInstanceId](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-TaskInstanceId"></a>
The unique identifier of this task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`

 ** [WorkflowArn](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow that contains this task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`

 ** [WorkflowVersion](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-WorkflowVersion"></a>
The version of the workflow that contains this task instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.+`

 ** [Xcom](#API_GetTaskInstance_ResponseSyntax) **   <a name="mwaaserverless-GetTaskInstance-response-Xcom"></a>
Cross-communication data exchanged between tasks in the workflow execution.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `.*`

## Errors
<a name="API_GetTaskInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An unexpected server-side error occurred during request processing.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 500

 ** OperationTimeoutException **
The operation timed out.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. You can only access or modify a resource that already exists.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of the resource.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.
 ** QuotaCode **
The code of the quota.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying the operation.
 ** ServiceCode **
The code for the service.
HTTP Status Code: 400

 ** ValidationException **
The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.
 ** FieldList **
The fields that failed validation.
 ** Reason **
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetTaskInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-serverless-2024-07-26/GetTaskInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-serverless-2024-07-26/GetTaskInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/GetTaskInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-serverless-2024-07-26/GetTaskInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/GetTaskInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-serverless-2024-07-26/GetTaskInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-serverless-2024-07-26/GetTaskInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-serverless-2024-07-26/GetTaskInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-serverless-2024-07-26/GetTaskInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/GetTaskInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
