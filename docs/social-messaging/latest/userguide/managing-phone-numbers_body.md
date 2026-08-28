---
source_url: https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-phone-numbers_body.html
---

# Phone number considerations for use with a WABA
<a name="managing-phone-numbers_body"></a>

When you link a phone number with your WhatsApp Business Account (WABA), you should consider the following:
+ Phone numbers can only be linked to one WABA at a time.
+ The phone number can still be used for SMS, MMS, and voice calls.
+ Each phone number has a quality rating from Meta.

You can obtain an SMS-capable phone number through AWS End User Messaging SMS by doing the following:

1. Make sure that the [country or region](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html) for the phone number supports two-way SMS.

1. Request the [phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-request.html). Depending on the country or region, you may be required to register the phone number.

1. [Enable two-way SMS messaging](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-two-way-sms.html) for the phone number. Once setup is complete, your incoming SMS messages are sent to an event destination.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
