---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-login-banner.html
---

# AWS Client VPN client login banners
<a name="cvpn-working-login-banner"></a>

AWS Client VPN provides the option to display a text banner on AWS provided Client VPN desktop applications when a VPN session is established. You can define the contents of the text banner to meet your regulatory and compliance needs. A maximum of 1400 UTF-8 encoded characters can be used.

**Note**
When a client login banner has been enabled, it will be displayed on newly created VPN sessions only. Existing VPN sessions are not interrupted, though the banner will be displayed when an existing session is re-established.

## Banner creation
<a name="configure-login-banner-endpoint-creation"></a>

Login banners are initially created and enabled during the creation of the Client VPN endpoint. For the steps to enable a client login banner during creation of a Client VPN endpoint, see [Create an AWS Client VPN endpoint](cvpn-working-endpoint-create.md).

**Topics**
+ [Banner creation](#configure-login-banner-endpoint-creation)
+ [Configure a client login banner for an existing endpoint](configure-login-banner-existing-endpoint.md)
+ [Deactivate a client login banner for an endpoint](disable-login-banner.md)
+ [Modify existing banner text](modify-banner-text.md)
+ [View a currently configured login banner](display-login-banner.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
