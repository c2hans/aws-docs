---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImagePipelines.html
---

# ListImagePipelines
<a name="API_ListImagePipelines"></a>

Returns a list of image pipelines.

## Request Syntax
<a name="API_ListImagePipelines_RequestSyntax"></a>

```
POST /ListImagePipelines HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListImagePipelines_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImagePipelines_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListImagePipelines_RequestSyntax) **   <a name="imagebuilder-ListImagePipelines-request-filters"></a>
Use the following filters to streamline results:
+  `description`
+  `distributionConfigurationArn`
+  `imageRecipeArn`
+  `infrastructureConfigurationArn`
+  `name`
+  `status`
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_ListImagePipelines_RequestSyntax) **   <a name="imagebuilder-ListImagePipelines-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListImagePipelines_RequestSyntax) **   <a name="imagebuilder-ListImagePipelines-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListImagePipelines_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imagePipelineList": [
      {
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
      }
   ],
   "nextToken": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_ListImagePipelines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imagePipelineList](#API_ListImagePipelines_ResponseSyntax) **   <a name="imagebuilder-ListImagePipelines-response-imagePipelineList"></a>
The list of image pipelines.
Type: Array of [ImagePipeline](API_ImagePipeline.md) objects

 ** [nextToken](#API_ListImagePipelines_ResponseSyntax) **   <a name="imagebuilder-ListImagePipelines-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListImagePipelines_ResponseSyntax) **   <a name="imagebuilder-ListImagePipelines-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListImagePipelines_Errors"></a>

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

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

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
<a name="API_ListImagePipelines_Examples"></a>

### List image pipelines filtered by name
<a name="API_ListImagePipelines_Example_1"></a>

The following example lists the image pipelines in your account, using a filter to match a specific pipeline name.

#### Sample Request
<a name="API_ListImagePipelines_Example_1_Request"></a>

```
POST /ListImagePipelines HTTP/1.1
Content-type: application/json

{
    "filters": [
        {
            "name": "name",
            "values": [
                "my-example-pipeline"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_ListImagePipelines_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "b818f3f9-b851-4de7-95f3-8fabed4e1841",
    "imagePipelineList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline",
            "name": "my-example-pipeline",
            "description": "Builds a new version of my image every Sunday",
            "platform": "Linux",
            "enhancedImageMetadataEnabled": true,
            "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0",
            "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure",
            "imageTestsConfiguration": {
                "imageTestsEnabled": true,
                "timeoutMinutes": 720
            },
            "schedule": {
                "scheduleExpression": "cron(0 9 ? * SUN *)",
                "pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
            },
            "status": "ENABLED",
            "dateCreated": "2026-09-09T19:52:05.146Z",
            "dateUpdated": "2026-09-09T19:52:05.146Z",
            "tags": {}
        }
    ]
}
```

## See Also
<a name="API_ListImagePipelines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListImagePipelines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListImagePipelines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListImagePipelines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListImagePipelines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListImagePipelines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListImagePipelines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListImagePipelines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListImagePipelines)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListImagePipelines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListImagePipelines)
