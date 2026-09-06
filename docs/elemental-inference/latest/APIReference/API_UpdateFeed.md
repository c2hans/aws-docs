---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_UpdateFeed.html
---

# UpdateFeed
<a name="API_UpdateFeed"></a>

Updates the name and/or outputs in a feed.

UpdateFeed is a PUT operation, which means that the payload that you specify completely overwrites the existing payload.

This means that if you want to touch the array of outputs, you must pass in the full new list. So you must omit outputs you want to delete, and include outputs you want to add or modify.

If you want to patch the array of outputs to make selective additions, use AssociateFeed.

## Request Syntax
<a name="API_UpdateFeed_RequestSyntax"></a>

```
PUT /v1/feed/{{id}} HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}",
   "outputs": [
      {
         "description": "{{string}}",
         "fromAssociation": {{boolean}},
         "name": "{{string}}",
         "outputConfig": { ... },
         "status": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateFeed_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateFeed_RequestSyntax) **   <a name="elementalinference-UpdateFeed-request-uri-id"></a>
The ID of the feed to update.
Pattern: `[a-z0-9]{19}`
Required: Yes

## Request Body
<a name="API_UpdateFeed_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_UpdateFeed_RequestSyntax) **   <a name="elementalinference-UpdateFeed-request-name"></a>
Required. You can specify the existing name (to leave it unchanged) or a new name.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** [outputs](#API_UpdateFeed_RequestSyntax) **   <a name="elementalinference-UpdateFeed-request-outputs"></a>
Required. You can specify the existing array of outputs (to leave outputs unchanged) or you can specify a new array.
Type: Array of [UpdateOutput](API_UpdateOutput.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdateFeed_ResponseSyntax"></a>

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
<a name="API_UpdateFeed_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateFeed_ResponseSyntax) **   <a name="elementalinference-UpdateFeed-response-arn"></a>
The ARN of the feed.
Type: String

 ** [association](#API_UpdateFeed_ResponseSyntax) **   <a name="elementalinference-UpdateFeed-response-association"></a>
Information about the resource that is associated with the feed, if any.
Type: [FeedAssociation](API_FeedAssociation.md) object

 ** [dataEndpoints](#API_UpdateFeed_ResponseSyntax) **   <a name="elementalinference-UpdateFeed-response-dataEndpoints"></a>
The data endpoints of the feed.
Type: Array of strings

 ** [id](#API_UpdateFeed_ResponseSyntax) **   <a name="elementalinference-UpdateFeed-response-id"></a>
The ID of the feed.
Type: String
Pattern: `[a-z0-9]{19}`

 ** [name](#API_UpdateFeed_ResponseSyntax) **   <a name="elementalinference-UpdateFeed-response-name"></a>
The updated or original name of the feed.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`

 ** [outputs](#API_UpdateFeed_ResponseSyntax) **   <a name="elementalinference-UpdateFeed-response-outputs"></a>
The array of outputs in the feed. You might have left this array unchanged, or you might have changed it.
Type: Array of [GetOutput](API_GetOutput.md) objects

 ** [status](#API_UpdateFeed_ResponseSyntax) **   <a name="elementalinference-UpdateFeed-response-status"></a>
The status of the feed.
Type: String
Valid Values: `CREATING | AVAILABLE | ACTIVE | UPDATING | DELETING | DELETED | ARCHIVED`

 ** [tags](#API_UpdateFeed_ResponseSyntax) **   <a name="elementalinference-UpdateFeed-response-tags"></a>
The tags associated with the feed.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_UpdateFeed_Errors"></a>

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

 ** ResourceNotFoundException **
The resource specified in the action doesn't exist.
HTTP Status Code: 404

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
<a name="API_UpdateFeed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/UpdateFeed)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/UpdateFeed)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/UpdateFeed)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/UpdateFeed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/UpdateFeed)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/UpdateFeed)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/UpdateFeed)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/UpdateFeed)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/UpdateFeed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/UpdateFeed)
