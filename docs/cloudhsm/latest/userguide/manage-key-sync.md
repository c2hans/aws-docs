---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-key-sync.html
---

# Key synchronization and durability settings in AWS CloudHSM
<a name="manage-key-sync"></a>

AWS CloudHSM synchronizes every token key you create. Key synchronization is mostly an automatic process, but you can use a minimum of two hardware security modules (HSM) in your cluster to make keys more durable. This topic describes key synchronization settings, common issues customers face working with keys on a cluster, and strategies for making keys more durable.

This topic describes key synchronization settings in AWS CloudHSM, common issues customers face working with keys on a cluster, and strategies for making keys more durable.

**Topics**
+ [Concepts](concepts-key-sync.md)
+ [Understanding key synchronization](understand-key-sync.md)
+ [Change client key durability settings](working-client-sync.md)
+ [Synchronizing keys across cloned clusters](cli-sync.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
