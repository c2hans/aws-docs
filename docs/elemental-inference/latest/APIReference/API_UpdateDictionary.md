---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_UpdateDictionary.html
---

# UpdateDictionary
<a name="API_UpdateDictionary"></a>

Updates the specified dictionary.

## Request Syntax
<a name="API_UpdateDictionary_RequestSyntax"></a>

```
PATCH /v1/dictionary/{{id}} HTTP/1.1
Content-type: application/json

{
   "entries": "{{string}}",
   "language": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDictionary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateDictionary_RequestSyntax) **   <a name="elementalinference-UpdateDictionary-request-uri-id"></a>
The ID of the dictionary to update.
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateDictionary_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [entries](#API_UpdateDictionary_RequestSyntax) **   <a name="elementalinference-UpdateDictionary-request-entries"></a>
New dictionary entries. If not specified, the entries are not changed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40960.
Required: No

 ** [language](#API_UpdateDictionary_RequestSyntax) **   <a name="elementalinference-UpdateDictionary-request-language"></a>
A new language for the dictionary. If not specified, the language is not changed.
Type: String
Valid Values: `eng | fra | ita | deu | spa | por`
Required: No

 ** [name](#API_UpdateDictionary_RequestSyntax) **   <a name="elementalinference-UpdateDictionary-request-name"></a>
A new name for the dictionary. If not specified, the name is not changed.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: No

## Response Syntax
<a name="API_UpdateDictionary_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateDictionary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateDictionary_ResponseSyntax) **   <a name="elementalinference-UpdateDictionary-response-arn"></a>
The ARN of the dictionary.
Type: String

 ** [id](#API_UpdateDictionary_ResponseSyntax) **   <a name="elementalinference-UpdateDictionary-response-id"></a>
The ID of the dictionary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[a-zA-Z0-9]+`

 ** [language](#API_UpdateDictionary_ResponseSyntax) **   <a name="elementalinference-UpdateDictionary-response-language"></a>
The updated or original language of the dictionary.
Type: String
Valid Values: `eng | fra | ita | deu | spa | por`

 ** [name](#API_UpdateDictionary_ResponseSyntax) **   <a name="elementalinference-UpdateDictionary-response-name"></a>
The updated or original name of the dictionary.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`

 ** [references](#API_UpdateDictionary_ResponseSyntax) **   <a name="elementalinference-UpdateDictionary-response-references"></a>
A list of feed IDs that reference this dictionary.
Type: Array of strings
Pattern: `[a-z0-9]{19}`

 ** [status](#API_UpdateDictionary_ResponseSyntax) **   <a name="elementalinference-UpdateDictionary-response-status"></a>
The current status of the dictionary.
Type: String
Valid Values: `CREATING | AVAILABLE | REFERENCED | DELETING | DELETED`

 ** [tags](#API_UpdateDictionary_ResponseSyntax) **   <a name="elementalinference-UpdateDictionary-response-tags"></a>
Any tags associated with the dictionary.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_UpdateDictionary_Errors"></a>

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
<a name="API_UpdateDictionary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/UpdateDictionary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/UpdateDictionary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/UpdateDictionary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/UpdateDictionary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/UpdateDictionary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/UpdateDictionary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/UpdateDictionary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/UpdateDictionary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/UpdateDictionary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/UpdateDictionary)
