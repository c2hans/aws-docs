---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImagePolicy.html
---

# GetImagePolicy
<a name="API_GetImagePolicy"></a>

Retrieves an image policy.

## Request Syntax
<a name="API_GetImagePolicy_RequestSyntax"></a>

```
GET /GetImagePolicy?imageArn={{imageArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetImagePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imageArn](#API_GetImagePolicy_RequestSyntax) **   <a name="imagebuilder-GetImagePolicy-request-uri-imageArn"></a>
The Amazon Resource Name (ARN) of the image whose policy you want to retrieve.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: Yes

## Request Body
<a name="API_GetImagePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetImagePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policy": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_GetImagePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_GetImagePolicy_ResponseSyntax) **   <a name="imagebuilder-GetImagePolicy-response-policy"></a>
The resource policy for the image, as a JSON policy document. If the image has no policy applied, the response contains an empty JSON object (`{}`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30000.

 ** [requestId](#API_GetImagePolicy_ResponseSyntax) **   <a name="imagebuilder-GetImagePolicy-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetImagePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
At least one of the resources referenced by your request does not exist.
HTTP Status Code: 404

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_GetImagePolicy_Examples"></a>

### Retrieve the resource policy for an image
<a name="API_GetImagePolicy_Example_1"></a>

The following example retrieves the resource policy for an image build version that was shared with account 444455556666.

#### Sample Request
<a name="API_GetImagePolicy_Example_1_Request"></a>

```
GET /GetImagePolicy?imageArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Aimage%2Fmy-example-recipe%2F1.0.0%2F1 HTTP/1.1
```

#### Sample Response
<a name="API_GetImagePolicy_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "bc0c8348-c0d9-452a-af20-2640430df585",
    "policy": "{\"Version\": \"2012-10-17\", \"Statement\": [{\"Effect\": \"Allow\", \"Principal\": {\"AWS\": \"arn:aws:iam::444455556666:root\"}, \"Action\": [\"imagebuilder:GetImage\", \"imagebuilder:ListImages\"], \"Resource\": [\"arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1\"]}]}"
}
```

## See Also
<a name="API_GetImagePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetImagePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetImagePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetImagePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetImagePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetImagePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetImagePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetImagePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetImagePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetImagePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetImagePolicy)
