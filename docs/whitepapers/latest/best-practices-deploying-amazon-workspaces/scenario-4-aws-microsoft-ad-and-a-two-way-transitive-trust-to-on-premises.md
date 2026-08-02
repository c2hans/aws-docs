---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/scenario-4-aws-microsoft-ad-and-a-two-way-transitive-trust-to-on-premises.html
---

# Scenario 4: AWS Microsoft AD and a two-way transitive trust to on-premises
<a name="scenario-4-aws-microsoft-ad-and-a-two-way-transitive-trust-to-on-premises"></a>

 This scenario, shown in the following figure, has AWS Managed AD deployed in the AWS Cloud, which has a two-way transitive trust to the customer on-premises AD. Users and WorkSpaces are created in the Managed AD, with the AD trust enabling resources to be accessed in the on-premises environment.

![Sample architecture showing AWS Managed AD deployed in the AWS Cloud, which has a two-way transitive trust to the customer on-premises AD.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/cloud-only-transitive-trust.png)

 As in scenario 3, the AD DS (Microsoft AD) is deployed into dedicated subnets that span two AZs, making AD DS highly available in the AWS Cloud.

 This scenario works well for customers who want to have a fully managed AWS Directory Service, including deployment, patching, high availability, and monitoring of their AWS Cloud. This scenario also allows WorkSpaces users to access AD-joined resources on their existing networks. This scenario requires a domain trust to be in place. Security groups and firewall rules need to allow communication between the two active directories.

 In addition to the placement of AWS Directory Service, the previous figure oulines the flow of traffic from a user to a workspace, and how the workspace interacts with the AD server and MFA server.

 This architecture uses the following components or construct.

## AWS
<a name="aws-3"></a>
+  **Amazon VPC** — Creation of an Amazon VPC with at least four private subnets across two AZs — two for AD DS [Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html), two for AD Connector or WorkSpaces.
+  **DHCP options set** — Creation of an Amazon VPC DHCP options set. This enables a customer to define a specified domain name and DNS (Microsoft AD). For more information, refer to [DHCP options sets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html).
+  **Optional: Amazon virtual private gateway** — Enable communication with a customer-owned network over an IPsec VPN tunnel (VPN) or AWS Direct Connect connection. Use for accessing on-premises back-end systems.
+  **AWS Directory Service** — Microsoft AD deployed into a dedicated pair of VPC subnets (AD DS Managed Service).
+  **Amazon EC2** — Customer *optional* RADIUS Servers for MFA.
+  **Amazon WorkSpaces** — WorkSpaces are deployed into the same private subnets as the AD Connector. For more information, refer to the [Active Directory: Sites and Services](design-considerations.md#active-directory-sites-and-services) section of this document.

## Customer
<a name="customer-3"></a>
+  **Network Connectivity** — Corporate VPN or AWS Direct Connect endpoints.
+  **End user devices** — Corporate or BYOL end-user devices (such as Windows, Macs, iPads, Android tablets, zero clients, and Chromebooks) used to access the Amazon WorkSpaces service. Refer to the [list of client applications for supported devices and web browsers](https://docs.aws.amazon.com/workspaces/latest/userguide/workspaces-user-getting-started.html#choose-client).

 This solution requires connectivity to the customer on-premises data center to allow the trust process to operate. If WorkSpaces users are using resources on the on-premises network, then latency and outbound data transfer costs need to be considered.
