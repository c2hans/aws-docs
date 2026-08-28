---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_directconnect.html
---

# How AWS Direct Connect uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_directconnect"></a>

Direct Connect links your internal network to an Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services.

Direct Connect stores a connectivity association key name and connectivity association key pair (CKN/CAK pair) in a [managed secret](service-linked-secrets.md) with the prefix `directconnect`. The cost of the secret is included with the charge for Direct Connect. To update the secret, you must use Direct Connect rather than Secrets Manager. For more information, see [Associate a MACsec CKN/CAK with a LAG ](https://docs.aws.amazon.com/directconnect/latest/UserGuide/associate-key-lag.html) in the *Direct Connect User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
