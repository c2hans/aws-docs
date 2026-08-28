---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/export-keys.html
---

# Export keys with the AWS CloudHSM KMU
<a name="export-keys"></a>

To export AWS CloudHSM secret keys—that is, symmetric keys and asymmetric private keys—from the hardware security module (HSM) using the AWS CloudHSM key\_mgmt\_util (KMU), you must first create a wrapping key. You can export public keys directly without a wrapping key.

Only the key owner can export a key. Users with whom the key is shared can use the key in cryptographic operations, but they cannot export it. When running this example, be sure to export a key that you created.

**Important**
The [exSymKey](key_mgmt_util-exSymKey.md) command writes a plaintext (unencrypted) copy of the secret key to a file. The export process requires a wrapping key, but the key in the file is ***not*** a wrapped key. To export a wrapped (encrypted) copy of a key, use the [wrapKey](key_mgmt_util-wrapKey.md) command.

**Topics**
+ [Export secret keys](export-secret-keys.md)
+ [Export public keys](export-public-keys.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
