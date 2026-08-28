---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_APPC.html
---

# How AWS AppConfig uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_APPC"></a>

AWS AppConfig is a capability of AWS Systems Manager that you can use to create, manage, and quickly deploy application configurations. A configuration can contain credential data or other sensitive information stored in Secrets Manager. When you create a freeform configuration profile, you can choose Secrets Manager as the source of your configuration data. For more information, see [Creating a freeform configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html#appconfig-creating-configuration-and-profile-free-form-configurations) in the *AWS AppConfig User Guide*. For information about how AWS AppConfig handles secrets that have automatic rotation turned on, see [Secrets Manager key rotation](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-security.html#appconfig-security-secrets-manager-key-rotation) in the *AWS AppConfig User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
