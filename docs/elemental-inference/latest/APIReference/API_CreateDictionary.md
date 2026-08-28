---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_CreateDictionary.html
---

# CreateDictionary
<a name="API_CreateDictionary"></a>

Creates a custom dictionary for improving transcription accuracy. A dictionary contains custom words and phrases that the ASR engine might not recognize, such as brand names, technical terms, or proper nouns. You can reference a dictionary when configuring a smart subtitles output.

## Request Syntax
<a name="API_CreateDictionary_RequestSyntax"></a>

```
POST /v1/dictionary HTTP/1.1
Content-type: application/json

{
   "entries": "{{string}}",
   "language": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDictionary_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDictionary_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [entries](#API_CreateDictionary_RequestSyntax) **   <a name="elementalinference-CreateDictionary-request-entries"></a>
The dictionary entries payload. Contains the custom words and phrases for the dictionary. Maximum size is 40,960 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40960.
Required: No

 ** [language](#API_CreateDictionary_RequestSyntax) **   <a name="elementalinference-CreateDictionary-request-language"></a>
The language of the dictionary entries. Specify the language using an ISO 639-2/T three-letter code. Supported values: eng, fra, ita, deu, spa, por.
Type: String
Valid Values: `eng | fra | ita | deu | spa | por`
Required: Yes

 ** [name](#API_CreateDictionary_RequestSyntax) **   <a name="elementalinference-CreateDictionary-request-name"></a>
A user-friendly name for this dictionary.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** [tags](#API_CreateDictionary_RequestSyntax) **   <a name="elementalinference-CreateDictionary-request-tags"></a>
Optional tags to associate with the dictionary.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDictionary_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "language": "string",
   "name": "string",
   "references": [ "string" ],
   "status": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateDictionary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateDictionary_ResponseSyntax) **   <a name="elementalinference-CreateDictionary-response-arn"></a>
The ARN of the dictionary.
Type: String

 ** [id](#API_CreateDictionary_ResponseSyntax) **   <a name="elementalinference-CreateDictionary-response-id"></a>
A unique ID that Elemental Inference assigns to the dictionary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[a-zA-Z0-9]+`

 ** [language](#API_CreateDictionary_ResponseSyntax) **   <a name="elementalinference-CreateDictionary-response-language"></a>
The language of the dictionary.
Type: String
Valid Values: `eng | fra | ita | deu | spa | por`

 ** [name](#API_CreateDictionary_ResponseSyntax) **   <a name="elementalinference-CreateDictionary-response-name"></a>
The name that you specified in the request.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`

 ** [references](#API_CreateDictionary_ResponseSyntax) **   <a name="elementalinference-CreateDictionary-response-references"></a>
A list of feed IDs that reference this dictionary.
Type: Array of strings
Pattern: `[a-z0-9]{19}`

 ** [status](#API_CreateDictionary_ResponseSyntax) **   <a name="elementalinference-CreateDictionary-response-status"></a>
The current status of the dictionary. After creation succeeds, the status will be AVAILABLE.
Type: String
Valid Values: `CREATING | AVAILABLE | REFERENCED | DELETING | DELETED`

 ** [tags](#API_CreateDictionary_ResponseSyntax) **   <a name="elementalinference-CreateDictionary-response-tags"></a>
Any tags that you included when you created the dictionary.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateDictionary_Errors"></a>

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
<a name="API_CreateDictionary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/CreateDictionary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/CreateDictionary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/CreateDictionary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/CreateDictionary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/CreateDictionary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/CreateDictionary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/CreateDictionary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/CreateDictionary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/CreateDictionary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/CreateDictionary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
