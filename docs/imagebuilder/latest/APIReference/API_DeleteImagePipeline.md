---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteImagePipeline.html
---

# DeleteImagePipeline
<a name="API_DeleteImagePipeline"></a>

Deletes an image pipeline. Images that the pipeline created aren't deleted - remove those separately with [DeleteImage](API_DeleteImage.md). You can delete a pipeline while a build that it started is still running. The build continues independently.

## Request Syntax
<a name="API_DeleteImagePipeline_RequestSyntax"></a>

```
DELETE /DeleteImagePipeline?imagePipelineArn={{imagePipelineArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteImagePipeline_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imagePipelineArn](#API_DeleteImagePipeline_RequestSyntax) **   <a name="imagebuilder-DeleteImagePipeline-request-uri-imagePipelineArn"></a>
The Amazon Resource Name (ARN) of the image pipeline to delete.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-pipeline/[a-z0-9-_]+$`
Required: Yes

## Request Body
<a name="API_DeleteImagePipeline_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteImagePipeline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imagePipelineArn": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_DeleteImagePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imagePipelineArn](#API_DeleteImagePipeline_ResponseSyntax) **   <a name="imagebuilder-DeleteImagePipeline-response-imagePipelineArn"></a>
The Amazon Resource Name (ARN) of the image pipeline that was deleted.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-pipeline/[a-z0-9-_]+$`

 ** [requestId](#API_DeleteImagePipeline_ResponseSyntax) **   <a name="imagebuilder-DeleteImagePipeline-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DeleteImagePipeline_Errors"></a>

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
<a name="API_DeleteImagePipeline_Examples"></a>

### Delete an image pipeline
<a name="API_DeleteImagePipeline_Example_1"></a>

The following example deletes an image pipeline.

#### Sample Request
<a name="API_DeleteImagePipeline_Example_1_Request"></a>

```
DELETE /DeleteImagePipeline?imagePipelineArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Aimage-pipeline%2Fmy-example-pipeline HTTP/1.1
```

#### Sample Response
<a name="API_DeleteImagePipeline_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "0536e4e9-5331-493a-921e-e8f86d367043",
    "imagePipelineArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline"
}
```

## See Also
<a name="API_DeleteImagePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/DeleteImagePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/DeleteImagePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/DeleteImagePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/DeleteImagePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/DeleteImagePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/DeleteImagePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/DeleteImagePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/DeleteImagePipeline)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/DeleteImagePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/DeleteImagePipeline)
