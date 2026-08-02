---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rule-authorize-add.html
---

# Add an authorization rule to an AWS Client VPN endpoint
<a name="cvpn-working-rule-authorize-add"></a>

You can add an authorization rule to grant or restrict access to a Client VPN endpoint by using the AWS Management Console. An authorization rule can be added to a Client VPN endpoint using either the Amazon VPC Console or by using the command line or API.

**To add an authorization rule to a Client VPN endpoint using AWS Management Console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to which to add the authorization rule, choose **Authorization rules**, and choose **Add authorization rule**.

1. For **Destination network to enable access**, enter the IP address, in CIDR notation, of the network that you want users to access (for example, the CIDR block of your VPC).

1. Specify which clients are allowed to access the specified network. For **For grant access to**, do one of the following:
   + To grant access to all clients, choose **Allow access to all users**.
   + To restrict access to specific clients, choose **Allow access to users in a specific access group**, and then for **Access group ID**, enter the ID for the group to grant access to. For example, the security identifier (SID) of an Active Directory group, or the ID/name of a group defined in a SAML-based identity provider (IdP).
     + (Active Directory) To get the SID, you can use the Microsoft Powershell [Get-ADGroup](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup) cmdlet, for example:

       ```
       Get-ADGroup -Filter 'Name -eq "<{{Name of the AD Group}}>"'
       ```

       Alternatively, open the Active Directory Users and Computers tool, view the properties for the group, go to the Attribute Editor tab, and get the value for `objectSID`. If necessary, first choose **View**, **Advanced Features** to enable the Attribute Editor tab.
     + (SAML-based federated authentication) The group ID/name should match the group attribute information that is returned in the SAML assertion.

1. For **Description**, enter a brief description of the authorization rule.

1. Choose **Add authorization rule**.

**To add an authorization rule to a Client VPN endpoint (AWS CLI)**
Use the [authorize-client-vpn-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-client-vpn-ingress.html) command.
