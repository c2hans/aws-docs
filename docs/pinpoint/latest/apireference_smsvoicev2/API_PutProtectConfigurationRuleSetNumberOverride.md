---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutProtectConfigurationRuleSetNumberOverride.html
---

# PutProtectConfigurationRuleSetNumberOverride
<a name="API_PutProtectConfigurationRuleSetNumberOverride"></a>

Create or update a phone number rule override and associate it with a protect configuration.

## Request Syntax
<a name="API_PutProtectConfigurationRuleSetNumberOverride_RequestSyntax"></a>

```
{
   "Action": "{{string}}",
   "ClientToken": "{{string}}",
   "DestinationPhoneNumber": "{{string}}",
   "ExpirationTimestamp": {{number}},
   "ProtectConfigurationId": "{{string}}"
}
```

## Request Parameters
<a name="API_PutProtectConfigurationRuleSetNumberOverride_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Action](#API_PutProtectConfigurationRuleSetNumberOverride_RequestSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-request-Action"></a>
The action for the rule to either block or allow messages to the destination phone number.
Type: String
Valid Values: `ALLOW | BLOCK`
Required: Yes

 ** [ClientToken](#API_PutProtectConfigurationRuleSetNumberOverride_RequestSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [DestinationPhoneNumber](#API_PutProtectConfigurationRuleSetNumberOverride_RequestSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-request-DestinationPhoneNumber"></a>
The destination phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** [ExpirationTimestamp](#API_PutProtectConfigurationRuleSetNumberOverride_RequestSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-request-ExpirationTimestamp"></a>
The time the rule will expire at. If `ExpirationTimestamp` is not set then the rule does not expire.
Type: Timestamp
Required: No

 ** [ProtectConfigurationId](#API_PutProtectConfigurationRuleSetNumberOverride_RequestSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-request-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_PutProtectConfigurationRuleSetNumberOverride_ResponseSyntax"></a>

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
<a name="API_PutProtectConfigurationRuleSetNumberOverride_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Action](#API_PutProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-response-Action"></a>
The action for the rule to take.
Type: String
Valid Values: `ALLOW | BLOCK`

 ** [CreatedTimestamp](#API_PutProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-response-CreatedTimestamp"></a>
The time when the rule was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DestinationPhoneNumber](#API_PutProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-response-DestinationPhoneNumber"></a>
The destination phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`

 ** [ExpirationTimestamp](#API_PutProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-response-ExpirationTimestamp"></a>
The time the rule will expire at.
Type: Timestamp

 ** [IsoCountryCode](#API_PutProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-response-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`

 ** [ProtectConfigurationArn](#API_PutProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-response-ProtectConfigurationArn"></a>
The Amazon Resource Name (ARN) of the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:\S+`

 ** [ProtectConfigurationId](#API_PutProtectConfigurationRuleSetNumberOverride_ResponseSyntax) **   <a name="pinpoint-PutProtectConfigurationRuleSetNumberOverride-response-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

## Errors
<a name="API_PutProtectConfigurationRuleSetNumberOverride_Errors"></a>

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
<a name="API_PutProtectConfigurationRuleSetNumberOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/PutProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/PutProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/PutProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/PutProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/PutProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/PutProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/PutProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/PutProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/PutProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/PutProtectConfigurationRuleSetNumberOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
