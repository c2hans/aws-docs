---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/missing-attribute.html
---

# Troubleshooting AWS Client VPN: Client software returns user name and password errors — federated authentication
<a name="missing-attribute"></a>

**Problem**
Trying to log in with a user name and password with federated authentication and getting the error "The credentials received were incorrect. Contact your IT administrator."

**Cause**
This error can be caused by not having at least one attribute included in the SAML response from the IdP.

**Solution**
Make sure at least one attribute is included in the SAML response from the IdP. See [SAML-based IdP configuration resources](federated-authentication.md#saml-config-resources) for more information.
