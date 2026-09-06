---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/scenario-5-aws-microsoft-ad-using-a-shared-services-virtual-private-cloud-vpc.html
---

# Scenario 5: AWS Microsoft AD using a shared services Virtual Private Cloud (VPC)
<a name="scenario-5-aws-microsoft-ad-using-a-shared-services-virtual-private-cloud-vpc"></a>

 This scenario, shown in the following figure, has an AWS Managed AD deployed in the AWS Cloud, providing authentication services for workloads that are either already hosted in AWS or are planned to be as part of a broader migration. The best practice recommendation is to have Amazon WorkSpaces in a dedicated VPC. Customers should also create a specific AD OU to organize the WorkSpaces computer objects.

 To deploy WorkSpaces with a shared services VPC hosting Managed AD, deploy an AD Connector (ADC) with an ADC service account created in the Managed AD. The service account requires permissions to create computer objects in the WorkSpaces designated OU in the shared services Managed AD.

![Sample architecture showing a WorkSpaces with a shared services VPC hosting Managed AD, deploy an AD Connector.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/microsoft-ad-shared-services-vpc.png)

 This architecture uses the following components or constructs.

## AWS
<a name="aws-4"></a>
+  **Amazon VPC** — Creation of an Amazon VPC with at least two private subnets across two AZs (two for AD Connector and WorkSpaces).
+  **DHCP options set** — Creation of an Amazon VPC DHCP options set. This allows a customer to define a specified domain name and DNS (Microsoft AD). For more information, refer to [DHCP options sets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html).
+  **Optional: Amazon virtual private gateway** — Enable communication with a customer-owned network over an IPsec VPN tunnel (VPN) or AWS Direct Connect connection. Use for accessing on-premises back-end systems.
+  **AWS Directory Service** — Microsoft AD deployed into a dedicated pair of VPC subnets (AD DS Managed Service), AD Connector
+  **AWS Transit Gateway/VPC Peering** — Enable connectivity between Workspaces VPC and the Shared Services VPC
+  **Amazon EC2** — Customer *optional* RADIUS Servers for MFA.
+  **Amazon WorkSpaces** — WorkSpaces are deployed into the same private subnets as the AD Connector. For more information, refer to the [Active Directory: Sites and Services](design-considerations.md#active-directory-sites-and-services) section of this document.

## Customer
<a name="customer-4"></a>
+  **Network Connectivity** — Corporate VPN or AWS Direct Connect endpoints.
+  **End user devices** — Corporate or BYOL end-user devices (such as Windows, Macs, iPads, Android tablets, zero clients, and Chromebooks) used to access the Amazon WorkSpaces service. Refer to the [list of client applications for supported devices and web browsers](https://docs.aws.amazon.com/workspaces/latest/userguide/workspaces-user-getting-started.html#choose-client).
