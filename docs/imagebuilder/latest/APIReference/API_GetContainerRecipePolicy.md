---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetContainerRecipePolicy.html
---

# GetContainerRecipePolicy
<a name="API_GetContainerRecipePolicy"></a>

Retrieves the policy for a container recipe.

## Request Syntax
<a name="API_GetContainerRecipePolicy_RequestSyntax"></a>

```
GET /GetContainerRecipePolicy?containerRecipeArn={{containerRecipeArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetContainerRecipePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [containerRecipeArn](#API_GetContainerRecipePolicy_RequestSyntax) **   <a name="imagebuilder-GetContainerRecipePolicy-request-uri-containerRecipeArn"></a>
The Amazon Resource Name (ARN) of the container recipe for the policy being requested.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: Yes

## Request Body
<a name="API_GetContainerRecipePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetContainerRecipePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policy": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_GetContainerRecipePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_GetContainerRecipePolicy_ResponseSyntax) **   <a name="imagebuilder-GetContainerRecipePolicy-response-policy"></a>
The container recipe policy object that is returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30000.

 ** [requestId](#API_GetContainerRecipePolicy_ResponseSyntax) **   <a name="imagebuilder-GetContainerRecipePolicy-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetContainerRecipePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ResourceNotFoundException **
At least one of the resources referenced by your request does not exist.
HTTP Status Code: 404

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_GetContainerRecipePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetContainerRecipePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetContainerRecipePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetContainerRecipePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetContainerRecipePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetContainerRecipePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetContainerRecipePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetContainerRecipePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetContainerRecipePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetContainerRecipePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetContainerRecipePolicy)
