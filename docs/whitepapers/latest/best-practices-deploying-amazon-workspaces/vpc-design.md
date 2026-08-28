---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/vpc-design.html
---

# VPC design
<a name="vpc-design"></a>

 This section describes best practices for sizing your VPC and subnets, traffic flow, and implications for directory services design.

 Here are a few things to consider when designing the VPC, subnets, security groups, routing policies, and network access control lists (ACLs) for your Amazon WorkSpaces so that you can build your WorkSpaces environment for scale, security, and ease of management:
+  **VPC** — We recommend using a separate VPC specifically for your WorkSpaces deployment. With a separate VPC, you can specify the necessary governance and security guardrails for your WorkSpaces by creating traffic separation.
+  **Directory Services** — Each Directory Service construct requires a pair of subnets that provides a highly available directory service split between AZs.
+  **Subnet size** — WorkSpaces deployments are tied to a directory construct and reside in the same VPC as your chosen Directory Service, but they can be in different VPC subnets. A few considerations:
  +  Subnet sizes are permanent and cannot change. You should leave ample room for future growth.
  +  You can specify a default security group for your chosen Directory Service. The security group applies to all WorkSpaces that are associated with the specific Directory Service construct.
  +  You can have multiple instances of Directory Service use the same subnet.

 Consider future plans when you design your VPC. For example, you might want to add management components, such as an antivirus server, a patch management server, or an AD or RADIUS MFA server. It’s worth planning for additional available IP addresses in your VPC design to accommodate such requirements.

 For in-depth guidance and considerations for VPC design and subnet sizing, refer to the re:Invent presentation [How Amazon.com is Moving to Amazon WorkSpaces](https://www.youtube.com/watch?v=kawZBGCLBJU).

## Network interfaces
<a name="network-interfaces"></a>

 Each WorkSpaces has two elastic network interfaces (ENIs), a management network interface (`eth0`), and a primary network interface (`eth1`). AWS uses the management network interface to manage the WorkSpace — it’s the interface on which your client connection terminates. AWS uses a private IP address range for this interface. For network routing to work properly, you can’t use this private address space on any network that can communicate with your WorkSpaces VPC.

 For a list of the private IP ranges that are used on a per Region basis, refer to [Amazon WorkSpaces Details](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html#management-ip-ranges).

**Note**
 Amazon WorkSpaces and their associated management network interfaces do not reside in your VPC, and you cannot view the management network interface or the Amazon Elastic Compute Cloud (Amazon EC2) instance ID in your AWS Management Console (refer to [Figure 5](scenario-1-using-ad-connector-to-proxy-authentication-to-on-premises-active-directory-service.md#fig5), [Figure 6](scenario-2-extending-on-premises-ad-ds-into-aws-replica.md#fig6), and [Figure 7](scenario-3-standalone-isolated-deployment-using-aws-directory-service-in-the-aws-cloud.md#fig7)). However, you can view and modify the security group settings of your primary network interface (`eth1`) in the console. The primary network interface of each WorkSpace does count toward your ENI Amazon EC2 resource quotas. For large deployments of Amazon WorkSpaces, you need to open a support ticket via the AWS Management Console to increase your ENI quotas.

## Traffic flow
<a name="traffic-flow"></a>

 You can break down Amazon WorkSpaces traffic into two main components:
+  The traffic between the client device and the Amazon WorkSpaces service.
+  The traffic between the Amazon WorkSpaces service and customer network traffic.

 The next section discusses both of these components.

## Client device to WorkSpace
<a name="client-device-to-workspace"></a>

 Regardless of its location (on-premises or remote), the device running the Amazon WorkSpaces client uses the same two ports for connectivity to the Amazon WorkSpaces service. The client uses port 443 (HTTPS port) for all authentication and session-related information, and port 4172 (PCoIP port), with both Transmission Control Protocol (TCP) and User Datagram Protocol (UDP), for pixel streaming to a given WorkSpace and network health checks. Traffic on both ports is encrypted. Port 443 traffic is used for authentication and session information and uses TLS for encrypting the traffic. Pixel streaming traffic uses AES-256-bit encryption for communication between the client and `eth0` of the WorkSpace, via the streaming gateway. More information can be found in the [Security](security.md) section of this document.

 We publish per-region IP ranges of our PCoIP streaming gateways and network health check endpoints. You can limit outbound traffic on port 4172 from your corporate network to the AWS streaming gateway and network health check endpoints by allowing only outbound traffic on port 4172 to the specific AWS Regions in which you’re using Amazon WorkSpaces. For the IP ranges and network health check endpoints, refer to [Amazon WorkSpaces PCoIP Gateway IP Ranges](https://aws.amazon.com/about-aws/whats-new/2015/09/amazon-workspaces-pcoip-gateway-ip-ranges/).

 The Amazon WorkSpaces client has a built-in network status check. This utility shows users whether their network can support a connection by way of a status indicator on the bottom right of the application. The following figure shows a more detailed view of the network status can be accessed by choosing **Network** on the top-right side of the client.

![Image showing WorkSpaces client browser network check window](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/workspaces-client-network-check.png)

A user initiates a connection from their client to the Amazon WorkSpaces service by supplying their login information for the directory used by the Directory Service construct, typically their corporate directory. The login information is sent via HTTPS to the authentication gateways of the Amazon WorkSpaces service in the Region where the WorkSpace is located. The authentication gateway of the Amazon WorkSpaces service then forwards the traffic to the specific AWS Directory Service construct associated with your WorkSpace.

 For example, when using the AD Connector, the AD Connector forwards the authentication request directly to your AD service, which could be on-premises or in an AWS VPC. For more information, refer to the [AD DS Deployment Scenarios](ad-ds-deployment-scenarios.md) section of this document. The AD Connector does not store any authentication information, and it acts as a stateless proxy. As a result, it’s imperative that the AD Connector has connectivity to an AD server. The AD Connector determines which AD server to connect to by using the DNS servers that you define when you create the AD Connector.

 If you’re using an AD Connector and you have MFA enabled on the directory, the MFA token is checked before the directory service authentication. Should the MFA validation fail, the user’s login information is not forwarded to your AWS Directory Service.

 Once a user is authenticated, the streaming traffic starts by using port 4172 (PCoIP port) through the AWS streaming gateway to the WorkSpace. Session-related information is still exchanged via HTTPS throughout the session. The streaming traffic uses the first ENI on the WorkSpace (`eth0` on the WorkSpace) that is not connected to your VPC. The network connection from the streaming gateway to the ENI is managed by AWS. In the event of a connection failure from the streaming gateways to the WorkSpaces streaming ENI, a CloudWatch event is generated. For more information, refer to the [Monitoring or Logging Using Amazon CloudWatch](security.md#monitoring-or-logging-using-amazon-cloudwatch) section of this document.

 The amount of data sent between the Amazon WorkSpaces service and the client depends on the level of pixel activity. To ensure an optimal experience for users, we recommend that the round-trip time (RTT) between the WorkSpaces client and the AWS Region where your WorkSpaces are located is less than 100 milliseconds (ms). Typically, this means your WorkSpaces client is located less than two thousand miles from the Region in which the WorkSpace is being hosted. The [Connection Health Check](https://clients.amazonworkspaces.com/Health.html) webpage can help you determine the most optimal AWS Region to connect to the Amazon WorkSpaces service.

## Amazon WorkSpaces Service to VPC
<a name="amazon-workspaces-service-to-vpc"></a>

 After a connection is authenticated from a client to a WorkSpace and streaming traffic is initiated, your WorkSpaces client will display either a Windows or Linux desktop (your Amazon WorkSpace) that is connected to your virtual private cloud (VPC), and your network should show that you have established that connection. The WorkSpace’s primary Elastic Network Interface (ENI), identified as `eth1`, will have an IP address assigned to it from the Dynamic Host Configuration Protocol (DHCP) service that is provided by your VPC, typically from the same subnets as your AWS Directory Service. The IP address stays with the WorkSpace for the duration of the life of the WorkSpace. The ENI in your VPC has access to any resource in the VPC, and to any network you have connected to your VPC (via a VPC peering, an AWS Direct Connect connection, or VPN connection).

 ENI access to your network resources is determined by the route table of the subnet and default security group that your AWS Directory Service configures for each WorkSpace, as well any additional security groups that you assign to the ENI. You can add security groups to the ENI facing your VPC at any time by using the AWS Management Console or AWS CLI. (For more information on security groups, refer to [Security Groups for Your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-security-groups.html).) In addition to security groups, you can use your preferred host-based firewall on a given WorkSpace to limit network access to resources within the VPC.

It is recommended to create your DHCP options set with the DNS Server IP(s) and fully qualified domain names that are authoritative to your Active Directory specific to your environment, then assign those [custom created DHCP options set to the Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html#DHCPOptionSet) used by Amazon WorkSpaces. By default, [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) (Amazon VPC) uses AWS DNS instead of your directory service DNS. Using a DHCP options set will ensure proper DNS name resolution and consistent configuration of your internal DNS name servers for not only your WorkSpaces, but any supporting workload(s) or instance(s) you may have planned for your deployment.

 When DHCP Options are applied, there are two important differences in how they will be applied to WorkSpaces in comparison to how they are applied with traditional EC2 instances:
+  The first difference is how DHCP Option DNS suffixes will be applied. Each WorkSpace has DNS settings configured for its network adapter with the *Append primary and connection specific DNS suffixes* and *Append parent suffixes of the primary DNS suffix* options enabled. The configuration will be updated with the DNS suffix configured within the AWS Directory Service you registered and associated with the WorkSpace by default. Also, if the DNS suffix configured within the DHCP Options Set used is different, it will be added and applied to any associated WorkSpaces.
+  The second difference is that the configured DHCP Option DNS IPs will **not** be applied to the WorkSpace due to the Amazon WorkSpaces service prioritizing the Domain Controllers IP addresses of the configured directory.

 Alternatively, you can configure a Route 53 private hosted zone to support a hybrid or split DNS environment and obtain proper DNS resolution for your Amazon WorkSpaces environment. For more information, refer to [Hybrid Cloud DNS Options for VPC](https://d1.awsstatic.com/whitepapers/hybrid-cloud-dns-options-for-vpc.pdf) and [AWS Hybrid DNS with Active Directory](https://d1.awsstatic.com/whitepapers/aws-hybrid-dns-with-active-directory.pdf).

**Note**
 Each WorkSpace must refresh the IP table when applying a new or different DHCP option set to the VPC. To refresh, you can run *ipconfig /renew* or reboot any WorkSpace(s) in the VPC configured with your updated DHCP options set. If you are using AD Connector, and update the IP addresses of your connected IP addresses/domain controllers, you must then update the Skylight `DomainJoinDNS` registry key on your WorkSpaces. It’s recommended to do this via a GPO. The path to this registry key is `HKLM:\SOFTWARE\Amazon\Skylight`. The value of this `REG_SZ` is not updated if the AD Connector's DNS settings are modified, and VPC DHCP Option Sets will not update this key either.

 The figure in the [AD DS Deployment Scenarios](ad-ds-deployment-scenarios.md) section of this whitepaper shows the traffic flow described.

As explained previously, the Amazon WorkSpaces service prioritizes the Domain Controller IP addresses of the configured Directory for DNS resolution, and ignores the DNS servers configured in your DHCP options set. If you need to have more granular control over your DNS server settings for your Amazon WorkSpaces, you can use the instructions to update DNS servers for Amazon WorkSpaces in the [Update DNS servers for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-dns-server.html) guide of the *Amazon WorkSpaces Administration Guide*.

If your WorkSpaces need to resolve other services in AWS, and if you’re using the [ default DHCP options set](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html) with your VPC, your Domain Controller DNS service in this VPC must therefore be configured to use DNS forwarding, pointing to the [Amazon DNS server](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#AmazonDNS) with the IP address at the base of your VPC CIDR plus two; that is, if your VPC CIDR is 10.0.0.0/24, you configure DNS forwarding to use the standard Route 53 DNS Resolver at 10.0.0.2.

In case your WorkSpaces require DNS resolution of resources on your on-premises network, you may use a [Route 53 Resolver Outbound Endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html), create a Route 53 Forwarding rule, and associate this rule with the VPCs requiring this DNS resolution. If you have configured the forwarding on your Domain Controller DNS service to the default Route 53 DNS Resolver of your VPC as explained in the previous paragraph, the DNS resolution process can be found in the [Resolving DNS queries between VPCs and your network ](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) guide of the *Amazon Route 53 Developer Guide*.

If you are using the default DHCP options set, and you require other hosts in your VPCs that are not part of your Active Directory domain to be able to resolve hostnames in your Active Directory namespace, you can use this Route 53 Resolver Outbound Endpoint, and add another Route 53 Forwarding rule that forwards DNS queries for your Active Directory domain to your Active Directory DNS servers. This Route 53 Forwarding rule will have to be associated with the Route 53 Resolver Outbound Endpoint that is able to reach your Active Directory DNS service, and with all VPCs that you want to enable to resolve DNS records in your WorkSpaces Active Directory domain.

Similarly, a [Route 53 Resolver Inbound Endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) can be used to allow DNS resolution of DNS records of your WorkSpaces Active Directory domain from your on-premises network.

![Image showing WorkSpaces DNS resolution](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/workspaces-route-53-dns-resolution.png)

+ Your Amazon WorkSpaces will use the AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) DNS service for DNS resolution. The AWS Managed Microsoft AD DNS service resolves the `example.aws` domain, and forwards all other DNS queries to the default Route 53 DNS Resolver at the VPC CIDR base IP address \+2 to enable DNS resolution

  The Shared Services VPC contains a Route 53 Outbound Resolver endpoint, which is associated with two Route 53 Forwarding rules. One of these rules forwards DNS queries for the `example.com` domain to the on-premises DNS servers. The second rule forwards DNS queries for your AWS Managed Microsoft AD domain `example.aws` to your Active Directory DNS service in the Shared Services VPC.

  With this architecture, your Amazon WorkSpaces will be able to resolve DNS queries for the following:
  + Your AWS Managed Microsoft AD domain `example.aws`.
  + EC2 instances in the domain configured with your default DHCP options set (for example, `host1.eu-west-1.compute.internal`) as well as other AWS services or endpoints.
  + Hosts and services in your on-premises domain, such as `host3.example.com`.
+ • The other EC2 workloads in the Shared Services VPC (`host1.eu-west-1.compute.internal`) and in the WorkSpaces VPC (`host2.eu-west-1.compute.internal`) can do the same DNS resolutions as your WorkSpaces, as long as the Route 53 Forwarding rules are associated with both VPCs. DNS resolution for the `example.aws` domain will in this case go via the default Route 53 DNS Resolver at the VPC CIDR base IP address \+2, which per configured and associated Route 53 Forwarding rules will forward them via the Route 53 Resolver Outbound Endpoint to the WorkSpaces Active Directory DNS service.
+ • Finally, an on-premises client can also do the same DNS resolution, since the on-premises DNS Server is configured with conditional forwarders for the `example.aws` and `eu-west-1.compute.internal` domains, forwarding DNS queries for these domains to the Route 53 Resolver Inbound Endpoint IP addresses.

## Example of a typical configuration
<a name="example-of-a-typical-configuration"></a>

 Let’s consider a scenario where you have two types of users and your AWS Directory Service uses a centralized AD for user authentication:
+  **Workers who need full access from anywhere** (for example, full-time employees) — These users will have full access to the internet and the internal network, and they will pass through a firewall from the VPC to the on-premises network.
+  **Workers who should have only restricted access from inside the corporate network** (for example, contractors and consultants) — These users have restricted internet access through a proxy server to specific websites in the VPC, and will have limited network access in the VPC and to the on-premises network.

 You’d like to give full-time employees the ability to have local administrator access on their WorkSpace to install software, and you would like to enforce two-factor authentication with MFA. You also want to allow full-time employees to access the internet without restrictions from their WorkSpace.

 For contractors, you want to block local administrator access so that they can only use specific pre-installed applications. You want to apply restrictive network access controls using security groups for these WorkSpaces. You need to open ports 80 and 443 to specific internal websites only, and you want to entirely block their access to the internet.

 In this scenario, there are two completely different types of user personas with different requirements for network and desktop access. It’s a best practice to manage and configure their WorkSpaces differently. You will need to create two AD Connectors, one for each user persona. Each AD Connector requires two subnets that have enough IP addresses available to meet your WorkSpaces usage growth estimates.

**Note**
 Each AWS VPC subnet consumes five IP addresses (the first four and the last IP address) for management purposes, and each AD Connector consumes one IP address in each subnet in which it persists.

 Further considerations for this scenario are as follows:
+  AWS VPC subnets should be private subnets, so that traffic, such as internet access, can be controlled through either a Network Address Translation (NAT) Gateway, Proxy-NAT server in the cloud, or routed back through your on-premises traffic management system.
+  A firewall is in place for all VPC traffic bound for the on-premises network.
+  Microsoft AD server and the MFA RADIUS servers are either on-premises (refer to [Scenario 1: Using AD Connector to Proxy Authentication to On-Premises AD DS](scenario-1-using-ad-connector-to-proxy-authentication-to-on-premises-active-directory-service.md) in this document) or part of the AWS Cloud implementation (refer to [Scenario 2](scenario-2-extending-on-premises-ad-ds-into-aws-replica.md) and [Scenario 3](scenario-3-standalone-isolated-deployment-using-aws-directory-service-in-the-aws-cloud.md), AD DS Deployment Scenarios, in this document).

 Given that all WorkSpaces are granted some form of internet access, and given that they are hosted in a private subnet, you also must create public subnets that can access the internet through an internet gateway. You need a NAT gateway for the full-time employees, allowing them to access the internet, and a Proxy-NAT server for the consultants and contractors, to limit their access to specific internal websites. To plan for failure, design for high availability, and limit cross-AZ traffic charges, you should have two NAT gateways and NAT or proxy servers in two different subnets in a multi-AZ deployment. The two AZs that you select as public subnets will match the two AZs that you use for your WorkSpaces subnets, in regions that have more than two zones. You can route all traffic from each WorkSpaces AZ to the corresponding public subnet to limit cross-AZ traffic charges and provide easier management. The following figure shows the VPC configuration.

![Sample architecture showing an example VPC configuration with NAT gateway](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/high-level-vpc-design.png)

 The following information describes how to configure the two different WorkSpaces types:

 **To configure WorkSpaces for full-time employees**:

1.  In the Amazon WorkSpaces Management Console, choose the **Directories** option on the menu bar.

1.  Choose the directory that hosts your full-time employees.

1.  Choose Local Administrator Setting.

 By enabling this option, any newly created WorkSpace will have local administrator privileges. To grant internet access, configure NAT for outbound internet access from your VPC. To enable MFA, you need to specify a RADIUS server, server IPs, ports, and a pre-shared key.

 For full-time employees’ WorkSpaces, inbound traffic to the WorkSpace can be limited to Remote Desktop Protocol (RDP) from the Helpdesk subnet by applying a default security group via the AD Connector settings.

 **To configure WorkSpaces for contractors and consultants**:

1.  In the Amazon WorkSpaces Management Console, disable **Internet Access** and the **Local Administrator** setting.

1.  Add a security group under the **Security Group** settings section to enforce a security group for all new WorkSpaces created under that directory.

 For consultants’ WorkSpaces, limit outbound and inbound traffic to the WorkSpaces by applying a default Security group via the AD Connector settings to all WorkSpaces associated with the AD Connector. The security group prevents outbound access from the WorkSpaces to anything other than HTTP and HTTPS traffic, and inbound traffic to RDP from the Helpdesk subnet in the on-premises network.

**Note**
 The security group applies only to the ENI that is in the VPC (`eth1` on the WorkSpace), and access to the WorkSpace from the WorkSpaces client is not restricted as a result of a security group. The following figure shows the final WorkSpaces VPC design.

![Sample architecture showing an example of a final WorkSpaces VPC design.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/workspaces-design-user-personas.png)

## AWS Directory Service
<a name="aws-directory-service"></a>

 As mentioned in the introduction, AWS Directory Service is a core component of Amazon WorkSpaces. With AWS Directory Service, you can create three types of directories with Amazon WorkSpaces:
+  [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) is a managed Microsoft AD, powered by Windows Server 2012 R2. AWS Managed Microsoft AD is available in Standard or Enterprise Edition.
+  [Simple AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html) is standalone, Microsoft AD-compatible, managed directory service powered by Samba 4.
+  [AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html) is a directory proxy for redirecting authentication requests and user or group lookups to your existing on-premises Microsoft AD.

 The following section describes communication flows for authentication between the Amazon WorkSpaces brokerage service and AWS Directory Service, best practices for implementing WorkSpaces with AWS Directory Service, and advanced concepts, such as MFA. It also discusses infrastructure architecture concepts for Amazon WorkSpaces at scale, requirements on Amazon VPC, and AWS Directory Service, including integration with on-premises Microsoft AD Domain Services (AD DS).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
