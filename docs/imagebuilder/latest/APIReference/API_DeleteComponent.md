---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteComponent.html
---

# DeleteComponent
<a name="API_DeleteComponent"></a>

Deletes a component build version. The request fails with `ResourceDependencyException` if an image recipe or container recipe references this component version. It also fails if the component build version is shared with other accounts.

## Request Syntax
<a name="API_DeleteComponent_RequestSyntax"></a>

```
DELETE /DeleteComponent?componentBuildVersionArn={{componentBuildVersionArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteComponent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [componentBuildVersionArn](#API_DeleteComponent_RequestSyntax) **   <a name="imagebuilder-DeleteComponent-request-uri-componentBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the component build version to delete.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):component/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: Yes

## Request Body
<a name="API_DeleteComponent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteComponent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "componentBuildVersionArn": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_DeleteComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [componentBuildVersionArn](#API_DeleteComponent_ResponseSyntax) **   <a name="imagebuilder-DeleteComponent-response-componentBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the component build version that this request deleted.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):component/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [requestId](#API_DeleteComponent_ResponseSyntax) **   <a name="imagebuilder-DeleteComponent-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DeleteComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ResourceDependencyException **
You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_DeleteComponent_Examples"></a>

### Delete a component build version
<a name="API_DeleteComponent_Example_1"></a>

The following example deletes the specified component build version.

#### Sample Request
<a name="API_DeleteComponent_Example_1_Request"></a>

```
DELETE /DeleteComponent?componentBuildVersionArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Acomponent%2Fmy-example-component%2F1.0.0%2F1 HTTP/1.1
```

#### Sample Response
<a name="API_DeleteComponent_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "c75a1764-2ca3-4cb4-9ce9-6d49f87942b0",
    "componentBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0/1"
}
```

## See Also
<a name="API_DeleteComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/DeleteComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/DeleteComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/DeleteComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/DeleteComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/DeleteComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/DeleteComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/DeleteComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/DeleteComponent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/DeleteComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/DeleteComponent)
