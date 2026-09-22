---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImagePipeline.html
---

# GetImagePipeline
<a name="API_GetImagePipeline"></a>

Retrieves an image pipeline.

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

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_GetImagePipeline_Examples"></a>

### Get the details of an image pipeline
<a name="API_GetImagePipeline_Example_1"></a>

The following example retrieves an image pipeline that builds a new image every Sunday, including the image tests configuration and schedule start condition defaults that Image Builder applied at creation.

#### Sample Request
<a name="API_GetImagePipeline_Example_1_Request"></a>

```
GET /GetImagePipeline?imagePipelineArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Aimage-pipeline%2Fmy-example-pipeline HTTP/1.1
```

#### Sample Response
<a name="API_GetImagePipeline_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "b7e58d62-36dc-43a5-87ff-546e04cdabf1",
    "imagePipeline": {
        "arn": "arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline",
        "name": "my-example-pipeline",
        "description": "Builds an Amazon Linux 2023 image every Sunday",
        "platform": "Linux",
        "enhancedImageMetadataEnabled": true,
        "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0",
        "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure",
        "imageTestsConfiguration": {
            "imageTestsEnabled": true,
            "timeoutMinutes": 720
        },
        "schedule": {
            "scheduleExpression": "cron(0 0 ? * SUN *)",
            "pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
        },
        "status": "ENABLED",
        "dateCreated": "2026-09-09T19:38:26.574Z",
        "dateUpdated": "2026-09-09T19:38:26.574Z",
        "tags": {}
    }
}
```

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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetImagePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetImagePipeline)
