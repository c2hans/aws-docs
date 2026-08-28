---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/application-security.html
---

# Application security
<a name="application-security"></a>

 Application security describes the overall process of how you design, build, and test the security properties of the workloads you develop. You should have appropriately trained people in your organization, understand the security properties of your build and release infrastructure, and use automation to identify security issues.

| HNSEC07: How do you provide encryption in transit? |
| --- |
|   |

 Ensuring proper encryption in transit is critical for protecting data as it moves between cloud and on-premises infrastructure. To achieve this, implement TLS 1.2 or later encryption for application-level traffic, maintain proper certificate management with automated rotation before expiration.

**Topics**
+ [HNSEC07-BP01 Enforce End-to-End TLS Encryption](hnsec07-bp01.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
