---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateDefaultVocabulary.html
---

# AssociateDefaultVocabulary
<a name="API_AssociateDefaultVocabulary"></a>

Associates an existing vocabulary as the default. Contact Lens for Connect Customer uses the vocabulary in post-call and real-time analysis sessions for the given language.

## Request Syntax
<a name="API_AssociateDefaultVocabulary_RequestSyntax"></a>

```
PUT /default-vocabulary/{{InstanceId}}/{{LanguageCode}} HTTP/1.1
Content-type: application/json

{
   "VocabularyId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateDefaultVocabulary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_AssociateDefaultVocabulary_RequestSyntax) **   <a name="connect-AssociateDefaultVocabulary-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [LanguageCode](#API_AssociateDefaultVocabulary_RequestSyntax) **   <a name="connect-AssociateDefaultVocabulary-request-uri-LanguageCode"></a>
The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see [What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html)
Valid Values: `ar-AE | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fr-CA | fr-FR | hi-IN | it-IT | ja-JP | ko-KR | pt-BR | pt-PT | zh-CN | en-NZ | en-ZA | ca-ES | da-DK | fi-FI | id-ID | ms-MY | nl-NL | no-NO | pl-PL | sv-SE | tl-PH`
Required: Yes

## Request Body
<a name="API_AssociateDefaultVocabulary_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [VocabularyId](#API_AssociateDefaultVocabulary_RequestSyntax) **   <a name="connect-AssociateDefaultVocabulary-request-VocabularyId"></a>
The identifier of the custom vocabulary. If this is empty, the default is set to none.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## Response Syntax
<a name="API_AssociateDefaultVocabulary_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateDefaultVocabulary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateDefaultVocabulary_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_AssociateDefaultVocabulary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/AssociateDefaultVocabulary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/AssociateDefaultVocabulary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociateDefaultVocabulary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/AssociateDefaultVocabulary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociateDefaultVocabulary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/AssociateDefaultVocabulary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/AssociateDefaultVocabulary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/AssociateDefaultVocabulary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/AssociateDefaultVocabulary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociateDefaultVocabulary)
