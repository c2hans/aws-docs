---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantTokenConfiguration.html
---

# ParticipantTokenConfiguration
<a name="API_ParticipantTokenConfiguration"></a>

Object specifying a participant token configuration in a stage.

## Contents
<a name="API_ParticipantTokenConfiguration_Contents"></a>

 ** attributes **   <a name="ivsrealtimeeapireference-Type-ParticipantTokenConfiguration-attributes"></a>
Application-provided attributes to encode into the corresponding participant token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
Type: String to string map
Required: No

 ** capabilities **   <a name="ivsrealtimeeapireference-Type-ParticipantTokenConfiguration-capabilities"></a>
Set of capabilities that the user is allowed to perform in the stage.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `PUBLISH | SUBSCRIBE`
Required: No

 ** duration **   <a name="ivsrealtimeeapireference-Type-ParticipantTokenConfiguration-duration"></a>
Duration (in minutes), after which the corresponding participant token expires. Default: 720 (12 hours).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20160.
Required: No

 ** userId **   <a name="ivsrealtimeeapireference-Type-ParticipantTokenConfiguration-userId"></a>
Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_ParticipantTokenConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ParticipantTokenConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ParticipantTokenConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ParticipantTokenConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
