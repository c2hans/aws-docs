---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/design-considerations.html
---

# Design considerations
<a name="design-considerations"></a>

 A functional AD DS deployment in the AWS Cloud requires a good understanding of both Active Directory concepts and specific AWS services. This section discusses key design considerations when deploying AD DS for Amazon WorkSpaces, VPC best practices for AWS Directory Service, DHCP and DNS requirements, AD Connector specifics, and AD sites and services.

## VPC design
<a name="vpc-design-1"></a>

 As previously discussed in the [Network Considerations](network-considerations.md) section of this document and documented earlier for scenarios 2 and 3, customers should deploy AD DS in the AWS Cloud into a dedicated pair of private subnets, across two AZs, and separated from AD Connector or WorkSpaces subnets. This construct provides highly available, low latency access to AD DS services for WorkSpaces, while maintaining standard best practices of separation of roles or functions within the Amazon VPC.

 The following figure shows the separation of AD DS and AD Connector into dedicated private subnets (scenario 3). In this example all services reside in the same Amazon VPC.

![Sample architecture showing the separation of AD DS and AD Connector into dedicated private subnets.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/registering-replicated-mad.png)

 The following figure shows a design similar to scenario 1; however, in this scenario the on-premises portion resides in a dedicated Amazon VPC.

![Sample architecture showing a design similar to scenario 1; however, in this scenario the on-premises portion resides in a dedicated Amazon VPC.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/ad-ds-network-separation.png)

**Note**
 For customers who have an existing AWS deployment where AD DS is being used, it’s recommended that they locate their WorkSpaces in a dedicated VPC, and use VPC peering for AD DS communications.

 In addition to the creation of dedicated private subnets for AD DS, domain controllers and member servers require several Security Group rules to allow traffic for services, such as AD DS replication, user authentication, Windows Time services, and distributed file system (DFS).

**Note**
 Best practice is to restrict the required security group rules to the WorkSpaces private subnets and, in the case of scenario 2, allow for bidirectional AD DS communications on-premises to and from the AWS Cloud, as shown in the following table.

 Table 1 — Bidirectional AD DS communications to and from the AWS Cloud

|  Protocol  |  Port  |  Use  |  Destination  |
| --- | --- | --- | --- |
|  TCP  |  53, 88, 135, 139, 389, <br /> 445, 464, 636  |  Auth (primary)  |  Active Directory (private data center or Amazon EC2) \*  |
|  TCP  |  49152 – 65535  |  RPC High Ports  |  Active Directory (private data center or Amazon EC2) \*\*  |
|  TCP  |  3268-3269  |  Trusts  |  Active Directory (private data center or Amazon EC2) \*  |
|  TCP  |  9389  |  Remote Microsoft Windows PowerShell (optional)  |  Active Directory (private data center or Amazon EC2) \*  |
|  UDP  |  53, 88, 123, 137, 138, <br /> 389, 445, 464  |  Auth (primary)  |  Active Directory (private data center or Amazon EC2) \*  |
|  UDP  |  1812  |  Auth (MFA) (optional)  |  RADIUS (private data center or Amazon EC2) \*  |

 For more information, refer to [Active Directory and Active Directory Domain Services Port Requirements](https://technet.microsoft.com/en-us/library/dd772723(v%3Dws.10).aspx) and [Service overview and network port requirements for Windows](https://support.microsoft.com/en-us/kb/832017)

 For step-by-step guidance for implementing rules, refer to [Adding Rules to a Security Group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#adding-security-group-rule) in the *Amazon Elastic Compute Cloud User Guide*.

### VPC design: DHCP and DNS
<a name="vpc-design-dhcp-and-dns"></a>

 With an Amazon VPC, Dynamic Host Configuration Protocol (DHCP) services are provided by default for your instances. By default, every VPC provides an internal Domain Name System (DNS) server that is accessible via the Classless Inter-Domain Routing (CIDR) \+2 address space, and is assigned to all instances via a default DHCP options set.

 DHCP options sets are used within an Amazon VPC to define scope options, such as the domain name or the name servers that should be handed to customer instances via DHCP. Correct functionality of Windows services within a customer VPC depends on this DHCP scope option. In each of the scenarios defined earlier, customers create and assign their own scope that defines the domain name and name servers. This ensures that domain-joined Windows instances or WorkSpaces are configured to use the AD DNS.

 The following table is an example of a custom set of DHCP scope options that must be created for Amazon WorkSpaces and AWS Directory Services to function correctly.

 Table 2 — Custom set of DHCP scope options

|  Parameter  |  Value  |
| --- | --- |
|  Name tag  |  Creates a tag with key = name and value set to a specific string <br /> Example: example.com  |
|  Domain name  |  example.com  |
|  Domain name servers  |  DNS server address, separated by commas <br /> Example: 192.0.2.10, 192.0.2.21  |
|  NTP servers  |  Leave this field blank  |
|  NetBIOS name servers  |  Enter the same comma separated IPs as per domain name servers <br /> Example: 192.0.2.10, 192.0.2.21  |
|  NetBIOS node type  |  2  |

 For details on creating a custom DHCP option set and associating it with an Amazon VPC, refer to [Working with DHCP options sets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html#DHCPOptionSet) in the *Amazon Virtual Private Cloud User Guide*.

 In scenario 1, the DHCP scope would be the on-premises DNS or AD DS. However, in scenarios 2 or 3, this would be the locally deployed directory service (AD DS on Amazon EC2 or AWS Directory Services: Microsoft AD). It’s recommended that each domain controller that resides in the AWS Cloud be a global catalog and Directory-Integrated DNS server.

## Active Directory: sites and services
<a name="active-directory-sites-and-services"></a>

 For [Scenario 2](scenario-2-extending-on-premises-ad-ds-into-aws-replica.md), sites and services are critical components for the correct function of AD DS. Site topology controls AD replication between domain controllers within the same site and across site boundaries. In scenario 2, at least two sites are present: on-premises, and the Amazon WorkSpaces in the cloud.

 Defining the correct site topology ensures client affinity, meaning that clients (in this case, WorkSpaces) use their preferred local domain controller.

![Sample architecture showing the client affinity using a local domain controller.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/dedicated-workspaces-vpc.png)

 **Best practice:** Define high cost for site links between on-premises AD DS and the AWS Cloud. The following figure is an example of what costs to assign to the site links (cost 100) to ensure site-independent client affinity.

 These associations help ensure that traffic — such as AD DS replication, and client authentication — uses the most efficient path to a domain controller. In the case of scenarios 2 and 3, this helps ensure lower latency and cross-link traffic.

## Protocol
<a name="protocol"></a>

 Amazon WorkSpaces Streaming Protocol (WSP) is a cloud-native streaming protocol that enables a consistent user experience across global distances and unreliable networks. WSP decouples the protocol from the WorkSpaces by offloading metric analysis, encoding, codec usage and selection. WSP uses port TCP/UDP 4195. When deciding whether or not use the WSP protocol, there are several key questions that should be answered prior to deployment. Please refer to the decision matrix below:

|  Question  |  WSP  |  PCoIP  |
| --- | --- | --- |
|  Will the identified WorkSpaces users need bi-directional audio / video?  |    |   |
|  Will zero clients be used as the remote endpoint (local device)?  |   |    |
|  Will Windows or macOS be used for remote endpoint?  |    |    |
|  Will Ubuntu 18.04 be used for remote endpoint?  |   |    |
|  Will the users access Amazon WorkSpaces via web access?  |   |    |
|  Is pre-session or in-session smartcard support (PIC/CAC) needed?  |    |   |
|  Will WorkSpaces be used in China (Ningxia) Region?  |   |    |
|  Will smart card pre-authentication or in-session support be required?  |    |   |
|  Are the end-users using unreliable, high-latency, or low-bandwidth connections?  |    |   |

The previous questions are critical to determine the protocol that should be used. Additional information on the recommended protocol use cases can be reviewed [here](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-protocols.html). The protocol used can also be changed at a later time using the Amazon WorkSpaces Migrate feature. More information on the use of this feature can be reviewed [here](https://docs.aws.amazon.com/workspaces/latest/adminguide/migrate-workspaces.html).

 When deploying WorkSpaces using WSP, the [WSP Gateways](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html#gateway_WSP) should be added to an allow list to ensure connectivity to the service. Additionally, users connecting to a WorkSpaces using WSP, the round-trip time (RTT) should be under 250ms for best performance. Connections with an RTT between 250ms and 400ms will be degraded. If the user’s connection is consistently degraded, it’s recommended to deploy an Amazon WorkSpaces in a [service-supported region](https://docs.aws.amazon.com/workspaces/latest/adminguide/azs-workspaces.html) closest to the end-user, if possible.

## Multi-Factor Authentication (MFA)
<a name="multi-factor-authentication-mfa"></a>

Implementing MFA requires Amazon WorkSpaces to be configured with either an Active Directory Connector (AD Connector) or AWS Managed Microsoft AD (MAD) as its Directory Service*,* and have a RADIUS server that is network accessible by the Directory Service. Simple Active Directory does not support MFA.

 Refer to the previous section, covering Active Directory and Directory Services Deployment considerations for AD, and RADIUS Design Options within each scenario.

### MFA – Two-Factor Authentication
<a name="mfa-two-factor-authentication"></a>

 After MFA is enabled, users are required to provide their Username, Password, and MFA Code to the WorkSpaces client for authentication to their respective WorkSpaces desktops.

![Screenshot of WorkSpaces console showing MFA enabled](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/workspaces-client-mfa.png)

**Note**
 The AWS Directory Service does not support selective *per user *or contextual MFA: this is a global setting per Directory. If selective “per user” MFA is required, users must be separated by an AD Connector, which can point back to the same source Active Directory.

WorkSpaces MFA requires one or more RADIUS servers. Typically, these are existing solutions you may already have deployed, for example RSA or Gemalto. Alternatively, RADIUS servers can be deployed within your VPC on EC2 Instances (refer to the AD DS Deployment Scenarios section of this document for architectural options). If you are deploying a new RADIUS solution, several implementations exist, such as [FreeRADIUS](https://aws.amazon.com/blogs/desktop-and-application-streaming/integrating-freeradius-mfa-with-amazon-workspaces/), along with SaaS offerings such as [Duo Security](https://www.duosecurity.com/docs/awsworkspaces) or [Okta MFA](https://aws.amazon.com/blogs/desktop-and-application-streaming/integrating-okta-mfa-with-amazon-workspaces/).

 It is best practice to leverage multiple RADIUS servers to ensure that your solution is resilient to failures. When configuring your Directory Service for MFA you are able to enter multiple IP addresses by separating them with a comma (e.g., 192.0.0.0,192.0.0.12). The Directory Services MFA feature will try the first IP address specified and will move to the second IP address in the event network connectivity cannot be established with the first. The configuration of RADIUS for a Highly Available architecture is unique to each solution set, however the over-arching recommendation is to place the underlying instances for your RADIUS capability in different Availability Zones. One configuration example is [Duo Security](https://duo.com/docs/awsworkspaces#high-availability-scenario) and for Okta MFA you are able to deploy multiple Okta RADIUS server agents in the same manner.

 For detailed steps to enable your AWS Directory Service for MFA, refer to [AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_mfa.html) and [AWS Managed Microsoft AD.](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html)

## Disaster Recovery / Business Continuity
<a name="disaster-recovery-business-continuity"></a>

### WorkSpaces Cross-Region Redirection
<a name="workspaces-cross-region-redirection"></a>

Amazon WorkSpaces is a regional service that provides remote desktop access to customers. Depending on business continuity and disaster recovery requirements (BC/DR), some customers require seamless failover to another region where the WorkSpaces service is available. This BC/DR requirement can be accomplished using the WorkSpaces cross-region redirection option. It allows customers to use a fully qualified domain name (FQDN) as their WorkSpaces registration code.

An important consideration is to determine at what point a redirection to a failover region should occur. The criteria for this decision should be based on your company policy, but should include the Recovery Time Objective (RTO) and the Recovery Point Objective (RPO). A Well-Architected WorkSpaces architecture design should include the potential for service failure. The time tolerance for normal business operation recovery will also factor into the decision.

When your end users log in to WorkSpaces with a FQDN as their WorkSpaces registration code, a DNS TXT record is resolved containing a connection identifier determining the registered directory the user will be directed to. The logon landing page of the WorkSpaces client will then be presented based on the registered directory associated with the connection identifier returned. This allows administrators to direct their end users to different WorkSpaces directories based on your DNS policies for the FQDN. This option can be used with public or private DNS zones, assuming the private zones can be resolved from the client machine. Cross-region redirection can be manual or automated. Both of these failovers can be achieved by changing the TXT record containing the connection identifier to be pointed at the desired directory.

While you develop your BC/DR strategy, it is important to consider the user data, since the WorkSpaces cross-region redirection option does not synchronize any user data, nor does it synchronize your WorkSpaces images. Your WorkSpaces deployments in different AWS Regions are independent entities. You will, therefore, have to take additional measures to ensure that your WorkSpaces users can access their data when a redirection to a secondary region occurs. There are many options available for user data replication such as WorkSpaces, Windows FSx (DFS Share), or third party utilities to synchronize data volumes between regions. Likewise, you’ll have to ensure that your secondary region has access to the required WorkSpaces images, for example, by copying the images across regions. For more information, see [Cross-Region Redirection for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html) in the *Amazon WorkSpaces Administration Guide*, and the example in the diagram.

![Image showing WorkSpaces cross-Region redirection with Route 53](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/workspaces-route-53-cross-region-redirection.png)

## WorkSpaces Interface VPC Endpoint (AWS PrivateLink) – API Calls
<a name="workspaces-interface-vpc-endpoint-aws-privatelink-api-calls"></a>

[Amazon WorkSpaces public APIs](https://docs.aws.amazon.com/workspaces/latest/api/API_Operations.html) are supported on [AWS PrivateLink](https://aws.amazon.com/privatelink/). AWS PrivateLink increases the security of data shared with cloud-based applications by reducing the exposure of data to the public internet. WorkSpaces API traffic can be secured inside a VPC by using an [interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html), which is an elastic network interface with a private IP address from the IP address range of your subnet that serves as an entry point for traffic destined to a supported service. This enables you to privately access WorkSpaces API services by using private IP addresses.

 Using PrivateLink with WorkSpaces Public APIs also enables you to securely expose REST APIs to resources only within your VPC or to those connected to your data centers via AWS Direct Connect.

 You can restrict access to selected Amazon VPCs and VPC Endpoints, and enable cross account access using resource-specific policies.

 Ensure that the security group that is associated with the endpoint network interface allows communication between the endpoint network interface and the resources in your VPC that communicate with the service. If the security group restricts inbound HTTPS traffic (port 443) from resources in the VPC, you might not be able to send traffic through the endpoint network interface. An interface endpoint supports TCP traffic only.
+  Endpoints support IPv4 traffic only.
+  When you create an endpoint, you can attach an endpoint policy to it that controls access to the service to which you are connecting.
+  You have a quota on the number of endpoints you can create per VPC.
+  Endpoints are supported within the same region only. You cannot create an endpoint between a VPC and a service in a different region.

**Create Notification to receive alerts on interface endpoint events** — You can create a notification to receive alerts for specific events that occur on your interface endpoint. To create a notification, you must associate an [Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/) with the notification. You can subscribe to the SNS topic to receive an email notification when an endpoint event occurs.

 **Create a VPC Endpoint Policy for Amazon WorkSpaces** — You can create a policy for Amazon VPC endpoints for Amazon WorkSpaces to specify the following:
+  The principal that can perform actions.
+  The actions that can be performed.
+  The resources on which actions can be performed.

**Connect Your Private Network to Your VPC** — To call the Amazon WorkSpaces API through your VPC, you have to connect from an instance that is inside the VPC, or connect your private network to your VPC by using an Amazon Virtual Private Network (VPN) or AWS Direct Connect. For information about Amazon VPN, refer to [VPN connections](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html) in the *Amazon Virtual Private Cloud User Guide*. For information about AWS Direct Connect, refer to [Creating a connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-connection.html) in the *AWS Direct Connect User Guide*.

 For more information about using Amazon WorkSpaces API through a VPC interface endpoint, refer to [Infrastructure Security in Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/infrastructure-security.html).

## Smart card support
<a name="smart-card-support"></a>

Smart card support is available for both Microsoft Windows and Amazon Linux WorkSpaces. Smart card support through Common Access Card (CAC) and Personal Identity Verification (PIV) are exclusively available through Amazon WorkSpaces using WorkSpaces Streaming Protocol (WSP). Smart card support on WSP WorkSpaces offers an increased security posture for authenticating users on organizationally approved connecting endpoints with specific hardware in the form of smart card readers. It is important to first become familiar with the [scope of support available for smart cards](https://docs.aws.amazon.com/workspaces/latest/adminguide/smart-cards.html), and determining how smart cards would function in existing and future WorkSpaces deployments.

 It is a best practice to determine which type of smart card support is required, pre-session authentication or in-session authentication. Pre-session authentication is only available at the time of this writing in [AWS GovCloud (US-West)](https://docs.aws.amazon.com/workspaces/latest/adminguide/smart-cards.html#smart-cards-limitations), [US East (Northern Virginia), US West (Oregon), Europe (Ireland), Asia Pacific (Tokyo), and Asia Pacific (Sydney)](https://aws.amazon.com/about-aws/whats-new/2021/08/aws-directory-service-supports-smart-card-authentication-ad-connector-amazon-workspaces-additional-aws-regions/). In-session smart card authentication is generally available with some considerations, such as:
+  Does your organization possess smart card infrastructure integrated with your Windows Active Directory?
+  Is your Online Certificate Status Protocol (OCSP) Responder public Internet accessible?
+  Are user certificates issued with User Principal Name (UPN) in the Subject Alternative Name (SAN) field?
+  More considerations are detailed for In-session and Pre-session sections.

 Smart card support is enabled through Group Policy. It is a best practice to add the [Amazon WorkSpaces Group Policy administrative template for WSP to the Central Store](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#gp_install_template_wsp) of your Active Directory Domain used by Amazon WorkSpaces Directory(ies). When applying this policy to an existing Amazon WorkSpaces deployment, all WorkSpaces will require the group policy update and a reboot for the change to take effect for all users as it is a computer-based policy.

## Root CA
<a name="root-ca"></a>

The nature of the portability of Amazon WorkSpaces client and user necessitates the requirement to remotely deliver third-party root CA certificate to the trusted root certificate store of each device users use to connect to their Amazon WorkSpaces. AD Domain Controllers and user devices with smart cards must trust the root CAs. Review the [guidelines provided by Microsoft](https://docs.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities) for enabling third-party CAs for more information on the exact requirements.

 In AD domain-joined environments, these devices meet this requirement through Group Policy distributing root CA certificates. In scenarios where Amazon WorkSpaces Client is used from non-domain-joined devices, an alternate delivery method for the third-party root CAs must be determined, such as [Intune](https://docs.microsoft.com/en-us/mem/intune/protect/certificates-pfx-configure).

## In-session
<a name="in-session"></a>

In-session authentication simplifies and secures application authentication after Amazon WorkSpaces user sessions have already started. As mentioned previously, the default behavior for Amazon WorkSpaces disables smart cards and must be enabled through Group Policy. From an Amazon WorkSpaces administration perspective, configuration is specifically required for applications that pass-through authentication (such as web browsers). No changes are required for AD Connectors and Directory(ies).

 Most common applications requiring in-session authentication support are through web browsers such as Mozilla Firefox and Google Chrome. Mozilla Firefox requires [limited configuration for in-session smart card support](https://docs.aws.amazon.com/workspaces/latest/userguide/smart_card_support.html#smart-card-windows-browsers). [Amazon Linux WSP WorkSpaces requires additional configuration](https://docs.aws.amazon.com/workspaces/latest/userguide/smart_card_support.html#smart-card-linux-browsers) for in-session smart card support for both Mozilla Firefox and Google Chrome.

 It is a best practice to ensure the root CAs are loaded in the user’s Personal certificate store before troubleshooting, as the Amazon WorkSpaces Client may not have permissions to the local computer. Additionally, use [OpenSC](https://github.com/OpenSC/OpenSC/wiki#download) to identify smart card devices when troubleshooting any suspected in-session authentication issues with smart cards. Lastly, an Online Certificate Status Protocol (OCSP) Responder is recommended to improve security posture of application authentication through a certificate revocation check.

## Pre-session
<a name="pre-session"></a>

 Support for pre-session authentication requires Windows WorkSpaces Client version 3.1.1 and later, or macOS WorkSpaces client version 3.1.5 and later. Pre-session authentication with smart cards is fundamentally different than standard authentication, requiring the user to authenticate through a combination of both inserting the smart card and entering a PIN code. With this authentication type, the duration of user’s sessions is bounded by the lifetime of the Kerberos ticket. A full installation guide can be found [here](https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/access-workspaces-with-access-cards.html).

![Screenshot showing the pre-session authentication which requires requires Windows WorkSpaces Client version 3.1.1 and later, or macOS WorkSpaces client version 3.1.5 and later.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/pre-session-auth.png)

1.  User opens Amazon WorkSpaces Client, inserts Smart Card, and enters their PIN. The PIN is used by Amazon WorkSpaces Client to decrypt the X.509 Certificate, which is the proxied to the AD Connector through the Authentication Gateway.

1.  AD Connector validates the X.509 Certificate against the publicly accessible OCSP Responder URL specified in the Directory Settings to ensure the certificate has not been revoked.

1.  If the certificate is valid, the Amazon WorkSpaces Client continues the authentication process by prompting the user to enter their PIN a second time to decrypt the X.509 Certificate and proxy to the AD Connector, where it is then matched with the AD Connector’s root and intermediary certificates for validation.

1.  Once the validation of the certificate is successfully matched, Active Directory is used by the AD Connector to authenticate the user and a Kerberos ticket is created.

1.  Kerberos ticket is passed to the user’s Amazon WorkSpace to authenticate and begin the WSP session.

OCSP Responder must be publicly accessible as connection is performed through the AWS Managed network and not the Customer Managed network, therefore there is no routing to private networks in this step.

 Entering the users name is not required as the user certificates presented to AD Connector includes the userPrincipalName (UPN) of the user in the subjectAltName (SAN) field of the certificate. It is a best practice to automate all users that require pre-session authentication with Smartcards have their AD user objects updated to authenticate with anticipated UPN in the certificate using PowerShell, rather than perform this individually in Microsoft Management Consoles.

![Screenshot showing the WorkSpaces sign in console](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/sign-in-console.png)

## Client deployment
<a name="client-deployment"></a>

 The Amazon WorkSpaces Client (version 3.X\+) uses standardized configuration files which can be leveraged by administrators to preconfigure their user’s WorkSpaces Client. The path for the two main configuration files can be found at:

|  OS  |  Configuration File Path  |
| --- | --- |
|  Windows  |  C:\\Users\\USERNAME\\AppData\\Local\\Amazon Web Services\\Amazon WorkSpaces  |
|  macOS  |  /Users/USERNAME/Library/Application Support/Amazon Web Services/Amazon WorkSpaces  |
|  Linux (Ubuntu 18.04)  |  /home/ubuntu/.local/share/Amazon Web Services/Amazon WorkSpaces/  |

Within these paths, you will find the two configuration files. The first configuration file is UserSettings.json, which will set things like current registration, proxy configuration, logging level, and the ability to save the registration list. The second configuration file is RegistrationList.json. This file will contain all of the WorkSpaces directory information for the client to use to map to the correct WorkSpaces directory. Preconfiguring the RegistrationList.json will populate all of the registration codes within the client for the user.

**Note**
 If your users are running WorkSpaces Client version 2.5.11, proxy.cfg will be used for Client proxy settings and client\_settings.ini will set log level as well as the ability to save the registration list. The default proxy setting will use what is set within the OS.

 Since these files are standardized, Administrators can download the [WorkSpaces Client](https://clients.amazonworkspaces.com/), set all of the applicable settings, and then push out the same configuration files to all of the end users. For the settings to take effect, the client must be started after the new configurations are set. If you change the configuration while the client is running, none of the changes will be set within the client.

 The last setting that can be set for WorkSpaces users is Windows Client auto update. This is not controlled via configuration files but the Windows Registry instead. When a new version of the client comes out, you can create a registry key to skip that version. This can bet set by creating a string registry entry names SkipThisVersion with a value of the full version number in the path below: Computer\\HKEY\_CURRENT\_USER\\Software\\Amazon Web Services. LLC\\Amazon WorkSpaces\\WinSparkle This option is also available for macOS; however, the configuration is within a plist file which requires special software to edit. If you would still like to perform this action, it can be done by adding a *SUSkippedVersion* entry within the com.amazon.workspaces domain located at: /Users/USERNAME/Library/Preferences

## Amazon WorkSpaces endpoint selection
<a name="amazon-workspaces-endpoint-selection"></a>

### Choosing an Endpoint for your WorkSpaces
<a name="choosing-an-endpoint-for-your-workspaces"></a>

 Amazon WorkSpaces provides support for multiple endpoint devices, from Windows desktops, to iPads, and Chromebooks. You can download the available Amazon WorkSpaces clients from the [Amazon Workspaces website](https://clients.amazonworkspaces.com/). Choosing the right endpoint for your users is an important decision. If your users require the use of bi-directional Audio/Video and will be utilizing the WorkSpaces Streaming Protocol, they must use the Windows or macOS client. For all clients ensure that the IP addresses and ports listed in [IP Address and Port Requirements for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) have been explicitly configured to ensure the client can connect to the service. Here are some additional considerations to assist you in choosing an endpoint device:
+  **Windows** — To utilize the Windows Amazon WorkSpaces client, the 4.x client must run the requires 64-bit Microsoft Windows 8.1, Windows 10 desktop. Users can install the client for just their user profile without administrative privileges on the local machine. System administrators can deploy the client to managed endpoints with Group Policy, Microsoft Endpoint Manager Configuration Manager (MEMCM), or other application deployment tools used in an environment. The Windows client support a maximum of four displays and a maximum resolution of 3840x2160.
+  **macOS** — To deploy the latest macOS Amazon WorkSpaces client, macOS devices must run macOS 10.12 (Sierra) or later. You can deploy an older version of the WorkSpaces client to connect to PCoIP WorkSpaces if the endpoint is running OSX 10.8.1 or later. The macOS client supports up to two 4K resolution monitors or four WUXGA (1920 x 1200) resolution monitors.
+  **Linux** — The Amazon WorkSpaces Linux client requires 64-bit Ubuntu 18.04 (AMD64) to run. If your Linux endpoints do not run this OS version, the Linux client is not supported. Before you deploy Linux clients or provide users with their registration code, ensure that you [enable Linux client access](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html#control-device-access) at the WorkSpaces directory level, as this is disabled by default and users will not be able to connect from Linux clients until it is enabled. The Linux client supports up to two 4K resolution monitors or four WUXGA (1920 x 1200) resolution monitors.
+  **iPad** — The Amazon WorkSpaces iPad client application supports PCoIP WorkSpaces. The iPads that are supported are the iPad2 or later with iOS 8.0 or later, iPad Retina with iOS 8.0 and later, iPad Mini with iOS 8.0 and later, and the iPad Pro with iOS 9.0 and later. Ensure the device the users will connect from meets those criteria. The iPad client application supports many different gestures. (Refer to [a full list of the supported gestures](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-ipad-client.html#ipad_gestures).) The Amazon WorkSpaces iPad client application also supports the Swiftpoint GT, ProPoint, and PadPoint mice. The Swiftpoint TRACPOINT, PenPoint and GoPoint mice are not supported.
+ **Android / Chromebook** — When looking to deploy an Android device or Chromebook as the endpoint for your end users, there are a few considerations that must be taken into account. Ensure the WorkSpaces the users will be connecting to are PCoIP WorkSpaces, as this client only supports PCoIP WorkSpaces. This client only supports a single display. If users require multi-monitor support, utilize a different endpoint. If you want to deploy a Chromebook, ensure that the model you deploy supports installing Android applications. Full feature support is supported only on the Android client, and not the legacy Chromebook client. This typically is only a consideration for Chromebooks made prior to 2019. Android support is provided for both tablets and phones as long as the Android is running OS 4.4 and later. However, it is recommended that the Android device runs OS 9 or above to utilize the latest WorkSpace Android client. If your Chromebooks are running WorkSpaces client version 3.0.1 or above, your users can now take advantage of the self-service WorkSpaces features. Additionally, as an administrator, you can utilize trusted-device certificates to restrict WorkSpaces access to trusted devices with valid certificates.
+  **Web Access** — Users can access their Windows WorkSpaces from any location using a web browser. This is ideal for users who must use a locked-down device or restrictive network. Instead of using a traditional remote access solution and installing the appropriate client application, users can visit the website to access their work resources. Users can utilize the WorkSpaces Web Access to connect to non-graphics-based Windows PCoIP WorkSpaces running Windows 10 or Windows Server 2016 with Desktop Experience. Users must connect using Chrome 53 or later, or Firefox 49 or later. For WSP based WorkSpaces, users can utilize the WorkSpaces Web Access to connect to non-graphics Windows based WorkSpaces. These users must connect using Microsoft Edge 91 or later or Google Chrome 91 or later. The minimum supported screen resolution is 960 x 720 with a maximum supported resolution of 2560 x 1600. Multiple monitors are not supported. For the best user experience, when possible, it’s recommended that users use an OS version of the client.
+  **PCoIP Zero Client** — You can deploy PCoIP zero clients to end users that have or will have PCoIP WorkSpaces assigned to them. The Tera2 zero client must have a firmware version of 6.0.0 or later to connect directly to the WorkSpace. To use multi-factor authentication with Amazon WorkSpaces, the Tera2 zero client device must run firmware version 6.0.0 or later. Support and troubleshooting of the zero-client hardware should be done with the manufacturer.
+  **IGEL OS** — You can utilize IGEL OS on endpoint devices to connect to PCoIP based WorkSpaces as long as the firmware version is 11.04.280 or above. The supported features match that of the existing Linux client today. Before you deploy IGEL OS clients or provide users with their registration code, ensure you [enable](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html#control-device-access) Linux client access at the WorkSpaces directory level as this is disabled by default and users will not be able to connect from IGEL OS clients until it is enabled. The lGEL OS client supports up to two 4K resolution monitors or four WUXGA (1920x1200) resolution monitors.

## Web access client
<a name="web-access-client"></a>

Designed for locked-down devices, the [Web Access client](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-web-access.html) delivers access to Amazon WorkSpaces without the need for deploying client software. The Web Access client is recommended only in settings where the Amazon WorkSpaces are Windows Operating System (OS) and are used for limited user workflows, such as a kiosk environment. Most use cases benefit from the feature set available from the Amazon WorkSpaces client. The Web Access client is only recommended in specific use cases where devices and network restrictions require an alternative connection method.

![Sample architecture showing the web access client network requirements.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/web-access-client-auth.png)

As shown in the diagram, The Web Access client has different [network requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html#web-access-ports) to stream the session to users. Web Access is available for Windows WorkSpaces using either the PCoIP or WSP protocol. DNS and HTTP/HTTPS are required for authentication and registration with the WorkSpaces gateways. For WorkSpaces using the WSP protocol, direct connection of UDP/TCP 4195 is required to be opened to the WSP Gateway IP address ranges. Streaming traffic is not allocated to a fixed port as it is with the full Amazon WorkSpaces client; instead, it is dynamic allocated. UDP is preferable for streaming traffic; however, the web browser will fall back to TCP when UDP is restricted. In environments where TCP/UDP port 4172 is blocked and cannot be unblocked due to organizational restrictions, the Web Access client provides an alternative connection method for users.

 By default, the Web Access client is disabled at the Directory level. To enable users to access their Amazon WorkSpaces through a web browser, either use the AWS Management Console to update the [Directory settings](https://docs.aws.amazon.com/workspaces/latest/adminguide/web-access.html) or programmatically use the [WorkspaceAccessProperties API](https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceAccessProperties.html) to modify DeviceTypeWeb to Allow. Additionally, the administrator must ensure [Group Policy settings](https://docs.aws.amazon.com/workspaces/latest/adminguide/web-access.html#configure_group_policy) do not conflict with login requirements.

## Amazon WorkSpaces tags
<a name="amazon-workspaces-tags"></a>

```
Tags enable you to associate metadata with AWS resources. Tags can be used with Amazon WorkSpaces to registered directories,
  bundles, IP Access Control Groups, or images. Tags assist with cost allocation to internal cost centers. Before using tags with Amazon WorkSpaces,
  refer to the [https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) whitepaper.

Tag restrictions
```
+  Maximum number of tags per resource—50
+  Maximum key length—127 Unicode characters
+  Maximum value length—255 Unicode characters
+  Tag keys and values are case-sensitive. Allowed characters are letters, spaces, and numbers representable in UTF-8, plus the following special characters: \+ - = . \_ : / @. Do not use leading or trailing spaces.
+  Do not use the aws: or aws:workspaces: prefixes in your tag names or values because they are reserved for AWS use. You can't edit or delete tag names or values with these prefixes.

 **Resources that you can tag**
+  You can add tags to the following resources when you create them: WorkSpaces, imported images, and IP access control groups.
+  You can add tags to existing resources of the following types: WorkSpaces, registered directories, custom bundles, images, and IP access control groups.

   **Using the cost allocation tag**

 To view your WorkSpaces resource tags in the Cost Explorer, activate the tags that you have applied to your WorkSpaces resources by following the instructions in [Activating User-Defined Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the AWS Billing and Cost Management and Cost Management User Guide.

 Although tags appear 24 hours after activation, it can take four to five days for values associated with those tags to appear in the Cost Explorer, to appear and provide cost data in Cost Explorer, WorkSpaces resources that have been tagged must incur charges during that time. Cost Explorer shows only cost data from the time when the tags were activated forward. No historical data is available at this time.

### Managing tags
<a name="managing-tags"></a>

 To update the tags for an existing resource using the AWS CLI, use the [create-tags](https://docs.aws.amazon.com/cli/latest/reference/workspaces/create-tags.html) and [delete-tags](https://docs.aws.amazon.com/cli/latest/reference/workspaces/delete-tags.html) commands. For bulk updates and to automate the task on a large number of WorkSpaces resource, [Amazon WorkSpaces](https://aws.amazon.com/workspaces/) adds support for AWS Resource Groups Tag Editor. AWS Resource Groups Tag Editor enables you to add, edit, or delete AWS tags from your WorkSpaces along with your other AWS resources.

## Amazon WorkSpaces service quotas
<a name="amazon-workspaces-service-quotas"></a>

Service Quotas make it easy to look up the value of a particular *quota*, also referred to as a *limit*. You can also look up all quotas for a particular service.

 **To view your quotas for WorkSpaces**

1.  Navigate to the [Service Quotas console](https://console.aws.amazon.com/servicequotas/).

1.  In the left-hand navigation pane, choose **AWS services**.

1.  Select **Amazon WorkSpaces** from the list, or enter **Amazon WorkSpaces** in the type-ahead search field.

1.  To view additional information about a quota, such as its description and Amazon Resource Name (ARN), choose the quota name.

 Amazon WorkSpaces provides different resources that you can use in your account in a given region, including WorkSpaces, images, bundles, directories, connection aliases, and IP control groups. When you create your Amazon Web Services account, default quotas are set (also referred to as limits) on the number of resources that you can create.

You can use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/) to view the default Service Quotas or to [request quota increases](https://amzn.to/3rMkD5g) for adjustable quotas.

 For more information, refer to [Viewing service quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html) and [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

## Automating Amazon WorkSpaces deployment
<a name="automating-amazon-workspaces-deployment"></a>

 With Amazon WorkSpaces, you can launch a Microsoft Windows or Amazon Linux desktop within minutes, and connect to and access your desktop software from on-premises or an external network securely, reliably, and quickly. You can automate the provisioning of Amazon WorkSpaces to enable you to integrate Amazon WorkSpaces into your existing provisioning workflows.

## Common WorkSpaces automation methods
<a name="common-workspaces-automation-methods"></a>

 Customers can use a number of tools to allow for rapid Amazon WorkSpaces deployment. The tools can be used to allow simplify management of WorkSpaces, reduce costs and enable an agile environment that can scale and move fast.

### AWS CLI and API
<a name="aws-cli-and-api"></a>

There are [Amazon WorkSpaces API operations](https://docs.aws.amazon.com/workspaces/latest/api/welcome.html) you can use to interact with the service securely, and at scale. All public APIs are available with the AWS CLI SDK and Tools for PowerShell, while private APIs such as image creation are available only through the AWS Management Console. When considering operational management and business self-service for Amazon WorkSpaces, consider that WorkSpaces APIs *do* require technical expertise and security permissions to use.

 API calls can be made using the [AWS SDK](https://aws.amazon.com/tools/). [AWS Tools for Windows PowerShell](https://aws.amazon.com/powershell/) and AWS Tools for PowerShell Core are PowerShell modules built on functionality exposed by the AWS SDK for .NET. These modules enable you to script operations on AWS resources from the PowerShell command line, and integrate with existing tools and services. For example, API calls can enable you to automatically manage the WorkSpaces lifecycle by integrating with AD to provision and decommission WorkSpaces based on a user’s AD group membership.

### AWS CloudFormation
<a name="aws-cloudformation"></a>

AWS CloudFormation enables you to model your entire infrastructure in a text file. This template becomes the single source of truth for your infrastructure. This helps you to standardize infrastructure components used across your organization, enabling configuration compliance and faster troubleshooting.

 AWS CloudFormation provisions your resources in a safe, repeatable manner, enabling you to build and rebuild your infrastructure and applications. You can use CloudFormation to commission and decommission environments, which is useful when you have a number of accounts that you want to build and decommission in a repeatable fashion. When considering operational management and business self-service for Amazon WorkSpaces, consider that [AWS CloudFormation](https://aws.amazon.com/cloudformation/) *does* require technical expertise and security permissions to use.

### Self-Service WorkSpaces portal
<a name="self-service-workspaces-portal"></a>

Customers can use build on WorkSpaces API commands and other AWS Services to create a WorkSpaces self-service portal. This helps customers streamline the process to deploy and reclaim WorkSpaces at scale. Using a WorkSpaces portal, you can enable your workforce to provision their own WorkSpaces with an integrated approval workflow that does not require IT intervention for each request. This reduces IT operational costs, while helping end-users get started with WorkSpaces faster. The additional built-in approval workflow simplifies the desktop approval process for businesses. A dedicated portal can offer an automated tool for provisioning Windows or Linux cloud desktops, and enable users to rebuild, restart, or migrate their WorkSpace, as well as provide a facility for password resets.

 There are guided examples of creating Self Service WorkSpaces Portals referenced in the [Further Reading](further-reading.md) section of this document. AWS Partners provide preconfigured WorkSpaces management portals via the [AWS Marketplace](https://aws.amazon.com/marketplace).

### Integration with Enterprise IT Service Management
<a name="integration-with-enterprise-it-service-management"></a>

 As enterprises adopt Amazon WorkSpaces as their virtual desktop solution at scale, there is a need to implement, or integrate with, IT Service Management (ITSM) systems. ITSM integration allows for self-service offerings for provisioning and operations. The [Service Catalog](https://aws.amazon.com/servicecatalog/) enables you to manage commonly deployed AWS services and provisioned software products centrally. This service helps your organization achieve consistent governance and compliance requirements, while enabling users to deploy only the approved AWS services they need. The Service Catalog can be used to enable a self-service lifecycle-management offering for Amazon WorkSpaces from within IT Service Management tools such as [ServiceNow](https://aws.amazon.com/blogs/mt/managing-amazon-workspaces-by-integrating-aws-service-catalog-with-servicenow/).

## WorkSpaces Deployment Automation best practices
<a name="workspaces-deployment-automation-best-practices"></a>

 You should consider Well Architected principles of selecting and designing WorkSpaces deployment automation.
+  **Design for Automation** — Design to deliver the least possible manual intervention in the process to enable repeatability and scale.
+  **Design for Cost Optimization** — By automatically creating and reclaiming WorkSpaces, you can reduce the administration effort needed to provide resources and remove idle or unused resources from generating unnecessary cost.
+  **Design for Efficiency** — Minimize the resources needed to create and terminate WorkSpaces. Where possible, provide Tier 0 self-service capabilities for the business to improve efficiency.
+  **Design for Flexibility** — Create a consistent deployment mechanism that can handle multiple scenarios, and can scale with the same mechanism (customized using tagged use case and profile identifiers).
+  **Design for Productivity** — Design your WorkSpaces operations to allow for the correct authorization and validation to add or remove resources.
+  **Design for Scalability** — The pay-as-you go model that Amazon WorkSpaces uses can drive cost savings by creating resources as needed, and removing them when they are no longer necessary.
+  **Design for Security** — Design your WorkSpaces operations to allow for the correct authorization and validation to add or remove resources.
+  **Design for Supportability** — Design your WorkSpaces operations to allow for non-invasive support and recovery mechanisms and processes.

## Amazon WorkSpaces patching and in-place upgrades
<a name="amazon-workspaces-patching-and-in-place-upgrades"></a>

 With Amazon WorkSpaces, you can manage patching and updates using existing third-party tools, such as Microsoft System Center Configuration Manager (SCCM), Puppet Enterprise, or Ansible. In-place deployment of security patches typically maintains a monthly patch cycle, with additional processes for escalation or rapid deployment. However, in the case of in-place operating system upgrades or feature updates, special considerations are often necessary.

## WorkSpace maintenance
<a name="workspace-maintenance"></a>

 Amazon WorkSpaces have a [default maintenance window](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html) during which the WorkSpace installs Amazon WorkSpaces agent updates and any available operating system updates. WorkSpaces will be unavailable to user connections during the scheduled maintenance window.
+  **AlwaysOn** WorkSpaces default maintenance window is 00h00 to 04h00, in the time zone of the WorkSpace, each Sunday morning.
+  Time zone redirection is enabled by default and can override the default window to match the user’s local time zone.
+  You can [disable time zone redirection for Windows WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#gp_time_zone) using Group Policy. You can [disable time zone redirection for Linux WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage_linux_workspace.html#linux_time_zone) by using the PCoIP Agent conf.
+  **AutoStop** WorkSpaces are started automatically once a month to install important updates. Beginning on the third Monday of the month, and for up to two weeks, the maintenance window is open each day from about 00h00 to 05h00, in the time zone of the AWS Region for the WorkSpace. The WorkSpace can be maintained on any one day in the maintenance window.
+  Although you cannot modify the time zone that is used for maintaining AutoStop WorkSpaces, you can [disable the maintenance window for your AutoStop WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html#autostop-maintenance).
+  [Manual maintenance windows](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html#admin-maintenance) can be set based on your preferred schedule by setting the state of the WorkSpace to ADMIN\_MAINTENANCE.
+  The AWS CLI command [modify-workspace-state](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/modify-workspace-state.html) can be used to modify the WorkSpace state to ADMIN\_MAINTENANCE.

## Amazon Linux WorkSpaces
<a name="amazon-linux-workspaces"></a>

 For considerations, prerequisites, and suggested patterns for managing updates and patches on Amazon Linux WorkSpaces custom images, refer to the whitepaper [Best Practices to Prepare your Amazon WorkSpaces for Linux Images](https://docs.aws.amazon.com/whitepapers/latest/workspaces-linux-best-practices/welcome.html).

### Linux patching prerequisites and considerations
<a name="linux-patching-prerequisites-and-vonsiderations"></a>
+  Amazon Linux repositories are hosted in Amazon Simple Storage Service (Amazon S3) buckets which can be accessed via public Internet-accessible endpoints or private endpoints. If your Amazon Linux WorkSpaces do not have Internet access, please refer to this process for making updates accessible: [How can I update yum or install packages without internet access on my EC2 instances running Amazon Linux 1 or Amazon Linux 2?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-al1-al2-update-yum-without-internet/)
+  You cannot configure the default maintenance window for Linux WorkSpaces. If customization of this window is required the [manual maintenance](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html#admin-maintenance) process can be utilized.

## Amazon Windows patching
<a name="amazon-windows-patching"></a>

 By default, your Windows WorkSpaces are configured to receive updates from Windows Update which require Internet access from your WorkSpaces VPC. To configure your own automatic update mechanisms for Windows, refer to the documentation for [Windows Server Update Services (WSUS)](https://docs.microsoft.com/windows-server/administration/windows-server-update-services/deploy/deploy-windows-server-update-services) and [Configuration Manager](https://docs.microsoft.com/configmgr/sum/deploy-use/deploy-software-updates).

## Amazon Windows in-place upgrade
<a name="amazon-windows-in-place-upgrade"></a>
+  If you plan to create an image from a Windows 10 WorkSpace, note that image creation is not supported on Windows 10 systems that have been upgraded from a previous version (a Windows feature/version upgrade). However, Windows cumulative or security updates are supported by the WorkSpaces image creation and capture process.
+  Custom Windows 10 Bring Your Own License (BYOL) images should start with the most current supported version of Windows on a VM as the source for the BYOL import process: refer to the [BYOL import documentation](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html#windows_images_supported_versions) for further detail.

### Windows In-place Upgrade Prerequisites
<a name="windows-in-place-upgrade-prerequisites"></a>
+  If you have deferred or paused Windows 10 upgrades using Active Directory Group Policy or SCCM, enable operating system upgrades for your Windows 10 WorkSpaces.
+  If the WorkSpace is an AutoStop WorkSpace, change the AutoStop time to at least three hours to accommodate the upgrade window.
+  The in-place upgrade process recreates the user profile by making a copy of Default User (C:\\Users\\Default). ***Do not use the default user profile to make customizations***. It’s recommended to make any customizations to the user profile through Group Policy Objects (GPOs) instead. Customizations made through GPOs can be easily modified or rolled back, and are less prone to error.
+  The in-place upgrade process can back up and recreate only one user profile. If you have multiple user profiles on drive D, delete all the profiles except for the one that you need.

### Windows In-place Upgrade Considerations
<a name="windows-in-place-upgrade-considerations"></a>
+  The in-place upgrade process uses two registry scripts (enable-inplace-upgrade.ps1 and update-pvdrivers.ps1) to make the necessary changes to your WorkSpaces and enable the Windows Update process to run. These changes involve creating a temporary user profile on drive C instead of drive D. If a user profile already exists on drive D, the data in that original user profile remains on drive D.
+  Once the in-place upgrade is deployed, you must restore the user profiles to the D drive to ensure that you can rebuild or migrate your WorkSpaces, and to avoid any potential problems with user shell folder redirection. You can do so by using the **PostUpgradeRestoreProfileOnD** registry key, as explained on the [BYOL upgrade reference page](https://docs.aws.amazon.com/workspaces/latest/adminguide/upgrade-windows-10-byol-workspaces.html).

## Amazon WorkSpaces language packs
<a name="amazon-workspaces-language-packs"></a>

 Amazon WorkSpaces bundles that provide the Windows 10 desktop experience supports English (US), French (Canadian), Korean, and Japanese. However, you can include additional language packs for Spanish, Italian, Portuguese, and many more language options. For more information, refer to [How do I create a new Windows WorkSpace image with a client language other than English?](https://aws.amazon.com/premiumsupport/knowledge-center/workspaces-client-language/).

## Amazon WorkSpaces profile management
<a name="amazon-workspaces-profile-management"></a>

Amazon WorkSpaces separates the user profile from the base Operating System (OS) by redirecting all profile writes to a separate [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) volume. In Microsoft Windows, the user profile is stored in D:\\Users\\username*.* In Amazon Linux, the user profile is stored in /home. The EBS volume is snapshotted automatically every 12 hours. The snapshot is automatically stored in an AWS Managed S3 bucket, to be used in the event that an Amazon WorkSpace is rebuilt or restored.

 For most organizations, having automatic snapshots every 12 hours is superior to the existing desktop deployment of no backups for user profiles. However, customers can require more granular control over user profiles; for example, migration from desktop to WorkSpaces, to a new OS/AWS Region, support for DR, and so on. There are alternative methods for profile management available for Amazon WorkSpaces.

## Folder redirection
<a name="folder-redirection"></a>

While folder redirection is a common design consideration in Virtual Desktop Infrastructure (VDI) architectures, it is not a best practice, or even a common requirement in Amazon WorkSpaces designs. The reason for this is Amazon WorkSpaces is a persistent Desktop as a Service (DaaS) solution, with application and user data persisting out of the box.

 There are specific scenarios where Folder Redirection for User Shell Folders (for example, D:\\Users\\username\\Desktop redirected to \\\\Server\\RedirectionShare$\\username\\Desktop) are required, such as immediate recovery point objective (RPO) for user profile data in disaster recovery (DR) environments.

## Best practices
<a name="best-practices"></a>

 The following best practices are listed for a robust folder redirection:
+  Host the Windows File Servers in the same AWS Region and AZ that the Amazon WorkSpaces are launched in.
+  Ensure AD Security Group Inbound Rules include the Windows File Server Security Group or private IP addresses; otherwise ensure that the on-premises firewall allows those same TCP and UDP port-based traffic.
+  Ensure Windows File Server Security Group Inbound Rules include TCP 445 (SMB) for all Amazon WorkSpaces Security Groups.
+  Create an AD Security Group for Amazon WorkSpaces users to authorize users’ access to the Windows File Share.
+  Use DFS Namespace (DFS-N) and DFS Replication (DFS-R) to ensure your Windows File Share is agile, not tied to anyone one specific Windows File Server, and all user data is automatically replicated between Windows File Servers.
+  Append ‘$’ to the end of the share name to hide the share hosting user data from view when browsing the network shares in Windows Explorer.
+  Create the file share following Microsoft’s guidance for redirected folders: [Deploy Folder Redirection with Offline Files](https://docs.microsoft.com/en-us/windows-server/storage/folder-redirection/deploy-folder-redirection). Follow the guidance for Security Permissions and GPO configuration closely.
+  If your Amazon WorkSpaces deployment is Bring Your Own License (BYOL), you must also specify disabling Offline Files following Microsoft’s guidance: [Disable Offline Files on Individual Redirected Folders](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj154097(v=ws.11)).
+  Install and run Data Deduplication (commonly referred to as ‘dedupe’) if your Windows File Server is Windows Server 2016 or newer to reduce storage consumption and optimize cost. Refer to [Install and enable Data Deduplication](https://docs.microsoft.com/en-us/windows-server/storage/data-deduplication/install-enable) and [Running Data Deduplication](https://docs.microsoft.com/en-us/windows-server/storage/data-deduplication/run).
+  Back up your Windows File Server file shares using existing organizational backup solutions.

## Thing to avoid
<a name="thing-to-avoid"></a>
+  Do not use Windows File Servers that are accessible only across a wide area network (WAN) connection, as the SMB protocol is not designed for that use.
+  Do not use the same Windows File Share that is used for Home Directories to mitigate the chances of users accidentally deleting their User Shell folders.
+  While enabling [Volume Shadow Copy Service](https://docs.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service) (VSS) is recommended for ease of file restores, this alone does not remove the requirement to back up the Windows File Server file shares.

## Other considerations
<a name="other-considerations"></a>
+  Amazon FSx for Windows File Server offers a managed service for Windows file shares, and simplify the operational overhead of folder redirection, including automatic backups.
+  Utilize [AWS Storage Gateway for SMB File Share](https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingAnSMBFileShare.html) to back up your file shares if there is no existing organizational backup solution.

## Profile settings
<a name="profile-settings"></a>

### Group policies
<a name="group-policies"></a>

 A common best practice in enterprise Microsoft Windows deployments is to define user environment settings through Group Policy Object (GPO) and Group Policy Preferences (GPP) settings. Settings such as shortcuts, drive mappings, registry keys, and printers are defined through the Group Policy Management Console. The benefits to defining the user environment through GPOs include, but are not limited to:
+  Centralized configuration management
+  User profile defined by AD Security Group Membership or OU placement
+  Protection against deletion of settings
+  Automate profile creation and personalization at first logon
+  Ease of future updating

**Note**
Follow Microsoft’s [Best Practices for optimizing Group Policy performance.](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc137720(v=msdn.10)?redirectedfrom=MSDN)

 Interactive Logon Banners Group Policies must not be used as they are not supported on Amazon WorkSpaces. Banners are presented on the Amazon WorkSpaces Client through AWS support requests. Additionally, removable devices must not be blocked through group policy, as they are required for Amazon WorkSpaces.

 GPOs can be used to manage Windows WorkSpaces. For more information, refer to [Manage Your Windows WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html).

## Amazon WorkSpaces volumes
<a name="amazon-workspaces-volumes"></a>

 Each Amazon WorkSpaces instance contains two volumes: an *operating system* volume and a *user* volume.
+  **Amazon Windows WorkSpaces** — The C:\\ drive is used for the Operating System (OS) and the D:\\ drive is user volume. The user profile is located on the user volume (AppData, Documents, Pictures, Downloads, and so on).
+  **Amazon Linux WorkSpaces** — With an Amazon Linux WorkSpace, the system volume (/dev/xvda1) mounts as the root folder. The user volume is for user data and applications; /dev/xvdf1 mounts as /home.

For operating system volumes, you can select a starting size for this drive of 80 GB or 175 GB. For user volumes, you can select a starting size of 10 GB, 50 GB, or 100 GB. Both volumes can be increased up to 2TB in size as needed; however, to increase the user volume beyond 100 GB, the OS volume must be 175 GB. Volume changes can be performed only once every six hours per volume. For additional information on modifying the WorkSpaces volume size, refer to the [Modify a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html#limitations_increasing_volumes) section of the Administration Guide.

 **WorkSpaces volumes best practices**

When planning an Amazon WorkSpaces deployment, it’s recommended to factor the minimum requirements for OS installation, in-place upgrades, and additional core applications that will be added to the image on the OS volume. For the user volume, it’s recommended to start with a smaller disk allocation, and incrementally increasing the user volume size as needed. Minimizing the size of the disk volumes reduces the cost of running the WorkSpace.

**Note**
 While a volume size can be increased, it cannot be decreased.

## Amazon WorkSpaces logging
<a name="amazon-workspaces-logging"></a>

In an Amazon WorkSpaces environment, there are many log sources that can be captured to troubleshoot issues and monitor the overall WorkSpaces performance.

 **Amazon WorkSpaces Client 3.x **On each Amazon WorkSpaces client, the client logs are located in the following directories:
+  Windows — %LOCALAPPDATA%\\Amazon Web Services\\Amazon WorkSpaces\\logs
+  macOS — \~/Library/"Application Support"/"Amazon Web Services"/"Amazon WorkSpaces"/logs
+  Linux (Ubuntu 18.04 or later) — /opt/workspacesclient/workspacesclient

 There are many instances where diagnostic or debugging details may be needed for a WorkSpaces session from the client side. Advanced client logs can be enabled as well by adding an “-l3“ to the workspaces executable file. For example:

```
"C:\Program Files (x86)\Amazon Web Services, Inc\Amazon WorkSpaces"
workspaces.exe -l3
```

 **Amazon WorkSpaces service**

Amazon WorkSpaces service is integrated with Amazon CloudWatch Metrics, CloudWatch Events, and CloudTrail. This integration allows of the performance data and API calls to be logged into central AWS service.

 When managing an Amazon WorkSpaces environment, it is important to constantly monitor certain CloudWatch metrics to determine the overall environment health status. **Metrics**

 While there are other CloudWatch metrics available for Amazon WorkSpaces (refer to [Monitor Your WorkSpaces Using CloudWatch Metrics](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-metrics.html)), the three following metrics will assist in maintaining the WorkSpace instance availability:
+  **Unhealthy** — The number of WorkSpaces that returned an unhealthy status.
+  **SessionLaunchTime** — The amount of time it takes to initiate a WorkSpaces session.
+  **InSessionLatency** — The round-trip time between the WorkSpaces client and the WorkSpace.

 For more information on WorkSpaces logging options, refer to [Logging Amazon WorkSpaces API Calls by Using CloudTrail](https://docs.aws.amazon.com/workspaces/latest/api/cloudtrail_logging.html). The additional CloudWatch Events will assist with capturing the client-side IP of the user session, when the user connected to the WorkSpaces session, and the what endpoint was used during the connection. All of these details assist with isolating or pinpointing user reported issues during troubleshooting sessions.

**Note**
 Some CloudWatch Metrics are available only with AWS Managed AD.
