---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchVocabularies.html
---

# SearchVocabularies
<a name="API_SearchVocabularies"></a>

Searches for vocabularies within a specific Connect Customer instance using `State`, `NameStartsWith`, and `LanguageCode`.

## Request Syntax
<a name="API_SearchVocabularies_RequestSyntax"></a>

```
POST /vocabulary-summary/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "LanguageCode": "{{string}}",
   "MaxResults": {{number}},
   "NameStartsWith": "{{string}}",
   "NextToken": "{{string}}",
   "State": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchVocabularies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_SearchVocabularies_RequestSyntax) **   <a name="connect-SearchVocabularies-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_SearchVocabularies_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LanguageCode](#API_SearchVocabularies_RequestSyntax) **   <a name="connect-SearchVocabularies-request-LanguageCode"></a>
The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see [What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html)
Type: String
Valid Values: `ar-AE | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fr-CA | fr-FR | hi-IN | it-IT | ja-JP | ko-KR | pt-BR | pt-PT | zh-CN | en-NZ | en-ZA | ca-ES | da-DK | fi-FI | id-ID | ms-MY | nl-NL | no-NO | pl-PL | sv-SE | tl-PH`
Required: No

 ** [MaxResults](#API_SearchVocabularies_RequestSyntax) **   <a name="connect-SearchVocabularies-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameStartsWith](#API_SearchVocabularies_RequestSyntax) **   <a name="connect-SearchVocabularies-request-NameStartsWith"></a>
The starting pattern of the name of the vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

 ** [NextToken](#API_SearchVocabularies_RequestSyntax) **   <a name="connect-SearchVocabularies-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131070.
Pattern: `.*\S.*`
Required: No

 ** [State](#API_SearchVocabularies_RequestSyntax) **   <a name="connect-SearchVocabularies-request-State"></a>
The current state of the custom vocabulary.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | CREATION_FAILED | DELETE_IN_PROGRESS`
Required: No

## Response Syntax
<a name="API_SearchVocabularies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "VocabularySummaryList": [
      {
         "Arn": "string",
         "FailureReason": "string",
         "Id": "string",
         "LanguageCode": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "State": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchVocabularies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SearchVocabularies_ResponseSyntax) **   <a name="connect-SearchVocabularies-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131070.
Pattern: `.*\S.*`

 ** [VocabularySummaryList](#API_SearchVocabularies_ResponseSyntax) **   <a name="connect-SearchVocabularies-response-VocabularySummaryList"></a>
The list of the available custom vocabularies.
Type: Array of [VocabularySummary](API_VocabularySummary.md) objects

## Errors
<a name="API_SearchVocabularies_Errors"></a>

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_SearchVocabularies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchVocabularies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchVocabularies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchVocabularies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchVocabularies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchVocabularies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchVocabularies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchVocabularies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchVocabularies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchVocabularies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchVocabularies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
