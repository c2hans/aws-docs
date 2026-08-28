---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_GetMLEndpoint.html
---

# GetMLEndpoint
<a name="API_GetMLEndpoint"></a>

Retrieves details about an inference endpoint. See [Managing inference endpoints using the endpoints command](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-endpoints.html).

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetMLEndpointStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getmlendpointstatus) IAM action in that cluster.

## Request Syntax
<a name="API_GetMLEndpoint_RequestSyntax"></a>

```
GET /ml/endpoints/{{id}}?neptuneIamRoleArn={{neptuneIamRoleArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMLEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetMLEndpoint_RequestSyntax) **   <a name="neptunedata-GetMLEndpoint-request-uri-id"></a>
The unique identifier of the inference endpoint.
Required: Yes

 ** [neptuneIamRoleArn](#API_GetMLEndpoint_RequestSyntax) **   <a name="neptunedata-GetMLEndpoint-request-uri-neptuneIamRoleArn"></a>
The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.

## Request Body
<a name="API_GetMLEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMLEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endpoint": {
      "arn": "string",
      "cloudwatchLogUrl": "string",
      "failureReason": "string",
      "name": "string",
      "outputLocation": "string",
      "status": "string"
   },
   "endpointConfig": {
      "arn": "string",
      "name": "string"
   },
   "id": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetMLEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endpoint](#API_GetMLEndpoint_ResponseSyntax) **   <a name="neptunedata-GetMLEndpoint-response-endpoint"></a>
The endpoint definition.
Type: [MlResourceDefinition](API_MlResourceDefinition.md) object

 ** [endpointConfig](#API_GetMLEndpoint_ResponseSyntax) **   <a name="neptunedata-GetMLEndpoint-response-endpointConfig"></a>
The endpoint configuration
Type: [MlConfigDefinition](API_MlConfigDefinition.md) object

 ** [id](#API_GetMLEndpoint_ResponseSyntax) **   <a name="neptunedata-GetMLEndpoint-response-id"></a>
The unique identifier of the inference endpoint.
Type: String

 ** [status](#API_GetMLEndpoint_ResponseSyntax) **   <a name="neptunedata-GetMLEndpoint-response-status"></a>
The status of the inference endpoint.
Type: String

## Errors
<a name="API_GetMLEndpoint_Errors"></a>

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
<a name="API_GetMLEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/GetMLEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/GetMLEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/GetMLEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/GetMLEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/GetMLEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/GetMLEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/GetMLEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/GetMLEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/GetMLEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/GetMLEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Neptune Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
