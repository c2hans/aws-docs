---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel-04.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL 4. How do you design interactions in a distributed system to prevent failures?
<a name="rel-04"></a>

Distributed systems rely on communications networks to interconnect components, such as servers or services. Your workload must operate reliably despite data loss or latency in these networks. Components of the distributed system must operate in a way that does not negatively impact other components or the workload. These best practices prevent failures and improve mean time between failures (MTBF).

**Topics**
+ [REL04-BP01 Identify which kind of distributed system is required](rel_prevent_interaction_failure_identify.md)
+ [REL04-BP02 Implement loosely coupled dependencies](rel_prevent_interaction_failure_loosely_coupled_system.md)
+ [REL04-BP03 Do constant work](rel_prevent_interaction_failure_constant_work.md)
+ [REL04-BP04 Make all responses idempotent](rel_prevent_interaction_failure_idempotent.md)
