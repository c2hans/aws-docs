---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateEnrichmentJob.html
---

# CreateEnrichmentJob
<a name="API_CreateEnrichmentJob"></a>

Creates an asynchronous enrichment job to analyze time-series sensor data. The operation returns immediately with job details while processing continues in the background.

 **Idempotency**

Include a clientToken to make the operation idempotent. If you submit the same request with the same token within the idempotency window, you receive the original job details without creating a duplicate.

 **Prerequisites**

Before creating a job, ensure:
+ The workspace is in ACTIVE state (not being deleted)
+ You have IAM permissions for the workspace, dataset, and time-series resources
+ You have KMS Decrypt permission on the workspace's customer-managed encryption key
+ No duplicate job (same workspace, dataset, property, and job type) is currently running

 **Workflow**

1. Submit the job with configuration specifying which video data to analyze and the time range

1. Capture the jobId from the response

1. Use DescribeEnrichmentJob to monitor progress and check job status

1. When status reaches a terminal state (COMPLETED, FAILED, TIMED\_OUT, CANCELLED), check results

1. For COMPLETED jobs, query IoT SiteWise for semantic search on video events

 **Error Handling**
+ ConflictingOperationException: A duplicate job is already running for the same configuration
+ InvalidRequestException: Invalid parameters (e.g., both timeSeriesId and propertyAlias specified)
+ AccessDeniedException: Insufficient IAM or KMS permissions
+ LimitExceededException: Too many concurrent jobs or requests

## Request Syntax
<a name="API_CreateEnrichmentJob_RequestSyntax"></a>

```
POST /workspaces/{{workspaceName}}/enrichment-jobs HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "jobConfiguration": { ... }
}
```

## URI Request Parameters
<a name="API_CreateEnrichmentJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceName](#API_CreateEnrichmentJob_RequestSyntax) **   <a name="iotsitewise-CreateEnrichmentJob-request-uri-workspaceName"></a>
The name of the IoT SiteWise workspace containing the video data to analyze.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_CreateEnrichmentJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateEnrichmentJob_RequestSyntax) **   <a name="iotsitewise-CreateEnrichmentJob-request-clientToken"></a>
Optional unique token that makes the operation idempotent. If you submit the same request with the same token within the idempotency window, the service returns the original job without creating a duplicate. Use a UUID or timestamp-based token for each unique request.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [jobConfiguration](#API_CreateEnrichmentJob_RequestSyntax) **   <a name="iotsitewise-CreateEnrichmentJob-request-jobConfiguration"></a>
Configuration defining the type of enrichment analysis to perform and which video data to analyze. Currently supports eventDetection for generating embeddings from video data for semantic search.
Type: [EnrichmentJobConfiguration](API_EnrichmentJobConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateEnrichmentJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "jobId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateEnrichmentJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-CreateEnrichmentJob-response-createdAt"></a>
Timestamp when the enrichment job was created in ISO 8601 format.
Type: Timestamp

 ** [jobId](#API_CreateEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-CreateEnrichmentJob-response-jobId"></a>
Unique identifier for the enrichment job. Use this ID with DescribeEnrichmentJob to monitor progress or with CancelEnrichmentJob to cancel the job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [status](#API_CreateEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-CreateEnrichmentJob-response-status"></a>
Initial status of the enrichment job, typically PENDING. The job will transition to RUNNING when processing begins, then to a terminal state (COMPLETED, FAILED, TIMED\_OUT, or CANCELLED). Use DescribeEnrichmentJob to track status changes.
Type: String
Valid Values: `PENDING | RUNNING | COMPLETED | FAILED | TIMED_OUT | CANCELLED`

## Errors
<a name="API_CreateEnrichmentJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CreateEnrichmentJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateEnrichmentJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateEnrichmentJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateEnrichmentJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateEnrichmentJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateEnrichmentJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateEnrichmentJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateEnrichmentJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateEnrichmentJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateEnrichmentJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateEnrichmentJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
