---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_GetFeed.html
---

# GetFeed
<a name="API_GetFeed"></a>

Retrieves information about the specified feed.

## Request Syntax
<a name="API_GetFeed_RequestSyntax"></a>

```
GET /v1/feed/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFeed_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetFeed_RequestSyntax) **   <a name="elementalinference-GetFeed-request-uri-id"></a>
The ID of the feed to query.
Pattern: `[a-z0-9]{19}`
Required: Yes

## Request Body
<a name="API_GetFeed_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFeed_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "association": {
      "associatedResourceName": "string"
   },
   "dataEndpoints": [ "string" ],
   "id": "string",
   "name": "string",
   "outputs": [
      {
         "description": "string",
         "fromAssociation": boolean,
         "name": "string",
         "outputConfig": { ... },
         "status": "string"
      }
   ],
   "status": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetFeed_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetFeed_ResponseSyntax) **   <a name="elementalinference-GetFeed-response-arn"></a>
The ARN of the feed.
Type: String

 ** [association](#API_GetFeed_ResponseSyntax) **   <a name="elementalinference-GetFeed-response-association"></a>
Information about the resource that is associated with the feed. It's possible that there is no associated resource. This is not an error.
Type: [FeedAssociation](API_FeedAssociation.md) object

 ** [dataEndpoints](#API_GetFeed_ResponseSyntax) **   <a name="elementalinference-GetFeed-response-dataEndpoints"></a>
The dataEndpoints of the feed.
Type: Array of strings

 ** [id](#API_GetFeed_ResponseSyntax) **   <a name="elementalinference-GetFeed-response-id"></a>
The ID of the feed.
Type: String
Pattern: `[a-z0-9]{19}`

 ** [name](#API_GetFeed_ResponseSyntax) **   <a name="elementalinference-GetFeed-response-name"></a>
The name of the feed.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`

 ** [outputs](#API_GetFeed_ResponseSyntax) **   <a name="elementalinference-GetFeed-response-outputs"></a>
An array of the outputs in the feed.
Type: Array of [GetOutput](API_GetOutput.md) objects

 ** [status](#API_GetFeed_ResponseSyntax) **   <a name="elementalinference-GetFeed-response-status"></a>
The status of the feed.
Type: String
Valid Values: `CREATING | AVAILABLE | ACTIVE | UPDATING | DELETING | DELETED | ARCHIVED`

 ** [tags](#API_GetFeed_ResponseSyntax) **   <a name="elementalinference-GetFeed-response-tags"></a>
A list of the tags, if any, for the feed.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetFeed_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource specified in the action doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestException **
The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying.
HTTP Status Code: 429

## See Also
<a name="API_GetFeed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/GetFeed)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/GetFeed)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/GetFeed)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/GetFeed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/GetFeed)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/GetFeed)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/GetFeed)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/GetFeed)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/GetFeed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/GetFeed)
