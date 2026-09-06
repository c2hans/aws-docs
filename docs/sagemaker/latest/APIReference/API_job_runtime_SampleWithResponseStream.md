---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_job_runtime_SampleWithResponseStream.html
---

# SampleWithResponseStream
<a name="API_job_runtime_SampleWithResponseStream"></a>

Sends a streaming inference request to the model during a job execution. Returns the response as a stream of payload chunks. Each turn is captured for later use.

## Request Syntax
<a name="API_job_runtime_SampleWithResponseStream_RequestSyntax"></a>

```
POST /sample-with-response-stream HTTP/1.1
X-Amzn-SageMaker-Job-Arn: {{JobArn}}
X-Amzn-SageMaker-Trajectory-Id: {{TrajectoryId}}

{{Body}}
```

## URI Request Parameters
<a name="API_job_runtime_SampleWithResponseStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [JobArn](#API_job_runtime_SampleWithResponseStream_RequestSyntax) **   <a name="sagemaker-job_runtime_SampleWithResponseStream-request-JobArn"></a>
The job ARN that identifies which model session to route the inference request to.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:job/[a-zA-Z0-9_\-]+/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [TrajectoryId](#API_job_runtime_SampleWithResponseStream_RequestSyntax) **   <a name="sagemaker-job_runtime_SampleWithResponseStream-request-TrajectoryId"></a>
The trajectory ID for grouping turns into a single rollout. Each turn is captured for later use.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_job_runtime_SampleWithResponseStream_RequestBody"></a>

The request accepts the following binary data.

 ** [Body](#API_job_runtime_SampleWithResponseStream_RequestSyntax) **   <a name="sagemaker-job_runtime_SampleWithResponseStream-request-Body"></a>
The raw inference request body in OpenAI-compatible JSON format.
Required: Yes

## Response Syntax
<a name="API_job_runtime_SampleWithResponseStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}

{{Body}}
```

## Response Elements
<a name="API_job_runtime_SampleWithResponseStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ContentType](#API_job_runtime_SampleWithResponseStream_ResponseSyntax) **   <a name="sagemaker-job_runtime_SampleWithResponseStream-response-ContentType"></a>
MIME type of the streaming inference result.

The response returns the following as the HTTP body.

 ** [Body](#API_job_runtime_SampleWithResponseStream_ResponseSyntax) **   <a name="sagemaker-job_runtime_SampleWithResponseStream-response-Body"></a>
The streaming response body, delivered as a series of PayloadPart events.

## Errors
<a name="API_job_runtime_SampleWithResponseStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServiceError **
An internal service error occurred. Retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have exceeded a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled. Retry the request after a brief wait.
HTTP Status Code: 429

 ** ValidationException **
The request is not valid. Check the request syntax and parameters.
HTTP Status Code: 400

## See Also
<a name="API_job_runtime_SampleWithResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemakerjobruntime-2026-02-01/SampleWithResponseStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemakerjobruntime-2026-02-01/SampleWithResponseStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakerjobruntime-2026-02-01/SampleWithResponseStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemakerjobruntime-2026-02-01/SampleWithResponseStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakerjobruntime-2026-02-01/SampleWithResponseStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemakerjobruntime-2026-02-01/SampleWithResponseStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemakerjobruntime-2026-02-01/SampleWithResponseStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemakerjobruntime-2026-02-01/SampleWithResponseStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemakerjobruntime-2026-02-01/SampleWithResponseStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakerjobruntime-2026-02-01/SampleWithResponseStream)
