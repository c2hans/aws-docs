---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_CreateWorkflow.html
---

# CreateWorkflow
<a name="API_CreateWorkflow"></a>

Creates a new workflow in Amazon Managed Workflows for Apache Airflow Serverless. This operation initializes a workflow with the specified configuration including the workflow definition, execution role, and optional settings for encryption, logging, and networking. You must provide the workflow definition as a YAML file stored in Amazon S3 that defines the DAG structure using supported AWS operators. Amazon Managed Workflows for Apache Airflow Serverless automatically creates the first version of the workflow and sets up the necessary execution environment with multi-tenant isolation and security controls.

## Request Syntax
<a name="API_CreateWorkflow_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Code": { ... },
   "DefinitionS3Location": {
      "Bucket": "{{string}}",
      "ObjectKey": "{{string}}",
      "VersionId": "{{string}}"
   },
   "Description": "{{string}}",
   "EncryptionConfiguration": {
      "KmsKeyId": "{{string}}",
      "Type": "{{string}}"
   },
   "EngineVersion": {{number}},
   "LoggingConfiguration": {
      "LogGroupName": "{{string}}"
   },
   "Name": "{{string}}",
   "NetworkConfiguration": {
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   },
   "RoleArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TriggerMode": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateWorkflow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow creation requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [Code](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-Code"></a>
The location of code artifacts in Amazon S3 for the workflow. The service copies the code from this location at the time of the request.
Type: [Code](API_Code.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [DefinitionS3Location](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-DefinitionS3Location"></a>
The Amazon S3 location where the workflow definition file is stored. This must point to a valid YAML file that defines the workflow structure using supported AWS operators and tasks. Amazon Managed Workflows for Apache Airflow Serverless takes a snapshot of the definition at creation time, so subsequent changes to the Amazon S3 object will not affect the workflow unless you create a new version. In your YAML definition, include task dependencies, scheduling information, and operator configurations that are compatible with the Amazon Managed Workflows for Apache Airflow Serverless execution environment.
Type: [DefinitionS3Location](API_DefinitionS3Location.md) object
Required: Yes

 ** [Description](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-Description"></a>
An optional description of the workflow that you can use to provide additional context about the workflow's purpose and functionality.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [EncryptionConfiguration](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-EncryptionConfiguration"></a>
The configuration for encrypting workflow data at rest and in transit. Specifies the encryption type and optional KMS key for customer-managed encryption.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [EngineVersion](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-EngineVersion"></a>
The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that you want to use for this workflow. This determines the feature set, supported operators, and execution environment capabilities available to your workflow. Amazon Managed Workflows for Apache Airflow Serverless maintains backward compatibility across versions while introducing new features and improvements. Currently supports version 1 with plans for additional versions as the service evolves.
Type: Integer
Required: No

 ** [LoggingConfiguration](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-LoggingConfiguration"></a>
The configuration for workflow logging. Specifies the CloudWatch log group where workflow execution logs are stored. Amazon Managed Workflows for Apache Airflow Serverless automatically exports worker logs and task-level information to the specified log group in your account using remote logging functionality. This provides comprehensive observability for debugging and monitoring workflow execution across the distributed, serverless environment.
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object
Required: No

 ** [Name](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-Name"></a>
The name of the workflow. You must use unique workflow names within your AWS account. The service generates a unique identifier that is appended to ensure temporal uniqueness across the account lifecycle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [NetworkConfiguration](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-NetworkConfiguration"></a>
Network configuration for the workflow execution environment, including VPC security groups and subnets for secure network access. When specified, Amazon Managed Workflows for Apache Airflow Serverless deploys ECS worker tasks in your customer VPC to provide secure connectivity to your resources. If not specified, tasks run in the service's default worker VPC with network isolation from other customers. This configuration enables secure access to VPC-only resources like RDS databases or private endpoints.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** [RoleArn](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when executing the workflow. This role must have the necessary permissions to access the required AWS services and resources that your workflow tasks will interact with. The role is used for task execution in the isolated, multi-tenant environment and should follow the principle of least privilege. Amazon Managed Workflows for Apache Airflow Serverless validates role access during workflow creation but runtime permission checks are performed by the target services.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:iam::[0-9]{12}:role(/[a-zA-Z0-9+=,.@_\-]{1,512})*?/[a-zA-Z0-9+=,.@_\-]{1,64}`
Required: Yes

 ** [Tags](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-Tags"></a>
A map of tags to assign to the workflow resource. Tags are key-value pairs that are used for resource organization and cost allocation.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`
Required: No

 ** [TriggerMode](#API_CreateWorkflow_RequestSyntax) **   <a name="mwaaserverless-CreateWorkflow-request-TriggerMode"></a>
The trigger mode for the workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_CreateWorkflow_ResponseSyntax"></a>

```
{
   "CreatedAt": "string",
   "IsLatestVersion": boolean,
   "RevisionId": "string",
   "Warnings": [ "string" ],
   "WorkflowArn": "string",
   "WorkflowStatus": "string",
   "WorkflowVersion": "string"
}
```

## Response Elements
<a name="API_CreateWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_CreateWorkflow_ResponseSyntax) **   <a name="mwaaserverless-CreateWorkflow-response-CreatedAt"></a>
The timestamp when the workflow was created, in ISO 8601 date-time format.
Type: Timestamp

 ** [IsLatestVersion](#API_CreateWorkflow_ResponseSyntax) **   <a name="mwaaserverless-CreateWorkflow-response-IsLatestVersion"></a>
A Boolean flag that indicates whether this workflow version is the latest version of the workflow.
Type: Boolean

 ** [RevisionId](#API_CreateWorkflow_ResponseSyntax) **   <a name="mwaaserverless-CreateWorkflow-response-RevisionId"></a>
A unique identifier for this revision of the workflow configuration. This ID changes when the workflow is updated and you can use it for optimistic concurrency control in update operations. The revision ID helps prevent conflicting updates and ensures that updates are applied to the expected version of the workflow configuration.
Type: String

 ** [Warnings](#API_CreateWorkflow_ResponseSyntax) **   <a name="mwaaserverless-CreateWorkflow-response-Warnings"></a>
Warning messages generated during workflow creation.
Type: Array of strings

 ** [WorkflowArn](#API_CreateWorkflow_ResponseSyntax) **   <a name="mwaaserverless-CreateWorkflow-response-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the newly created workflow. This ARN uniquely identifies the workflow resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`

 ** [WorkflowStatus](#API_CreateWorkflow_ResponseSyntax) **   <a name="mwaaserverless-CreateWorkflow-response-WorkflowStatus"></a>
The current status of the workflow. Possible values are `READY` (workflow is ready to run) and `DELETING` (workflow is being deleted).
Type: String
Valid Values: `READY | DELETING`

 ** [WorkflowVersion](#API_CreateWorkflow_ResponseSyntax) **   <a name="mwaaserverless-CreateWorkflow-response-WorkflowVersion"></a>
The version identifier of the workflow. This is a service-generated alphanumeric string that uniquely identifies this version of the workflow. Amazon Managed Workflows for Apache Airflow Serverless uses a version-first approach where each workflow can have multiple immutable versions, which allows you to maintain different configurations and roll back to previous versions as needed. The version identifier is used in ARNs and API operations to reference specific workflow versions.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9]{32}`

## Errors
<a name="API_CreateWorkflow_Errors"></a>

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
<a name="API_CreateWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-serverless-2024-07-26/CreateWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-serverless-2024-07-26/CreateWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/CreateWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-serverless-2024-07-26/CreateWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/CreateWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-serverless-2024-07-26/CreateWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-serverless-2024-07-26/CreateWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-serverless-2024-07-26/CreateWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-serverless-2024-07-26/CreateWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/CreateWorkflow)
