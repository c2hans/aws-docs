---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionScalingConfig.html
---

# PutFunctionScalingConfig
<a name="API_PutFunctionScalingConfig"></a>

Sets the scaling configuration for a Lambda Managed Instances function. The scaling configuration defines the minimum and maximum number of execution environments that can be provisioned for the function, allowing you to control scaling behavior and resource allocation.

## Request Syntax
<a name="API_PutFunctionScalingConfig_RequestSyntax"></a>

```
PUT /2025-11-30/functions/{{FunctionName}}/function-scaling-config?Qualifier={{Qualifier}} HTTP/1.1
Content-type: application/json

{
   "FunctionScalingConfig": {
      "MaxExecutionEnvironments": {{number}},
      "MinExecutionEnvironments": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_PutFunctionScalingConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_PutFunctionScalingConfig_RequestSyntax) **   <a name="lambda-PutFunctionScalingConfig-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)`
Required: Yes

 ** [Qualifier](#API_PutFunctionScalingConfig_RequestSyntax) **   <a name="lambda-PutFunctionScalingConfig-request-uri-Qualifier"></a>
Specify a version or alias to set the scaling configuration for a published version of the function.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(\$LATEST\.PUBLISHED|[0-9]+)`
Required: Yes

## Request Body
<a name="API_PutFunctionScalingConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FunctionScalingConfig](#API_PutFunctionScalingConfig_RequestSyntax) **   <a name="lambda-PutFunctionScalingConfig-request-FunctionScalingConfig"></a>
The scaling configuration to apply to the function, including minimum and maximum execution environment limits.
Type: [FunctionScalingConfig](API_FunctionScalingConfig.md) object
Required: No

## Response Syntax
<a name="API_PutFunctionScalingConfig_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "FunctionState": "string"
}
```

## Response Elements
<a name="API_PutFunctionScalingConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [FunctionState](#API_PutFunctionScalingConfig_ResponseSyntax) **   <a name="lambda-PutFunctionScalingConfig-response-FunctionState"></a>
The current state of the function after applying the scaling configuration.
Type: String
Valid Values: `Pending | Active | Inactive | Failed | Deactivating | Deactivated | ActiveNonInvocable | Deleting`

## Errors
<a name="API_PutFunctionScalingConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource already exists, or another operation is in progress.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_PutFunctionScalingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/PutFunctionScalingConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/PutFunctionScalingConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/PutFunctionScalingConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/PutFunctionScalingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/PutFunctionScalingConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/PutFunctionScalingConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/PutFunctionScalingConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/PutFunctionScalingConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/PutFunctionScalingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/PutFunctionScalingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
