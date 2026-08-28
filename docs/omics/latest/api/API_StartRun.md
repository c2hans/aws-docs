---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_StartRun.html
---

# StartRun
<a name="API_StartRun"></a>

Starts a new run and returns details about the run, or duplicates an existing run. A run is a single invocation of a workflow. If you provide request IDs, AWS HealthOmics identifies duplicate requests and starts the run only once. Monitor the progress of the run by calling the `GetRun` API operation.

To start a new run, the following inputs are required:
+ A service role ARN (`roleArn`).
+ The run's workflow ID (`workflowId`, not the `uuid` or `runId`).
+ An Amazon S3 location (`outputUri`) where the run outputs will be saved.
+ All required workflow parameters (`parameter`), which can include optional parameters from the parameter template. The run cannot include any parameters that are not defined in the parameter template. To see all possible parameters, use the `GetRun` API operation.
+ For runs with a `STATIC` (default) storage type, specify the required storage capacity (in gibibytes). A storage capacity value is not required for runs that use `DYNAMIC` storage.

 `StartRun` can also duplicate an existing run using the run's default values. You can modify these default values and/or add other optional inputs. To duplicate a run, the following inputs are required:
+ A service role ARN (`roleArn`).
+ The ID of the run to duplicate (`runId`).
+ An Amazon S3 location where the run outputs will be saved (`outputUri`).

To learn more about the optional parameters for `StartRun`, see [Starting a run](https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html) in the * AWS HealthOmics User Guide*.

Use the `retentionMode` input to control how long the metadata for each run is stored in CloudWatch. There are two retention modes:
+ Specify `REMOVE` to automatically remove the oldest runs when you reach the maximum service retention limit for runs. It is recommended that you use the `REMOVE` mode to initiate major run requests so that your runs do not fail when you reach the limit.
+ The `retentionMode` is set to the `RETAIN` mode by default, which allows you to manually remove runs after reaching the maximum service retention limit. Under this setting, you cannot create additional runs until you remove the excess runs.

To learn more about the retention modes, see [Run retention mode](https://docs.aws.amazon.com/omics/latest/dev/run-retention.html) in the * AWS HealthOmics User Guide*.

You can use Amazon Q CLI to analyze run logs and make performance optimization recommendations. To get started, see the [AWS HealthOmics MCP server](https://github.com/awslabs/mcp/tree/main/src/aws-healthomics-mcp-server) on GitHub.

## Request Syntax
<a name="API_StartRun_RequestSyntax"></a>

```
POST /run HTTP/1.1
Content-type: application/json

{
   "cacheBehavior": "{{string}}",
   "cacheId": "{{string}}",
   "configurationName": "{{string}}",
   "engineSettings": {{JSON value}},
   "logLevel": "{{string}}",
   "name": "{{string}}",
   "networkingMode": "{{string}}",
   "outputUri": "{{string}}",
   "parameters": {{JSON value}},
   "priority": {{number}},
   "requestId": "{{string}}",
   "retentionMode": "{{string}}",
   "roleArn": "{{string}}",
   "runGroupId": "{{string}}",
   "runId": "{{string}}",
   "scratchStorageMode": "{{string}}",
   "storageCapacity": {{number}},
   "storageType": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "workflowId": "{{string}}",
   "workflowOwnerId": "{{string}}",
   "workflowType": "{{string}}",
   "workflowVersionName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartRun_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [cacheBehavior](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-cacheBehavior"></a>
The cache behavior for the run. You specify this value if you want to override the default behavior for the cache. You had set the default value when you created the cache. For more information, see [Run cache behavior](https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior) in the * AWS HealthOmics User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CACHE_ON_FAILURE | CACHE_ALWAYS`
Required: No

 ** [cacheId](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-cacheId"></a>
Identifier of the cache associated with this run. If you don't specify a cache ID, no task outputs are cached for this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** [configurationName](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-configurationName"></a>
Optional configuration name to use for the workflow run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: No

 ** [engineSettings](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-engineSettings"></a>
Engine-specific settings for the workflow run. Use this field to specify configuration options that are specific to the workflow engine (for example, Nextflow profiles).
Type: JSON value
Required: No

 ** [logLevel](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-logLevel"></a>
A log level for the run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `OFF | FATAL | ERROR | ALL`
Required: No

 ** [name](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-name"></a>
A name for the run. This is recommended to view and organize runs in the AWS HealthOmics console and CloudWatch logs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [networkingMode](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-networkingMode"></a>
Optional configuration for run networking behavior. If not specified, this will default to RESTRICTED.
Type: String
Valid Values: `RESTRICTED | VPC`
Required: No

 ** [outputUri](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-outputUri"></a>
An output S3 URI for the run. The S3 bucket must be in the same region as the workflow. The role ARN must have permission to write to this S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [parameters](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-parameters"></a>
Parameters for the run. The run needs all required parameters and can include optional parameters. The run cannot include any parameters that are not defined in the parameter template. To retrieve parameters from the run, use the GetRun API operation.
Type: JSON value
Required: No

 ** [priority](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-priority"></a>
Use the run priority (highest: 1) to establish the order of runs in a run group when you start a run. If multiple runs share the same priority, the run that was initiated first will have the higher priority. Runs that do not belong to a run group can be assigned a priority. The priorities of these runs are ranked among other runs that are not in a run group. For more information, see [Run priority](https://docs.aws.amazon.com/omics/latest/dev/creating-run-groups.html#run-priority) in the * AWS HealthOmics User Guide*.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** [requestId](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-requestId"></a>
An idempotency token used to dedupe retry requests so that duplicate runs are not created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [retentionMode](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-retentionMode"></a>
The retention mode for the run. The default value is `RETAIN`.
 AWS HealthOmics stores a fixed number of runs that are available to the console and API. In the default mode (`RETAIN`), you need to remove runs manually when the number of run exceeds the maximum. If you set the retention mode to `REMOVE`, AWS HealthOmics automatically removes runs (that have mode set to `REMOVE`) when the number of run exceeds the maximum. All run logs are available in CloudWatch logs, if you need information about a run that is no longer available to the API.
For more information about retention mode, see [Specifying run retention mode](https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html) in the * AWS HealthOmics User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `RETAIN | REMOVE`
Required: No

 ** [roleArn](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-roleArn"></a>
A service role for the run. The `roleArn` requires access to AWS HealthOmics, S3, Cloudwatch logs, and EC2. An example `roleArn` is `arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ`. In this example, the AWS account ID is `123456789012` and the role name is `omics-service-role-serviceRole-W8O1XMPL7QZ`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`
Required: Yes

 ** [runGroupId](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-runGroupId"></a>
The run's group ID. Use a run group to cap the compute resources (and number of concurrent runs) for the runs that you add to the run group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** [runId](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-runId"></a>
The ID of a run to duplicate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** [scratchStorageMode](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-scratchStorageMode"></a>
Optional configuration for enabling scratch ephemeral storage mounted at /tmp. If not specified, this will default to SHARED. This configuration is applicable only for CPU tasks. For tasks using GPUs, scratch storage is always LOCAL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `LOCAL | SHARED`
Required: No

 ** [storageCapacity](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-storageCapacity"></a>
The `STATIC` storage capacity (in gibibytes, GiB) for this run. The default run storage capacity is 1200 GiB. If your requested storage capacity is unavailable, the system rounds up the value to the nearest 1200 GiB multiple. If the requested storage capacity is still unavailable, the system rounds up the value to the nearest 2400 GiB multiple. This field is not required if the storage type is `DYNAMIC` (the system ignores any value that you enter).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** [storageType](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-storageType"></a>
The storage type for the run. If you set the storage type to `DYNAMIC`, AWS HealthOmics dynamically scales the storage up or down, based on file system utilization. By default, the run uses `STATIC` storage type, which allocates a fixed amount of storage. For more information about `DYNAMIC` and `STATIC` storage, see [Run storage types](https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html) in the * AWS HealthOmics User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `STATIC | DYNAMIC`
Required: No

 ** [tags](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-tags"></a>
Tags for the run. You can add up to 50 tags per run. For more information, see [Adding a tag](https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html) in the * AWS HealthOmics User Guide*.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [workflowId](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-workflowId"></a>
The run's workflow ID. The `workflowId` is not the UUID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** [workflowOwnerId](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-workflowOwnerId"></a>
The 12-digit account ID of the workflow owner that is used for running a shared workflow. The workflow owner ID can be retrieved using the `GetShare` API operation. If you are the workflow owner, you do not need to include this ID.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [workflowType](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-workflowType"></a>
The run's workflow type. The `workflowType` must be specified if you are running a `READY2RUN` workflow. If you are running a `PRIVATE` workflow (default), you do not need to include the workflow type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PRIVATE | READY2RUN`
Required: No

 ** [workflowVersionName](#API_StartRun_RequestSyntax) **   <a name="omics-StartRun-request-workflowVersionName"></a>
The name of the workflow version. Use workflow versions to track and organize changes to the workflow. If your workflow has multiple versions, the run uses the default version unless you specify a version name. To learn more, see [Workflow versioning](https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html) in the * AWS HealthOmics User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: No

## Response Syntax
<a name="API_StartRun_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "configuration": {
      "arn": "string",
      "name": "string",
      "uuid": "string"
   },
   "id": "string",
   "networkingMode": "string",
   "runOutputUri": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "uuid": "string"
}
```

## Response Elements
<a name="API_StartRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_StartRun_ResponseSyntax) **   <a name="omics-StartRun-response-arn"></a>
Unique resource identifier for the run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`

 ** [configuration](#API_StartRun_ResponseSyntax) **   <a name="omics-StartRun-response-configuration"></a>
Configuration details for the workflow run.
Type: [ConfigurationDetails](API_ConfigurationDetails.md) object

 ** [id](#API_StartRun_ResponseSyntax) **   <a name="omics-StartRun-response-id"></a>
The run's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [networkingMode](#API_StartRun_ResponseSyntax) **   <a name="omics-StartRun-response-networkingMode"></a>
Networking mode for the workflow run.
Type: String

 ** [runOutputUri](#API_StartRun_ResponseSyntax) **   <a name="omics-StartRun-response-runOutputUri"></a>
The destination for workflow outputs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [status](#API_StartRun_ResponseSyntax) **   <a name="omics-StartRun-response-status"></a>
The run's status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PENDING | STARTING | RUNNING | STOPPING | COMPLETED | DELETED | CANCELLED | FAILED`

 ** [tags](#API_StartRun_ResponseSyntax) **   <a name="omics-StartRun-response-tags"></a>
The run's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [uuid](#API_StartRun_ResponseSyntax) **   <a name="omics-StartRun-response-uuid"></a>
The universally unique identifier for a run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_StartRun_Errors"></a>

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
<a name="API_StartRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/StartRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/StartRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/StartRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/StartRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/StartRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/StartRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/StartRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/StartRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/StartRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/StartRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
