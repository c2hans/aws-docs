---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/incident-response.html
---

# Incident response
<a name="incident-response"></a>

 Security incidents can span both on-premises and cloud infrastructure, requiring coordinated response capabilities across environment boundaries. The complexity of hybrid architectures - with multiple connection types, intricate routing policies, and layered security controls - creates unique challenges for incident response teams. Responders must understand how incidents can propagate across interconnection points and impact different parts of the infrastructure while coordinating containment and remediation efforts across both environments.

| HNSEC06: How do you isolate a hybrid networking environment from a security incident that originates from your on-premises network? |
| --- |
|   |

 Security incidents originating in one environment can quickly spread across hybrid network connections, potentially compromising both on-premises and cloud resources. Organizations need rapid isolation capabilities and clear procedures to contain threats while maintaining essential business operations and preventing unauthorized lateral movement between environments.

**Topics**
+ [HNSEC06-BP01 Monitor your environment for malicious behavior](hnsec06-bp01.md)
+ [HNSEC06-BP02 Automate incident response](hnsec06-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
