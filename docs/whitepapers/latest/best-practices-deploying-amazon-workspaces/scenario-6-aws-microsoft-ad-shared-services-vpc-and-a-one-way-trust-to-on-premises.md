---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/scenario-6-aws-microsoft-ad-shared-services-vpc-and-a-one-way-trust-to-on-premises.html
---

# Scenario 6: AWS Microsoft AD, shared services VPC, and a one-way trust to on-premises
<a name="scenario-6-aws-microsoft-ad-shared-services-vpc-and-a-one-way-trust-to-on-premises"></a>

This scenario, as shown in the following figure, uses an existing on-premises Active Directory for users, and introduces a separate Managed Active Directory in AWS Cloud to host the computer objects associated with the WorkSpaces. This scenario allows the computer objects and Active Directory group policies to be managed independently from the corporate Active Directory.

 This scenario is useful when a third party wants to manage Windows WorkSpaces on a customer’s behalf as it allows the third party to define and control the WorkSpaces and policies associated with them, without a need to grant the third-party access to the customer AD. In this scenario, a specific Active Directory organizational unit (OU) is created to organize the WorkSpaces computer objects in the Shared Services AD.

**Note**
 Amazon Linux WorkSpaces require a two-way trust to be in place for them to be created.

To deploy Windows WorkSpaces with the computer objects created in the Shared Services VPC hosting Managed Active Directory using users from the customer identity domain, deploy an Active Directory Connector (ADC) referencing the corporate AD. Use an ADC service account created in the corporate AD (identity domain) that has delegated permissions to create computer objects in the Organizational Unit (OU) that was configured for the Windows WorkSpaces in the Shared Services Managed AD, and that has read permissions to the corporate Active Directory (identity domain).

 To ensure the Domain Locator function is able to authenticate WorkSpaces users in the desired AD Site for the identity domain, name both domain’s AD Sites for the Amazon WorkSpaces Subnets identically as per [Microsoft’s documentation](https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/domain-locator-across-a-forest-trust/ba-p/395689). It is a best practice to have both identity domain and Shared Services domain AD Domain Controllers in the same AWS Region as Amazon WorkSpaces.

 For detailed instructions to configure this scenario, review the implementation guide to [set up a one-way trust for Amazon WorkSpaces with AWS Directory Services](https://d1.awsstatic.com/Projects/deploy-amazon-workspaces-one-way-trust-with-aws-directory-service.pdf)

In this scenario we establish a one-way transitive trust between the AWS Managed Microsoft AD in the Shared Services VPC and the on-premises AD. Figure 11 shows the direction of trust and access, and how the AWS AD Connector uses the AD Connector service account to create computer objects in the resource domain.

A forest trust is used per Microsoft recommendation to ensure that Kerberos authentication is used whenever possible. Your WorkSpaces receive Group Policy Objects (GPOs) from your resource domain in the AWS Managed Microsoft AD. Furthermore, your WorkSpaces perform Kerberos authentication with your identity domain. For this to work reliably it is best practice to extend your identity domain to AWS as already explained above. We suggest to review the [Deploy Amazon WorkSpaces using a One-Way Trust Resource Domain with Directory Service](https://aws.amazon.com/getting-started/hands-on/deploy-workspaces-one-way-trust/) implementation guide for further detail.

Both, the AD Connector and your WorkSpaces, must be able to communicate with the Domain Controllers of your identity domain and your resource domain. For more information, see [IP address and port requirements for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) in the *Amazon WorkSpaces Administration Guide*.

If you use multiple AD Connectors, it is best practice for each of the AD Connectors to use its own AD Connector Service Account.

![ASample architecture showing a Windows WorkSpaces with the computer objects created in the Shared Services VPC hosting Managed Active Directory using users from the customer identity domain.](https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/one-way-trust-ad-onprem.png)

 This architecture uses the following components or constructs:

## AWS
<a name="aws-5"></a>
+  **Amazon VPC** — Creation of an Amazon VPC with at least two private subnets across two AZs — two for AD Connector and WorkSpaces.
+  **DHCP options set** — Creation of an Amazon VPC DHCP options set. This allows a customer to define a specified domain name and DNS (Microsoft AD). For more information, refer to [DHCP options sets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html).
+  **Optional: Amazon virtual private gateway** — Enable communication with a customer-owned network over an IPsec VPN tunnel (VPN) or AWS Direct Connect connection. Use for accessing on-premises back-end systems.
+  **AWS Directory Service** — Microsoft AD deployed into a dedicated pair of VPC subnets (AD DS Managed Service), AD Connector.
+  **Transit Gateway/VPC Peering** — Enable connectivity between Workspaces VPC and the Shared Services VPC.
+  **Amazon EC2** — Customer “Optional” RADIUS Servers for MFA.
+  **Amazon WorkSpaces** — WorkSpaces are deployed into the same private subnets as the AD Connector. For more information, refer to the [Active Directory: Sites and Services](design-considerations.md#active-directory-sites-and-services) section of this document.

## Customer
<a name="customer-5"></a>
+  **Network Connectivity** — Corporate VPN or AWS Direct Connect endpoints.
+  **End user devices** — Corporate or BYOL end-user devices (such as Windows, Macs, iPads, Android tablets, zero clients, and Chromebooks) used to access the Amazon WorkSpaces service. Refer to [this list of client applications for supported devices and web browsers](https://docs.aws.amazon.com/workspaces/latest/userguide/workspaces-user-getting-started.html#choose-client).
