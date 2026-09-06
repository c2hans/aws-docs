---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_UpdateWorkflow.html
---

# UpdateWorkflow
<a name="API_UpdateWorkflow"></a>

Updates an existing workflow with new configuration settings. This operation allows you to modify the workflow definition, role, and other settings. When you update a workflow, Amazon Managed Workflows for Apache Airflow Serverless automatically creates a new version with the updated configuration and disables scheduling on all previous versions to ensure only one version is actively scheduled at a time. The update operation maintains workflow history while providing a clean transition to the new configuration.

## Request Syntax
<a name="API_UpdateWorkflow_RequestSyntax"></a>

```
{
   "Code": { ... },
   "DefinitionS3Location": {
      "Bucket": "{{string}}",
      "ObjectKey": "{{string}}",
      "VersionId": "{{string}}"
   },
   "Description": "{{string}}",
   "EngineVersion": {{number}},
   "LoggingConfiguration": {
      "LogGroupName": "{{string}}"
   },
   "NetworkConfiguration": {
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   },
   "RoleArn": "{{string}}",
   "TriggerMode": "{{string}}",
   "WorkflowArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateWorkflow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Code](#API_UpdateWorkflow_RequestSyntax) **   <a name="mwaaserverless-UpdateWorkflow-request-Code"></a>
The location of code artifacts in Amazon S3 for the updated workflow. The service copies the code from this location at the time of the request.
Type: [Code](API_Code.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [DefinitionS3Location](#API_UpdateWorkflow_RequestSyntax) **   <a name="mwaaserverless-UpdateWorkflow-request-DefinitionS3Location"></a>
The Amazon S3 location where the updated workflow definition file is stored.
Type: [DefinitionS3Location](API_DefinitionS3Location.md) object
Required: Yes

 ** [Description](#API_UpdateWorkflow_RequestSyntax) **   <a name="mwaaserverless-UpdateWorkflow-request-Description"></a>
An updated description for the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [EngineVersion](#API_UpdateWorkflow_RequestSyntax) **   <a name="mwaaserverless-UpdateWorkflow-request-EngineVersion"></a>
The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that you want to use for the updated workflow.
Type: Integer
Required: No

 ** [LoggingConfiguration](#API_UpdateWorkflow_RequestSyntax) **   <a name="mwaaserverless-UpdateWorkflow-request-LoggingConfiguration"></a>
Updated logging configuration for the workflow.
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object
Required: No

 ** [NetworkConfiguration](#API_UpdateWorkflow_RequestSyntax) **   <a name="mwaaserverless-UpdateWorkflow-request-NetworkConfiguration"></a>
Updated network configuration for the workflow execution environment.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** [RoleArn](#API_UpdateWorkflow_RequestSyntax) **   <a name="mwaaserverless-UpdateWorkflow-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when it executes the updated workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:iam::[0-9]{12}:role(/[a-zA-Z0-9+=,.@_\-]{1,512})*?/[a-zA-Z0-9+=,.@_\-]{1,64}`
Required: Yes

 ** [TriggerMode](#API_UpdateWorkflow_RequestSyntax) **   <a name="mwaaserverless-UpdateWorkflow-request-TriggerMode"></a>
The trigger mode for the workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [WorkflowArn](#API_UpdateWorkflow_RequestSyntax) **   <a name="mwaaserverless-UpdateWorkflow-request-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`
Required: Yes

## Response Syntax
<a name="API_UpdateWorkflow_ResponseSyntax"></a>

```
{
   "ModifiedAt": "string",
   "Warnings": [ "string" ],
   "WorkflowArn": "string",
   "WorkflowVersion": "string"
}
```

## Response Elements
<a name="API_UpdateWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModifiedAt](#API_UpdateWorkflow_ResponseSyntax) **   <a name="mwaaserverless-UpdateWorkflow-response-ModifiedAt"></a>
The timestamp when the workflow was last modified, in ISO 8601 date-time format.
Type: Timestamp

 ** [Warnings](#API_UpdateWorkflow_ResponseSyntax) **   <a name="mwaaserverless-UpdateWorkflow-response-Warnings"></a>
Warning messages generated during workflow update.
Type: Array of strings

 ** [WorkflowArn](#API_UpdateWorkflow_ResponseSyntax) **   <a name="mwaaserverless-UpdateWorkflow-response-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the updated workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`

 ** [WorkflowVersion](#API_UpdateWorkflow_ResponseSyntax) **   <a name="mwaaserverless-UpdateWorkflow-response-WorkflowVersion"></a>
The version identifier of the updated workflow.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9]{32}`

## Errors
<a name="API_UpdateWorkflow_Errors"></a>

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
<a name="API_UpdateWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-serverless-2024-07-26/UpdateWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-serverless-2024-07-26/UpdateWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/UpdateWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-serverless-2024-07-26/UpdateWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/UpdateWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-serverless-2024-07-26/UpdateWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-serverless-2024-07-26/UpdateWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-serverless-2024-07-26/UpdateWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-serverless-2024-07-26/UpdateWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/UpdateWorkflow)
