---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateGlobalSettings.html
---

# UpdateGlobalSettings
<a name="API_voice-chime_UpdateGlobalSettings"></a>

Updates global settings for the Amazon Chime SDK Voice Connectors in an AWS account.

## Request Syntax
<a name="API_voice-chime_UpdateGlobalSettings_RequestSyntax"></a>

```
PUT /settings HTTP/1.1
Content-type: application/json

{
   "VoiceConnector": {
      "CdrBucket": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_voice-chime_UpdateGlobalSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_voice-chime_UpdateGlobalSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [VoiceConnector](#API_voice-chime_UpdateGlobalSettings_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateGlobalSettings-request-VoiceConnector"></a>
The Voice Connector settings.
Type: [VoiceConnectorSettings](API_voice-chime_VoiceConnectorSettings.md) object
Required: No

## Response Syntax
<a name="API_voice-chime_UpdateGlobalSettings_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_voice-chime_UpdateGlobalSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_voice-chime_UpdateGlobalSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The number of customer requests exceeds the request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client isn't authorized to request a resource.
HTTP Status Code: 401

## See Also
<a name="API_voice-chime_UpdateGlobalSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/UpdateGlobalSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/UpdateGlobalSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/UpdateGlobalSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/UpdateGlobalSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/UpdateGlobalSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/UpdateGlobalSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/UpdateGlobalSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/UpdateGlobalSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/UpdateGlobalSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/UpdateGlobalSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
