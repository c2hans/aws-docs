---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_AssociateFeed.html
---

# AssociateFeed
<a name="API_AssociateFeed"></a>

Associates a resource with the feed. The resource provides the input that Elemental Inference needs in order to perform an Elemental Inference feature, such as cropping video. You always provide the resource by associating it with a feed. You can associate only one resource with each feed. With an association, a specific source media is claiming ownership of the feed.

AssociateFeed is a PATCH operation, which means that you can include only parameters that you want to change. Parameters that you don't include will not be affected by the operation.

Specifically:
+ You can add more outputs to the existing outputs. New outputs will be appended.
+ You can't modify an existing output (for example to change its name). Instead, use UpdateFeed.
+ You can't delete an existing output. Instead, use UpdateFeed.

Also note that you can't change the feed name with AssociateFeed. Instead, use UpdateFeed.

## Request Syntax
<a name="API_AssociateFeed_RequestSyntax"></a>

```
POST /v1/feed/{{id}}/associate HTTP/1.1
Content-type: application/json

{
   "associatedResourceName": "{{string}}",
   "dryRun": {{boolean}},
   "outputs": [
      {
         "description": "{{string}}",
         "name": "{{string}}",
         "outputConfig": { ... },
         "status": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_AssociateFeed_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_AssociateFeed_RequestSyntax) **   <a name="elementalinference-AssociateFeed-request-uri-id"></a>
The ID of the feed.
Pattern: `[a-z0-9]{19}`
Required: Yes

## Request Body
<a name="API_AssociateFeed_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associatedResourceName](#API_AssociateFeed_RequestSyntax) **   <a name="elementalinference-AssociateFeed-request-associatedResourceName"></a>
An identifier for the resource. This name must not resemble an ARN.
The resource is the source media that the feed will process. The name you assign should help you to later identify the source media that belongs to the feed. In this way, you will know which source media to push to the feed (using PutMedia).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w \-\.',@:;/]*`
Required: Yes

 ** [dryRun](#API_AssociateFeed_RequestSyntax) **   <a name="elementalinference-AssociateFeed-request-dryRun"></a>
Set to true if you want to do a dry run of the associate action.
Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions, quota limits exceeded, conflicting outputs, and so on. If the dry run fails, the action returns a 4xx error code. After you've fixed the errors, resubmit the request.
Type: Boolean
Required: No

 ** [outputs](#API_AssociateFeed_RequestSyntax) **   <a name="elementalinference-AssociateFeed-request-outputs"></a>
An array of one or more outputs that you want to add to this feed now, to supplement any outputs that you specified when you created or updated the feed.
Type: Array of [CreateOutput](API_CreateOutput.md) objects
Required: Yes

## Response Syntax
<a name="API_AssociateFeed_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string"
}
```

## Response Elements
<a name="API_AssociateFeed_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_AssociateFeed_ResponseSyntax) **   <a name="elementalinference-AssociateFeed-response-arn"></a>
The ARN of the feed.
Type: String

 ** [id](#API_AssociateFeed_ResponseSyntax) **   <a name="elementalinference-AssociateFeed-response-id"></a>
The ID of the feed.
Type: String
Pattern: `[a-z0-9]{19}`

## Errors
<a name="API_AssociateFeed_Errors"></a>

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
<a name="API_AssociateFeed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/AssociateFeed)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/AssociateFeed)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/AssociateFeed)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/AssociateFeed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/AssociateFeed)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/AssociateFeed)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/AssociateFeed)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/AssociateFeed)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/AssociateFeed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/AssociateFeed)
