---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImagePipelineImages.html
---

# ListImagePipelineImages
<a name="API_ListImagePipelineImages"></a>

Returns a list of images created by the specified pipeline.

## Request Syntax
<a name="API_ListImagePipelineImages_RequestSyntax"></a>

```
POST /ListImagePipelineImages HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "imagePipelineArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListImagePipelineImages_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImagePipelineImages_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListImagePipelineImages_RequestSyntax) **   <a name="imagebuilder-ListImagePipelineImages-request-filters"></a>
Use the following filters to streamline results:
+  `name`
+  `version`
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [imagePipelineArn](#API_ListImagePipelineImages_RequestSyntax) **   <a name="imagebuilder-ListImagePipelineImages-request-imagePipelineArn"></a>
The Amazon Resource Name (ARN) of the image pipeline whose images you want to view.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-pipeline/[a-z0-9-_]+$`
Required: Yes

 ** [maxResults](#API_ListImagePipelineImages_RequestSyntax) **   <a name="imagebuilder-ListImagePipelineImages-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListImagePipelineImages_RequestSyntax) **   <a name="imagebuilder-ListImagePipelineImages-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListImagePipelineImages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imageSummaryList": [
      {
         "arn": "string",
         "buildType": "string",
         "dateCreated": "string",
         "deprecationTime": number,
         "imageSource": "string",
         "lifecycleExecutionId": "string",
         "loggingConfiguration": {
            "logGroupName": "string"
         },
         "name": "string",
         "osVersion": "string",
         "outputResources": {
            "amis": [
               {
                  "accountId": "string",
                  "description": "string",
                  "image": "string",
                  "name": "string",
                  "region": "string",
                  "state": {
                     "failureContext": {
                        "componentFailure": {
                           "action": "string",
                           "componentArn": "string",
                           "errorMessage": "string",
                           "phaseName": "string",
                           "stepName": "string"
                        },
                        "distributionFailure": {
                           "errorMessage": "string",
                           "regionFailures": [
                              {
                                 "errorMessage": "string",
                                 "imageConfigurationStep": "string",
                                 "region": "string",
                                 "status": "string",
                                 "targetAccountId": "string"
                              }
                           ]
                        },
                        "failedStep": "string",
                        "imageStatus": "string",
                        "stepExecutionId": "string",
                        "workflowArn": "string",
                        "workflowExecutionId": "string"
                     },
                     "reason": "string",
                     "status": "string"
                  }
               }
            ],
            "containers": [
               {
                  "imageUris": [ "string" ],
                  "region": "string"
               }
            ]
         },
         "owner": "string",
         "platform": "string",
         "state": {
            "failureContext": {
               "componentFailure": {
                  "action": "string",
                  "componentArn": "string",
                  "errorMessage": "string",
                  "phaseName": "string",
                  "stepName": "string"
               },
               "distributionFailure": {
                  "errorMessage": "string",
                  "regionFailures": [
                     {
                        "errorMessage": "string",
                        "imageConfigurationStep": "string",
                        "region": "string",
                        "status": "string",
                        "targetAccountId": "string"
                     }
                  ]
               },
               "failedStep": "string",
               "imageStatus": "string",
               "stepExecutionId": "string",
               "workflowArn": "string",
               "workflowExecutionId": "string"
            },
            "reason": "string",
            "status": "string"
         },
         "tags": {
            "string" : "string"
         },
         "type": "string",
         "version": "string"
      }
   ],
   "nextToken": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_ListImagePipelineImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageSummaryList](#API_ListImagePipelineImages_ResponseSyntax) **   <a name="imagebuilder-ListImagePipelineImages-response-imageSummaryList"></a>
The list of images built by this pipeline.
Type: Array of [ImageSummary](API_ImageSummary.md) objects

 ** [nextToken](#API_ListImagePipelineImages_ResponseSyntax) **   <a name="imagebuilder-ListImagePipelineImages-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListImagePipelineImages_ResponseSyntax) **   <a name="imagebuilder-ListImagePipelineImages-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListImagePipelineImages_Errors"></a>

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
<a name="API_ListImagePipelineImages_Examples"></a>

### List the images that an image pipeline created
<a name="API_ListImagePipelineImages_Example_1"></a>

The following example lists the images that the specified pipeline created, including a build that is still in progress.

#### Sample Request
<a name="API_ListImagePipelineImages_Example_1_Request"></a>

```
POST /ListImagePipelineImages HTTP/1.1
Content-type: application/json

{
    "imagePipelineArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline"
}
```

#### Sample Response
<a name="API_ListImagePipelineImages_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "071a0ecb-b07d-4485-832c-e6b88de8ebed",
    "imageSummaryList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1",
            "name": "my-example-recipe",
            "type": "AMI",
            "version": "1.0.0/1",
            "platform": "Linux",
            "state": {
                "status": "BUILDING"
            },
            "owner": "111122223333",
            "dateCreated": "2026-09-09T19:39:20.458Z",
            "outputResources": {
                "amis": []
            },
            "tags": {},
            "buildType": "USER_INITIATED"
        }
    ]
}
```

## See Also
<a name="API_ListImagePipelineImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListImagePipelineImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListImagePipelineImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListImagePipelineImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListImagePipelineImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListImagePipelineImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListImagePipelineImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListImagePipelineImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListImagePipelineImages)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListImagePipelineImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListImagePipelineImages)
