---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateConfigurationSet.html
---

# CreateConfigurationSet
<a name="API_CreateConfigurationSet"></a>

Creates a new configuration set. After you create the configuration set, you can add one or more event destinations to it.

A configuration set is a set of rules that you apply to the SMS and voice messages that you send.

When you send a message, you can optionally specify a single configuration set.

## Request Syntax
<a name="API_CreateConfigurationSet_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "ConfigurationSetName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateConfigurationSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateConfigurationSet_RequestSyntax) **   <a name="pinpoint-CreateConfigurationSet-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [ConfigurationSetName](#API_CreateConfigurationSet_RequestSyntax) **   <a name="pinpoint-CreateConfigurationSet-request-ConfigurationSetName"></a>
The name to use for the new configuration set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [Tags](#API_CreateConfigurationSet_RequestSyntax) **   <a name="pinpoint-CreateConfigurationSet-request-Tags"></a>
An array of key and value pair tags that's associated with the new configuration set.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateConfigurationSet_ResponseSyntax"></a>

```
{
   "ConfigurationSetArn": "string",
   "ConfigurationSetName": "string",
   "CreatedTimestamp": number,
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateConfigurationSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationSetArn](#API_CreateConfigurationSet_ResponseSyntax) **   <a name="pinpoint-CreateConfigurationSet-response-ConfigurationSetArn"></a>
The Amazon Resource Name (ARN) of the newly created configuration set.
Type: String

 ** [ConfigurationSetName](#API_CreateConfigurationSet_ResponseSyntax) **   <a name="pinpoint-CreateConfigurationSet-response-ConfigurationSetName"></a>
The name of the new configuration set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [CreatedTimestamp](#API_CreateConfigurationSet_ResponseSyntax) **   <a name="pinpoint-CreateConfigurationSet-response-CreatedTimestamp"></a>
The time when the configuration set was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [Tags](#API_CreateConfigurationSet_ResponseSyntax) **   <a name="pinpoint-CreateConfigurationSet-response-Tags"></a>
An array of key and value pair tags that's associated with the configuration set.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_CreateConfigurationSet_Errors"></a>

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
<a name="API_CreateConfigurationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/CreateConfigurationSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/CreateConfigurationSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CreateConfigurationSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/CreateConfigurationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CreateConfigurationSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/CreateConfigurationSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/CreateConfigurationSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/CreateConfigurationSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/CreateConfigurationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CreateConfigurationSet)
