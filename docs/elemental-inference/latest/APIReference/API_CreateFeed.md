---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_CreateFeed.html
---

# CreateFeed
<a name="API_CreateFeed"></a>

Creates a feed. The feed is the target for the live media stream that is being sent by the calling application. An example of a calling application is AWS Elemental MediaLive.

The key contents of the feed is an array of outputs. Each output represents an Elemental Inference feature. After you create the feed, you must associate a resource with the feed. At that point, you will have a useable feed: resource - feed - output or outputs.

## Request Syntax
<a name="API_CreateFeed_RequestSyntax"></a>

```
POST /v1/feed HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}",
   "outputs": [
      {
         "description": "{{string}}",
         "name": "{{string}}",
         "outputConfig": { ... },
         "status": "{{string}}"
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateFeed_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateFeed_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_CreateFeed_RequestSyntax) **   <a name="elementalinference-CreateFeed-request-name"></a>
A user-friendly name for this feed.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** [outputs](#API_CreateFeed_RequestSyntax) **   <a name="elementalinference-CreateFeed-request-outputs"></a>
An array of outputs for this feed. Each output represents a specific Elemental Inference feature. For example, there is one output type for the smart crop feature. You must specify at least one output, but you can later add outputs using AssociateFeed, or add, modify, and delete outputs using UpdateFeed.
Type: Array of [CreateOutput](API_CreateOutput.md) objects
Required: Yes

 ** [tags](#API_CreateFeed_RequestSyntax) **   <a name="elementalinference-CreateFeed-request-tags"></a>
Optional tags. You can also add tags later, using TagResource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateFeed_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_CreateFeed_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateFeed_ResponseSyntax) **   <a name="elementalinference-CreateFeed-response-arn"></a>
A unique ARN that Elemental Inference assigns to the feed.
Type: String

 ** [association](#API_CreateFeed_ResponseSyntax) **   <a name="elementalinference-CreateFeed-response-association"></a>
The association for this feed. When you create the feed, this property is empty. You must associate a resource with the feed using AssociateFeed or UpdateFeed.
Type: [FeedAssociation](API_FeedAssociation.md) object

 ** [dataEndpoints](#API_CreateFeed_ResponseSyntax) **   <a name="elementalinference-CreateFeed-response-dataEndpoints"></a>
An array of endpoints for the feed. Typically, there is only one endpoint. The feed receives source media at this endpoint (when the calling application calls PutMedia) and returns the resulting metadata to this endpoint (when the calling application calls GetMetadata).
Type: Array of strings

 ** [id](#API_CreateFeed_ResponseSyntax) **   <a name="elementalinference-CreateFeed-response-id"></a>
A unique ID that Elemental Inference assigns to the feed.
Type: String
Pattern: `[a-z0-9]{19}`

 ** [name](#API_CreateFeed_ResponseSyntax) **   <a name="elementalinference-CreateFeed-response-name"></a>
The name that you specified in the request.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`

 ** [outputs](#API_CreateFeed_ResponseSyntax) **   <a name="elementalinference-CreateFeed-response-outputs"></a>
Repeats the outputs that you specified in the request.
Type: Array of [GetOutput](API_GetOutput.md) objects

 ** [status](#API_CreateFeed_ResponseSyntax) **   <a name="elementalinference-CreateFeed-response-status"></a>
The current status of the feed. After creation of the feed has succeeded, the status will be AVAILABLE.
Type: String
Valid Values: `CREATING | AVAILABLE | ACTIVE | UPDATING | DELETING | DELETED | ARCHIVED`

 ** [tags](#API_CreateFeed_ResponseSyntax) **   <a name="elementalinference-CreateFeed-response-tags"></a>
Any tags that you included when you created the feed.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateFeed_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict.
HTTP Status Code: 409

 ** InternalServerErrorException **
An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase.
HTTP Status Code: 402

 ** TooManyRequestException **
The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying.
HTTP Status Code: 400

## See Also
<a name="API_CreateFeed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/CreateFeed)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/CreateFeed)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/CreateFeed)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/CreateFeed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/CreateFeed)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/CreateFeed)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/CreateFeed)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/CreateFeed)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/CreateFeed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/CreateFeed)
