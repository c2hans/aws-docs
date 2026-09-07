---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/scenario-1-using-ad-connector-to-proxy-authentication-to-on-premises-active-directory-service.html
---

# Scenario 1: Using AD connector to proxy authentication to on-premises Active Directory Service
<a name="scenario-1-using-ad-connector-to-proxy-authentication-to-on-premises-active-directory-service"></a>

 This scenario is for customers who don’t want to extend their on-premises AD service into AWS, or where a new deployment of AD DS is not an option. The following figure shows at a high level, each of the components, and the user authentication flow.

![Sample architecture showing at a high-level each component and user authentication flow.](https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/ad-connector-to-onprem.png)

 In this scenario, AWS Directory Service (AD Connector) is used for all user or MFA authentication that is proxied through the AD Connector to the customer on-premises AD DS (detailed in the following figure). For details on the protocols or encryption used for the authentication process, refer to the [Security](security.md) section of this document.

![Sample architecture showing how AD Connector is used for all user or MFA authentication that is proxied through the AD Connector to the customer on-premises AD DS.](https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/user-authentication-auth-gateway.png)

 Scenario 1 shows a hybrid architecture where the customer might already have resources in AWS, as well as resources in an on-premises data center that could be accessed via Amazon WorkSpaces. The customer can leverage their existing on-premises AD DS and RADIUS servers for user and MFA authentication.

 This architecture uses the following components or constructs:

## AWS
<a name="aws"></a>
+  **Amazon VPC** — Creation of an Amazon VPC with at least two private subnets across two AZs.
+  **DHCP Options Set** — Creation of an Amazon VPC DHCP Options Set. This allows customer-specified domain name and domain name servers (DNS) (on-premises services) to be defined. For more information, refer to [DHCP options sets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html).
+  **Amazon Virtual Private Gateway** — Enable communication with your own network over an IPsec VPN tunnel or an AWS Direct Connect connection.
+  **AWS Directory Service** — AD Connector is deployed into a pair of Amazon VPC private subnets.
+  **Amazon WorkSpaces** — WorkSpaces are deployed in the same private subnets as the AD Connector. For more information, refer to the [Active Directory: Sites and Services](design-considerations.md#active-directory-sites-and-services) section of this document.

## Customer
<a name="customer"></a>
+  **Network connectivity** — Corporate VPN or Direct Connect endpoints.
+  **AD DS** — Corporate AD DS.
+  **MFA (optional)** — Corporate RADIUS server.
+  **End user devices** — Corporate or bring your own license (BYOL) end user devices (such as Windows, Macs, iPads, Android tablets, zero clients, and Chromebooks) used to access the Amazon WorkSpaces service. Refer to [this list of client applications for supported devices and web browsers](https://docs.aws.amazon.com/workspaces/latest/userguide/workspaces-user-getting-started.html#choose-client).

 Although this solution is great for customers who don’t want to deploy AD DS into the cloud, it does come with some caveats:
+  **Reliance on connectivity** — If connectivity to the data center is lost, users cannot log in to their respective WorkSpaces, and existing connections will remain active for the Kerberos/Ticket-Granting Ticket (TGT) lifetime.
+  **Latency** — If latency exists via the connection (this is more the case with VPN than Direct Connect), then WorkSpaces authentication and any AD DS-related activity, such as Group Policy (GPO) enforcement, will take more time.
+  **Traffic costs** — All authentication must traverse the VPN or Direct Connect link, and so it depends on the connection type. This is either Data Transfer Out from Amazon EC2 to internet or Data Transfer Out (Direct Connect).

**Note**
 AD Connector is a proxy service. It doesn’t store or cache user credentials. Instead, all authentication, lookup, and management requests are handled by your AD. An account with delegation privileges is required in your directory service with rights to read all user information and join a computer to the domain.

 In general, the WorkSpaces experience is highly dependent on the Active Directory authentication process shown in the previous figure. For this scenario, the WorkSpaces authentication experience is highly dependent on the network link between the customer AD and the WorkSpaces VPC. The customer should ensure the link is highly available.
