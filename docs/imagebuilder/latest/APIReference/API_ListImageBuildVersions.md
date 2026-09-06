---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImageBuildVersions.html
---

# ListImageBuildVersions
<a name="API_ListImageBuildVersions"></a>

Returns a list of image build versions.

## Request Syntax
<a name="API_ListImageBuildVersions_RequestSyntax"></a>

```
POST /ListImageBuildVersions HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "imageVersionArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListImageBuildVersions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImageBuildVersions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListImageBuildVersions_RequestSyntax) **   <a name="imagebuilder-ListImageBuildVersions-request-filters"></a>
Use the following filters to streamline results:
+  `name`
+  `osVersion`
+  `platform`
+  `type`
+  `version`
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [imageVersionArn](#API_ListImageBuildVersions_RequestSyntax) **   <a name="imagebuilder-ListImageBuildVersions-request-imageVersionArn"></a>
The Amazon Resource Name (ARN) of the image whose build versions you want to retrieve.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

 ** [maxResults](#API_ListImageBuildVersions_RequestSyntax) **   <a name="imagebuilder-ListImageBuildVersions-request-maxResults"></a>
Specify the maximum number of items to return in a request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListImageBuildVersions_RequestSyntax) **   <a name="imagebuilder-ListImageBuildVersions-request-nextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListImageBuildVersions_ResponseSyntax"></a>

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
<a name="API_ListImageBuildVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageSummaryList](#API_ListImageBuildVersions_ResponseSyntax) **   <a name="imagebuilder-ListImageBuildVersions-response-imageSummaryList"></a>
The list of image build versions.
Type: Array of [ImageSummary](API_ImageSummary.md) objects

 ** [nextToken](#API_ListImageBuildVersions_ResponseSyntax) **   <a name="imagebuilder-ListImageBuildVersions-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListImageBuildVersions_ResponseSyntax) **   <a name="imagebuilder-ListImageBuildVersions-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListImageBuildVersions_Errors"></a>

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

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_ListImageBuildVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListImageBuildVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListImageBuildVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListImageBuildVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListImageBuildVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListImageBuildVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListImageBuildVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListImageBuildVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListImageBuildVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListImageBuildVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListImageBuildVersions)
