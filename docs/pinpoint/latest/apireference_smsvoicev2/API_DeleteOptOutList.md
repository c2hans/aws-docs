---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteOptOutList.html
---

# DeleteOptOutList
<a name="API_DeleteOptOutList"></a>

Deletes an existing opt-out list. All opted out phone numbers in the opt-out list are deleted.

If the specified opt-out list name doesn't exist or is in-use by an origination phone number or pool, an error is returned.

## Request Syntax
<a name="API_DeleteOptOutList_RequestSyntax"></a>

```
{
   "OptOutListName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteOptOutList_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OptOutListName](#API_DeleteOptOutList_RequestSyntax) **   <a name="pinpoint-DeleteOptOutList-request-OptOutListName"></a>
The OptOutListName or OptOutListArn of the OptOutList to delete. You can use [DescribeOptOutLists](API_DescribeOptOutLists.md) to find the values for OptOutListName and OptOutListArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteOptOutList_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "OptOutListArn": "string",
   "OptOutListName": "string"
}
```

## Response Elements
<a name="API_DeleteOptOutList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_DeleteOptOutList_ResponseSyntax) **   <a name="pinpoint-DeleteOptOutList-response-CreatedTimestamp"></a>
The time when the OptOutList was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [OptOutListArn](#API_DeleteOptOutList_ResponseSyntax) **   <a name="pinpoint-DeleteOptOutList-response-OptOutListArn"></a>
The Amazon Resource Name (ARN) of the OptOutList that was removed.
Type: String

 ** [OptOutListName](#API_DeleteOptOutList_ResponseSyntax) **   <a name="pinpoint-DeleteOptOutList-response-OptOutListName"></a>
The name of the OptOutList that was removed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

## Errors
<a name="API_DeleteOptOutList_Errors"></a>

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
<a name="API_DeleteOptOutList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteOptOutList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteOptOutList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteOptOutList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteOptOutList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteOptOutList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteOptOutList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteOptOutList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteOptOutList)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteOptOutList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteOptOutList)
