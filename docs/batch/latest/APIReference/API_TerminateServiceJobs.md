---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_TerminateServiceJobs.html
---

# TerminateServiceJobs
<a name="API_TerminateServiceJobs"></a>

Terminates up to 50 service jobs in a job queue. This is a bulk version of [TerminateServiceJob](API_TerminateServiceJob.md).

 AWS Batch reports the result for each service job individually in the response. Service jobs that were processed successfully are reported in the `successful` list. Service jobs that encountered errors are reported in the `errors` list. The response returns an HTTP status code of `200` even when some service jobs encountered errors, so check the `errors` list. Service jobs that can't be found are treated as successfully processed.

**Important**
This operation requires `batch:TerminateServiceJob` permission for each service job in the request. There is no separate `batch:TerminateServiceJobs` IAM action. If a caller's IAM policy grants `batch:TerminateServiceJob`, they can use both the singular `TerminateServiceJob` and bulk `TerminateServiceJobs` operations.

## Request Syntax
<a name="API_TerminateServiceJobs_RequestSyntax"></a>

```
POST /v1/terminateservicejobs HTTP/1.1
Content-type: application/json

{
   "jobs": [ "{{string}}" ],
   "reason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_TerminateServiceJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TerminateServiceJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobs](#API_TerminateServiceJobs_RequestSyntax) **   <a name="Batch-TerminateServiceJobs-request-jobs"></a>
An array of up to 50 service job IDs of the service jobs to terminate.
Type: Array of strings
Required: Yes

 ** [reason](#API_TerminateServiceJobs_RequestSyntax) **   <a name="Batch-TerminateServiceJobs-request-reason"></a>
A message to attach to the service job that explains the reason for terminating it. This message is returned by `DescribeServiceJob` operations on the service job.
Type: String
Required: Yes

## Response Syntax
<a name="API_TerminateServiceJobs_ResponseSyntax"></a>

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
<a name="API_TerminateServiceJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_TerminateServiceJobs_ResponseSyntax) **   <a name="Batch-TerminateServiceJobs-response-errors"></a>
A list of `TerminateServiceJobsErrorDetail` items, one for each service job that couldn't be terminated. Each item includes the service job ID along with a code and message that describe why the service job wasn't terminated.
Type: Array of [TerminateServiceJobsErrorDetail](API_TerminateServiceJobsErrorDetail.md) objects

 ** [successful](#API_TerminateServiceJobs_ResponseSyntax) **   <a name="Batch-TerminateServiceJobs-response-successful"></a>
A list of the service job IDs whose termination request was accepted.
Type: Array of strings

## Errors
<a name="API_TerminateServiceJobs_Errors"></a>

 ** ClientException **
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
HTTP Status Code: 500

## Examples
<a name="API_TerminateServiceJobs_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_TerminateServiceJobs_Example_1"></a>

This example terminates the specified service jobs with a reason.

#### Sample Request
<a name="API_TerminateServiceJobs_Example_1_Request"></a>

```
POST /v1/terminateservicejobs HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T164055Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
  "jobs": [
    "a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d",
    "b3d0f26e-6d3a-4a5b-9c2e-7f4a1b2c3d4e"
  ],
  "reason": "Job terminated by user request"
}
```

#### Sample Response
<a name="API_TerminateServiceJobs_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Fri, 01 Aug 2025 16:40:56 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 254fde64p7r0s3t6u9v2w5x8y1zexample.cloudfront.net (CloudFront)
X-Amz-Cf-Id: pqr8stu1vwx4yz7012fghijklmnopqrstuvwxyzabexample

{
  "successful": [
    "a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d"
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
<a name="API_TerminateServiceJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/TerminateServiceJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/TerminateServiceJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/TerminateServiceJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/TerminateServiceJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/TerminateServiceJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/TerminateServiceJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/TerminateServiceJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/TerminateServiceJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/TerminateServiceJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/TerminateServiceJobs)
