---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/security-protocol-considerations.html
---

# SMS protocol security considerations
<a name="security-protocol-considerations"></a>

It's important to understand the inherent limitations of the SMS protocol itself. Unlike secure messaging apps, SMS does not provide end-to-end encryption, message revocation, or inherent sender authentication, checksum error detection, and in some cases may store SMS in plain text on the device. There are also practical limitations such as message size that can impact how recipients view your message, see [Messaging limits and restrictions](sms-limitations.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
