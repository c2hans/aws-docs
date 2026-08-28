---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_AccountLimit.html
---

# AccountLimit
<a name="API_AccountLimit"></a>

The current resource quotas associated with an AWS account.

## Contents
<a name="API_AccountLimit_Contents"></a>

 ** Max **   <a name="pinpoint-Type-AccountLimit-Max"></a>
The AWS set limit for that resource type, in US dollars.
Type: Long
Required: Yes

 ** Name **   <a name="pinpoint-Type-AccountLimit-Name"></a>
The name of the attribute to apply the account limit to.
Type: String
Valid Values: `PHONE_NUMBERS | POOLS | CONFIGURATION_SETS | OPT_OUT_LISTS | SENDER_IDS | REGISTRATIONS | REGISTRATION_ATTACHMENTS | VERIFIED_DESTINATION_NUMBERS`
Required: Yes

 ** Used **   <a name="pinpoint-Type-AccountLimit-Used"></a>
The current amount that has been spent, in US dollars.
Type: Long
Required: Yes

## See Also
<a name="API_AccountLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/AccountLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/AccountLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/AccountLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
