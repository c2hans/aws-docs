---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_GetLayerVersionPolicy.html
---

# GetLayerVersionPolicy
<a name="API_GetLayerVersionPolicy"></a>

Returns the permission policy for a version of an [AWS Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html). For more information, see [AddLayerVersionPermission](API_AddLayerVersionPermission.md).

## Request Syntax
<a name="API_GetLayerVersionPolicy_RequestSyntax"></a>

```
GET /2018-10-31/layers/{{LayerName}}/versions/{{VersionNumber}}/policy HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLayerVersionPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LayerName](#API_GetLayerVersionPolicy_RequestSyntax) **   <a name="lambda-GetLayerVersionPolicy-request-uri-LayerName"></a>
The name or Amazon Resource Name (ARN) of the layer.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+`
Required: Yes

 ** [VersionNumber](#API_GetLayerVersionPolicy_RequestSyntax) **   <a name="lambda-GetLayerVersionPolicy-request-uri-VersionNumber"></a>
The version number.
Required: Yes

## Request Body
<a name="API_GetLayerVersionPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLayerVersionPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": "string",
   "RevisionId": "string"
}
```

## Response Elements
<a name="API_GetLayerVersionPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_GetLayerVersionPolicy_ResponseSyntax) **   <a name="lambda-GetLayerVersionPolicy-response-Policy"></a>
The policy document.
Type: String

 ** [RevisionId](#API_GetLayerVersionPolicy_ResponseSyntax) **   <a name="lambda-GetLayerVersionPolicy-response-RevisionId"></a>
A unique identifier for the current revision of the policy.
Type: String

## Errors
<a name="API_GetLayerVersionPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

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
<a name="API_GetLayerVersionPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/GetLayerVersionPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/GetLayerVersionPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/GetLayerVersionPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/GetLayerVersionPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/GetLayerVersionPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/GetLayerVersionPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/GetLayerVersionPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/GetLayerVersionPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/GetLayerVersionPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/GetLayerVersionPolicy)
