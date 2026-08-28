---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ParticipantCapabilities.html
---

# ParticipantCapabilities
<a name="API_ParticipantCapabilities"></a>

The configuration for the allowed video and screen sharing capabilities for participants present over the call. For more information, see [Set up in-app, web, video calling, and screen sharing capabilities](https://docs.aws.amazon.com/connect/latest/adminguide/inapp-calling.html) in the *Connect Customer Administrator Guide*.

## Contents
<a name="API_ParticipantCapabilities_Contents"></a>

 ** ScreenShare **   <a name="connect-Type-ParticipantCapabilities-ScreenShare"></a>
The screen sharing capability that is enabled for the participant. `SEND` indicates the participant can share their screen.
Type: String
Valid Values: `SEND`
Required: No

 ** Video **   <a name="connect-Type-ParticipantCapabilities-Video"></a>
The configuration having the video and screen sharing capabilities for participants over the call.
Type: String
Valid Values: `SEND`
Required: No

## See Also
<a name="API_ParticipantCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ParticipantCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ParticipantCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ParticipantCapabilities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
