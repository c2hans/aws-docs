---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/ad-connector-role-with-workspaces.html
---

# The Role of the AWS AD Connector with Amazon WorkSpaces
<a name="ad-connector-role-with-workspaces"></a>

The [AWS AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html) is an AWS Directory Service that acts as a proxy service for an Active Directory. It does not store or cache any user credentials, but forwards authentication or lookup requests to your Active Directory—on-premises or on AWS. Unless you are using AWS Managed Microsoft AD, it is also the only way to register your Active Directory (on-premises or extended to AWS) for use with Amazon WorkSpaces (WorkSpaces).

An AD Connector can point to your on-premises Active Directory, to an Active Directory extended to AWS (AD Domain Controllers on Amazon EC2), or to an AWS Managed Microsoft AD.

The AD Connector plays an important role with most of the deployment scenarios covered in the following sections. Using the AD Connector with WorkSpaces provides a number of benefits:
+ When pointed to your corporate Active Directory, it allows your users to use their existing corporate credentials to log on to WorkSpaces and other services, such as [Amazon WorkDocs](https://aws.amazon.com/workdocs/).
+ You can consistently apply existing security policies (password expiration, account lockouts, etc.) whether your users are accessing resources in your on-premises infrastructure or in the AWS Cloud, such as WorkSpaces.
+ The AD Connector enables a simple integration with your existing RADIUS-based MFA infrastructure to provide an additional layer of security.
+ It enables segregation of your users. For example, it allows the configuration of a number of WorkSpaces options per business unit or persona, since multiple AD Connectors can be pointing to the same Domain Controllers (DNS servers) of Active Directory for user authentication:
  + Target Domain or Organizational Unit for targeted application of Active Directory Group Policy Objects (GPOs)
  + Different Security Groups to control traffic flow to/from WorkSpaces
  + Different Access Control Options (allowed client devices) and IP Access Control Groups (limit access to IP ranges)
  + Selective enabling of Local Administrator Permissions
  + Different Self-Service Permissions
  + Selective enforcement of Multi-Factor Authentication (MFA)
  + Placement of your WorkSpaces Elastic Network Interfaces (ENI) into different VPCs or Subnets for isolation

Multiple AD Connectors also allow to support a larger number of users, if you are hitting the performance limit of a single small or large AD Connector. Please refer to the [Sizing of AWS Managed Microsoft AD](#sizing-aws-managed-microsoft-ad) section for more detail.

The use of AD Connectors with WorkSpaces is free of charge, as long as you have at least one active WorkSpaces user in a small AD Connector and at least 100 active WorkSpaces users in a large AD Connector. For more information, see the [AWS Directory Services Pricing](https://aws.amazon.com/directoryservice/pricing/) page.

## The Importance of Your Network Link to AWS With an On-Premises Active Directory
<a name="network-link-to-aws-with-on-premises-ad"></a>

WorkSpaces relies on connectivity to your Active Directory. Hence, the availability of the network link to your Active Directory is of utmost importance. For example, if your network link in [ Scenario 1](scenario-1-using-ad-connector-to-proxy-authentication-to-on-premises-active-directory-service.md) is down, your users won’t be able to authenticate, and as a result won’t be able to use their WorkSpaces.

If an on-premises Active Directory is to be used as part of the scenario, you’ll need to consider resiliency, latency, and traffic cost of your network link to AWS. In a multi-region WorkSpaces deployment, this may involve multiple network links in different AWS Regions, or multiple AWS Transit Gateways with peering established between them to route your AD traffic to the VPC with connectivity to your on-premises AD. These network link considerations apply to most of the scenarios outlined in the following sections, but are especially important for those scenarios where your AD traffic from AD Connectors and WorkSpaces needs to traverse the network link to reach your on-premise Active Directory. [ Scenario 1](scenario-1-using-ad-connector-to-proxy-authentication-to-on-premises-active-directory-service.md) highlights some of the caveats.

## Using Multi-Factor Authentication with WorkSpaces
<a name="multi-factor-auth-with-workspaces"></a>

If you plan to use Multi-Factor Authentication (MFA) with WorkSpaces, you must use an AWS AD Connector or an AWS Managed Microsoft AD, since only these services allow registration of the directory for use with WorkSpaces and configuration of RADIUS. For the placement of your RADIUS servers, the network link considerations covered in the [The Importance of Your Network Link to AWS With an On-Premises Active Directory](#network-link-to-aws-with-on-premises-ad) section apply.

## Separating Account and Resource Domain
<a name="separating-account-and-resource-domain"></a>

For security reasons or for better manageability, it might be desirable to separate the Account Domain from the Resource Domain. For example, place the WorkSpaces Computer Objects into a separate Resource Domain, while the Users are part of the Account Domain. An implementation like this can be used to allow a partner organization to manage the WorkSpaces using AD Group Policies in the Resource Domain, while not relinquishing control or granting access to the Account Domain. This can be accomplished by using two Active Directories with a configured Active Directory Trust. The following sections cover this in more detail:
+ [Scenario 4: AWS Microsoft AD and a two-way transitive trust to on-premises](scenario-4-aws-microsoft-ad-and-a-two-way-transitive-trust-to-on-premises.md)
+ [Scenario 6: AWS Microsoft AD, shared services VPC, and a one-way trust to on-premises](scenario-6-aws-microsoft-ad-shared-services-vpc-and-a-one-way-trust-to-on-premises.md)

## Large Active Directory Deployments
<a name="large-ad-deployments"></a>

You must ensure that Active Directory Sites & Services is configured accordingly. This is especially important if your Active Directory consists of a large number of domain controllers in different geographical locations. Your Windows WorkSpaces use the [standard Microsoft mechanism](https://social.technet.microsoft.com/wiki/contents/articles/24457.how-domain-controllers-are-located-in-windows.aspx) to discover their domain controller for the Active Directory Site they’re assigned to. This DC Locator process relies on DNS and may be significantly prolonged in case a lengthy list of domain controllers with unspecific priority and weight is returned at the early stage of the DC Locator process. More importantly, if your WorkSpaces get “pinned“ to a sub-optimal domain controller, all subsequent communication with this domain controller may suffer from increased network latency and reduced bandwidth when traversing wide area network links. This will slow down any communication with the domain controller, including processing of a potentially large number of Group Policy Objects (GPOs), and file transfers from the domain controller. Depending on the network topology, it may also increase your networking cost, because the data exchanged between WorkSpaces and domain controllers might unnecessarily traverse a costlier network path. Refer to the [VPC design](design-considerations.md) and [Design considerations](design-considerations.md) sections for guidance on DHCP and DNS with your VPC design, and Active Directory Sites & Services.

## Using Microsoft Azure Active Directory or Active Directory Domain Services with WorkSpaces
<a name="using-ms-azure-ad-adds-with-workspaces"></a>

If you intend to use Microsoft Azure Active Directory with WorkSpaces, you might use Azure AD Connect to synchronize your identity with your on-premises Active Directory or with your Active Directory on AWS (Domain Controller on Amazon EC2 or AWS Managed Microsoft AD). However, this will not allow you to join WorkSpaces to your Azure Active Directory. For more information, see the [ Microsoft Hybrid Identity Documentation](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/) in the *Microsoft Azure Documentation*.

If you want to join your WorkSpaces to your Azure Active Directory, you will need to deploy Microsoft Azure Active Directory Domain Services (Azure AD DS), establish connectivity between AWS and Azure, and use an AWS AD Connector pointing to your Azure AD DS Domain Controllers. For more information about how to set this up, see the [ Add your WorkSpaces to Azure AD using Azure Active Directory Domain Services](https://aws.amazon.com/blogs/desktop-and-application-streaming/add-your-workspaces-to-azure-ad-using-azure-active-directory-domain-services/) blog post.

When using AWS Directory Services with WorkSpaces, you’ll have to consider the size of your WorkSpaces deployment and its expected growth in order to size the AWS Directory Service appropriately. This section provides guidance on sizing the AWS Directory Service for use with WorkSpaces. We also recommend you review the [Best practices for AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_best_practices.html) and the [Best practices for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_best_practices.html) sections in the *AWS Directory Service Administration Guide*.

## Sizing of AD Connector with WorkSpaces
<a name="sizing-ad-connector-with-workspaces"></a>

The Active Directory Connector (AD Connector) is available in two sizes, Small and Large. While there are no enforced user or connection limits, we recommend to use a small AD Connector for up to 500 WorkSpaces entitled users, and a large AD Connector for up to 5000 WorkSpaces entitled users. You can spread application loads across multiple AD Connector to scale to your performance needs. For example, if you need to support 1500 WorkSpaces users, you may spread your WorkSpaces equally across three small AD Connector, each supporting 500 users. If all of your users reside in the same Domain, the AD Connector can all point to the same set of DNS Servers resolving your Active Directory Domain.

Note, if you started with a small AD Connector, and your WorkSpaces deployment grows over time, you can raise a support ticket to have the size of your AD Connector changed from small to large in order to handle the larger number of WorkSpaces entitled users.

## Sizing of AWS Managed Microsoft AD
<a name="sizing-aws-managed-microsoft-ad"></a>

[AWS Managed Microsoft AD](https://aws.amazon.com/directoryservice/active-directory/) lets you run Microsoft Active Directory as a managed service. You can choose between Standard Edition and Enterprise Edition when you launch the service. The Standard Edition is recommended for small and midsize business with up to 5,000 users, and supports up to roughly 30,000 directory objects, such as users, groups, and computers. The Enterprise Edition is designed to support up to 500,000 directory objects and also offers an additional feature, such as [multi-Region replication](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_configure_multi_region_replication.html).

If you need to support more than 500,000 directory objects, consider deploying Microsoft Active Directory Domain Controllers on Amazon EC2. For the sizing of these Domain Controllers refer to Microsoft’s [Capacity planning for Active Directory Domain Services](https://docs.microsoft.com/en-us/windows-server/administration/performance-tuning/role/active-directory-server/capacity-planning-for-active-directory-domain-services) document.
