---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdateProtectConfiguration.html
---

# UpdateProtectConfiguration
<a name="API_UpdateProtectConfiguration"></a>

Update the setting for an existing protect configuration.

## Request Syntax
<a name="API_UpdateProtectConfiguration_RequestSyntax"></a>

```
{
   "DeletionProtectionEnabled": {{boolean}},
   "ProtectConfigurationId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateProtectConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeletionProtectionEnabled](#API_UpdateProtectConfiguration_RequestSyntax) **   <a name="pinpoint-UpdateProtectConfiguration-request-DeletionProtectionEnabled"></a>
When set to true deletion protection is enabled. By default this is set to false.
Type: Boolean
Required: No

 ** [ProtectConfigurationId](#API_UpdateProtectConfiguration_RequestSyntax) **   <a name="pinpoint-UpdateProtectConfiguration-request-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_UpdateProtectConfiguration_ResponseSyntax"></a>

```
{
   "AccountDefault": boolean,
   "CreatedTimestamp": number,
   "DeletionProtectionEnabled": boolean,
   "ProtectConfigurationArn": "string",
   "ProtectConfigurationId": "string"
}
```

## Response Elements
<a name="API_UpdateProtectConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountDefault](#API_UpdateProtectConfiguration_ResponseSyntax) **   <a name="pinpoint-UpdateProtectConfiguration-response-AccountDefault"></a>
This is true if the protect configuration is set as your account default protect configuration.
Type: Boolean

 ** [CreatedTimestamp](#API_UpdateProtectConfiguration_ResponseSyntax) **   <a name="pinpoint-UpdateProtectConfiguration-response-CreatedTimestamp"></a>
The time when the protect configuration was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DeletionProtectionEnabled](#API_UpdateProtectConfiguration_ResponseSyntax) **   <a name="pinpoint-UpdateProtectConfiguration-response-DeletionProtectionEnabled"></a>
The status of deletion protection for the protect configuration. When set to true deletion protection is enabled. By default this is set to false.
Type: Boolean

 ** [ProtectConfigurationArn](#API_UpdateProtectConfiguration_ResponseSyntax) **   <a name="pinpoint-UpdateProtectConfiguration-response-ProtectConfigurationArn"></a>
The Amazon Resource Name (ARN) of the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:\S+`

 ** [ProtectConfigurationId](#API_UpdateProtectConfiguration_ResponseSyntax) **   <a name="pinpoint-UpdateProtectConfiguration-response-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

## Errors
<a name="API_UpdateProtectConfiguration_Errors"></a>

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
<a name="API_UpdateProtectConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/UpdateProtectConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/UpdateProtectConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/UpdateProtectConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/UpdateProtectConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/UpdateProtectConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/UpdateProtectConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/UpdateProtectConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/UpdateProtectConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/UpdateProtectConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/UpdateProtectConfiguration)
