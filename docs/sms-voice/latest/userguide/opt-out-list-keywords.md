---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-keywords.html
---

# Required AWS End User Messaging SMS opt-out list keywords
<a name="opt-out-list-keywords"></a>

Where required by local laws and regulations (such as in the US and Canada), SMS and MMS recipients can use their devices to opt out by replying to the message with any of the following:
+ ARRET
+ CANCEL
+ END
+ OPT-OUT
+ OPTOUT
+ QUIT
+ REMOVE
+ STOP
+ TD
+ UNSUBSCRIBE

To opt out, the recipient must reply to the same long code or short code that AWS End User Messaging SMS used to deliver the message. After opting out, the recipient no longer receives SMS or MMS messages from your AWS account.

**Note**
For US toll-free numbers, opt-outs are managed at the carrier level. The only supported opt-out keyword for a US toll-free number is STOP. You can't add additional opt-out keywords, or change the response message that your recipients get when they opt-out.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
