---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/email-synchronization-federated-users.html
---

# Quick email synchronization for federated users
<a name="email-synchronization-federated-users"></a>

**Note**
This feature is available only for the Enterprise edition of Amazon Quick.

When IAM users self-provision access to Quick, administrators can't control which email address the user provides to Quick. Users could enter a personal email address instead of their work email address. This might not be acceptable for some organizations. However, when you're using an identity provider to provide federated access to Quick Enterprise edition, Quick has a feature that ensures the user's email address in Quick matches the user's email address in the identity provider.

In the IdP, you add a SAML attribute for the user's email address. The process for creating the attribute or token differs for each IdP. See the instructions for [Okta](https://www.okta.com/blog/2019/11/okta-and-aws-partner-to-simplify-access-via-session-tags/) or [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-abac.html), or see the documentation for your organization's IdP. The IdP passes the user's email as an IAM `Principal` session tag. Quick uses this session tag instead of prompting the user to provide their email address. For instructions about how to enable this feature, see [Configuring email syncing for federated users](https://docs.aws.amazon.com/quicksuite/latest/userguide/jit-email-syncing.html) in the Quick documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
