---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_DisassociateFeed.html
---

# DisassociateFeed
<a name="API_DisassociateFeed"></a>

Releases the resource (the source media) that is associated with this feed. The outputs in the feed become DISABLED.

## Request Syntax
<a name="API_DisassociateFeed_RequestSyntax"></a>

```
POST /v1/feed/{{id}}/disassociate HTTP/1.1
Content-type: application/json

{
   "associatedResourceName": "{{string}}",
   "dryRun": {{boolean}}
}
```

## URI Request Parameters
<a name="API_DisassociateFeed_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_DisassociateFeed_RequestSyntax) **   <a name="elementalinference-DisassociateFeed-request-uri-id"></a>
The ID of the feed where you want to release the resource.
Pattern: `[a-z0-9]{19}`
Required: Yes

## Request Body
<a name="API_DisassociateFeed_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associatedResourceName](#API_DisassociateFeed_RequestSyntax) **   <a name="elementalinference-DisassociateFeed-request-associatedResourceName"></a>
The name of the resource currently associated with the feed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w \-\.',@:;/]*`
Required: Yes

 ** [dryRun](#API_DisassociateFeed_RequestSyntax) **   <a name="elementalinference-DisassociateFeed-request-dryRun"></a>
Set to true if you want to do a dry run of the disassociate action.
Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions. If the dry run fails, the action returns a 4xx error code.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DisassociateFeed_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string"
}
```

## Response Elements
<a name="API_DisassociateFeed_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DisassociateFeed_ResponseSyntax) **   <a name="elementalinference-DisassociateFeed-response-arn"></a>
The ARN of the feed.
Type: String

 ** [id](#API_DisassociateFeed_ResponseSyntax) **   <a name="elementalinference-DisassociateFeed-response-id"></a>
The ID of the feed.
Type: String
Pattern: `[a-z0-9]{19}`

## Errors
<a name="API_DisassociateFeed_Errors"></a>

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

 ** TooManyRequestException **
The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateFeed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/DisassociateFeed)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/DisassociateFeed)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/DisassociateFeed)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/DisassociateFeed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/DisassociateFeed)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/DisassociateFeed)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/DisassociateFeed)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/DisassociateFeed)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/DisassociateFeed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/DisassociateFeed)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
