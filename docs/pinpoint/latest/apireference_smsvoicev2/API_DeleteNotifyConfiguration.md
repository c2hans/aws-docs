---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteNotifyConfiguration.html
---

# DeleteNotifyConfiguration
<a name="API_DeleteNotifyConfiguration"></a>

Deletes an existing notify configuration.

If deletion protection is enabled, an error is returned.

## Request Syntax
<a name="API_DeleteNotifyConfiguration_RequestSyntax"></a>

```
{
   "NotifyConfigurationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteNotifyConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NotifyConfigurationId](#API_DeleteNotifyConfiguration_RequestSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-request-NotifyConfigurationId"></a>
The identifier of the notify configuration to delete. The NotifyConfigurationId can be found using the [DescribeNotifyConfigurations](API_DescribeNotifyConfigurations.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteNotifyConfiguration_ResponseSyntax"></a>

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
   "Tier": "string",
   "TierUpgradeStatus": "string",
   "UseCase": "string"
}
```

## Response Elements
<a name="API_DeleteNotifyConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-CreatedTimestamp"></a>
The time when the notify configuration was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DefaultTemplateId](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-DefaultTemplateId"></a>
The default template identifier associated with the notify configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([A-Za-z0-9_-]*|UNSET_DEFAULT_TEMPLATE)`

 ** [DeletionProtectionEnabled](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-DeletionProtectionEnabled"></a>
When set to true deletion protection is enabled. By default this is set to false.
Type: Boolean

 ** [DisplayName](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-DisplayName"></a>
The display name associated with the notify configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `[A-Za-z0-9_ -]+`

 ** [EnabledChannels](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-EnabledChannels"></a>
An array of channels enabled for the notify configuration. Supported values include `SMS` and `VOICE`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`

 ** [EnabledCountries](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-EnabledCountries"></a>
An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`

 ** [NotifyConfigurationArn](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-NotifyConfigurationArn"></a>
The Amazon Resource Name (ARN) for the notify configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:\S+`

 ** [NotifyConfigurationId](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-NotifyConfigurationId"></a>
The unique identifier for the notify configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [PoolId](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-PoolId"></a>
The identifier of the pool associated with the notify configuration.
Type: String

 ** [RejectionReason](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-RejectionReason"></a>
The reason the notify configuration was rejected, if applicable.
Type: String

 ** [Status](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-Status"></a>
The current status of the notify configuration.
Type: String
Valid Values: `PENDING | ACTIVE | REJECTED | REQUIRES_VERIFICATION`

 ** [Tier](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-Tier"></a>
The tier of the notify configuration.
Type: String
Valid Values: `BASIC | ADVANCED`

 ** [TierUpgradeStatus](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-TierUpgradeStatus"></a>
The tier upgrade status of the notify configuration.
Type: String
Valid Values: `BASIC | PENDING_UPGRADE | ADVANCED | REJECTED`

 ** [UseCase](#API_DeleteNotifyConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyConfiguration-response-UseCase"></a>
The use case for the notify configuration.
Type: String
Valid Values: `CODE_VERIFICATION`

## Errors
<a name="API_DeleteNotifyConfiguration_Errors"></a>

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
<a name="API_DeleteNotifyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
