---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/troubleshoot-connector-scep-client-errors.html
---

# Troubleshoot Connector for SCEP client errors
<a name="troubleshoot-connector-scep-client-errors"></a>

Use the following guidance to troubleshoot client errors related to Connector for SCEP.

| Message example | Root cause | Solution |
| --- | --- | --- |
| ECDSA keys are not supported | The connector is connected to a private CA that uses an ECDSA key instead of RSA. While this service supports ECDSA keys, not all client devices may be compatible with this algorithm. | Consider using an RSA-encrypted private CA instead of ECDSA. If you create a private CA that uses RSA, you'll need to also create a new connector. A connector can only be tied to one private CA through its lifespan. |
| Encryption or signing certificate is not present | According to RFC 8894, a SCEP service returns intermediate CA certificates to the client. These certificates are used by the client to perform encryption and signature validation operations as part of the SCEP protocol.<br />Connector for SCEP uses the same certificate for both encryption and signature validation purposes, which is a common approach. However, some clients may expect to have two separate certificates instead. | If you are unable to use compatible clients, contact [AWS Support](https://aws.amazon.com/contact-us/) for assistance. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
