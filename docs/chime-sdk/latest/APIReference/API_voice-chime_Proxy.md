---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_Proxy.html
---

# Proxy
<a name="API_voice-chime_Proxy"></a>

The proxy configuration for an Amazon Chime SDK Voice Connector.

## Contents
<a name="API_voice-chime_Proxy_Contents"></a>

 ** DefaultSessionExpiryMinutes **   <a name="chimesdk-Type-voice-chime_Proxy-DefaultSessionExpiryMinutes"></a>
The default number of minutes allowed for proxy sessions.
Type: Integer
Required: No

 ** Disabled **   <a name="chimesdk-Type-voice-chime_Proxy-Disabled"></a>
When true, stops proxy sessions from being created on the specified Amazon Chime SDK Voice Connector.
Type: Boolean
Required: No

 ** FallBackPhoneNumber **   <a name="chimesdk-Type-voice-chime_Proxy-FallBackPhoneNumber"></a>
The phone number to route calls to after a proxy session expires.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: No

 ** PhoneNumberCountries **   <a name="chimesdk-Type-voice-chime_Proxy-PhoneNumberCountries"></a>
The countries for proxy phone numbers to be selected from.
Type: Array of strings
Required: No

## See Also
<a name="API_voice-chime_Proxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/Proxy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/Proxy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/Proxy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
