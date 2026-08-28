---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/export-public-keys.html
---

# Export public keys with the AWS CloudHSM KMU
<a name="export-public-keys"></a>

Use the **exportPubKey** command in the AWS CloudHSM key\_mgmt\_util (KMU) to export a public key. To see all available options, use the **exportPubKey -h** command.

The following example exports an RSA public key to a file named `rsa2048.pub.exp`.

```
Command: exportPubKey -k 524294 -out rsa2048.pub.exp
PEM formatted public key is written to rsa2048.pub.key

Cfm3ExportPubKey returned: 0x00 : HSM Return: SUCCESS
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
