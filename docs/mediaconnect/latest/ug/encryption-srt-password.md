---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-srt-password.html
---

# SRT password encryption in AWS Elemental MediaConnect
<a name="encryption-srt-password"></a>

You can use the Secure Reliable Transport (SRT) password encryption option to encrypt sources, outputs and router I/O when using the SRT protocols. SRT protocols are a highly available, low-latency protocol suitable for long-distance applications. You store your encryption password in AWS Secrets Manager, and then you give MediaConnect permission to obtain the encryption password from Secrets Manager.

**Topics**
+ [Password management for SRT password encryption](encryption-srt-password-password-management.md)
+ [Setting up SRT password encryption using AWS Elemental MediaConnect](encryption-srt-password-set-up.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
