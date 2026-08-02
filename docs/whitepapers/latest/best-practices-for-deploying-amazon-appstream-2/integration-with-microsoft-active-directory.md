---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/integration-with-microsoft-active-directory.html
---

# Integration with Microsoft Active Directory
<a name="integration-with-microsoft-active-directory"></a>

 Amazon WorkSpaces Applications Image Builders and fleets can be integrated with Microsoft Active Directory. This enables you to provide a centralized method for user authentication, authorization, and to apply Active Directory Group policies to domain- joined WorkSpaces Applications instances. Using WorkSpaces Applications fleets joined to a domain provides the same administrative benefits an on-premises environment. This includes centralized management of network file shares, user-app entitlements, roaming profiles, printer access, and other policy-based settings.

 When integrating a WorkSpaces Applications environment with Active Directory, it is important to note that the initial authentication to the WorkSpaces Applications stack is still managed by a SAML2.0 IdP. After the user is successfully authenticated to the IdP, when the user launches a session, they must enter their domain password or a smart card authentication for the Active Directory domain.

 When designing the Active Directory Domain Services (ADDS) environment that will be used with WorkSpaces Applications, there are two service options and many deployment scenarios available. Also, ensure that the WorkSpaces Applications networking is reviewed with your Active Directory site topology owner.

## Service options
<a name="service-options"></a>

 Active Directory can also be deployed using [https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) (AD). AWS Managed Microsoft AD is a fully managed service that allows you to run Microsoft Active Directory. Microsoft Active Directory can also be used in a self-hosted environment, running on EC2 or on-premises.

## Deployment scenarios
<a name="deployment-scenarios"></a>

 The following deployment scenarios listed are commonly used and recommended integration options for WorkSpaces Applications with Microsoft Managed AD or a customer’s self-managed Active Directory. All of the architecture diagrams listed below use core Amazon constructs.
+  **Amazon Virtual Private Cloud (VPC)** — Creation of an Amazon VPC dedicated for WorkSpaces Applications services with at least four private subnets spread across four AZs. Two of the private subnets are used for WorkSpaces Applications fleets and Image Builders. The remaining two subnets are used for the domain controllers on EC2 or Microsoft Managed AD).
+  **Dynamic Host Configuration Protocol (DHCP) Options Set** — Provides a standard for passing configuration info to the WorkSpaces Applications fleet and Image Builders that will be provisioned in the VPC. The DHCP Option Set is defined at the VPC level. It enables customers to define a specified domain name and DNS settings that will be used with the WorkSpaces Applications instanced upon being provisioned.
+  **AWS Directory Services** — Amazon Microsoft Managed AD can be deployed into two private subnets that will be used in conjunction with WorkSpaces Applications workloads.
+  **WorkSpaces Applications fleets** — The WorkSpaces Applications fleets or Image Builders are hosted in the AWS Managed VPC. Each WorkSpaces Applications instance has two Elastic Network Interfaces (ENI). The primary interface (`eth0`) is used for management purposes and brokering the end-user connection to the instance through the streaming gateway. The secondary interface (`eth1`) is injected into the customer-VPC and can be used to access other resources in the bespoke VPC or on-premises.

### Scenario 1: Active Directory Domain Services (ADDS) deployed on- premises
<a name="scenario-1-active-directory-domain-services-adds-deployed-on--premises"></a>

 All authentication traffic traverses the VPN or Direct Connect connection from the customer VPC to the customer gateway. The advantage of this scenario is the benefit of using a possibly already deployed AD environment without having to provision additional domain controllers in the customer VPC. The disadvantage is the sole dependency on the VPN or Direct Connect to authenticate and authorize users for the WorkSpaces Applications fleet. If there is any network connectivity issue, the WorkSpaces Applications fleet or Image Builders would be directly impacted. Providing dual VPN tunnels or Direct Connect connections with different paths mitigates this potential risk.

![A diagram of Active Directory Domain Services (ADDS) deployed on-premises](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/images/adds-on-premises.png)

 *Scenario 1 — Active Directory Domain Services (ADDS) deployed on-premises*

### Scenario 2: Extend Active Domain Services (ADDS) into AWS customer VPC
<a name="scenario-2-extend-active-domain-services-adds-into-aws-customer-vpc"></a>

 The Active Directory is extended to your customer VPC. An Active Directory site should be created for the new domain controllers in the customer VPC. The authentication traffic is routed to the domain controllers in the AWS customer VPC instead of traversing the VPN or Direct Connect connection.

![A diagram showing Extend Active Domain Services into AWS customer Virtual Private Cloud](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/images/extend-active-domain.png)

 *Scenario 2 — Extend Active Domain Services into AWS customer Virtual Private Cloud*

### Scenario 3: AWS Managed Microsoft Active Directory
<a name="scenario-3-aws-managed-microsoft-active-directory"></a>

 AWS Managed Microsoft AD is deployed in the AWS Cloud and is used as the identity and resource domain for the WorkSpaces Applications fleets and Image Builders.

![A diagram of the AWS Managed Active Directory](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/images/aws-managed-directory.png)

 *Scenario 3 — AWS Managed Active Directory*

## Active Directory Service Site Topology
<a name="active-directory-service-site-topology"></a>

 An Active Directory service site topology is a logical representation of your physical network.

 A site topology helps you efficiently route client queries and Active Directory replication traffic. A well-designed and maintained site topology helps your organization achieve the following benefits:
+  Minimize the cost of replicating Active Directory data when synchronizing between on-premises and AWS Cloud.
+  Optimize the ability of client computers to locate the nearest resources, such as domain controllers. This helps to reduce network traffic over slow wide area network (WAN) links, improve logon and logoff processes, and speed up resource access operations.

 When introducing WorkSpaces Applications services, ensure that the address ranges used for the WorkSpaces Applications instances’ subnets are assigned to the correct site for your environment.

 For Scenario 1 and Scenario 2, sites and services are critical components for the best user experience in terms of logon times, and time for Active Directory resource access.

 Site topology controls Active Directory replication between domain controllers within the same site and across site boundaries.

 Defining the correct site topology ensures client affinity, meaning that clients (in this case, WorkSpaces Applications streaming instances) use their preferred local domain controller.

![AD diagram of Active Directory sites and services — client affinity](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/images/active-directory-client-affinity.png)

 *Active Directory sites and services — client affinity*

**Tip**
 As a best practice, define high cost for site links between on-premises AD DS and the AWS Cloud. The preceding figure is an example of what costs you should assign to the site links (cost 100) to ensure site-independent client affinity.

 For more information on site topology, refer to [https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology).

## Active Directory Organizational Units
<a name="active-directory-organizational-units"></a>

AWS recommends storing the Organizational Units (OUs) configured in a single WorkSpaces Applications Directory Config object. It is a best practice for each WorkSpaces Applications stack to have its own OU. This allows you the flexibility to have specific GPOs per stack. Ensure that the OUs are dedicated to WorkSpaces Applications computer objects to avoid mixing WorkSpaces Applications-specific policies with on-premises desktops. Consider using sub-OUs for each AWS Region you deploy WorkSpaces Applications into.

## Active Directory computer object cleanup
<a name="active-directory-computer-object-cleanup"></a>

 WorkSpaces Applications instances are ephemeral. A fleet creates and reuses Active Directory computer objects as fleets scale out and scale in.

 AWS recommends creating an AD cleanup process to delete stale Active Directory computer objects that can exist after an WorkSpaces Applications fleet is removed.
