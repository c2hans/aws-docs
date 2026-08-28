---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorProxy.html
---

# PutVoiceConnectorProxy
<a name="API_voice-chime_PutVoiceConnectorProxy"></a>

Puts the specified proxy configuration to the specified Amazon Chime SDK Voice Connector.

**Important**
End of support notice: On April 7, 2026, AWS will end support for Amazon Chime SDK proxy sessions.

## Request Syntax
<a name="API_voice-chime_PutVoiceConnectorProxy_RequestSyntax"></a>

```
PUT /voice-connectors/{{voiceConnectorId}}/programmable-numbers/proxy HTTP/1.1
Content-type: application/json

{
   "DefaultSessionExpiryMinutes": {{number}},
   "Disabled": {{boolean}},
   "FallBackPhoneNumber": "{{string}}",
   "PhoneNumberPoolCountries": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_voice-chime_PutVoiceConnectorProxy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [voiceConnectorId](#API_voice-chime_PutVoiceConnectorProxy_RequestSyntax) **   <a name="chimesdk-voice-chime_PutVoiceConnectorProxy-request-uri-VoiceConnectorId"></a>
The Voice Connector ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_PutVoiceConnectorProxy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DefaultSessionExpiryMinutes](#API_voice-chime_PutVoiceConnectorProxy_RequestSyntax) **   <a name="chimesdk-voice-chime_PutVoiceConnectorProxy-request-DefaultSessionExpiryMinutes"></a>
The default number of minutes allowed for proxy session.
Type: Integer
Required: Yes

 ** [Disabled](#API_voice-chime_PutVoiceConnectorProxy_RequestSyntax) **   <a name="chimesdk-voice-chime_PutVoiceConnectorProxy-request-Disabled"></a>
When true, stops proxy sessions from being created on the specified Amazon Chime SDK Voice Connector.
Type: Boolean
Required: No

 ** [FallBackPhoneNumber](#API_voice-chime_PutVoiceConnectorProxy_RequestSyntax) **   <a name="chimesdk-voice-chime_PutVoiceConnectorProxy-request-FallBackPhoneNumber"></a>
The phone number to route calls to after a proxy session expires.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: No

 ** [PhoneNumberPoolCountries](#API_voice-chime_PutVoiceConnectorProxy_RequestSyntax) **   <a name="chimesdk-voice-chime_PutVoiceConnectorProxy-request-PhoneNumberPoolCountries"></a>
The countries for proxy phone numbers to be selected from.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `^$|^[A-Z]{2,2}$`
Required: Yes

## Response Syntax
<a name="API_voice-chime_PutVoiceConnectorProxy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Proxy": {
      "DefaultSessionExpiryMinutes": number,
      "Disabled": boolean,
      "FallBackPhoneNumber": "string",
      "PhoneNumberCountries": [ "string" ]
   }
}
```

## Response Elements
<a name="API_voice-chime_PutVoiceConnectorProxy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Proxy](#API_voice-chime_PutVoiceConnectorProxy_ResponseSyntax) **   <a name="chimesdk-voice-chime_PutVoiceConnectorProxy-response-Proxy"></a>
The proxy configuration details.
Type: [Proxy](API_voice-chime_Proxy.md) object

## Errors
<a name="API_voice-chime_PutVoiceConnectorProxy_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **
You don't have the permissions needed to run this action.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
The requested resource couldn't be found.
HTTP Status Code: 404

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
<a name="API_voice-chime_PutVoiceConnectorProxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/PutVoiceConnectorProxy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/PutVoiceConnectorProxy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/PutVoiceConnectorProxy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/PutVoiceConnectorProxy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/PutVoiceConnectorProxy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/PutVoiceConnectorProxy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/PutVoiceConnectorProxy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/PutVoiceConnectorProxy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/PutVoiceConnectorProxy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/PutVoiceConnectorProxy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
