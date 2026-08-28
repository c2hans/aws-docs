---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_Origination.html
---

# Origination
<a name="API_voice-chime_Origination"></a>

Origination settings enable your SIP hosts to receive inbound calls using your Amazon Chime SDK Voice Connector.

**Note**
The parameters listed below are not required, but you must use at least one.

## Contents
<a name="API_voice-chime_Origination_Contents"></a>

 ** Disabled **   <a name="chimesdk-Type-voice-chime_Origination-Disabled"></a>
When origination settings are disabled, inbound calls are not enabled for your Amazon Chime SDK Voice Connector. This parameter is not required, but you must specify this parameter or `Routes`.
Type: Boolean
Required: No

 ** Routes **   <a name="chimesdk-Type-voice-chime_Origination-Routes"></a>
The call distribution properties defined for your SIP hosts. Valid range: Minimum value of 1. Maximum value of 20. This parameter is not required, but you must specify this parameter or `Disabled`.
Type: Array of [OriginationRoute](API_voice-chime_OriginationRoute.md) objects
Required: No

## See Also
<a name="API_voice-chime_Origination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/Origination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/Origination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/Origination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
