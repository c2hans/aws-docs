---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteKeyword.html
---

# DeleteKeyword
<a name="API_DeleteKeyword"></a>

Deletes an existing keyword from an origination phone number or pool.

A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, AWS End User Messaging SMS responds with a customizable message.

Keywords "HELP" and "STOP" can't be deleted or modified.

## Request Syntax
<a name="API_DeleteKeyword_RequestSyntax"></a>

```
{
   "Keyword": "{{string}}",
   "OriginationIdentity": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteKeyword_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Keyword](#API_DeleteKeyword_RequestSyntax) **   <a name="pinpoint-DeleteKeyword-request-Keyword"></a>
The keyword to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[ \S]+`
Required: Yes

 ** [OriginationIdentity](#API_DeleteKeyword_RequestSyntax) **   <a name="pinpoint-DeleteKeyword-request-OriginationIdentity"></a>
The origination identity to use such as a PhoneNumberId, PhoneNumberArn, PoolId or PoolArn. You can use [DescribePhoneNumbers](API_DescribePhoneNumbers.md) to find the values for PhoneNumberId and PhoneNumberArn and [DescribePools](API_DescribePools.md) to find the values of PoolId and PoolArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteKeyword_ResponseSyntax"></a>

```
{
   "Keyword": "string",
   "KeywordAction": "string",
   "KeywordMessage": "string",
   "OriginationIdentity": "string",
   "OriginationIdentityArn": "string"
}
```

## Response Elements
<a name="API_DeleteKeyword_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Keyword](#API_DeleteKeyword_ResponseSyntax) **   <a name="pinpoint-DeleteKeyword-response-Keyword"></a>
The keyword that was deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[ \S]+`

 ** [KeywordAction](#API_DeleteKeyword_ResponseSyntax) **   <a name="pinpoint-DeleteKeyword-response-KeywordAction"></a>
The action that was associated with the deleted keyword.
Type: String
Valid Values: `AUTOMATIC_RESPONSE | OPT_OUT | OPT_IN`

 ** [KeywordMessage](#API_DeleteKeyword_ResponseSyntax) **   <a name="pinpoint-DeleteKeyword-response-KeywordMessage"></a>
The message that was associated with the deleted keyword.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(?!\s*$)[\s\S]+`

 ** [OriginationIdentity](#API_DeleteKeyword_ResponseSyntax) **   <a name="pinpoint-DeleteKeyword-response-OriginationIdentity"></a>
The PhoneNumberId or PoolId that the keyword was associated with.
Type: String

 ** [OriginationIdentityArn](#API_DeleteKeyword_ResponseSyntax) **   <a name="pinpoint-DeleteKeyword-response-OriginationIdentityArn"></a>
The PhoneNumberArn or PoolArn that the keyword was associated with.
Type: String

## Errors
<a name="API_DeleteKeyword_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.
 ** Reason **
The reason for the exception.
 ** ResourceId **
The unique identifier of the request.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteKeyword_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteKeyword)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteKeyword)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteKeyword)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteKeyword)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteKeyword)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteKeyword)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteKeyword)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteKeyword)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteKeyword)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteKeyword)
