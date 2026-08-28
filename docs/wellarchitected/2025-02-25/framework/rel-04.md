---
source_url: https://docs.aws.amazon.com/wellarchitected/2025-02-25/framework/rel-04.html
---

# REL 4. How do you design interactions in a distributed system to prevent failures?
<a name="rel-04"></a>

Distributed systems rely on communications networks to interconnect components, such as servers or services. Your workload must operate reliably despite data loss or latency in these networks. Components of the distributed system must operate in a way that does not negatively impact other components or the workload. These best practices prevent failures and improve mean time between failures (MTBF).

**Topics**
+ [REL04-BP01 Identify the kind of distributed systems you depend on](rel_prevent_interaction_failure_identify.md)
+ [REL04-BP02 Implement loosely coupled dependencies](rel_prevent_interaction_failure_loosely_coupled_system.md)
+ [REL04-BP03 Do constant work](rel_prevent_interaction_failure_constant_work.md)
+ [REL04-BP04 Make mutating operations idempotent](rel_prevent_interaction_failure_idempotent.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
