---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/concepts-key-sync.html
---

# AWS CloudHSM key concepts
<a name="concepts-key-sync"></a>

The following are concepts to be aware of when working with keys in AWS CloudHSM.

**Token keys**
Persistent keys that you create during key generate, import or unwrap operations. AWS CloudHSM synchronizes token keys across a cluster.

**Session keys**
Ephemeral keys that exist only on one hardware security module (HSM) in the cluster. AWS CloudHSM does *not* synchronize session keys across a cluster.

**Client-side key synchronization**
A client-side process that clones token keys you create during key generate, import or unwrap operations. You can make token keys more durable by running a cluster with a minimum of two HSMs.

**Server-side key synchronization**
Periodically clones keys to every HSM in the cluster. Requires no management.

**Client key durability settings**
Settings you configure on the client that impact key durability. These settings work differently in Client SDK 5 and Client SDK 3.
+ In Client SDK 5, use this setting to run a single HSM cluster.
+ In Client SDK 3, use this setting to specify the number of HSMs required for key creation operations to succeed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
