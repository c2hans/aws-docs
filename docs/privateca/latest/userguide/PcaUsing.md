---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/PcaUsing.html
---

# Issue and manage certificates in AWS Private CA
<a name="PcaUsing"></a>

After you have created and activated a private certificate authority (CA) and configured access to it, you or your authorized users can issue and manage certificates. If you have not yet set up AWS Identity and Access Management (IAM) policies for the CA, you can learn more about configuring them in the [Identity and Access Management](https://docs.aws.amazon.com/privateca/latest/userguide/security-iam.html) section of this guide. For information about configuring CA access in single-account and cross-account scenarios, see [Control access to the private CA](granting-ca-access.md).

**Topics**
+ [Issue private end-entity certificates](PcaIssueCert.md)
+ [Retrieve a private certificate](PcaGetCert.md)
+ [List private certificates](PcaListCerts.md)
+ [Export a private certificate and its secret key](export-in-acm.md)
+ [Revoke a private certificate](PcaRevokeCert.md)
+ [Automate export of a renewed certificate](auto-export.md)
+ [Use AWS Private CA certificate templates](UsingTemplates.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
