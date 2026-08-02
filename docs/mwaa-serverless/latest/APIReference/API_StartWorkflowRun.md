---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_StartWorkflowRun.html
---

# StartWorkflowRun
<a name="API_StartWorkflowRun"></a>

Starts a new execution of a workflow. This operation creates a workflow run that executes the tasks that are defined in the workflow. Amazon Managed Workflows for Apache Airflow Serverless schedules the workflow execution across its managed Airflow environment, automatically scaling ECS worker tasks based on the workload. The service handles task isolation, dependency resolution, and provides comprehensive monitoring and logging throughout the execution lifecycle.

## Request Syntax
<a name="API_StartWorkflowRun_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "OverrideParameters": {
      "{{string}}" : {{JSON value}}
   },
   "WorkflowArn": "{{string}}",
   "WorkflowVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_StartWorkflowRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_StartWorkflowRun_RequestSyntax) **   <a name="mwaaserverless-StartWorkflowRun-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow run requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [OverrideParameters](#API_StartWorkflowRun_RequestSyntax) **   <a name="mwaaserverless-StartWorkflowRun-request-OverrideParameters"></a>
Optional parameters to override default workflow parameters for this specific run. These parameters are passed to the workflow during execution and can be used to customize behavior without modifying the workflow definition. Parameters are made available as environment variables to tasks and you can reference them within the YAML workflow definition using standard parameter substitution syntax.
Type: String to JSON value map
Required: No

 ** [WorkflowArn](#API_StartWorkflowRun_RequestSyntax) **   <a name="mwaaserverless-StartWorkflowRun-request-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow you want to run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`
Required: Yes

 ** [WorkflowVersion](#API_StartWorkflowRun_RequestSyntax) **   <a name="mwaaserverless-StartWorkflowRun-request-WorkflowVersion"></a>
Optional. The specific version of the workflow to execute. If not specified, the latest version is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.+`
Required: No

## Response Syntax
<a name="API_StartWorkflowRun_ResponseSyntax"></a>

```
{
   "RunId": "string",
   "StartedAt": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_StartWorkflowRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RunId](#API_StartWorkflowRun_ResponseSyntax) **   <a name="mwaaserverless-StartWorkflowRun-response-RunId"></a>
The unique identifier of the newly started workflow run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`

 ** [StartedAt](#API_StartWorkflowRun_ResponseSyntax) **   <a name="mwaaserverless-StartWorkflowRun-response-StartedAt"></a>
The timestamp when the workflow run was started, in ISO 8601 date-time format.
Type: Timestamp

 ** [Status](#API_StartWorkflowRun_ResponseSyntax) **   <a name="mwaaserverless-StartWorkflowRun-response-Status"></a>
The initial status of the workflow run. This is typically `STARTING` when you first create the run.
Type: String
Valid Values: `STARTING | QUEUED | RUNNING | SUCCESS | FAILED | TIMEOUT | STOPPING | STOPPED`

## Errors
<a name="API_StartWorkflowRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** ConflictException **
You cannot create a resource that already exists, or the resource is in a state that prevents the requested operation.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of the resource.
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

 ** ServiceQuotaExceededException **
The request exceeds the service quota for Amazon Managed Workflows for Apache Airflow Serverless resources. This can occur when you attempt to create more workflows than allowed, exceed concurrent workflow run limits, or surpass task execution limits. Amazon Managed Workflows for Apache Airflow Serverless implements admission control using DynamoDB-based counters to manage resource utilization across the multi-tenant environment. Contact AWS Support to request quota increases if you need higher limits for your use case.
 ** QuotaCode **
The code of the quota.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource affected.
 ** ServiceCode **
The code for the service.
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
<a name="API_StartWorkflowRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-serverless-2024-07-26/StartWorkflowRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-serverless-2024-07-26/StartWorkflowRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/StartWorkflowRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-serverless-2024-07-26/StartWorkflowRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/StartWorkflowRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-serverless-2024-07-26/StartWorkflowRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-serverless-2024-07-26/StartWorkflowRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-serverless-2024-07-26/StartWorkflowRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-serverless-2024-07-26/StartWorkflowRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/StartWorkflowRun)
