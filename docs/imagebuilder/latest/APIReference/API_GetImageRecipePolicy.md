---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImageRecipePolicy.html
---

# GetImageRecipePolicy
<a name="API_GetImageRecipePolicy"></a>

Gets an image recipe policy.

## Request Syntax
<a name="API_GetImageRecipePolicy_RequestSyntax"></a>

```
GET /GetImageRecipePolicy?imageRecipeArn={{imageRecipeArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetImageRecipePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imageRecipeArn](#API_GetImageRecipePolicy_RequestSyntax) **   <a name="imagebuilder-GetImageRecipePolicy-request-uri-imageRecipeArn"></a>
The Amazon Resource Name (ARN) of the image recipe whose policy you want to retrieve.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: Yes

## Request Body
<a name="API_GetImageRecipePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetImageRecipePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policy": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_GetImageRecipePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_GetImageRecipePolicy_ResponseSyntax) **   <a name="imagebuilder-GetImageRecipePolicy-response-policy"></a>
The image recipe policy object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30000.

 ** [requestId](#API_GetImageRecipePolicy_ResponseSyntax) **   <a name="imagebuilder-GetImageRecipePolicy-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetImageRecipePolicy_Errors"></a>

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
<a name="API_GetImageRecipePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetImageRecipePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetImageRecipePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetImageRecipePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetImageRecipePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetImageRecipePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetImageRecipePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetImageRecipePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetImageRecipePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetImageRecipePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetImageRecipePolicy)
