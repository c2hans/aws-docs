---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/security.html
---

# Security
<a name="security"></a>

 This section explains how to secure data by using encryption when using Amazon WorkSpaces services. It describes encryption in transit and at rest, and the use of security groups to protect network access to the WorkSpaces. This section also provides information on how to control end device access to WorkSpaces by using Trusted Devices, and IP Access Control Groups.

 Additional information on authentication (including MFA support) in the AWS Directory Service can be found in this section.

## Encryption in transit
<a name="encryption-in-transit"></a>

 Amazon WorkSpaces uses cryptography to protect confidentiality at different stages of communication (in transit) and also to protect data at rest (encrypted WorkSpaces). The processes in each stage of the encryption used by Amazon WorkSpaces in transit is described in the following sections.

 For information about the encryption at rest, refer to the [Encrypted WorkSpaces](#network-access-control-lists-acls) section of this document.

### Registration and updates
<a name="registration-and-updates"></a>

 The desktop client application communicates with Amazon for updates and registration using HTTPS.

### Authentication stage
<a name="authentication-stage"></a>

 The desktop client initiates authentication by sending credentials to the authentication gateway. The communication between the desktop client and authentication gateway uses HTTPS. At the end of this stage, if the authentication succeeds, the authentication gateway returns an OAuth 2.0 token to the desktop client, through the same HTTPS connection.

**Note**
 The desktop client application supports the use of a proxy server for port 443 (HTTPS) traffic, for updates, registration, and authentication.

 After receiving credentials from the client, the authentication gateway sends an authentication request to AWS Directory Service. The communication from the authentication gateway to AWS Directory Service takes place over HTTPS, so no user credentials are transmitted in plaintext.

### Authentication — Active Directory Connector (ADC)
<a name="authentication-active-directory-connector-adc"></a>

AD Connector uses [Kerberos](https://en.wikipedia.org/wiki/Kerberos_(protocol)) to establish authenticated communication with on-premises AD, so it can bind to LDAP and execute subsequent LDAP queries. Client-side LDAPS support in ADC is also available to encrypt queries between Microsoft AD and AWS Applications. Before implementing client-side LDAPS functionality, review the [prerequisites for client-side LDAPS](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_ldap_client_side.html).

 The AWS Directory Service also supports LDAP with TLS. No user credentials are transmitted in plaintext at any time. For increased security, it is possible to connect a WorkSpaces VPC with the on-premises network (where AD resides) using a VPN connection. When using an AWS hardware VPN connection, customers can set up encryption in transit by using standard IPSEC (Internet Key Exchange (IKE) and IPSEC SAs) with AES-128 or AES-256 symmetric encryption keys, SHA-1 or SHA-256 for integrity hash, and DH groups (2,14-18, 22, 23 and 24 for phase 1; 1,2,5, 14-18, 22, 23 and 24 for phase 2) using perfect forward secrecy (PFS).

### Broker stage
<a name="broker-stage"></a>

 After receiving the OAuth 2.0 token (from the authentication gateway, if the authentication succeeded), the desktop client queries Amazon WorkSpaces services (Broker Connection Manager) using HTTPS. The desktop client authenticates itself by sending the OAuth 2.0 token and, as a result, the client receives the endpoint information of the WorkSpaces streaming gateway.

### Streaming stage
<a name="streaming-stage"></a>

 The desktop client requests to open a PCoIP session with the streaming gateway (using the OAuth 2.0 token). This session is AES-256 encrypted and uses the PCoIP port for communication control (4172/TCP).

 Using the OAuth2.0 token, the streaming gateway requests the user-specific WorkSpaces information from the Amazon WorkSpaces service, over HTTPS.

 The streaming gateway also receives the TGT from the client (which is encrypted using the client user’s password) and, by using Kerberos TGT pass-through, the gateway initiates a Windows login on the WorkSpace, using the user’s retrieved Kerberos TGT.

 The WorkSpace then initiates an authentication request to the configured AWS Directory Service, using standard Kerberos authentication.

 After the WorkSpace is successfully logged in, the PCoIP streaming starts. The connection is initiated by the client on port TCP 4172 with the return traffic on port UDP 4172. Additionally, the initial connection between the streaming gateway and a WorkSpaces desktop over the management interface is via UDP 55002. (Refer to documentation for [IP Address and Port Requirements for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html). The initial outbound UDP port is 55002.) The streaming connection, using ports 4172 (TCP and UDP), is encrypted by using AES 128- and 256-bit ciphers, but default to 128-bit. Customers can actively change this to 256-bit, either using PCoIP-specific AD Group Policy settings for Windows WorkSpaces, or with the [pcoip-agent.conf](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage_linux_workspace.html) file for Amazon Linux WorkSpaces. For more information about Group Policy administration for Amazon WorkSpaces, refer to the [documentation](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html).

## Network interfaces
<a name="network-interfaces-1"></a>

 Each Amazon WorkSpace has two network interfaces, called the [primary network interface and management network interface](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html#network-interfaces).

 The primary network interface provides connectivity to resources inside the customer VPC, such as access to AWS Directory Service, the internet, and the customer corporate network. It is possible to attach security groups to this primary network interface. Conceptually, the security groups are differentiated attached to this ENI based on the scope of the deployment: WorkSpaces security group and ENI security groups.

### Management network interface
<a name="management-network-interface"></a>

 The management network interface cannot be controlled via security groups; however, customers can use a host-based firewall on WorkSpaces to block ports or control access. We don’t recommend applying restrictions on the management network interface. If a customer decides to add host-based firewall rules to manage this interface, a few ports should be open so the Amazon WorkSpaces service can manage the health and accessibility to the WorkSpace. For more information, refer to [Network Interfaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html#network-interfaces) in the Amazon Workspaces Administration Guide.

## WorkSpaces security groups
<a name="workspaces-security-groups"></a>

 A default security group is created per AWS Directory Service and is automatically attached to all WorkSpaces that belong to that specific directory.

 Amazon WorkSpaces, like many other AWS services, makes use of security groups. Amazon WorkSpaces creates two AWS Security Groups when you register a directory with the WorkSpaces service. One for directory controllers directoryId\_controllers and one for WorkSpaces in the directory directoryId\_workspacesMembers. Do not delete either of these security groups, or your WorkSpaces will become impaired. By default, the WorkSpaces Members security group has egress open to 0.0.0.0/0. You can add a default WorkSpaces security group to a directory. After you associate a new security group with a WorkSpaces directory, new WorkSpaces that you launch or existing WorkSpaces that you rebuild will have the new security group. You can also add this new default security group to existing WorkSpaces without rebuilding them. When you associate multiple security groups with a WorkSpaces directory, WorkSpaces aggregate the rules from each security group into a single set of rules. We recommend condensing your security group rules as much as possible. For more information about security groups, refer to [Security Groups for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon VPC User Guide.*

For more infomation about adding a security group to a WorkSpaces directory or existing WorkSpace, refer to the [WorkSpaces Admin guide.](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-security-groups.html)

 Some customers want to restrict ports and destinations the WorkSpaces traffic can egress. To restrict egress traffic from the WorkSpaces, you must ensure you leave specific ports required for service communication; otherwise, your users will not be able to log in to their WorkSpaces.

 WorkSpaces utilize the Elastic Network Interface (ENI) in the customer VPC for communication to the domain controllers during WorkSpace log in. To allow your users to log in to their WorkSpaces successfully, you must allow the following ports to access your domain controllers or the CIDR ranges that include your domain controllers in the \_workspacesMembers security group.
+  TCP/UDP 53 - DNS
+  TCP/UDP 88 - Kerberos authentication
+  TCP/UDP 389 – LDAP
+  TCP/UDP 445 - SMB
+  TCP 3268-3269 - Global Catalog
+  TCP/UDP 464 - Kerberos password change
+  TCP 139 - Netlogon
+  UDP 137-138 - Netlogon
+  UDP 123 - NTP
+  TCP/UDP 49152-65535 Ephemeral ports for RPC

 If your WorkSpaces need to access other applications, the Internet, or other locations, you will need to allow those ports and destinations in CIDR notation within the \_workspacesMembers security group. If you do not add those ports and destinations, the WorkSpaces will not reach anything other than the ports listed above. One final consideration, by default, a new security group has no inbound rules. Therefore, no inbound traffic originating from another host to your instance is allowed until you add inbound rules to the security group. The above steps are only required if you want to either restrict egress from the WorkSpaces or have ingress rules locked down to only the resources or CIDR ranges that should have access to them.

**Note**
 A newly associated security group will be attached only to WorkSpaces created or rebuilt after the modification.

### ENI security groups
<a name="eni-security-groups"></a>

 Because the primary network interface is a regular ENI, it can be managed by using the different AWS management tools. For more information, refer to [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html). Navigate to the WorkSpace IP address (in the WorkSpaces page in the Amazon WorkSpaces console), and then use that IP address as a filter to find the corresponding ENI (in the Network Interfaces section of the Amazon EC2 console).

 Once the ENI is located, it can be directly managed by security groups. When manually assigning security groups to the primary network interface, consider the port requirements of Amazon WorkSpaces. For more information, refer to [Network Interfaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html#network-interfaces) in the *Amazon Workspaces Administration Guide*.

![Screenshot showing a WorkSpaces client with MFA enabled](https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/pre-session-authentication.png)

## Network Access Control Lists (ACLs)
<a name="network-access-control-lists-acls"></a>

Due to the added complexity in managing yet another firewall, Network ACLs are commonly used in very complex deployments and not generally used as a best practice. As Network ACLs are attached to the subnets in the VPC, that focuses their function at Layer 3 (Network) of the OSI model. Due to Amazon WorkSpaces being designed on Directory Services, two subnets must be defined. Network ACLs are managed separately from Directory Services, and it is entirely likely that a Network ACL may be assigned to only one of the WorkSpaces’ assigned subnets.

 When a stateless firewall is required, Network ACLs are a best practice for security. Ensure any changes made to Network ACLs beyond the default settings are validated on a per subnet basis as a best practice. If the Network ACLs are not performing as intended, consider using [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) to analyze the traffic.

## AWS Network Firewall
<a name="aws-network-firewall"></a>

 [AWS Network Firewall](https://aws.amazon.com/network-firewall/) offers functionality beyond what native Security Groups and Network ACLs offer, however at a cost. When customers *have* asked for the ability to increase security around network connections such as Server Name Inspection (SNI) for HTTPS-based websites, Intrusion Detection and Prevent, and an allow and deny list for domain names, they were left to find alternative firewalls on the AWS Marketplace. The complexity in deploying these firewalls presented challenges beyond what standard EUC administrators are skilled at. AWS Network Firewall offers a native AWS experience while enabling Layers 3 through 7 protections. Using AWS Network Firewall in conjunction with NAT Gateway is a best practice when organizations do not possess any other means (existing on-premises licensing for third party firewalls that can be transferred to the cloud or separate teams that manage firewalls excluded) to cover all the EUC network protections. NAT Gateway is also free of charge with AWS Network Firewall.

 Deployments of AWS Network Firewall are designed around the existing EUC design. Single VPC designs can achieve a simplified architecture with subnets for firewall endpoints and separate Internet egress routing considerations, whereas multi VPC designs benefit great from a consolidated inspection VPC with firewall and Transit Gateways endpoints.

### Design scenarios
<a name="design-scenarios"></a>

#### Scenario 1: Basic instance lockdown
<a name="scenario-1-basic-instance-lockdown"></a>

 The default WorkSpaces Security Group does not allow any traffic inbound, as Security Groups are denied by default, and stateful. This means that there are no additional configurations that need to be configured to further secure the WorkSpaces instances themselves. Consider the outbound rules which allow all traffic, and if that fits the use case. For instance, it may be best to deny all outbound traffic to port 443 to any address, and specific IP ranges that that fit port use cases such as 389 for LDAP, 636 for LDAPS, 445 for SMB, among others; although note the complexity of the environment may necessitate multiple rules and thus be better served through Network ACLs or a firewall appliance.

#### Scenario 2: Inbound exceptions
<a name="scenario-2-inbound-exceptions"></a>

 While it is not a constant requirement, there may be times when network traffic is initiated inbound to WorkSpaces. For instance, triaging instances when the WorkSpaces Client cannot connect require alternative remote connectivity. In these instances, it is best to temporarily enable inbound TCP 3389 to the Security Group of the WorkSpace’s customer ENI.

 Another scenario are organizational scripts that perform commands for inventory or automation functions, initiated by a centralized instance. Securing the traffic on that port from those specific centralized instances on the Inbound can be permanently configured, however, it is a best practice to do this on the additional Security Group attached to the Directory configuration as it can be applied to multiple deployments in the AWS account.

 Lastly, there is some network traffic that is not stateful-based and will require ephemeral ports to be specified in the inbound exceptions. If queries and scripts are failing, it is a best practice to allow ephemeral ports, at least temporarily, while determining the root cause of connectivity failure.

#### Scenario 3: Single VPC inspection
<a name="scenario-3-single-vpc-inspection"></a>

 Simplified deployments of WorkSpaces (such as a single VPC with no scaling plans) do not require a separate VPC for inspection, and thus connection to other VPCs can be simplified with VPC peering. Separate subnets, however, for firewall endpoints must be created with routing configured to those endpoints as well as Internet Gateway (IGW) egress routing, which otherwise would not need to be configured. Existing deployments may not have the available IP space if all subnets utilize the entire of the VPC CIDR block. In those instances, Scenario 4 may serve better as the deployment has already scaled beyond its initial design.

#### Scenario 4: Centralized inspection
<a name="scenario-4-centralized-inspection"></a>

 Often preferred in multiple EUC deployments in an AWS Region, simplifying the administration of the AWS Network Firewall’s stateful and stateless rules. Existing VPC peers will be replaced with Transit Gateways, as this design necessitates the use of Transit Gateway attachments as well as the inspection routing that can only be configured through those attachments. Greater degree of control is exercised over this configuration as well, and enables security beyond the default WorkSpaces experience.

![Sample architecture using Transit Gateway attachments.](https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/transit-gateway-attach.png)

## Encrypted WorkSpaces
<a name="encrypted-workspaces"></a>

 Each Amazon WorkSpace is provisioned with a root volume (C: drive for Windows WorkSpaces, root for Amazon Linux WorkSpaces) and a user volume (D: drive for Windows WorkSpaces, /home for Amazon Linux WorkSpaces). The encrypted WorkSpaces feature enables one or both volumes to be encrypted.

### What is encrypted?
<a name="what-is-encrypted"></a>

 The data stored at rest, disk input/output (I/O) to the volume, and snapshots created from encrypted volumes are all encrypted.

### When does encryption occur?
<a name="when-does-encryption-occur"></a>

 Encryption for a WorkSpace should be specified when launching (creating) the WorkSpace. WorkSpaces volumes can be encrypted only at launch time: after launch, the volume encryption status cannot be changed. The following figure shows the Amazon WorkSpaces console page for choosing encryption during the launch of a new WorkSpace.

![Screenshot of WorkSpaces console and how to excrypt the root volume](https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/root-volume.png)

### How is a new WorkSpace encrypted?
<a name="how-is-a-new-workspace-encrypted"></a>

 A customer can choose the Encrypted WorkSpaces option from either the Amazon WorkSpaces console or AWS CLI, or by using the Amazon WorkSpaces API when a customer launches a new WorkSpace.

 To encrypt the volumes, Amazon WorkSpaces uses a CMK from AWS Key Management Service (AWS KMS). A default AWS KMS CMK is created the first time a WorkSpace is launched in a Region. (CMKs have a Region scope.)

 A customer can also create a customer-managed CMK to use with encrypted WorkSpaces. The CMK is used to encrypt the data keys that are used by Amazon WorkSpaces service to encrypt each of the WorkSpace volumes. (In a strict sense, it is [Amazon EBS](https://aws.amazon.com/ebs/) that will encrypt the volumes). For current CMK limits, refer to [AWS KMS Resource quotas](https://docs.aws.amazon.com/kms/latest/developerguide/resource-limits.html).

**Note**
 Creating custom images from an encrypted WorkSpace is not supported. Also, WorkSpaces launched with root volume encryption enabled can take up to an hour to be provisioned.

 For a detailed description of the WorkSpaces encryption process, refer to [How Amazon WorkSpaces uses AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/services-workspaces.html). Consider how the use of CMK will be monitored to ensure that a request for an encrypted WorkSpace is serviced correctly. For additional information about AWS KMS keys and data keys, refer to the [AWS KMS page](https://aws.amazon.com/kms/).

## Access control options and trusted devices
<a name="access-control-options-and-trusted-devices"></a>

Amazon WorkSpaces provides customers options to manage which client devices can access WorkSpaces. Customers can limit WorkSpaces access to trusted devices only. Access to WorkSpaces can be allowed from macOS and Microsoft Windows PCs using digital certificates. It can also allow or block access for iOS, Android, Chrome OS, Linux, and zero clients, as well as the WorkSpaces Web Access client. With these capabilities, it can further improve the security posture.

 Access control options are enabled for new deployments for users to access their WorkSpaces from clients on Windows, MacOS, iOS, Android, ChromeOS, and Zero Clients. Access using Web Access or a Linux WorkSpaces client is not enabled by default for a new WorkSpaces deployment and will need to be enabled.

 If there are limits on corporate data access from trusted devices (also known as managed devices), WorkSpaces access can be restricted to trusted devices with valid certificates. When this feature is enabled, Amazon WorkSpaces uses certificate-based authentication to determine whether a device is trusted. If the WorkSpaces client application can't verify that a device is trusted, it blocks attempts to log in or reconnect from the device.

 Trusted device support is available for the following clients:
+  Amazon WorkSpaces Android Client app on [Google Play](https://play.google.com/store/apps/details?id=com.amazon.workspaces) that runs on Android and [Android-compatible Chrome OS devices](https://www.chromium.org/chromium-os/chrome-os-systems-supporting-android-apps)
+  Amazon WorkSpaces macOS Client app running on macOS devices
+  Amazon WorkSpaces Windows Client app running on Windows devices

 For more information about controlling which devices can access WorkSpaces, refer to [Restrict WorkSpaces Access to Trusted Devices](https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html).

**Note**
 Certificates for trusted devices apply only to Amazon WorkSpaces Windows, macOS, and Android clients. This feature does not apply to the Amazon WorkSpaces Web Access client, or any third-party clients, including but not limited to Teradici PCoIP software and mobile clients, Teradici PCoIP zero clients, RDP clients, and remote desktop applications.

## IP Access control groups
<a name="ip-access-control-groups"></a>

 Using IP address-based control groups, customers can define and manage groups of trusted IP addresses, and allow users to access their WorkSpaces only when they're connected to a trusted network. This feature helps customers gain greater control over their security posture.

 IP access control groups can be added at the WorkSpaces directory level. There are two ways to get started using IP access control groups.
+  **IP Access Controls page** — From the WorkSpaces management console, IP access control groups can be created on the **IP Access Controls** page. Rules can be added to these groups by entering the IP addresses or IP ranges from which WorkSpaces can be accessed. These groups can then be added to directories on the **Update Details** page.
+  **Workspace APIs** — WorkSpaces APIs can be used to create, delete, and view groups; create or delete access rules; or to add and remove groups from directories.

 For a detailed description of the using IP access control groups with the Amazon WorkSpaces encryption process, refer to [IP Access Control Groups for Your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-ip-access-control-groups.html).

## Monitoring or logging using Amazon CloudWatch
<a name="monitoring-or-logging-using-amazon-cloudwatch"></a>

 Monitoring network, servers, and logs is an integral part of any infrastructure. Customers who deploy Amazon WorkSpaces need to monitor their deployments, specifically the overall health and connection status of individual WorkSpaces.

### Amazon CloudWatch metrics for WorkSpaces
<a name="amazon-cloudwatch-metrics-for-workspaces"></a>

 CloudWatch metrics for WorkSpaces is designed to provide administrators with additional insight into the overall health and connection status of individual WorkSpaces. Metrics are available per WorkSpace, or aggregated for all WorkSpaces in an organization within a given directory.

 These metrics, like all CloudWatch metrics, can be viewed in the AWS Management Console (shown in the following figure), accessed via the CloudWatch APIs, and monitored by CloudWatch alarms and third-party tools.

![Screenshot of metrics in the console](https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/cloudwatch-metrics.png)

By default, the following metrics are enabled and are available at no extra cost:
+  **Available** — WorkSpaces that respond to a status check are counted in this metric.
+  **Unhealthy** — WorkSpaces that don’t respond to the same status check are counted in this metric.
+  **ConnectionAttempt** — The number of connection attempts made to a WorkSpace.
+  **ConnectionSuccess** — The number of successful connection attempts.
+  **ConnectionFailure** — The number of unsuccessful connection attempts.
+  **SessionLaunchTime** — The amount of time taken to initiate a session, as measured by the WorkSpaces client.
+  **InSessionLatency** — The round-trip time between the WorkSpaces client and WorkSpaces, as measured and reported by the client.
+  **SessionDisconnect** — The number of user-initiated and automatically closed sessions.

 Additionally, alarms can be created, as shown in the following figure.

![Screenshot showing a CloudWatch alarm for connection errors](https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/cloudwatch-alarm.png)

### Amazon CloudWatch Events for WorkSpaces
<a name="amazon-cloudwatch-events-for-workspaces"></a>

 Events from Amazon CloudWatch Events can be used to view, search, download, archive, analyze, and respond to successful logins to WorkSpaces. The service can monitor client WAN IP addresses, Operating System, WorkSpaces ID, and Directory ID information for users’ logins to WorkSpaces. For example, it can use events for the following purposes:
+  Store or archive WorkSpaces login events as logs for future reference, analyze the logs to look for patterns, and take action based on those patterns.
+  Use the WAN IP address to determine where users are logged in from, and then use policies to allow users access only to files or data from WorkSpaces that meet the access criteria found in the CloudWatch Event type of WorkSpaces Access.
+  Use policy controls to block access to files and applications from unauthorized IP addresses.

 For more information on how to use CloudWatch Events, refer to the [Amazon CloudWatch Events User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html). To learn more about CloudWatch Events for WorkSpaces, refer to [Monitor your WorkSpaces using Cloudwatch Events](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-events.html).

### YubiKey support for Amazon WorkSpaces
<a name="yubikey-support-for-amazon-workspaces"></a>

In order to add an additional security layer, customers often choose to secure tools and sites with multifactor authentication. Some customers choose to do this with a Yubico YubiKey. Amazon WorkSpaces supports both one-time passcodes (OTP) and FIDO U2F authentication protocol with YubiKeys.

 Amazon WorkSpaces currently supports OTP mode, and there are no additional steps required from an administrator or end user to utilize a YubiKey with OTP. The user can attach their YubiKey to their computer, ensure the keyboard is focused within the WorkSpace (specifically in the field where the OTP needs to be entered), and touch the gold contact on the YubiKey. The YubiKey will automatically enter the OTP into the selected field.

 In order to utilize FIDO U2F mode with YubiKey and WorkSpaces, additional steps are required. Ensure your users are issued one of these supported YubiKey models in order to utilize U2F redirection with WorkSpaces:
+  YubiKey 4
+  YubiKey 5 NFC
+  YubiKey 5 Nano
+  YubiKey 5C
+  YubiKey 5C Nano
+  YubiKey 5 NFC

**To enable USB redirection for YubiKey U2F**

 By default, USB redirection is disabled for PCoIP WorkSpaces; to utilize U2F mode with YubiKeys, you must enable it.

1.  Make sure that you've installed the most recent [WorkSpaces Group Policy administrative template for PCoIP (32-Bit)](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#gp_install_template_pcoip_32_bit) or [WorkSpaces Group Policy administrative template for PCoIP (64-Bit)](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#gp_install_template_pcoip_64_bit).

1.  On a directory administration WorkSpace or an Amazon EC2 instance that is joined to your WorkSpaces directory, open the Group Policy Management tool (**gpmc.msc**) and navigate to **PCoIP Session Variables**.

1.  To allow the user to override your setting, choose **Overridable Administrator Defaults**. Otherwise, choose **Not Overridable Administrator Defaults**.

1.  Open the Enable/disable USB in the PCOIP session setting.

1.  Choose **Enabled**, and then choose **OK**.

1.  Open the Configure PCoIP USB allowed and unallowed device rules setting.

1.  Choose **Enabled**, and under **Enter the USB authorization table (maximum ten rules)**, configure your USB device allow list rules.

   1.  Authorization rule - 110500407. This value is a combination of a Vendor ID (VID) and a Product ID (PID). The format for a VID/PID combination is `1xxxxyyyy`, where `xxxx` is the VID in hexadecimal format and `yyyy` is the PID in hexadecimal format. For this example, 1050 is the VID, and 0407 is the PID. For more YubiKey USB values, refer to [YubiKey USB ID Values](https://support.yubico.com/hc/en-us/articles/360016614920-YubiKey-USB-ID-Values).

1.  Under Enter the USB authorization table (maximum ten rules), configure your USB device blocklist rules.

   1. For **Unauthorization Rule**, set an empty string. This means that only USB devices in the authorization list are allowed.
**Note**
 You can define a maximum of 10 USB authorization rules and a maximum of 10 USB unauthorization rules. Use the vertical bar (\|) character to separate multiple rules. For detailed information about the authorization/unauthorization rules, refer to [Teradici PCoIP Standard Agent for Windows](https://www.teradici.com/web-help/pcoip_agent/standard_agent/windows/20.10/admin-guide/configuring/configuring/#pcoip-usb-allowed-and-unallowed-device-rules)

1.  Choose **OK**.

1.  The Group Policy setting change takes effect after the next Group Policy update for the WorkSpace and after the WorkSpace session is restarted. To apply the Group Policy changes, do one of the following:

   1.  Reboot the WorkSpace (in the Amazon WorkSpaces console, select the WorkSpace, then choose **Actions**, **Reboot WorkSpaces**).

   1.  In an administrative command prompt, enter gpupdate /force.

1.  After the setting takes effect, all supported USB devices will be able to be redirected to WorkSpaces unless restrictions are configured through the USB device rules setting.

 Once you have enabled USB redirection for YubiKey U2F you can utilize your YubiKey with Fido U2F mode.
