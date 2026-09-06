---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-cannot-connect-mutual.html
---

# Troubleshooting AWS Client VPN: Clients cannot connect — mutual authentication
<a name="client-cannot-connect-mutual"></a>

**Problem**
I use mutual authentication for my Client VPN endpoint. Clients are getting TLS key negotiation failed errors and timeout errors.

**Possible causes**
The configuration file that was provided to the clients does not contain the client certificate and the client private key, or the certificate and key are incorrect.

**Solution**
Ensure that the configuration file contains the correct client certificate and key. If necessary, fix the configuration file and redistribute it to your clients. For more information, see [AWS Client VPN endpoint configuration file export](cvpn-working-endpoint-export.md).
