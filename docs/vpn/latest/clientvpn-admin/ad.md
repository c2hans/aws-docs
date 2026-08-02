---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/ad.html
---

# Active Directory authentication in Client VPN
<a name="ad"></a>

Client VPN provides Active Directory support by integrating with Directory Service. With Active Directory authentication, clients are authenticated against existing Active Directory groups. Using Directory Service, Client VPN can connect to existing Active Directories provisioned in AWS or in your on-premises network. This allows you to use your existing client authentication infrastructure. If you are using an on-premises Active Directory and you do not have an existing AWS Managed Microsoft AD, you must configure an Active Directory Connector (AD Connector). You can use one Active Directory server to authenticate the users. For more information about Active Directory integration, see the [AWS Directory Service Administration Guide](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/).

Client VPN supports multi-factor authentication (MFA) when it's enabled for AWS Managed Microsoft AD or AD Connector. If MFA is enabled, clients must enter a user name, password, and MFA code when they connect to a Client VPN endpoint. For more information about enabling MFA, see [Enable Multi-Factor Authentication for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html) and [Enable Multi-Factor Authentication for AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_mfa.html) in the *AWS Directory Service Administration Guide*.

For quotas and rules for configuring users and groups in Active Directory, see [Users and groups quotas](limits.md#quotas-users-groups).
