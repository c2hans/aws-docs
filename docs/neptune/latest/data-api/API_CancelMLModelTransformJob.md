---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelMLModelTransformJob.html
---

# CancelMLModelTransformJob
<a name="API_CancelMLModelTransformJob"></a>

Cancels a specified model transform job. See [Use a trained model to generate new model artifacts](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-model-transform.html).

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:CancelMLModelTransformJob](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelmlmodeltransformjob) IAM action in that cluster.

## Request Syntax
<a name="API_CancelMLModelTransformJob_RequestSyntax"></a>

```
DELETE /ml/modeltransform/{{id}}?clean={{clean}}&neptuneIamRoleArn={{neptuneIamRoleArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelMLModelTransformJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clean](#API_CancelMLModelTransformJob_RequestSyntax) **   <a name="neptunedata-CancelMLModelTransformJob-request-uri-clean"></a>
If this flag is set to `TRUE`, all Neptune ML S3 artifacts should be deleted when the job is stopped. The default is `FALSE`.

 ** [id](#API_CancelMLModelTransformJob_RequestSyntax) **   <a name="neptunedata-CancelMLModelTransformJob-request-uri-id"></a>
The unique ID of the model transform job to be canceled.
Required: Yes

 ** [neptuneIamRoleArn](#API_CancelMLModelTransformJob_RequestSyntax) **   <a name="neptunedata-CancelMLModelTransformJob-request-uri-neptuneIamRoleArn"></a>
The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.

## Request Body
<a name="API_CancelMLModelTransformJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelMLModelTransformJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_CancelMLModelTransformJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_CancelMLModelTransformJob_ResponseSyntax) **   <a name="neptunedata-CancelMLModelTransformJob-response-status"></a>
the status of the cancelation.
Type: String

## Errors
<a name="API_CancelMLModelTransformJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
Raised when a request is submitted that cannot be processed.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the bad request.
HTTP Status Code: 400

 ** ClientTimeoutException **
Raised when a request timed out in the client.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 408

 ** ConstraintViolationException **
Raised when a value in a request field did not satisfy required constraints.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** IllegalArgumentException **
Raised when an argument in a request is not supported.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** InvalidArgumentException **
Raised when an argument in a request has an invalid value.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** InvalidParameterException **
Raised when a parameter value is not valid.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that includes an invalid parameter.
HTTP Status Code: 400

 ** MissingParameterException **
Raised when a required parameter is missing.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in which the parameter is missing.
HTTP Status Code: 400

 ** MLResourceNotFoundException **
Raised when a specified machine-learning resource could not be found.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 404

 ** PreconditionsFailedException **
Raised when a precondition for processing a request is not satisfied.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** TooManyRequestsException **
Raised when the number of requests being processed exceeds the limit.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that could not be processed for this reason.
HTTP Status Code: 429

 ** UnsupportedOperationException **
Raised when a request attempts to initiate an operation that is not supported.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

## See Also
<a name="API_CancelMLModelTransformJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/CancelMLModelTransformJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/CancelMLModelTransformJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/CancelMLModelTransformJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/CancelMLModelTransformJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/CancelMLModelTransformJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/CancelMLModelTransformJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/CancelMLModelTransformJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/CancelMLModelTransformJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/CancelMLModelTransformJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/CancelMLModelTransformJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Neptune Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
