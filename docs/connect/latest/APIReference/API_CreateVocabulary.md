---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateVocabulary.html
---

# CreateVocabulary
<a name="API_CreateVocabulary"></a>

Creates a custom vocabulary associated with your Connect Customer instance. You can set a custom vocabulary to be your default vocabulary for a given language. Contact Lens for Connect Customer uses the default vocabulary in post-call and real-time contact analysis sessions for that language.

## Request Syntax
<a name="API_CreateVocabulary_RequestSyntax"></a>

```
POST /vocabulary/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Content": "{{string}}",
   "LanguageCode": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "VocabularyName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateVocabulary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateVocabulary_RequestSyntax) **   <a name="connect-CreateVocabulary-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateVocabulary_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateVocabulary_RequestSyntax) **   <a name="connect-CreateVocabulary-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/). If a create request is received more than once with same client token, subsequent requests return the previous response without creating a vocabulary again.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Content](#API_CreateVocabulary_RequestSyntax) **   <a name="connect-CreateVocabulary-request-Content"></a>
The content of the custom vocabulary in plain-text format with a table of values. Each row in the table represents a word or a phrase, described with `Phrase`, `IPA`, `SoundsLike`, and `DisplayAs` fields. Separate the fields with TAB characters. The size limit is 50KB. For more information, see [Create a custom vocabulary using a table](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html#create-vocabulary-table).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60000.
Required: Yes

 ** [LanguageCode](#API_CreateVocabulary_RequestSyntax) **   <a name="connect-CreateVocabulary-request-LanguageCode"></a>
The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see [What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html)
Type: String
Valid Values: `ar-AE | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fr-CA | fr-FR | hi-IN | it-IT | ja-JP | ko-KR | pt-BR | pt-PT | zh-CN | en-NZ | en-ZA | ca-ES | da-DK | fi-FI | id-ID | ms-MY | nl-NL | no-NO | pl-PL | sv-SE | tl-PH`
Required: Yes

 ** [Tags](#API_CreateVocabulary_RequestSyntax) **   <a name="connect-CreateVocabulary-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [VocabularyName](#API_CreateVocabulary_RequestSyntax) **   <a name="connect-CreateVocabulary-request-VocabularyName"></a>
A unique name of the custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

## Response Syntax
<a name="API_CreateVocabulary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "State": "string",
   "VocabularyArn": "string",
   "VocabularyId": "string"
}
```

## Response Elements
<a name="API_CreateVocabulary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [State](#API_CreateVocabulary_ResponseSyntax) **   <a name="connect-CreateVocabulary-response-State"></a>
The current state of the custom vocabulary.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | CREATION_FAILED | DELETE_IN_PROGRESS`

 ** [VocabularyArn](#API_CreateVocabulary_ResponseSyntax) **   <a name="connect-CreateVocabulary-response-VocabularyArn"></a>
The Amazon Resource Name (ARN) of the custom vocabulary.
Type: String

 ** [VocabularyId](#API_CreateVocabulary_ResponseSyntax) **   <a name="connect-CreateVocabulary-response-VocabularyId"></a>
The identifier of the custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_CreateVocabulary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateVocabulary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateVocabulary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateVocabulary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateVocabulary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateVocabulary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateVocabulary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateVocabulary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateVocabulary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateVocabulary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateVocabulary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateVocabulary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
