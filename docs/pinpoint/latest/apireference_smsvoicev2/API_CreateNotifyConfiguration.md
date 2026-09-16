---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateNotifyConfiguration.html
---

# CreateNotifyConfiguration
<a name="API_CreateNotifyConfiguration"></a>

Creates a new notify configuration for managed messaging. A notify configuration defines the settings for sending templated messages, including the display name, use case, enabled channels, and enabled countries.

## Request Syntax
<a name="API_CreateNotifyConfiguration_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DefaultTemplateId": "{{string}}",
   "DeletionProtectionEnabled": {{boolean}},
   "DisplayName": "{{string}}",
   "EnabledChannels": [ "{{string}}" ],
   "EnabledCountries": [ "{{string}}" ],
   "PoolId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UseCase": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateNotifyConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateNotifyConfiguration_RequestSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [DefaultTemplateId](#API_CreateNotifyConfiguration_RequestSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-request-DefaultTemplateId"></a>
The default template identifier to associate with the notify configuration. If specified, this template is used when sending messages without an explicit template identifier.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([A-Za-z0-9_-]*|UNSET_DEFAULT_TEMPLATE)`
Required: No

 ** [DeletionProtectionEnabled](#API_CreateNotifyConfiguration_RequestSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-request-DeletionProtectionEnabled"></a>
By default this is set to false. When set to true the notify configuration can't be deleted. You can change this value using the [UpdateNotifyConfiguration](API_UpdateNotifyConfiguration.md) action.
Type: Boolean
Required: No

 ** [DisplayName](#API_CreateNotifyConfiguration_RequestSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-request-DisplayName"></a>
The display name to associate with the notify configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `[A-Za-z0-9_ -]+`
Required: Yes

 ** [EnabledChannels](#API_CreateNotifyConfiguration_RequestSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-request-EnabledChannels"></a>
An array of channels to enable for the notify configuration. Supported values include `SMS` and `VOICE`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`
Required: Yes

 ** [EnabledCountries](#API_CreateNotifyConfiguration_RequestSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-request-EnabledCountries"></a>
An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

 ** [PoolId](#API_CreateNotifyConfiguration_RequestSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-request-PoolId"></a>
The identifier of the pool to associate with the notify configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]*`
Required: No

 ** [Tags](#API_CreateNotifyConfiguration_RequestSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-request-Tags"></a>
An array of tags (key and value pairs) associated with the notify configuration.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [UseCase](#API_CreateNotifyConfiguration_RequestSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-request-UseCase"></a>
The use case for the notify configuration.
Type: String
Valid Values: `CODE_VERIFICATION`
Required: Yes

## Response Syntax
<a name="API_CreateNotifyConfiguration_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "DefaultTemplateId": "string",
   "DeletionProtectionEnabled": boolean,
   "DisplayName": "string",
   "EnabledChannels": [ "string" ],
   "EnabledCountries": [ "string" ],
   "NotifyConfigurationArn": "string",
   "NotifyConfigurationId": "string",
   "PoolId": "string",
   "RejectionReason": "string",
   "Status": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ],
   "Tier": "string",
   "TierUpgradeStatus": "string",
   "UseCase": "string"
}
```

## Response Elements
<a name="API_CreateNotifyConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-CreatedTimestamp"></a>
The time when the notify configuration was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DefaultTemplateId](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-DefaultTemplateId"></a>
The default template identifier associated with the notify configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([A-Za-z0-9_-]*|UNSET_DEFAULT_TEMPLATE)`

 ** [DeletionProtectionEnabled](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-DeletionProtectionEnabled"></a>
When set to true deletion protection is enabled. By default this is set to false.
Type: Boolean

 ** [DisplayName](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-DisplayName"></a>
The display name associated with the notify configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `[A-Za-z0-9_ -]+`

 ** [EnabledChannels](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-EnabledChannels"></a>
An array of channels enabled for the notify configuration. Supported values include `SMS` and `VOICE`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`

 ** [EnabledCountries](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-EnabledCountries"></a>
An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`

 ** [NotifyConfigurationArn](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-NotifyConfigurationArn"></a>
The Amazon Resource Name (ARN) for the notify configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:\S+`

 ** [NotifyConfigurationId](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-NotifyConfigurationId"></a>
The unique identifier for the notify configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [PoolId](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-PoolId"></a>
The identifier of the pool associated with the notify configuration.
Type: String

 ** [RejectionReason](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-RejectionReason"></a>
The reason the notify configuration was rejected, if applicable.
Type: String

 ** [Status](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-Status"></a>
The current status of the notify configuration.
Type: String
Valid Values: `PENDING | ACTIVE | REJECTED | REQUIRES_VERIFICATION`

 ** [Tags](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-Tags"></a>
An array of tags (key and value pairs) associated with the notify configuration.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [Tier](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-Tier"></a>
The tier of the notify configuration.
Type: String
Valid Values: `BASIC | ADVANCED`

 ** [TierUpgradeStatus](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-TierUpgradeStatus"></a>
The tier upgrade status of the notify configuration.
Type: String
Valid Values: `BASIC | PENDING_UPGRADE | ADVANCED | REJECTED`

 ** [UseCase](#API_CreateNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-CreateNotifyConfiguration-response-UseCase"></a>
The use case for the notify configuration.
Type: String
Valid Values: `CODE_VERIFICATION`

## Errors
<a name="API_CreateNotifyConfiguration_Errors"></a>

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
<a name="API_CreateNotifyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/CreateNotifyConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/CreateNotifyConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CreateNotifyConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/CreateNotifyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CreateNotifyConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/CreateNotifyConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/CreateNotifyConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/CreateNotifyConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/CreateNotifyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CreateNotifyConfiguration)
