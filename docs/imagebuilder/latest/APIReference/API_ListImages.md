---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImages.html
---

# ListImages
<a name="API_ListImages"></a>

Returns the list of images that you have access to. Newly created images can take up to two minutes to appear in the ListImages API Results.

## Request Syntax
<a name="API_ListImages_RequestSyntax"></a>

```
POST /ListImages HTTP/1.1
Content-type: application/json

{
   "byName": {{boolean}},
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "includeDeprecated": {{boolean}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "owner": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListImages_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImages_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [byName](#API_ListImages_RequestSyntax) **   <a name="imagebuilder-ListImages-request-byName"></a>
Requests a list of images with a specific recipe name.
Type: Boolean
Required: No

 ** [filters](#API_ListImages_RequestSyntax) **   <a name="imagebuilder-ListImages-request-filters"></a>
Use the following filters to streamline results:
+  `name`
+  `osVersion`
+  `platform`
+  `type`
+  `version`
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [includeDeprecated](#API_ListImages_RequestSyntax) **   <a name="imagebuilder-ListImages-request-includeDeprecated"></a>
Includes deprecated images in the response list.
Type: Boolean
Required: No

 ** [maxResults](#API_ListImages_RequestSyntax) **   <a name="imagebuilder-ListImages-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListImages_RequestSyntax) **   <a name="imagebuilder-ListImages-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** [owner](#API_ListImages_RequestSyntax) **   <a name="imagebuilder-ListImages-request-owner"></a>
Filters the list to images owned by you, by Amazon, or shared with you by other accounts. By default, only your account's images are returned.
Type: String
Valid Values: `Self | Shared | Amazon | ThirdParty | AWSMarketplace`
Required: No

## Response Syntax
<a name="API_ListImages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imageVersionList": [
      {
         "arn": "string",
         "buildType": "string",
         "dateCreated": "string",
         "imageSource": "string",
         "name": "string",
         "osVersion": "string",
         "owner": "string",
         "platform": "string",
         "type": "string",
         "version": "string"
      }
   ],
   "nextToken": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_ListImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageVersionList](#API_ListImages_ResponseSyntax) **   <a name="imagebuilder-ListImages-response-imageVersionList"></a>
The list of image semantic versions.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Filtering:** You can use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.
Type: Array of [ImageVersion](API_ImageVersion.md) objects

 ** [nextToken](#API_ListImages_ResponseSyntax) **   <a name="imagebuilder-ListImages-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListImages_ResponseSyntax) **   <a name="imagebuilder-ListImages-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListImages_Errors"></a>

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
<a name="API_ListImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListImages)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListImages)
