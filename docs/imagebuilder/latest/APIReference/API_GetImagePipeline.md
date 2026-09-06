---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImagePipeline.html
---

# GetImagePipeline
<a name="API_GetImagePipeline"></a>

Gets an image pipeline.

## Request Syntax
<a name="API_GetImagePipeline_RequestSyntax"></a>

```
GET /GetImagePipeline?imagePipelineArn={{imagePipelineArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetImagePipeline_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imagePipelineArn](#API_GetImagePipeline_RequestSyntax) **   <a name="imagebuilder-GetImagePipeline-request-uri-imagePipelineArn"></a>
The Amazon Resource Name (ARN) of the image pipeline that you want to retrieve.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-pipeline/[a-z0-9-_]+$`
Required: Yes

## Request Body
<a name="API_GetImagePipeline_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetImagePipeline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imagePipeline": {
      "arn": "string",
      "consecutiveFailures": number,
      "containerRecipeArn": "string",
      "dateCreated": "string",
      "dateLastRun": "string",
      "dateNextRun": "string",
      "dateUpdated": "string",
      "description": "string",
      "distributionConfigurationArn": "string",
      "enhancedImageMetadataEnabled": boolean,
      "executionRole": "string",
      "imageRecipeArn": "string",
      "imageScanningConfiguration": {
         "ecrConfiguration": {
            "containerTags": [ "string" ],
            "repositoryName": "string"
         },
         "imageScanningEnabled": boolean
      },
      "imageTags": {
         "string" : "string"
      },
      "imageTestsConfiguration": {
         "imageTestsEnabled": boolean,
         "timeoutMinutes": number
      },
      "infrastructureConfigurationArn": "string",
      "lastRunStatus": "string",
      "loggingConfiguration": {
         "imageLogGroupName": "string",
         "pipelineLogGroupName": "string"
      },
      "name": "string",
      "platform": "string",
      "schedule": {
         "autoDisablePolicy": {
            "failureCount": number
         },
         "pipelineExecutionStartCondition": "string",
         "scheduleExpression": "string",
         "timezone": "string"
      },
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "workflows": [
         {
            "onFailure": "string",
            "parallelGroup": "string",
            "parameters": [
               {
                  "name": "string",
                  "value": [ "string" ]
               }
            ],
            "workflowArn": "string"
         }
      ]
   },
   "requestId": "string"
}
```

## Response Elements
<a name="API_GetImagePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imagePipeline](#API_GetImagePipeline_ResponseSyntax) **   <a name="imagebuilder-GetImagePipeline-response-imagePipeline"></a>
The image pipeline object.
Type: [ImagePipeline](API_ImagePipeline.md) object

 ** [requestId](#API_GetImagePipeline_ResponseSyntax) **   <a name="imagebuilder-GetImagePipeline-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetImagePipeline_Errors"></a>

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

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_GetImagePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetImagePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetImagePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetImagePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetImagePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetImagePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetImagePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetImagePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetImagePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetImagePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetImagePipeline)
