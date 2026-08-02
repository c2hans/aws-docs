---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutKeyword.html
---

# PutKeyword
<a name="API_PutKeyword"></a>

Creates or updates a keyword configuration on an origination phone number or pool.

 A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, AWS End User Messaging SMS responds with a customizable message.

If you specify a keyword that isn't valid, an error is returned.

## Request Syntax
<a name="API_PutKeyword_RequestSyntax"></a>

```
{
   "Keyword": "{{string}}",
   "KeywordAction": "{{string}}",
   "KeywordMessage": "{{string}}",
   "OriginationIdentity": "{{string}}"
}
```

## Request Parameters
<a name="API_PutKeyword_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Keyword](#API_PutKeyword_RequestSyntax) **   <a name="pinpoint-PutKeyword-request-Keyword"></a>
The new keyword to add.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[ \S]+`
Required: Yes

 ** [KeywordAction](#API_PutKeyword_RequestSyntax) **   <a name="pinpoint-PutKeyword-request-KeywordAction"></a>
The action to perform for the new keyword when it is received.
+ AUTOMATIC\_RESPONSE: A message is sent to the recipient.
+ OPT\_OUT: Keeps the recipient from receiving future messages.
+ OPT\_IN: The recipient wants to receive future messages.
Type: String
Valid Values: `AUTOMATIC_RESPONSE | OPT_OUT | OPT_IN`
Required: No

 ** [KeywordMessage](#API_PutKeyword_RequestSyntax) **   <a name="pinpoint-PutKeyword-request-KeywordMessage"></a>
The message associated with the keyword.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(?!\s*$)[\s\S]+`
Required: Yes

 ** [OriginationIdentity](#API_PutKeyword_RequestSyntax) **   <a name="pinpoint-PutKeyword-request-OriginationIdentity"></a>
The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use [DescribePhoneNumbers](API_DescribePhoneNumbers.md) get the values for PhoneNumberId and PhoneNumberArn while [DescribeSenderIds](API_DescribeSenderIds.md) can be used to get the values for SenderId and SenderIdArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_PutKeyword_ResponseSyntax"></a>

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
<a name="API_PutKeyword_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Keyword](#API_PutKeyword_ResponseSyntax) **   <a name="pinpoint-PutKeyword-response-Keyword"></a>
The keyword that was added.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[ \S]+`

 ** [KeywordAction](#API_PutKeyword_ResponseSyntax) **   <a name="pinpoint-PutKeyword-response-KeywordAction"></a>
The action to perform when the keyword is used.
Type: String
Valid Values: `AUTOMATIC_RESPONSE | OPT_OUT | OPT_IN`

 ** [KeywordMessage](#API_PutKeyword_ResponseSyntax) **   <a name="pinpoint-PutKeyword-response-KeywordMessage"></a>
The message associated with the keyword.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(?!\s*$)[\s\S]+`

 ** [OriginationIdentity](#API_PutKeyword_ResponseSyntax) **   <a name="pinpoint-PutKeyword-response-OriginationIdentity"></a>
The PhoneNumberId or PoolId that the keyword was associated with.
Type: String

 ** [OriginationIdentityArn](#API_PutKeyword_ResponseSyntax) **   <a name="pinpoint-PutKeyword-response-OriginationIdentityArn"></a>
The PhoneNumberArn or PoolArn that the keyword was associated with.
Type: String

## Errors
<a name="API_PutKeyword_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** Reason **
The reason for the exception.
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
<a name="API_PutKeyword_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/PutKeyword)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/PutKeyword)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/PutKeyword)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/PutKeyword)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/PutKeyword)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/PutKeyword)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/PutKeyword)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/PutKeyword)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/PutKeyword)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/PutKeyword)
