---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_job_runtime_Sample.html
---

# Sample
<a name="API_job_runtime_Sample"></a>

Sends an inference request to the model during a job execution. The request and response bodies are forwarded to and from the model without modification. Each turn (prompt and response) is captured for later use.

## Request Syntax
<a name="API_job_runtime_Sample_RequestSyntax"></a>

```
POST /sample HTTP/1.1
X-Amzn-SageMaker-Job-Arn: {{JobArn}}
X-Amzn-SageMaker-Trajectory-Id: {{TrajectoryId}}

{{Body}}
```

## URI Request Parameters
<a name="API_job_runtime_Sample_RequestParameters"></a>

The request uses the following URI parameters.

 ** [JobArn](#API_job_runtime_Sample_RequestSyntax) **   <a name="sagemaker-job_runtime_Sample-request-JobArn"></a>
The job ARN that identifies which model session to route the inference request to.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:job/[a-zA-Z0-9_\-]+/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [TrajectoryId](#API_job_runtime_Sample_RequestSyntax) **   <a name="sagemaker-job_runtime_Sample-request-TrajectoryId"></a>
The trajectory ID for grouping turns into a single rollout. Each turn (prompt and response) is captured for later use.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_job_runtime_Sample_RequestBody"></a>

The request accepts the following binary data.

 ** [Body](#API_job_runtime_Sample_RequestSyntax) **   <a name="sagemaker-job_runtime_Sample-request-Body"></a>
The raw inference request body in OpenAI-compatible JSON format.
Required: Yes

## Response Syntax
<a name="API_job_runtime_Sample_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}

{{Body}}
```

## Response Elements
<a name="API_job_runtime_Sample_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ContentType](#API_job_runtime_Sample_ResponseSyntax) **   <a name="sagemaker-job_runtime_Sample-response-ContentType"></a>
MIME type of the inference result.

The response returns the following as the HTTP body.

 ** [Body](#API_job_runtime_Sample_ResponseSyntax) **   <a name="sagemaker-job_runtime_Sample-response-Body"></a>
The raw inference response body from the model.

## Errors
<a name="API_job_runtime_Sample_Errors"></a>

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
<a name="API_job_runtime_Sample_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemakerjobruntime-2026-02-01/Sample)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemakerjobruntime-2026-02-01/Sample)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakerjobruntime-2026-02-01/Sample)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemakerjobruntime-2026-02-01/Sample)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakerjobruntime-2026-02-01/Sample)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemakerjobruntime-2026-02-01/Sample)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemakerjobruntime-2026-02-01/Sample)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemakerjobruntime-2026-02-01/Sample)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemakerjobruntime-2026-02-01/Sample)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakerjobruntime-2026-02-01/Sample)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
