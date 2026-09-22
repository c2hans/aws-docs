---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImageRecipes.html
---

# ListImageRecipes
<a name="API_ListImageRecipes"></a>

Returns a list of image recipes.

## Request Syntax
<a name="API_ListImageRecipes_RequestSyntax"></a>

```
POST /ListImageRecipes HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "owner": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListImageRecipes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImageRecipes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListImageRecipes_RequestSyntax) **   <a name="imagebuilder-ListImageRecipes-request-filters"></a>
Use the following filters to streamline results:
+  `name`
+  `parentImage`
+  `platform`
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_ListImageRecipes_RequestSyntax) **   <a name="imagebuilder-ListImageRecipes-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListImageRecipes_RequestSyntax) **   <a name="imagebuilder-ListImageRecipes-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** [owner](#API_ListImageRecipes_RequestSyntax) **   <a name="imagebuilder-ListImageRecipes-request-owner"></a>
You can specify the recipe owner to filter results by that owner. By default, this request will only show image recipes owned by your account. To filter by a different owner, specify one of the `Valid Values` that are listed for this parameter.
Type: String
Valid Values: `Self | Shared | Amazon | ThirdParty | AWSMarketplace`
Required: No

## Response Syntax
<a name="API_ListImageRecipes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imageRecipeSummaryList": [
      {
         "arn": "string",
         "dateCreated": "string",
         "name": "string",
         "owner": "string",
         "parentImage": "string",
         "platform": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_ListImageRecipes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageRecipeSummaryList](#API_ListImageRecipes_ResponseSyntax) **   <a name="imagebuilder-ListImageRecipes-response-imageRecipeSummaryList"></a>
A list of `ImageRecipeSummary` objects that contain identifying characteristics for the image recipe, such as the name, the Amazon Resource Name (ARN), and the date created, along with other key details.
Type: Array of [ImageRecipeSummary](API_ImageRecipeSummary.md) objects

 ** [nextToken](#API_ListImageRecipes_ResponseSyntax) **   <a name="imagebuilder-ListImageRecipes-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListImageRecipes_ResponseSyntax) **   <a name="imagebuilder-ListImageRecipes-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListImageRecipes_Errors"></a>

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
<a name="API_ListImageRecipes_Examples"></a>

### List the image recipes that you own
<a name="API_ListImageRecipes_Example_1"></a>

The following example lists the image recipes that you own.

#### Sample Request
<a name="API_ListImageRecipes_Example_1_Request"></a>

```
POST /ListImageRecipes HTTP/1.1
Content-type: application/json

{
    "owner": "Self"
}
```

#### Sample Response
<a name="API_ListImageRecipes_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "4b036f1a-3716-441d-a401-419249f6569e",
    "imageRecipeSummaryList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-linux-recipe/1.0.0",
            "name": "my-example-linux-recipe",
            "platform": "Linux",
            "owner": "111122223333",
            "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/amazon-linux-2023-x86/x.x.x",
            "dateCreated": "2026-09-09T19:30:33.064Z",
            "tags": {}
        },
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-windows-recipe/1.0.0",
            "name": "my-example-windows-recipe",
            "platform": "Windows",
            "owner": "111122223333",
            "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/windows-server-2022-english-full-base-x86/x.x.x",
            "dateCreated": "2026-09-09T19:30:35.110Z",
            "tags": {}
        }
    ]
}
```

## See Also
<a name="API_ListImageRecipes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListImageRecipes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListImageRecipes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListImageRecipes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListImageRecipes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListImageRecipes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListImageRecipes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListImageRecipes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListImageRecipes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListImageRecipes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListImageRecipes)
