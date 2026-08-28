---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.46.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Infrastructure 6.46 release
<a name="infra-release-notes-6.46"></a>

The following release notes include information for infrastructure release 6.46. For information on the release timeline, see [Change log](#infra-release-notes-6.46-change-log).

**Platform version**

|  |  |
| --- | --- |
| Infrastructure | 6.46.1 <br />Replicated Native Scheduler (2080)<br />Replicated KOTS (1785) |

**New features**:

Customers can now establish global federation with other Wickr Enterprise deployments and AWS Wickr networks using self-signed certificates.

**Improvements**:
+ A new federated outbox has been introduced to provide a more reliable messaging send flow across global federation.
+ Added the ability to monitor the TLS certificate file change and automatically restart TCPProxy for the new certificate to take effect.

## Change log
<a name="infra-release-notes-6.46-change-log"></a>

**Change log for 6.46 release and release notes**

| Change | Description | Date |
| --- | --- | --- |
| Final release | Final notes with Replicated build number | October 16, 2024 |
| Infrastructure update | Updates to address vulnerability scan results and improvements | October 16, 2024 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
