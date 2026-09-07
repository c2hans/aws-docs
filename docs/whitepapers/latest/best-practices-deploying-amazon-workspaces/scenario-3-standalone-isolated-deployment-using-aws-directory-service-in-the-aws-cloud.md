---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/scenario-3-standalone-isolated-deployment-using-aws-directory-service-in-the-aws-cloud.html
---

# Scenario 3: Standalone isolated deployment using AWS Directory Service in the AWS Cloud
<a name="scenario-3-standalone-isolated-deployment-using-aws-directory-service-in-the-aws-cloud"></a>

 This scenario, shown in the following figure, has AD DS deployed in the AWS Cloud in a standalone isolated environment. AWS Directory Service is used exclusively in this scenario. Instead of fully managing AD DS, customers can rely on AWS Directory Service for tasks such as building a highly available directory topology, monitoring domain controllers, and configuring backups and snapshots.

![Sample architecture showing AD DS deployed in the AWS Cloud in a standalone isolated environment.](https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/cloud-only-ad-microsoft.png)

 As in scenario 2, the AD DS (Microsoft AD) is deployed into dedicated subnets that span two AZs, making AD DS highly available in the AWS Cloud. In addition to Microsoft AD, AD Connector (in all three scenarios) is deployed for WorkSpaces authentication or MFA. This ensures separation of roles or functions within the Amazon VPC, which is a standard best practice. For more information, refer to the [Design Considerations](using-multi-region-aws-managed-active-directory-with-amazon-workspaces.md) section of this document.

 Scenario 3 is a standard, all-in configuration that works well for customers who want to have AWS manage the deployment, patching, high availability, and monitoring of the AWS Directory Service. The scenario also works well for proof of concepts, lab, and production environments because of its isolation mode.

 In addition to the placement of AWS Directory Service, this figure shows the flow of traffic from a user to a workspace and how the workspace interacts with the AD server and MFA server.

 This architecture uses the following components or constructs.

## AWS
<a name="aws-2"></a>
+  **Amazon VPC** — Creation of an Amazon VPC with at least four private subnets across two AZs — two for AD DS [Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html), two for AD Connector or WorkSpaces.
+  **DHCP options set** — Creation of an Amazon VPC DHCP options set. This allows a customer to define a specified domain name and DNS (Microsoft AD). For more information, refer to [DHCP options sets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html).
+  **Optional: Amazon virtual private gateway** — Enable communication with a customer-owned network over an IPsec VPN tunnel (VPN) or AWS Direct Connect connection. Use for accessing on-premises back-end systems.
+  **AWS Directory Service** — Microsoft AD deployed into a dedicated pair of VPC subnets (AD DS Managed Service).
+  **Amazon EC2** — Customer “Optional” RADIUS Servers for MFA.
+  **AWS Directory Services** — AD Connector is deployed into a pair of Amazon VPC private subnets.
+  **Amazon WorkSpaces** — WorkSpaces are deployed into the same private subnets as the AD Connector. For more information, refer to the [Active Directory: Sites and Services](design-considerations.md#active-directory-sites-and-services) section of this document.

## Customer
<a name="customer-2"></a>
+  **Optional: Network Connectivity** — Corporate VPN or AWS Direct Connect endpoints.
+  **End user devices** — Corporate or BYOL end-user devices (such as Windows, Macs, iPads, Android tablets, zero clients, and Chromebooks) used to access the Amazon WorkSpaces service. Refer to [this list of client applications for supported devices and web browsers](https://docs.aws.amazon.com/workspaces/latest/userguide/workspaces-user-getting-started.html#choose-client).

 Like scenario 2, this scenario doesn’t have issues with reliance on connectivity to the customer on-premises data center, latency, or data out transfer costs (except where internet access is enabled for WorkSpaces within the VPC) because, by design, this is an isolated or cloud-only scenario.
