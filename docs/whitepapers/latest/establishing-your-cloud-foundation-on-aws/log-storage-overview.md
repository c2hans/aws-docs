---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/log-storage-overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Overview
<a name="log-storage-overview"></a>

The Log Storage capability primary mapping is to Security. The **Security team **should be responsible for implementing this capability according to your governance requirements.

Having a separated ***log storage*** allows you to establish a secure location where the logs become the source of truth for the actions and events happening in your environment relevant to security and operations. For example access to different accounts, or infrastructure updates.

Log storage must be tamper resistant and encrypted, and only accessed by controlled, automated, and monitored mechanisms, based on least privilege access by role. Controls need to be implemented around the log storage to protect the integrity and availability of the logs and their management process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
