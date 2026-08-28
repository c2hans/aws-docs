---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html
---

# Use AWS Private CA certificate templates
<a name="UsingTemplates"></a>

AWS Private CA uses configuration templates to issue both CA certificates and end-entity certificates. When you issue a CA certificate from the PCA console, the appropriate root or subordinate CA certificate template is applied automatically.

If you use the CLI or API to issue a certificate, you can supply a template ARN as a parameter to the `IssueCertificate` action. If you provide no ARN, then the `EndEntityCertificate/V1` template is applied by default. For more information, see the [IssueCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html) API and [issue-certificate](https://docs.aws.amazon.com/cli/latest/reference/acm-pca/issue-certificate.html) command documentation.

**Note**
AWS Certificate Manager (ACM) users with cross-account shared access to a private CA can issue managed certificates that are signed by the CA. When you grant permission to the `IssueCertificate` action, you can restrict the certificate templates used for certificate issuance by adding a `acm-pca:TemplateArn` Condition to the policy.
For more information, see [Resource-based policies](pca-rbp.md).

**Topics**
+ [AWS Private CA template varieties](template-varieties.md)
+ [AWS Private CA template order of operations](template-order-of-operations.md)
+ [AWS Private CA template definitions](template-definitions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
