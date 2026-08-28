---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ParticipantDetailsToAdd.html
---

# ParticipantDetailsToAdd
<a name="API_ParticipantDetailsToAdd"></a>

The details to add for the participant.

## Contents
<a name="API_ParticipantDetailsToAdd_Contents"></a>

 ** DisplayName **   <a name="connect-Type-ParticipantDetailsToAdd-DisplayName"></a>
The display name of the participant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ParticipantCapabilities **   <a name="connect-Type-ParticipantDetailsToAdd-ParticipantCapabilities"></a>
The configuration for the allowed video and screen sharing capabilities for participants present over the call. For more information, see [Set up in-app, web, video calling, and screen sharing capabilities](https://docs.aws.amazon.com/connect/latest/adminguide/inapp-calling.html) in the *Connect Customer Administrator Guide*.
Type: [ParticipantCapabilities](API_ParticipantCapabilities.md) object
Required: No

 ** ParticipantRole **   <a name="connect-Type-ParticipantDetailsToAdd-ParticipantRole"></a>
The role of the participant being added.
Type: String
Valid Values: `AGENT | CUSTOMER | SYSTEM | CUSTOM_BOT | SUPERVISOR`
Required: No

## See Also
<a name="API_ParticipantDetailsToAdd_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ParticipantDetailsToAdd)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ParticipantDetailsToAdd)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ParticipantDetailsToAdd)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
