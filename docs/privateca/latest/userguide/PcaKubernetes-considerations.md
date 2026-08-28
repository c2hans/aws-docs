---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/PcaKubernetes-considerations.html
---

# Considerations
<a name="PcaKubernetes-considerations"></a>

When using AWS Private Certificate Authority with Kubernetes, keep the following considerations in mind.

## Cross-account use of cert-manager
<a name="kubernetes-cross-account"></a>

Administrators with cross-account access to a CA can use the `cert-manager` add on for Kubernetes to provision certificates for a cluster using the shared CA. For more information, refer to [Security best practices for Cross-account access to private CAs](pca-resource-sharing.md).

You can use only certain AWS Private CA certificate templates in cross-account scenarios.

The following table lists AWS Private CA templates that you can use with cert-manager to provision a Kubernetes cluster.

| Templates supported for Kubernetes | Support for cross-account use |
| --- | --- |
| [BlankEndEntityCertificate\_CSRPassthrough/V1 definition](template-definitions.md#BlankEndEntityCertificate_CSRPassthrough) | No |
| [CodeSigningCertificate/V1 definition](template-definitions.md#CodeSigningCertificate-V1) | No |
| [EndEntityCertificate/V1 definition](template-definitions.md#EndEntityCertificate-V1) | Yes |
| [EndEntityClientAuthCertificate/V1 definition](template-definitions.md#EndEntityClientAuthCertificate-V1) | Yes |
| [EndEntityServerAuthCertificate/V1 definition](template-definitions.md#EndEntityServerAuthCertificate-V1) | Yes |
| [OCSPSigningCertificate/V1 definition](template-definitions.md#OCSPSigningCertificate-V1) | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
