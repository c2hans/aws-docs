---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/mutual.html
---

# Mutual authentication in AWS Client VPN
<a name="mutual"></a>

With mutual authentication, Client VPN uses certificates to perform authentication between the client and the server. Certificates are a digital form of identification issued by a certificate authority (CA). The server uses client certificates to authenticate clients when they attempt to connect to the Client VPN endpoint. You must create a server certificate and key, and at least one client certificate and key.

You must upload the server certificate to AWS Certificate Manager (ACM) and specify it when you create a Client VPN endpoint. When you upload the server certificate to ACM, you also specify the certificate authority (CA). You only need to upload the client certificate to ACM when the CA of the client certificate is different from the CA of the server certificate. For more information about ACM, see the [AWS Certificate Manager User Guide](https://docs.aws.amazon.com/acm/latest/userguide/).

You can create a separate client certificate and key for each client that will connect to the Client VPN endpoint. This enables you to revoke a specific client certificate if a user leaves your organization. In this case, when you create the Client VPN endpoint, you can specify the server certificate ARN for the client certificate, provided that the client certificate has been issued by the same CA as the server certificate.

Certificates used in AWS Client VPN must adhere to [RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](https://datatracker.ietf.org/doc/html/rfc5280), including the Certificate Extensions specified in section 4.2 of the memo.

**Note**
A Client VPN endpoint supports 1024-bit and 2048-bit RSA key sizes only. Also, the client certificate must have the CN attribute in the Subject field.
When certificates being used with the Client VPN service are updated, whether through ACM auto-rotation, manually importing a new certificate, or metadata updates to IAM Identity Center the Client VPN service will automatically update theClient VPN endpoint with the newer certificate. This is an automated process that can take up to 5 hours.

**Topics**
+ [Enable mutual authentication](client-auth-mutual-enable.md)
+ [Renew your server certificate](mutual-renew.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
