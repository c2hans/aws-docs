---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_Termination.html
---

# Termination
<a name="API_voice-chime_Termination"></a>

Termination settings enable SIP hosts to make outbound calls using an Amazon Chime SDK Voice Connector.

## Contents
<a name="API_voice-chime_Termination_Contents"></a>

 ** CallingRegions **   <a name="chimesdk-Type-voice-chime_Termination-CallingRegions"></a>
The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.
Type: Array of strings
Required: No

 ** CidrAllowedList **   <a name="chimesdk-Type-voice-chime_Termination-CidrAllowedList"></a>
The IP addresses allowed to make calls, in CIDR format.
Type: Array of strings
Required: No

 ** CpsLimit **   <a name="chimesdk-Type-voice-chime_Termination-CpsLimit"></a>
The limit on calls per second. Max value based on account service quota. Default value of 1.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** DefaultPhoneNumber **   <a name="chimesdk-Type-voice-chime_Termination-DefaultPhoneNumber"></a>
The default outbound calling number.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: No

 ** Disabled **   <a name="chimesdk-Type-voice-chime_Termination-Disabled"></a>
When termination is disabled, outbound calls cannot be made.
Type: Boolean
Required: No

## See Also
<a name="API_voice-chime_Termination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/Termination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/Termination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/Termination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
