---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys.html
---

# Keys in AWS CloudHSM
<a name="manage-keys"></a>

Before you can use your AWS CloudHSM cluster for cryptoprocessing, you must create [users](manage-hsm-users.md) and keys on the hardware security modules (HSM) in your cluster.

In AWS CloudHSM, use any of the following to manage keys on the HSMs in your cluster:
+ PKCS \#11 library
+ JCE provider
+ CNG and KSP providers
+ CloudHSM CLI

Before you can manage keys, you must log in to the HSM with the user name and password of a crypto user (CU). Only a CU can create a key. The CU who creates a key owns and manages that key.

See the following topics for more information about managing keys in AWS CloudHSM.

**Topics**
+ [Key sync and durability](manage-key-sync.md)
+ [AES key wrapping](manage-aes-key-wrapping.md)
+ [Trusted keys](manage-keys-using-trusted-keys.md)
+ [Key management with CloudHSM CLI](manage-keys-chsm-cli.md)
+ [Key management with KMU](manage-keys-kmu-cmu.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
