---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/export-in-acm.html
---

# Export a private certificate and its secret key
<a name="export-in-acm"></a>

AWS Private CA cannot directly export a private certificate that it has signed and issued. However, you can use AWS Certificate Manager to export such a certificate along with its encrypted secret key. The certificate is then completely portable for deployment anywhere in your private PKI. For more information, see [Exporting a private certificate](https://docs.aws.amazon.com/acm/latest/userguide/export-private.html) in the AWS Certificate Manager User Guide.

As an added benefit, AWS Certificate Manager provides managed renewal for private certificates that were issued using the ACM console, the `RequestCertificate` action of the ACM API, or the **request-certificate** command in the ACM section of the AWS CLI. For more information about renewals, see [Renewing certificates in a private PKI.](https://docs.aws.amazon.com/acm/latest/userguide/renew-private-cert.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
