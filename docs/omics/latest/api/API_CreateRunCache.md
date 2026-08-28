---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CreateRunCache.html
---

# CreateRunCache
<a name="API_CreateRunCache"></a>

Creates a run cache to store and reference task outputs from completed private runs. Specify an Amazon S3 location where AWS HealthOmics saves the cached data. This data must be immediately accessible and not in an archived state. You can save intermediate task files to a run cache if they are declared as task outputs in the workflow definition file.

For more information, see [Call caching](https://docs.aws.amazon.com/omics/latest/dev/workflows-call-caching.html) and [Creating a run cache](https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-create.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_CreateRunCache_RequestSyntax"></a>

```
POST /runCache HTTP/1.1
Content-type: application/json

{
   "cacheBehavior": "{{string}}",
   "cacheBucketOwnerId": "{{string}}",
   "cacheS3Location": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "requestId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRunCache_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRunCache_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [cacheBehavior](#API_CreateRunCache_RequestSyntax) **   <a name="omics-CreateRunCache-request-cacheBehavior"></a>
Default cache behavior for runs that use this cache. Supported values are:
 `CACHE_ON_FAILURE`: Caches task outputs from completed tasks for runs that fail. This setting is useful if you're debugging a workflow that fails after several tasks completed successfully. The subsequent run uses the cache outputs for previously-completed tasks if the task definition, inputs, and container in ECR are identical to the prior run.
 `CACHE_ALWAYS`: Caches task outputs from completed tasks for all runs. This setting is useful in development mode, but do not use it in a production setting.
If you don't specify a value, the default behavior is CACHE\_ON\_FAILURE. When you start a run that uses this cache, you can override the default cache behavior.
For more information, see [Run cache behavior](https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior) in the * AWS HealthOmics User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CACHE_ON_FAILURE | CACHE_ALWAYS`
Required: No

 ** [cacheBucketOwnerId](#API_CreateRunCache_RequestSyntax) **   <a name="omics-CreateRunCache-request-cacheBucketOwnerId"></a>
The AWS account ID of the expected owner of the S3 bucket for the run cache. If not provided, your account ID is set as the owner of the bucket.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** [cacheS3Location](#API_CreateRunCache_RequestSyntax) **   <a name="omics-CreateRunCache-request-cacheS3Location"></a>
Specify the S3 location for storing the cached task outputs. This data must be immediately accessible (not in an archived state).
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])(/(.{0,1024}))?`
Required: Yes

 ** [description](#API_CreateRunCache_RequestSyntax) **   <a name="omics-CreateRunCache-request-description"></a>
Enter a description of the run cache.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [name](#API_CreateRunCache_RequestSyntax) **   <a name="omics-CreateRunCache-request-name"></a>
Enter a user-friendly name for the run cache.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [requestId](#API_CreateRunCache_RequestSyntax) **   <a name="omics-CreateRunCache-request-requestId"></a>
A unique request token, to ensure idempotency. If you don't specify a token, AWS HealthOmics automatically generates a universally unique identifier (UUID) for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [tags](#API_CreateRunCache_RequestSyntax) **   <a name="omics-CreateRunCache-request-tags"></a>
Specify one or more tags to associate with this run cache.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateRunCache_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateRunCache_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateRunCache_ResponseSyntax) **   <a name="omics-CreateRunCache-response-arn"></a>
Unique resource identifier for the run cache.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`

 ** [id](#API_CreateRunCache_ResponseSyntax) **   <a name="omics-CreateRunCache-response-id"></a>
Identifier for the run cache.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [status](#API_CreateRunCache_ResponseSyntax) **   <a name="omics-CreateRunCache-response-status"></a>
Run cache status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `ACTIVE | DELETED | FAILED`

 ** [tags](#API_CreateRunCache_ResponseSyntax) **   <a name="omics-CreateRunCache-response-tags"></a>
The tags associated with this run cache.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateRunCache_Errors"></a>

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
<a name="API_CreateRunCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CreateRunCache)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CreateRunCache)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CreateRunCache)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CreateRunCache)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CreateRunCache)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CreateRunCache)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CreateRunCache)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CreateRunCache)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CreateRunCache)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CreateRunCache)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
