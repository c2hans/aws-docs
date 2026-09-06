---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-no-port.html
---

# Troubleshooting AWS Client VPN: Client returns no available ports error — federated authentication
<a name="client-no-port"></a>

**Problem**
I use federated authentication for my Client VPN endpoint. When clients try to connect to the endpoint, the client software returns the following error:

```
The authentication flow could not be initiated. There are no available ports.
```

**Cause**
The AWS provided client requires the use of TCP port 35001 to complete authentication. For more information, see [Requirements and considerations for SAML-based federated authentication](federated-authentication.md#saml-requirements).

**Solution**
Verify that the client's device is not blocking TCP port 35001 or is using it for a different process.
