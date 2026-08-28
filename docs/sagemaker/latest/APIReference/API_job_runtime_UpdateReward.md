---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_job_runtime_UpdateReward.html
---

# UpdateReward
<a name="API_job_runtime_UpdateReward"></a>

Updates the reward values for a trajectory and transitions it to reward-received status, signaling that it is eligible for processing. Call this operation after CompleteRollout to provide the computed reward scores.

## Request Syntax
<a name="API_job_runtime_UpdateReward_RequestSyntax"></a>

```
POST /update-reward HTTP/1.1
X-Amzn-SageMaker-Job-Arn: {{JobArn}}
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Rewards": [ {{number}} ],
   "TrajectoryId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_job_runtime_UpdateReward_RequestParameters"></a>

The request uses the following URI parameters.

 ** [JobArn](#API_job_runtime_UpdateReward_RequestSyntax) **   <a name="sagemaker-job_runtime_UpdateReward-request-JobArn"></a>
The job ARN.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:job/[a-zA-Z0-9_\-]+/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Request Body
<a name="API_job_runtime_UpdateReward_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_job_runtime_UpdateReward_RequestSyntax) **   <a name="sagemaker-job_runtime_UpdateReward-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

 ** [Rewards](#API_job_runtime_UpdateReward_RequestSyntax) **   <a name="sagemaker-job_runtime_UpdateReward-request-Rewards"></a>
The list of reward values to assign to this trajectory. Provide one reward value per turn in the trajectory.
Type: Array of doubles
Required: Yes

 ** [TrajectoryId](#API_job_runtime_UpdateReward_RequestSyntax) **   <a name="sagemaker-job_runtime_UpdateReward-request-TrajectoryId"></a>
The trajectory ID to update with reward values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_job_runtime_UpdateReward_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_job_runtime_UpdateReward_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_job_runtime_UpdateReward_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
HTTP Status Code: 409

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
<a name="API_job_runtime_UpdateReward_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemakerjobruntime-2026-02-01/UpdateReward)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemakerjobruntime-2026-02-01/UpdateReward)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakerjobruntime-2026-02-01/UpdateReward)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemakerjobruntime-2026-02-01/UpdateReward)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakerjobruntime-2026-02-01/UpdateReward)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemakerjobruntime-2026-02-01/UpdateReward)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemakerjobruntime-2026-02-01/UpdateReward)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemakerjobruntime-2026-02-01/UpdateReward)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemakerjobruntime-2026-02-01/UpdateReward)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakerjobruntime-2026-02-01/UpdateReward)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
