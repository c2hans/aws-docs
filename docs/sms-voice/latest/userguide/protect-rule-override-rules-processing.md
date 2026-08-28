---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-rule-override-rules-processing.html
---

# How phone number override rules are processed in AWS End User Messaging SMS
<a name="protect-rule-override-rules-processing"></a>

If a phone number is in the opt-out list then the message is not sent regardless if there is an override to allow. The phone number override always takes precedent over the country rule mode. For example, if the country rule mode is block and a phone number override rule is always allow then sending to the phone number is allowed. The opposite is also true, if the country rule mode is allow and a phone number override rule is always block then sending to the phone number is not allowed.

![Shows the decisions for using a phone number override rule.](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/phone-number-override-rule-process.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
