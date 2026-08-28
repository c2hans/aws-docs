---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetRun.html
---

# GetRun
<a name="API_GetRun"></a>

Gets detailed information about a specific run using its ID.

 AWS HealthOmics stores a configurable number of runs, as determined by service limits, that are available to the console and API. If `GetRun` does not return the requested run, you can find all run logs in the CloudWatch logs. For more information about viewing the run logs, see [CloudWatch logs](https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_GetRun_RequestSyntax"></a>

```
GET /run/{{id}}?export={{export}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [export](#API_GetRun_RequestSyntax) **   <a name="omics-GetRun-request-uri-export"></a>
The run's export format.
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `DEFINITION`

 ** [id](#API_GetRun_RequestSyntax) **   <a name="omics-GetRun-request-uri-id"></a>
The run's ID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accelerators": "string",
   "arn": "string",
   "batchId": "string",
   "cacheBehavior": "string",
   "cacheId": "string",
   "configuration": {
      "arn": "string",
      "name": "string",
      "uuid": "string"
   },
   "creationTime": "string",
   "definition": "string",
   "digest": "string",
   "engineSettings": JSON value,
   "engineVersion": "string",
   "failureReason": "string",
   "id": "string",
   "logLevel": "string",
   "logLocation": {
      "engineLogStream": "string",
      "runLogStream": "string"
   },
   "name": "string",
   "networkingMode": "string",
   "outputUri": "string",
   "parameters": JSON value,
   "priority": number,
   "resourceDigests": {
      "string" : "string"
   },
   "retentionMode": "string",
   "roleArn": "string",
   "runGroupId": "string",
   "runId": "string",
   "runOutputUri": "string",
   "scratchStorageMode": "string",
   "startedBy": "string",
   "startTime": "string",
   "status": "string",
   "statusMessage": "string",
   "stopTime": "string",
   "storageCapacity": number,
   "storageType": "string",
   "tags": {
      "string" : "string"
   },
   "uuid": "string",
   "vpcConfig": {
      "securityGroupIds": [ "string" ],
      "subnetIds": [ "string" ],
      "vpcId": "string"
   },
   "workflowId": "string",
   "workflowOwnerId": "string",
   "workflowType": "string",
   "workflowUuid": "string",
   "workflowVersionName": "string"
}
```

## Response Elements
<a name="API_GetRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accelerators](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-accelerators"></a>
The computational accelerator used to run the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `GPU`

 ** [arn](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-arn"></a>
The run's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`

 ** [batchId](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-batchId"></a>
The run's batch ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [cacheBehavior](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-cacheBehavior"></a>
The run cache behavior for the run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CACHE_ON_FAILURE | CACHE_ALWAYS`

 ** [cacheId](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-cacheId"></a>
The run cache associated with the run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [configuration](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-configuration"></a>
Configuration details for the workflow run.
Type: [ConfigurationDetails](API_ConfigurationDetails.md) object

 ** [creationTime](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-creationTime"></a>
When the run was created.
Type: Timestamp

 ** [definition](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-definition"></a>
The run's definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [digest](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-digest"></a>
The run's digest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [engineSettings](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-engineSettings"></a>
The engine-specific settings for the workflow run.
Type: JSON value

 ** [engineVersion](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-engineVersion"></a>
The actual Nextflow engine version that AWS HealthOmics used for the run. The other workflow definition languages don't provide a value for this field.
Type: String
Pattern: `[0-9]{2}.[0-9]{2}.[0-9]`

 ** [failureReason](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-failureReason"></a>
The reason a run has failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [id](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-id"></a>
The run's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [logLevel](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-logLevel"></a>
The run's log level.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `OFF | FATAL | ERROR | ALL`

 ** [logLocation](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-logLocation"></a>
The location of the run log.
Type: [RunLogLocation](API_RunLogLocation.md) object

 ** [name](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-name"></a>
The run's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [networkingMode](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-networkingMode"></a>
Configuration for run networking behavior. If absent, this will default to RESTRICTED.
Type: String
Valid Values: `RESTRICTED | VPC`

 ** [outputUri](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-outputUri"></a>
The run's output URI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [parameters](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-parameters"></a>
The run's parameters.
Type: JSON value

 ** [priority](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-priority"></a>
The run's priority.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.

 ** [resourceDigests](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-resourceDigests"></a>
The run's resource digests.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Value Length Constraints: Minimum length of 0. Maximum length of 64.
Value Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [retentionMode](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-retentionMode"></a>
The run's retention mode.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `RETAIN | REMOVE`

 ** [roleArn](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-roleArn"></a>
The run's service role ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`

 ** [runGroupId](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-runGroupId"></a>
The run's group ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [runId](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-runId"></a>
The run's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [runOutputUri](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-runOutputUri"></a>
The destination for workflow outputs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [scratchStorageMode](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-scratchStorageMode"></a>
Optional configuration for enabling scratch ephemeral storage mounted at /tmp. If absent, this will default to SHARED. This configuration is applicable only for CPU tasks. For tasks using GPUs, scratch storage is always LOCAL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `LOCAL | SHARED`

 ** [startedBy](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-startedBy"></a>
Who started the run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [startTime](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-startTime"></a>
When the run started.
Type: Timestamp

 ** [status](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-status"></a>
The run's status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PENDING | STARTING | RUNNING | STOPPING | COMPLETED | DELETED | CANCELLED | FAILED`

 ** [statusMessage](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-statusMessage"></a>
The run's status message.
Type: String
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [stopTime](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-stopTime"></a>
The run's stop time.
Type: Timestamp

 ** [storageCapacity](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-storageCapacity"></a>
The run's storage capacity in gibibytes. For dynamic storage, after the run has completed, this value is the maximum amount of storage used during the run.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.

 ** [storageType](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-storageType"></a>
The run's storage type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `STATIC | DYNAMIC`

 ** [tags](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-tags"></a>
The run's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [uuid](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-uuid"></a>
The universally unique identifier for a run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [vpcConfig](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-vpcConfig"></a>
VPC configuration for the workflow run.
Type: [VpcConfigResponse](API_VpcConfigResponse.md) object

 ** [workflowId](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-workflowId"></a>
The run's workflow ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [workflowOwnerId](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-workflowOwnerId"></a>
The ID of the workflow owner.
Type: String
Pattern: `[0-9]{12}`

 ** [workflowType](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-workflowType"></a>
The run's workflow type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PRIVATE | READY2RUN`

 ** [workflowUuid](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-workflowUuid"></a>
The universally unique identifier (UUID) value for the workflow.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [workflowVersionName](#API_GetRun_ResponseSyntax) **   <a name="omics-GetRun-response-workflowVersionName"></a>
The workflow version name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`

## Errors
<a name="API_GetRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
