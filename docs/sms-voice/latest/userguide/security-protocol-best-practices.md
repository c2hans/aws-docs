---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/security-protocol-best-practices.html
---

# SMS protocol security best practices
<a name="security-protocol-best-practices"></a>

Given the limitations of the SMS protocols, here are some industry best practices to consider depending on your use case and your own security assessments:
+ Choose a short time-to-live (TTL) for one time passwords (OTP).
+ Block sending SMS messages to countries you don't do business in with AWS End User Messaging SMS Protect configurations.
+ For sensitive information refer your customer to a secure portal.
+ Use URL shorteners with caution to avoid the appearance of phishing or social engineering.
+ Keep message content concise and include only necessary information.

For more information on the best practices of creating and sending SMS and MMS messages, see [SMS and MMS best practices](best-practices.md#best-practices-sms).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
