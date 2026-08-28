---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-export.html
---

# AWS Client VPN endpoint configuration file export
<a name="cvpn-working-endpoint-export"></a>

The AWS Client VPN endpoint configuration file is the file that clients (users) use to establish a VPN connection with the Client VPN endpoint. You must download (export) this file and distribute it to all clients who need access to the VPN. Alternatively, if you enabled the self-service portal for your Client VPN endpoint, clients can log into the portal and download the configuration file themselves. For more information, see [AWS Client VPN access to the self-service portal](cvpn-self-service-portal.md).

If your Client VPN endpoint uses mutual authentication, you must [add the client certificate and the client private key to the .ovpn configuration file](add-config-file-cert-key.md) that you download. After you add the information, clients can import the .ovpn file into the OpenVPN client software.

**Important**
If you do not add the client certificate and the client private key information to the file, clients that authenticate using mutual authentication cannot connect to the Client VPN endpoint.

By default, the “remote-random-hostname” option in the OpenVPN client configuration enables wildcard DNS. Because wildcard DNS is enabled, the client does not cache the IP address of the endpoint and you will not be able to ping the DNS name of the endpoint.

If your Client VPN endpoint uses Active Directory authentication and if you enable multi-factor authentication (MFA) on your directory after you distribute the client configuration file, you must download a new file and redistribute it to your clients. Clients cannot use the previous configuration file to connect to the Client VPN endpoint.

**Topics**
+ [Export the client configuration file](export-client-config-file.md)
+ [Add the client certificate and key information for mutual authentication](add-config-file-cert-key.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
