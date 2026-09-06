---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_PutComponentPolicy.html
---

# PutComponentPolicy
<a name="API_PutComponentPolicy"></a>

Applies a policy to a component. We recommend that you call the RAM API [CreateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html) to share resources. If you call the Image Builder API `PutComponentPolicy`, you must also call the RAM API [PromoteResourceShareCreatedFromPolicy](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html) in order for the resource to be visible to all principals with whom the resource is shared.

## Request Syntax
<a name="API_PutComponentPolicy_RequestSyntax"></a>

```
PUT /PutComponentPolicy HTTP/1.1
Content-type: application/json

{
   "componentArn": "{{string}}",
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutComponentPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutComponentPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [componentArn](#API_PutComponentPolicy_RequestSyntax) **   <a name="imagebuilder-PutComponentPolicy-request-componentArn"></a>
The Amazon Resource Name (ARN) of the component that this policy should be applied to.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):component/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: Yes

 ** [policy](#API_PutComponentPolicy_RequestSyntax) **   <a name="imagebuilder-PutComponentPolicy-request-policy"></a>
The policy to apply.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30000.
Required: Yes

## Response Syntax
<a name="API_PutComponentPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "componentArn": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_PutComponentPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [componentArn](#API_PutComponentPolicy_ResponseSyntax) **   <a name="imagebuilder-PutComponentPolicy-response-componentArn"></a>
The Amazon Resource Name (ARN) of the component that this policy was applied to.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):component/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [requestId](#API_PutComponentPolicy_ResponseSyntax) **   <a name="imagebuilder-PutComponentPolicy-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_PutComponentPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidParameterValueException **
The value that you provided for the specified parameter is invalid.
HTTP Status Code: 400

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
<a name="API_PutComponentPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/PutComponentPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/PutComponentPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/PutComponentPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/PutComponentPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/PutComponentPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/PutComponentPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/PutComponentPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/PutComponentPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/PutComponentPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/PutComponentPolicy)
