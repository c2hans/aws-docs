---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeEnrichmentJob.html
---

# DescribeEnrichmentJob
<a name="API_DescribeEnrichmentJob"></a>

Retrieves detailed information about a specific enrichment job, including its current status, configuration, and timestamps.

 **Use Cases**
+ Monitor job progress by checking status updates with DescribeEnrichmentJob
+ Retrieve the complete job configuration submitted during creation
+ Debug failed jobs by examining the failureMessage field
+ Track job lifecycle with creation, update, completion, and cancellation timestamps

 **Status Monitoring**

Jobs progress through statuses: PENDING → RUNNING → terminal state

Terminal states:
+ COMPLETED: Job finished successfully; query IoT SiteWise for semantic search results
+ FAILED: Job encountered an error; check failureMessage for details
+ TIMED\_OUT: Job exceeded maximum processing time
+ CANCELLED: Job was cancelled via CancelEnrichmentJob

 **Response Fields**

The response includes:
+ Current job status and type
+ Full job configuration as originally submitted
+ Lifecycle timestamps (created, updated, completed, cancelled)
+ Failure details if status is FAILED

## Request Syntax
<a name="API_DescribeEnrichmentJob_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}}/enrichment-jobs/{{jobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeEnrichmentJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_DescribeEnrichmentJob_RequestSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-request-uri-jobId"></a>
The unique identifier of the enrichment job to retrieve. This is the jobId returned by CreateEnrichmentJob.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [workspaceName](#API_DescribeEnrichmentJob_RequestSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-request-uri-workspaceName"></a>
The name of the IoT SiteWise workspace containing the enrichment job.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_DescribeEnrichmentJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeEnrichmentJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cancelledAt": number,
   "completedAt": number,
   "createdAt": number,
   "failureMessage": "string",
   "jobConfiguration": { ... },
   "jobId": "string",
   "jobType": "string",
   "status": "string",
   "updatedAt": number,
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_DescribeEnrichmentJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cancelledAt](#API_DescribeEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-response-cancelledAt"></a>
Timestamp when the job was cancelled in ISO 8601 format. Only present if status is CANCELLED.
Type: Timestamp

 ** [completedAt](#API_DescribeEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-response-completedAt"></a>
Timestamp when the job completed successfully in ISO 8601 format. Only present if status is COMPLETED.
Type: Timestamp

 ** [createdAt](#API_DescribeEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-response-createdAt"></a>
Timestamp when the enrichment job was created in ISO 8601 format.
Type: Timestamp

 ** [failureMessage](#API_DescribeEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-response-failureMessage"></a>
Human-readable error message explaining why the job failed. Only present if status is FAILED. Use this information to diagnose configuration issues, permission problems, or data processing errors.
Type: String

 ** [jobConfiguration](#API_DescribeEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-response-jobConfiguration"></a>
The complete job configuration as originally submitted, including the analysis type and parameters. For event detection jobs, this includes the dataset ID, time series identifier, and trim settings defining the analysis time range.
Type: [EnrichmentJobConfiguration](API_EnrichmentJobConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [jobId](#API_DescribeEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-response-jobId"></a>
The unique identifier of the enrichment job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [jobType](#API_DescribeEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-response-jobType"></a>
The type of enrichment job, derived from the job configuration. Currently EVENT\_DETECTION is the only supported type.
Type: String
Valid Values: `EVENT_DETECTION`

 ** [status](#API_DescribeEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-response-status"></a>
Current status of the enrichment job. Possible values:
+ PENDING: Job is waiting to start processing
+ RUNNING: Job is actively processing video data
+ COMPLETED: Job finished successfully; embeddings available in IoT SiteWise
+ FAILED: Job encountered an error; see failureMessage for details
+ TIMED\_OUT: Job exceeded maximum processing time limit
+ CANCELLED: Job was cancelled by user request
Type: String
Valid Values: `PENDING | RUNNING | COMPLETED | FAILED | TIMED_OUT | CANCELLED`

 ** [updatedAt](#API_DescribeEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-response-updatedAt"></a>
Timestamp when the job status was last updated in ISO 8601 format. Useful for tracking recent activity.
Type: Timestamp

 ** [workspaceName](#API_DescribeEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-DescribeEnrichmentJob-response-workspaceName"></a>
The name of the IoT SiteWise workspace containing the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_DescribeEnrichmentJob_Errors"></a>

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
<a name="API_DescribeEnrichmentJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeEnrichmentJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeEnrichmentJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeEnrichmentJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeEnrichmentJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeEnrichmentJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeEnrichmentJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeEnrichmentJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeEnrichmentJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeEnrichmentJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeEnrichmentJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
