---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ExternalSystemsConfiguration.html
---

# ExternalSystemsConfiguration
<a name="API_voice-chime_ExternalSystemsConfiguration"></a>

Contains information about an external systems configuration for a Voice Connector.

## Contents
<a name="API_voice-chime_ExternalSystemsConfiguration_Contents"></a>

 ** ContactCenterSystemTypes **   <a name="chimesdk-Type-voice-chime_ExternalSystemsConfiguration-ContactCenterSystemTypes"></a>
The contact center system.
Type: Array of strings
Valid Values: `GENESYS_ENGAGE_ON_PREMISES | AVAYA_AURA_CALL_CENTER_ELITE | AVAYA_AURA_CONTACT_CENTER | CISCO_UNIFIED_CONTACT_CENTER_ENTERPRISE`
Required: No

 ** SessionBorderControllerTypes **   <a name="chimesdk-Type-voice-chime_ExternalSystemsConfiguration-SessionBorderControllerTypes"></a>
The session border controllers.
Type: Array of strings
Valid Values: `RIBBON_SBC | ORACLE_ACME_PACKET_SBC | AVAYA_SBCE | CISCO_UNIFIED_BORDER_ELEMENT | AUDIOCODES_MEDIANT_SBC`
Required: No

## See Also
<a name="API_voice-chime_ExternalSystemsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/ExternalSystemsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/ExternalSystemsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/ExternalSystemsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
