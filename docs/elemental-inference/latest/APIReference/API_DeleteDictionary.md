---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_DeleteDictionary.html
---

# DeleteDictionary
<a name="API_DeleteDictionary"></a>

Deletes the specified dictionary. You cannot delete a dictionary that is referenced by a feed. You must first remove the dictionary reference from the feed's subtitling configuration.

## Request Syntax
<a name="API_DeleteDictionary_RequestSyntax"></a>

```
DELETE /v1/dictionary/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDictionary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_DeleteDictionary_RequestSyntax) **   <a name="elementalinference-DeleteDictionary-request-uri-id"></a>
The ID of the dictionary to delete.
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_DeleteDictionary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDictionary_ResponseSyntax"></a>

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
<a name="API_DeleteDictionary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DeleteDictionary_ResponseSyntax) **   <a name="elementalinference-DeleteDictionary-response-arn"></a>
The ARN of the deleted dictionary.
Type: String

 ** [id](#API_DeleteDictionary_ResponseSyntax) **   <a name="elementalinference-DeleteDictionary-response-id"></a>
The ID of the deleted dictionary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[a-zA-Z0-9]+`

 ** [status](#API_DeleteDictionary_ResponseSyntax) **   <a name="elementalinference-DeleteDictionary-response-status"></a>
The status of the dictionary after deletion.
Type: String
Valid Values: `CREATING | AVAILABLE | REFERENCED | DELETING | DELETED`

## Errors
<a name="API_DeleteDictionary_Errors"></a>

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
<a name="API_DeleteDictionary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/DeleteDictionary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/DeleteDictionary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/DeleteDictionary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/DeleteDictionary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/DeleteDictionary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/DeleteDictionary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/DeleteDictionary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/DeleteDictionary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/DeleteDictionary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/DeleteDictionary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
