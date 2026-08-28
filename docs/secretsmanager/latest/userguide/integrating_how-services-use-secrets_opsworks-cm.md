---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_opsworks-cm.html
---

# How AWS OpsWorks for Chef Automate uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_opsworks-cm"></a>

OpsWorks is a configuration management service that helps you configure and operate applications in a cloud enterprise by using OpsWorks for Puppet Enterprise or AWS OpsWorks for Chef Automate.

When you create a new server in AWS OpsWorks CM, OpsWorks CM stores information for the server in a Secrets Manager [managed secret](service-linked-secrets.md) with the prefix `opsworks-cm`. The cost of the secret is included in the charge for OpsWorks. For more information, see [Integration with AWS Secrets Manager](https://docs.aws.amazon.com/opsworks/latest/userguide/data-protection.html#data-protection-secrets-manager) in the *OpsWorks User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
