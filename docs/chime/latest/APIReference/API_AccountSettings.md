---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_AccountSettings.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# AccountSettings
<a name="API_AccountSettings"></a>

Settings related to the Amazon Chime account. This includes settings that start or stop remote control of shared screens, or start or stop the dial-out option in the Amazon Chime web application. For more information about these settings, see [Use the Policies Page](https://docs.aws.amazon.com/chime/latest/ag/policies.html) in the *Amazon Chime Administration Guide*.

## Contents
<a name="API_AccountSettings_Contents"></a>

 ** DisableRemoteControl **   <a name="chime-Type-AccountSettings-DisableRemoteControl"></a>
Setting that stops or starts remote control of shared screens during meetings.
Type: Boolean
Required: No

 ** EnableDialOut **   <a name="chime-Type-AccountSettings-EnableDialOut"></a>
Setting that allows meeting participants to choose the **Call me at a phone number** option. For more information, see [Join a Meeting without the Amazon Chime App](https://docs.aws.amazon.com/chime/latest/ug/chime-join-meeting.html).
Type: Boolean
Required: No

## See Also
<a name="API_AccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/AccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/AccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/AccountSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
