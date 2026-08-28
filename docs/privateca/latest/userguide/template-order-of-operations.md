---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/template-order-of-operations.html
---

# AWS Private CA template order of operations
<a name="template-order-of-operations"></a>

Information contained in an issued certificate can come from four sources: the template definition, API passthrough, CSR passthrough, and the CA configuration.

API passthrough values are only respected when you use an API passthrough or APICSR passthrough template. CSR passthrough is only respected when you use a CSRPassthrough or APICSR passthrough template. When these sources of information are in conflict, a general rule usually applies: For each extension value, the template definition has highest priority, followed by API passthrough values, followed by CSR passthrough extensions.

**Examples**

1. The template definition for [EndEntityClientAuthCertificate\_APIPassthrough](template-definitions.md#EndEntityClientAuthCertificate_APIPassthrough) defines the ExtendedKeyUsage extension with a value of "TLS web server authentication, TLS web client authentication". If ExtendedKeyUsage is defined in the CSR or in the `IssueCertificate` `ApiPassthrough` parameter, the `ApiPassthrough` value for ExtendedKeyUsage will be ignored because the template definition takes priority, and the CSR value for ExtendedKeyUsage value will be ignored because the template is not a CSR passthrough variety.
**Note**
The template definition nonetheless copies over other values from the CSR, such as Subject and Subject Alternative Name. These values are still taken from the CSR even though the template is not a CSR passthrough variety, because the template definition always takes highest priority.

1. The template definition for [EndEntityClientAuthCertificate\_APICSRPassthrough](template-definitions.md#EndEntityClientAuthCertificate_APICSRPassthrough) defines the Subject Alternative Name (SAN) extension as being copied from the API or CSR. If the SAN extension is defined in the CSR and provided in the `IssueCertificate`` ApiPassthrough` parameter, the API passthrough value will take priority because API passthrough values take priority over CSR passthrough values.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
