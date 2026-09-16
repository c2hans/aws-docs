---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CancelEnrichmentJob.html
---

# CancelEnrichmentJob
<a name="API_CancelEnrichmentJob"></a>

Cancels a running or pending enrichment job. This is an idempotent operation—calling it multiple times with the same jobId is safe and returns the current status.

 **Behavior**
+ Jobs in PENDING or RUNNING status transition to CANCELLED
+ Jobs in RUNNING state may not be cancellable once they have progressed to certain processing stages
+ Jobs already in terminal states (COMPLETED, FAILED, TIMED\_OUT) cannot be cancelled; the operation returns a ConflictingOperationException
+ Cancelling an already-CANCELLED job is a no-op and returns the current status (idempotent behavior)
+ The API responds immediately after recording the cancellation
+ Cleanup of job resources happens asynchronously in the background

 **When to Cancel**

Cancel a job when:
+ The job is taking longer than expected
+ The job was created with incorrect parameters
+ You no longer need the results

 **Idempotency**

You can safely retry cancellation requests. Calling CancelEnrichmentJob multiple times for the same job returns the current status without error as long as the job is not in a terminal state other than CANCELLED.

## Request Syntax
<a name="API_CancelEnrichmentJob_RequestSyntax"></a>

```
POST /workspaces/{{workspaceName}}/enrichment-jobs/{{jobId}}/cancel HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelEnrichmentJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_CancelEnrichmentJob_RequestSyntax) **   <a name="iotsitewise-CancelEnrichmentJob-request-uri-jobId"></a>
The unique identifier of the enrichment job to cancel. This is the jobId returned by CreateEnrichmentJob.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [workspaceName](#API_CancelEnrichmentJob_RequestSyntax) **   <a name="iotsitewise-CancelEnrichmentJob-request-uri-workspaceName"></a>
The name of the IoT SiteWise workspace containing the enrichment job to cancel.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_CancelEnrichmentJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelEnrichmentJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CancelEnrichmentJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobId](#API_CancelEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-CancelEnrichmentJob-response-jobId"></a>
The unique identifier of the cancelled enrichment job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [status](#API_CancelEnrichmentJob_ResponseSyntax) **   <a name="iotsitewise-CancelEnrichmentJob-response-status"></a>
The status of the enrichment job after cancellation. This will be CANCELLED, indicating the job was successfully cancelled or was already in CANCELLED state (idempotent behavior).
Type: String
Valid Values: `PENDING | RUNNING | COMPLETED | FAILED | TIMED_OUT | CANCELLED`

## Errors
<a name="API_CancelEnrichmentJob_Errors"></a>

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
<a name="API_CancelEnrichmentJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CancelEnrichmentJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CancelEnrichmentJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CancelEnrichmentJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CancelEnrichmentJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CancelEnrichmentJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CancelEnrichmentJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CancelEnrichmentJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CancelEnrichmentJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CancelEnrichmentJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CancelEnrichmentJob)
