---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/import-public-keys.html
---

# Import public keys with the AWS CloudHSM KMU
<a name="import-public-keys"></a>

Use the [importPubKey](key_mgmt_util-importPubKey.md) command in the AWS CloudHSM key\_mgmt\_util (KMU) to import a public key. To see all available options, use the **importPubKey -h** command.

The following example imports an RSA public key from a file named `rsa2048.pub`.

```
Command: importPubKey -f rsa2048.pub -l rsa2048-public-imported
Cfm3CreatePublicKey returned: 0x00 : HSM Return: SUCCESS

Public Key Handle: 524302

Cluster Error Status
Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
Node id 2 and err state 0x00000000 : HSM Return: SUCCESS
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
