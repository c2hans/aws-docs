---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_DeleteFeed.html
---

# DeleteFeed
<a name="API_DeleteFeed"></a>

Deletes the specified feed. You can delete the feed at any time. Elemental Inference doesn't block you from deleting a feed when the calling application is calling PutMedia or GetMetadata on that feed, although both these calls will start to fail. For more information about managing inactive feeds, see the Elemental Inference User Guide.

## Request Syntax
<a name="API_DeleteFeed_RequestSyntax"></a>

```
DELETE /v1/feed/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteFeed_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_DeleteFeed_RequestSyntax) **   <a name="elementalinference-DeleteFeed-request-uri-id"></a>
The ID of the feed.
Pattern: `[a-z0-9]{19}`
Required: Yes

## Request Body
<a name="API_DeleteFeed_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteFeed_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteFeed_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DeleteFeed_ResponseSyntax) **   <a name="elementalinference-DeleteFeed-response-arn"></a>
The ARN of the deleted feed.
Type: String

 ** [id](#API_DeleteFeed_ResponseSyntax) **   <a name="elementalinference-DeleteFeed-response-id"></a>
The ID of the deleted feed.
Type: String
Pattern: `[a-z0-9]{19}`

 ** [status](#API_DeleteFeed_ResponseSyntax) **   <a name="elementalinference-DeleteFeed-response-status"></a>
The current status of the feed. When deletion of the feed has succeeded, the status will be DELETED.
Type: String
Valid Values: `CREATING | AVAILABLE | ACTIVE | UPDATING | DELETING | DELETED | ARCHIVED`

## Errors
<a name="API_DeleteFeed_Errors"></a>

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
<a name="API_DeleteFeed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/DeleteFeed)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/DeleteFeed)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/DeleteFeed)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/DeleteFeed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/DeleteFeed)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/DeleteFeed)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/DeleteFeed)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/DeleteFeed)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/DeleteFeed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/DeleteFeed)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
