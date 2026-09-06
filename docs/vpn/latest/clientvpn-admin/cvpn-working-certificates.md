---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates.html
---

# AWS Client VPN client certificate revocation lists
<a name="cvpn-working-certificates"></a>

Client VPN client certificate revocation lists are used to revoke access to a Client VPN endpoint for specific client certificates. You can either generate a revocation list or import an existing list. You can also export your current list a revocation list file. Generating a list is performed using the OpenVPN software on either Linux/macOS or on Windows. Importing and exporting can be done using either the Amazon VPC Console or by using the AWS CLI.

For more information about generating the server and client certificates and keys, see [Mutual authentication in AWS Client VPN](mutual.md)

**Note**
If a client certificate revocation list has expired, you cannot connect to the Client VPN endpoint. You'll need to create a new one and import it into the Client VPN endpoint.

You can add only a limited number of entries to a client certificate revocation list. For more information about the number of entries you can add to a revocation list, see [Client VPN quotas](limits.md#quotas-endpoints).

**Topics**
+ [Generate a client certificate revocation list](cvpn-working-certificates-generate.md)
+ [Import a client certificate revocation list](cvpn-working-certificates-import.md)
+ [Export a client certificate revocation list](cvpn-working-certificates-export.md)
