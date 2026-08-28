---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutOptedOutNumber.html
---

# PutOptedOutNumber
<a name="API_PutOptedOutNumber"></a>

Creates an opted out destination phone number in the opt-out list.

If the destination phone number isn't valid or if the specified opt-out list doesn't exist, an error is returned.

## Request Syntax
<a name="API_PutOptedOutNumber_RequestSyntax"></a>

```
{
   "OptedOutNumber": "{{string}}",
   "OptOutListName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutOptedOutNumber_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OptedOutNumber](#API_PutOptedOutNumber_RequestSyntax) **   <a name="pinpoint-PutOptedOutNumber-request-OptedOutNumber"></a>
The phone number to add to the OptOutList in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** [OptOutListName](#API_PutOptedOutNumber_RequestSyntax) **   <a name="pinpoint-PutOptedOutNumber-request-OptOutListName"></a>
The OptOutListName or OptOutListArn to add the phone number to.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_PutOptedOutNumber_ResponseSyntax"></a>

```
{
   "EndUserOptedOut": boolean,
   "OptedOutNumber": "string",
   "OptedOutTimestamp": number,
   "OptOutListArn": "string",
   "OptOutListName": "string"
}
```

## Response Elements
<a name="API_PutOptedOutNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndUserOptedOut](#API_PutOptedOutNumber_ResponseSyntax) **   <a name="pinpoint-PutOptedOutNumber-response-EndUserOptedOut"></a>
This is true if it was the end user who requested their phone number be removed.
Type: Boolean

 ** [OptedOutNumber](#API_PutOptedOutNumber_ResponseSyntax) **   <a name="pinpoint-PutOptedOutNumber-response-OptedOutNumber"></a>
The phone number that was added to the OptOutList.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`

 ** [OptedOutTimestamp](#API_PutOptedOutNumber_ResponseSyntax) **   <a name="pinpoint-PutOptedOutNumber-response-OptedOutTimestamp"></a>
The time that the phone number was added to the OptOutList, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [OptOutListArn](#API_PutOptedOutNumber_ResponseSyntax) **   <a name="pinpoint-PutOptedOutNumber-response-OptOutListArn"></a>
The OptOutListArn that the phone number was removed from.
Type: String

 ** [OptOutListName](#API_PutOptedOutNumber_ResponseSyntax) **   <a name="pinpoint-PutOptedOutNumber-response-OptOutListName"></a>
The OptOutListName that the phone number was removed from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

## Errors
<a name="API_PutOptedOutNumber_Errors"></a>

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
<a name="API_PutOptedOutNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/PutOptedOutNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/PutOptedOutNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/PutOptedOutNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/PutOptedOutNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/PutOptedOutNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/PutOptedOutNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/PutOptedOutNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/PutOptedOutNumber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/PutOptedOutNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/PutOptedOutNumber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
