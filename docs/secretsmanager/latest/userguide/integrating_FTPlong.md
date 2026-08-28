---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_FTPlong.html
---

# How AWS Transfer Family uses AWS Secrets Manager secrets
<a name="integrating_FTPlong"></a>

AWS Transfer Family is a secure transfer service that enables you to transfer files into and out of AWS storage services.

Transfer Family now supports using Basic authentication for servers that use the Applicability Statement 2 (AS2) protocol. You can create a new Secrets Manager secret or choose an existing secret for your credentials. For more information, see [Basic authentication for AS2 connectors](https://docs.aws.amazon.com/transfer/latest/userguide/as2-connectors-details.html#as2-basic-auth) in the *AWS Transfer Family User Guide*.

To authenticate Transfer Family users, you can use AWS Secrets Manager as an identity provider. For more information, see [Working with custom identity providers](https://docs.aws.amazon.com/transfer/latest/userguide/custom-identity-provider-users.html) in the *AWS Transfer Family User Guide* and the blog article [Enable password authentication for AWS Transfer Family using AWS Secrets Manager](https://aws.amazon.com/blogs/storage/enable-password-authentication-for-aws-transfer-family-using-aws-secrets-manager-updated/).

You can use Pretty Good Privacy (PGP) decryption with the files that Transfer Family processes with workflows. To use decryption in a workflow step, you provide a PGP key that you manage in Secrets Manager. For more information, see [Generate and manage PGP keys](https://docs.aws.amazon.com/transfer/latest/userguide/key-management.html#pgp-key-management) in the *AWS Transfer Family User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
