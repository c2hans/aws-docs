---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteProtectConfigurationRuleSetNumberOverride.html
---

# DeleteProtectConfigurationRuleSetNumberOverride
<a name="API_DeleteProtectConfigurationRuleSetNumberOverride"></a>

Permanently delete the protect configuration rule set number override.

## Request Syntax
<a name="API_DeleteProtectConfigurationRuleSetNumberOverride_RequestSyntax"></a>

```
{
   "DestinationPhoneNumber": "{{string}}",
   "ProtectConfigurationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteProtectConfigurationRuleSetNumberOverride_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DestinationPhoneNumber](#API_DeleteProtectConfigurationRuleSetNumberOverride_RequestSyntax) **   <a name="pinpoint-DeleteProtectConfigurationRuleSetNumberOverride-request-DestinationPhoneNumber"></a>
The destination phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** [ProtectConfigurationId](#API_DeleteProtectConfigurationRuleSetNumberOverride_RequestSyntax) **   <a name="pinpoint-DeleteProtectConfigurationRuleSetNumberOverride-request-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteProtectConfigurationRuleSetNumberOverride_ResponseSyntax"></a>

```
{
   "Action": "string",
   "CreatedTimestamp": number,
   "DestinationPhoneNumber": "string",
   "ExpirationTimestamp": number,
   "IsoCountryCode": "string",
   "ProtectConfigurationArn": "string",
   "ProtectConfigurationId": "string"
}
```

## Response Elements
<a name="API_DeleteProtectConfigurationRuleSetNumberOverride_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Action](#API_DeleteProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-DeleteProtectConfigurationRuleSetNumberOverride-response-Action"></a>
The action associated with the rule.
Type: String
Valid Values: `ALLOW | BLOCK`

 ** [CreatedTimestamp](#API_DeleteProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-DeleteProtectConfigurationRuleSetNumberOverride-response-CreatedTimestamp"></a>
The time when the rule was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DestinationPhoneNumber](#API_DeleteProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-DeleteProtectConfigurationRuleSetNumberOverride-response-DestinationPhoneNumber"></a>
The destination phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`

 ** [ExpirationTimestamp](#API_DeleteProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-DeleteProtectConfigurationRuleSetNumberOverride-response-ExpirationTimestamp"></a>
The time when the resource-based policy was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [IsoCountryCode](#API_DeleteProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-DeleteProtectConfigurationRuleSetNumberOverride-response-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`

 ** [ProtectConfigurationArn](#API_DeleteProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-DeleteProtectConfigurationRuleSetNumberOverride-response-ProtectConfigurationArn"></a>
The Amazon Resource Name (ARN) of the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:\S+`

 ** [ProtectConfigurationId](#API_DeleteProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-DeleteProtectConfigurationRuleSetNumberOverride-response-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

## Errors
<a name="API_DeleteProtectConfigurationRuleSetNumberOverride_Errors"></a>

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
<a name="API_DeleteProtectConfigurationRuleSetNumberOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteProtectConfigurationRuleSetNumberOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
