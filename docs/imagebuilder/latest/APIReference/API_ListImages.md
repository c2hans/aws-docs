---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImages.html
---

# ListImages
<a name="API_ListImages"></a>

Returns the list of images that you have access to.

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
Specifies whether to return one entry per image name, with all versions of each image aggregated. Defaults to `false`, which returns one entry per image version. You can't combine this option with the `version` filter.
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
Specifies whether to include deprecated Amazon-managed images in the results. Deprecated images that you own are always returned. Defaults to `false`.
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
<a name="API_ListImages_Examples"></a>

### List images that you own
<a name="API_ListImages_Example_1"></a>

The following example lists the image versions that you own. Setting `byName` to `false` returns each image version as its own entry, instead of grouping build versions under their image name.

#### Sample Request
<a name="API_ListImages_Example_1_Request"></a>

```
POST /ListImages HTTP/1.1
Content-type: application/json

{
    "owner": "Self",
    "byName": false
}
```

#### Sample Response
<a name="API_ListImages_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "19794296-a45f-4079-8741-e00d3c916318",
    "imageVersionList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0",
            "name": "my-example-recipe",
            "type": "AMI",
            "version": "1.0.0",
            "platform": "Linux",
            "osVersion": "Amazon Linux 2023",
            "owner": "111122223333",
            "dateCreated": "2026-09-09T19:12:18.677Z",
            "buildType": "USER_INITIATED"
        },
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-windows-image/1.0.0",
            "name": "my-example-windows-image",
            "type": "AMI",
            "version": "1.0.0",
            "platform": "Windows",
            "osVersion": "Microsoft Windows Server 2025",
            "owner": "111122223333",
            "dateCreated": "2026-03-10T19:57:27.323Z",
            "buildType": "USER_INITIATED"
        },
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-windows-image/1.0.1",
            "name": "my-example-windows-image",
            "type": "AMI",
            "version": "1.0.1",
            "platform": "Windows",
            "osVersion": "Microsoft Windows Server 2025",
            "owner": "111122223333",
            "dateCreated": "2026-03-10T20:32:31.795Z",
            "buildType": "USER_INITIATED"
        }
    ]
}
```

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
