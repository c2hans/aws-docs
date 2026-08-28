---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_marketplace-deployment.html
---

# AWS Marketplace
<a name="integrating_how-services-use-secrets_marketplace-deployment"></a>

When you use AWS Marketplace Quick Launch, AWS Marketplace distributes your software along with the license key. AWS Marketplace stores the license key in your account as a Secrets Manager [managed secret](service-linked-secrets.md). The cost of storing the secret is included with the charges for AWS Marketplace. To update the secret, you must use AWS Marketplace rather than Secrets Manager. For more information, see [Configure Quick Launch](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-product-settings.html#saas-quick-launch) in the *AWS Marketplace Seller Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
