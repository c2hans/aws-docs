---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeChannelDefinition.html
---

# MedicalScribeChannelDefinition
<a name="API_MedicalScribeChannelDefinition"></a>

Defines a channel in the audio stream

## Contents
<a name="API_MedicalScribeChannelDefinition_Contents"></a>

 ** channelId **   <a name="connecthealth-Type-MedicalScribeChannelDefinition-channelId"></a>
The channel identifier
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** participantRole **   <a name="connecthealth-Type-MedicalScribeChannelDefinition-participantRole"></a>
The role of the participant on this channel
Type: String
Valid Values: `PATIENT | CLINICIAN`
Required: Yes

## See Also
<a name="API_MedicalScribeChannelDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalScribeChannelDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalScribeChannelDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalScribeChannelDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
