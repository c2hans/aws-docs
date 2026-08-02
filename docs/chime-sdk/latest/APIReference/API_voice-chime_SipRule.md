---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipRule.html
---

# SipRule
<a name="API_voice-chime_SipRule"></a>

The details of a SIP rule, including name, triggers, and target applications. An AWS account can have multiple SIP rules.

## Contents
<a name="API_voice-chime_SipRule_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_SipRule-CreatedTimestamp"></a>
The time at which the SIP rule was created, in ISO 8601 format.
Type: Timestamp
Required: No

 ** Disabled **   <a name="chimesdk-Type-voice-chime_SipRule-Disabled"></a>
Indicates whether the SIP rule is enabled or disabled. You must disable a rule before you can delete it.
Type: Boolean
Required: No

 ** Name **   <a name="chimesdk-Type-voice-chime_SipRule-Name"></a>
A SIP rule's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: No

 ** SipRuleId **   <a name="chimesdk-Type-voice-chime_SipRule-SipRuleId"></a>
A SIP rule's ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TargetApplications **   <a name="chimesdk-Type-voice-chime_SipRule-TargetApplications"></a>
The target SIP media application and other details, such as priority and AWS Region, to be specified in the SIP rule. Only one SIP rule per AWS Region can be provided.
Type: Array of [SipRuleTargetApplication](API_voice-chime_SipRuleTargetApplication.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

 ** TriggerType **   <a name="chimesdk-Type-voice-chime_SipRule-TriggerType"></a>
The type of trigger set for a SIP rule, either a phone number or a URI request host name.
Type: String
Valid Values: `ToPhoneNumber | RequestUriHostname`
Required: No

 ** TriggerValue **   <a name="chimesdk-Type-voice-chime_SipRule-TriggerValue"></a>
The value set for a SIP rule's trigger type. Either a phone number or a URI hostname.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_SipRule-UpdatedTimestamp"></a>
The time at which the SIP rule was updated, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_voice-chime_SipRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/SipRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/SipRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/SipRule)
