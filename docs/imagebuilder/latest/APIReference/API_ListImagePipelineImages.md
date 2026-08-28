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
Specify the maximum number of items to return in a request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListImagePipelineImages_RequestSyntax) **   <a name="imagebuilder-ListImagePipelineImages-request-nextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
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
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
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
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListImagePipelineImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListImagePipelineImages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
