---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteImage.html
---

# DeleteImage
<a name="API_DeleteImage"></a>

Deletes an Image Builder image resource. This does not delete any EC2 AMIs or ECR container images that are created during the image build process. You must clean those up separately, using the appropriate Amazon EC2 or Amazon ECR console actions, or API or AWS CLI commands.

The request fails with `ResourceDependencyException` if the image is shared with other accounts, or if other resources depend on it. It also fails while the image build is still running. Cancel an in-progress build with [CancelImageCreation](API_CancelImageCreation.md) before you delete the image.
+ To deregister an EC2 Linux AMI, see [Deregister your Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html) in the * *Amazon EC2 User Guide* *.
+ To deregister an EC2 Windows AMI, see [Deregister your Windows AMI](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/deregister-ami.html) in the * *Amazon EC2 Windows Guide* *.
+ To delete a container image from Amazon ECR, see [Deleting an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/delete_image.html) in the *Amazon ECR User Guide*.

## Request Syntax
<a name="API_DeleteImage_RequestSyntax"></a>

```
DELETE /DeleteImage?imageBuildVersionArn={{imageBuildVersionArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteImage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imageBuildVersionArn](#API_DeleteImage_RequestSyntax) **   <a name="imagebuilder-DeleteImage-request-uri-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the Image Builder image resource to delete.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: Yes

## Request Body
<a name="API_DeleteImage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteImage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imageBuildVersionArn": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_DeleteImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageBuildVersionArn](#API_DeleteImage_ResponseSyntax) **   <a name="imagebuilder-DeleteImage-response-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the Image Builder image resource that this request deleted.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [requestId](#API_DeleteImage_ResponseSyntax) **   <a name="imagebuilder-DeleteImage-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DeleteImage_Errors"></a>

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
<a name="API_DeleteImage_Examples"></a>

### Delete an image build version
<a name="API_DeleteImage_Example_1"></a>

The following example deletes the Image Builder image record for the specified build version. EC2 AMIs or ECR container images that the build created aren't removed.

#### Sample Request
<a name="API_DeleteImage_Example_1_Request"></a>

```
DELETE /DeleteImage?imageBuildVersionArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Aimage%2Fmy-example-recipe%2F1.0.0%2F1 HTTP/1.1
```

#### Sample Response
<a name="API_DeleteImage_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "fd45526c-ec37-4345-8843-329e4268e00e",
    "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1"
}
```

## See Also
<a name="API_DeleteImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/DeleteImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/DeleteImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/DeleteImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/DeleteImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/DeleteImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/DeleteImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/DeleteImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/DeleteImage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/DeleteImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/DeleteImage)
