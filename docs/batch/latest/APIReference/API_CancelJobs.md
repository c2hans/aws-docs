---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_CancelJobs.html
---

# CancelJobs
<a name="API_CancelJobs"></a>

Cancels up to 50 jobs in an AWS Batch job queue. This is a bulk version of [CancelJob](API_CancelJob.md). Jobs that are in a `SUBMITTED`, `PENDING`, or `RUNNABLE` state are cancelled and the job status is updated to `FAILED`.

**Note**
A `PENDING` job is cancelled after all dependency jobs are completed. Therefore, it might take longer than expected to cancel a job in `PENDING` status.
When you try to cancel an array parent job in `PENDING`, AWS Batch attempts to cancel all child jobs. The array parent job is cancelled when all child jobs are completed.

Jobs that progressed to the `STARTING` or `RUNNING` state aren't cancelled. These jobs must be terminated with the [TerminateJob](API_TerminateJob.md) or [TerminateJobs](API_TerminateJobs.md) operation.

 AWS Batch reports the result for each job individually in the response. Jobs that were processed successfully are reported in the `successful` list. Jobs that encountered errors are reported in the `errors` list. The response returns an HTTP status code of `200` even when some jobs encountered errors, so check the `errors` list. Jobs that can't be found are treated as successfully processed.

**Important**
This operation requires `batch:CancelJob` permission for each job in the request. There is no separate `batch:CancelJobs` IAM action. If a caller's IAM policy grants `batch:CancelJob`, they can use both the singular [CancelJob](API_CancelJob.md) and bulk `CancelJobs` operations.

## Request Syntax
<a name="API_CancelJobs_RequestSyntax"></a>

```
POST /v1/canceljobs HTTP/1.1
Content-type: application/json

{
   "jobs": [ "{{string}}" ],
   "reason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CancelJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CancelJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobs](#API_CancelJobs_RequestSyntax) **   <a name="Batch-CancelJobs-request-jobs"></a>
An array of up to 50 AWS Batch job IDs of the jobs to cancel.
Type: Array of strings
Required: Yes

 ** [reason](#API_CancelJobs_RequestSyntax) **   <a name="Batch-CancelJobs-request-reason"></a>
A message to attach to the job that explains the reason for cancelling it. This message is returned by future [DescribeJobs](API_DescribeJobs.md) operations on the job. It is also recorded in the AWS Batch activity logs.
This parameter has a limit of 1024 characters.
Type: String
Required: Yes

## Response Syntax
<a name="API_CancelJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "code": "string",
         "job": "string",
         "message": "string"
      }
   ],
   "successful": [ "string" ]
}
```

## Response Elements
<a name="API_CancelJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_CancelJobs_ResponseSyntax) **   <a name="Batch-CancelJobs-response-errors"></a>
A list of `CancelJobsErrorDetail` items, one for each job that couldn't be cancelled. Each item includes the job ID along with a code and message that describe why the job wasn't cancelled.
Type: Array of [CancelJobsErrorDetail](API_CancelJobsErrorDetail.md) objects

 ** [successful](#API_CancelJobs_ResponseSyntax) **   <a name="Batch-CancelJobs-response-successful"></a>
A list of the job IDs whose cancellation request was accepted.
Type: Array of strings

## Errors
<a name="API_CancelJobs_Errors"></a>

 ** ClientException **
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
HTTP Status Code: 500

## Examples
<a name="API_CancelJobs_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CancelJobs_Example_1"></a>

This example cancels the jobs with the specified job IDs.

#### Sample Request
<a name="API_CancelJobs_Example_1_Request"></a>

```
POST /v1/canceljobs HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161130T001258Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.1.0 botocore/1.4.79

{
  "jobs": [
    "1d828f65-7a4d-42e8-996d-3b900ed59dc4",
    "b3d0f26e-6d3a-4a5b-9c2e-7f4a1b2c3d4e"
  ],
  "reason": "Cancelling jobs."
}
```

#### Sample Response
<a name="API_CancelJobs_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Wed, 30 Nov 2016 00:12:59 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 bfdd5909914586f5bc4851846228c27f.cloudfront.net (CloudFront)
X-Amz-Cf-Id: whn1dX1uTx34Lvao7-7ZdkDXEbCZ_sjn3v3hHVFgbo1ORJtXyeggSw==

{
  "successful": [
    "1d828f65-7a4d-42e8-996d-3b900ed59dc4"
  ],
  "errors": [
    {
      "job": "b3d0f26e-6d3a-4a5b-9c2e-7f4a1b2c3d4e",
      "code": "ServerException",
      "message": "Failed to read job state. Please retry this job."
    }
  ]
}
```

## See Also
<a name="API_CancelJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/CancelJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/CancelJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/CancelJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/CancelJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CancelJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/CancelJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/CancelJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/CancelJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CancelJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/CancelJobs)
