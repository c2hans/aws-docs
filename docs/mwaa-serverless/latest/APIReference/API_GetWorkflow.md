---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_GetWorkflow.html
---

# GetWorkflow
<a name="API_GetWorkflow"></a>

Retrieves detailed information about a workflow, including its configuration, status, and metadata.

## Request Syntax
<a name="API_GetWorkflow_RequestSyntax"></a>

```
{
   "WorkflowArn": "{{string}}",
   "WorkflowVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_GetWorkflow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WorkflowArn](#API_GetWorkflow_RequestSyntax) **   <a name="mwaaserverless-GetWorkflow-request-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow you want to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`
Required: Yes

 ** [WorkflowVersion](#API_GetWorkflow_RequestSyntax) **   <a name="mwaaserverless-GetWorkflow-request-WorkflowVersion"></a>
Optional. The specific version of the workflow to retrieve. If not specified, the latest version is returned.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9]{32}`
Required: No

## Response Syntax
<a name="API_GetWorkflow_ResponseSyntax"></a>

```
{
   "Code": { ... },
   "CodeSnapshottedAt": "string",
   "CreatedAt": "string",
   "DefinitionS3Location": {
      "Bucket": "string",
      "ObjectKey": "string",
      "VersionId": "string"
   },
   "Description": "string",
   "EncryptionConfiguration": {
      "KmsKeyId": "string",
      "Type": "string"
   },
   "EngineVersion": number,
   "LoggingConfiguration": {
      "LogGroupName": "string"
   },
   "ModifiedAt": "string",
   "Name": "string",
   "NetworkConfiguration": {
      "SecurityGroupIds": [ "string" ],
      "SubnetIds": [ "string" ]
   },
   "RoleArn": "string",
   "ScheduleConfiguration": {
      "CronExpression": "string"
   },
   "TriggerMode": "string",
   "WorkflowArn": "string",
   "WorkflowDefinition": "string",
   "WorkflowStatus": "string",
   "WorkflowVersion": "string"
}
```

## Response Elements
<a name="API_GetWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Code](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-Code"></a>
The Amazon S3 location of the code artifacts provided during workflow creation or update.
Type: [Code](API_Code.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [CodeSnapshottedAt](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-CodeSnapshottedAt"></a>
The time at which the code artifacts were copied for this workflow, in ISO 8601 date-time format.
Type: Timestamp

 ** [CreatedAt](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-CreatedAt"></a>
The timestamp when the workflow was created, in ISO 8601 date-time format.
Type: Timestamp

 ** [DefinitionS3Location](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-DefinitionS3Location"></a>
The Amazon S3 location of the workflow definition file.
Type: [DefinitionS3Location](API_DefinitionS3Location.md) object

 ** [Description](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-Description"></a>
The description of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [EncryptionConfiguration](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-EncryptionConfiguration"></a>
The encryption configuration for the workflow.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [EngineVersion](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-EngineVersion"></a>
The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that this workflow uses.
Type: Integer

 ** [LoggingConfiguration](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-LoggingConfiguration"></a>
The logging configuration for the workflow.
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object

 ** [ModifiedAt](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-ModifiedAt"></a>
The timestamp when the workflow was last modified, in ISO 8601 date-time format.
Type: Timestamp

 ** [Name](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-Name"></a>
The name of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`

 ** [NetworkConfiguration](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-NetworkConfiguration"></a>
The network configuration for the workflow execution environment.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object

 ** [RoleArn](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used for workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:iam::[0-9]{12}:role(/[a-zA-Z0-9+=,.@_\-]{1,512})*?/[a-zA-Z0-9+=,.@_\-]{1,64}`

 ** [ScheduleConfiguration](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-ScheduleConfiguration"></a>
The schedule configuration for the workflow, including cron expressions for automated execution. Amazon Managed Workflows for Apache Airflow Serverless uses EventBridge Scheduler for cost-effective, timezone-aware scheduling. When a workflow includes schedule information in its YAML definition, the service automatically configures the appropriate triggers for automated execution. Only one version of a workflow can have an active schedule at any given time.
Type: [ScheduleConfiguration](API_ScheduleConfiguration.md) object

 ** [TriggerMode](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-TriggerMode"></a>
The trigger mode for the workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`

 ** [WorkflowArn](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`

 ** [WorkflowDefinition](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-WorkflowDefinition"></a>
The workflow definition content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`

 ** [WorkflowStatus](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-WorkflowStatus"></a>
The current status of the workflow.
Type: String
Valid Values: `READY | DELETING`

 ** [WorkflowVersion](#API_GetWorkflow_ResponseSyntax) **   <a name="mwaaserverless-GetWorkflow-response-WorkflowVersion"></a>
The version identifier of the workflow.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9]{32}`

## Errors
<a name="API_GetWorkflow_Errors"></a>

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
<a name="API_GetWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-serverless-2024-07-26/GetWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-serverless-2024-07-26/GetWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/GetWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-serverless-2024-07-26/GetWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/GetWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-serverless-2024-07-26/GetWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-serverless-2024-07-26/GetWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-serverless-2024-07-26/GetWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-serverless-2024-07-26/GetWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/GetWorkflow)
