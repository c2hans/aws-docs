---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/troubleshoot-certificate-revocation.html
---

# Troubleshoot AWS Private CA certificate revocation issues
<a name="troubleshoot-certificate-revocation"></a>

## OCSP response latency
<a name="OCSP-latency-troubleshooting"></a>

OCSP responsiveness may be slower if the caller is geographically distant from a regional edge cache or from the Region of the issuing CA. For more information about regional edge cache availability, see [Global Edge Network](https://aws.amazon.com/cloudfront/details#Global_Edge_Network). We recommend issuing certificates in a Region near where they will be used.

## Revocation of self-signed certificates
<a name="PcaRevokeSelfSigned"></a>

You can't revoke a self-signed CA certificate. To functionally revoke the certificate, delete the CA.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
