---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/import-keys.html
---

# Import keys with the AWS CloudHSM KMU
<a name="import-keys"></a>

To import secret keys—that is, symmetric keys and asymmetric private keys—into the hardware security module (HSM) using the AWS CloudHSM key\_mgmt\_util, you must first create a wrapping key on the HSM. You can import public keys directly without a wrapping key.

**Topics**
+ [Import secret keys](import-secret-keys.md)
+ [Import public keys](import-public-keys.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
