---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authentication.html
---

# Client authentication in AWS Client VPN
<a name="client-authentication"></a>

Client authentication is implemented at the first point of entry into the AWS Cloud. It is used to determine whether clients are allowed to connect to the Client VPN endpoint. If authentication succeeds, clients connect to the Client VPN endpoint and establish a VPN session. If authentication fails, the connection is denied and the client is prevented from establishing a VPN session.

Client VPN offers the following types of client authentication:
+ [Active Directory authentication](ad.md) (user-based)
+ [Mutual authentication](mutual.md) (certificate-based)
+ [Single sign-on (SAML-based federated authentication)](federated-authentication.md) (user-based)

You can use one of the preceding methods alone, or you can use a combination of mutual authentication with a user-based method such as the following:
+ Mutual authentication and federated authentication
+ Mutual authentication and Active Directory authentication

**Important**
To create a Client VPN endpoint, you must provision a server certificate in AWS Certificate Manager, regardless of the type of authentication that you use. For more information about creating and provisioning a server certificate, see the steps in [Mutual authentication in AWS Client VPN](mutual.md).
If you use a combination of mutual authentication and user-based authentication, both methods must then be used to correctly authenticate in VPN.
