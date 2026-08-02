---
source_url: https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/terminology-and-definitions.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Terminology and definitions
<a name="terminology-and-definitions"></a>

 **AWS Managed Microsoft Active Directory**. AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, is Microsoft Windows Server Active Directory Domain Services (AD DS) deployed and managed by AWS for you. The service runs on actual Windows Server for the highest possible fidelity and provides the most complete implementation of AD DS functionality of cloud-managed AD DS services available today.

 **Active Directory Connector (AD Connector)** is a directory gateway (proxy) that redirects directory requests from AWS applications and services to existing Microsoft Active Directory without caching any information in the cloud. It does not require any trusts or synchronization of users.

 **Active Directory Trust**. A trust relationship (also called a trust) is a logical relationship established between domains to allow authentication and authorization to shared resources. The authentication process verifies the identity of the user. The authorization process determines what the user is permitted to do on a computer system or network.

 **Active Directory Sites and Services.** In Active Directory, a site represents a physical or logical entity that is defined on the domain controller. Each site is associated with an Active Directory domain. Each site also has IP definitions for what IP addresses and ranges belong to that site. Domain controllers use site information to inform Active Directory clients about domain controllers present within the closest site to the client.

 **Amazon Virtual Private Cloud (**Amazon VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including the selection of your own private IP address ranges, creation of subnets, and configuration of route tables and network gateways. You can also create a hardware Virtual Private Network (VPN) connection between your corporate data center and your VPC to leverage the AWS Cloud as an extension of your corporate data center.

 **AWS Direct Connect** is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS. Using AWS Direct Connect, you can establish private connectivity between AWS and your data center, office, or colocation environment.

 **AWS IAM Identity Center** is a cloud SSO service that makes it easy to centrally manage SSO access to multiple AWS accounts and business applications. With IAM Identity Center, you can easily manage SSO access and user permissions to all of your accounts in AWS Organizations centrally.

 **AWS Transit Gateway** is a service that enables customers to connect their VPCs and their on-premises networks to a single gateway.

 Domain controller (DC) – an Active Directory server that responds to authentication requests and store a replica of Active Directory database.

 **Flexible Single Master Operation (FSMO)** roles. In Active Directory, some critical updates are performed by a designated domain controller with a specific role and then replicated to all other DCs. Active Directory uses roles that are assigned to DCs for these special tasks. Refer to the Microsoft documentation web-site for [more information on FSMO roles](https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/fsmo-roles).

 **Global Catalog.** A global catalog server is a domain controller that stores partial copies of all Active Directory objects in the forest. It stores a complete copy of all objects in the directory of your domain and a partial copy of all objects of all other forest domains.

 **Read Only Domain Controller (RODC**). Read-only domain controllers (RODCs) hold a copy of the AD DS database and respond to authentication requests, but applications or other servers cannot write to them. RODCs are typically deployed in locations where physical security cannot be provided.

 **VPC Peering.** A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them using private IPv4 or IPv6 addresses. Instances in either VPC can communicate with each other as if they are within the same network.
