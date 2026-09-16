---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeKeywords.html
---

# DescribeKeywords
<a name="API_DescribeKeywords"></a>

Describes the specified keywords or all keywords on your origination phone number or pool.

A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, AWS End User Messaging SMS responds with a customizable message.

If you specify a keyword that isn't valid, an error is returned.

## Request Syntax
<a name="API_DescribeKeywords_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Keywords": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OriginationIdentity": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeKeywords_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeKeywords_RequestSyntax) **   <a name="pinpoint-DescribeKeywords-request-Filters"></a>
An array of keyword filters to filter the results.
Type: Array of [KeywordFilter](API_KeywordFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [Keywords](#API_DescribeKeywords_RequestSyntax) **   <a name="pinpoint-DescribeKeywords-request-Keywords"></a>
An array of keywords to search for.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[ \S]+`
Required: No

 ** [MaxResults](#API_DescribeKeywords_RequestSyntax) **   <a name="pinpoint-DescribeKeywords-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeKeywords_RequestSyntax) **   <a name="pinpoint-DescribeKeywords-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [OriginationIdentity](#API_DescribeKeywords_RequestSyntax) **   <a name="pinpoint-DescribeKeywords-request-OriginationIdentity"></a>
The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use [DescribePhoneNumbers](API_DescribePhoneNumbers.md) to find the values for PhoneNumberId and PhoneNumberArn while [DescribeSenderIds](API_DescribeSenderIds.md) can be used to get the values for SenderId and SenderIdArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeKeywords_ResponseSyntax"></a>

```
{
   "Keywords": [
      {
         "Keyword": "string",
         "KeywordAction": "string",
         "KeywordMessage": "string"
      }
   ],
   "NextToken": "string",
   "OriginationIdentity": "string",
   "OriginationIdentityArn": "string"
}
```

## Response Elements
<a name="API_DescribeKeywords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Keywords](#API_DescribeKeywords_ResponseSyntax) **   <a name="pinpoint-DescribeKeywords-response-Keywords"></a>
An array of KeywordInformation objects that contain the results.
Type: Array of [KeywordInformation](API_KeywordInformation.md) objects

 ** [NextToken](#API_DescribeKeywords_ResponseSyntax) **   <a name="pinpoint-DescribeKeywords-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [OriginationIdentity](#API_DescribeKeywords_ResponseSyntax) **   <a name="pinpoint-DescribeKeywords-response-OriginationIdentity"></a>
The PhoneNumberId or PoolId that is associated with the OriginationIdentity.
Type: String

 ** [OriginationIdentityArn](#API_DescribeKeywords_ResponseSyntax) **   <a name="pinpoint-DescribeKeywords-response-OriginationIdentityArn"></a>
The PhoneNumberArn or PoolArn that is associated with the OriginationIdentity.
Type: String

## Errors
<a name="API_DescribeKeywords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
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
<a name="API_DescribeKeywords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeKeywords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeKeywords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeKeywords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeKeywords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeKeywords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeKeywords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeKeywords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeKeywords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeKeywords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeKeywords)
