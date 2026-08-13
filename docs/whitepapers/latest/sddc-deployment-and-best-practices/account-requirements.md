---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/account-requirements.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Account requirements
<a name="account-requirements"></a>

**Topics**
+ [AWS account](#aws-account)
+ [VMware Customer Connect account](#myvmware-account)
+ [VMware Cloud on AWS account](#vmware-cloud-on-aws-account)
+ [Infrastructure preparation and planning](#infrastructure-preparation-and-planning)

## AWS account
<a name="aws-account"></a>

 One of the requirements of VMware Cloud on AWS is that all deployed SDDCs must be linked to your AWS account. If you have a pre-existing account, you can use it for this purpose. If you don’t have an AWS account, see [How do I create and activate a new AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) for instructions.

**Important**
After an AWS account has been associated with a VMware Organization as the seller of record, the AWS account number cannot be updated. There can be only one AWS seller of record per VMware Organization.

 Once you have an AWS account, ensure that all technical personnel have been added to the account and that they have been configured with the permissions necessary to properly manage the account. At minimum, there must be one user within the AWS account who has sufficient permissions to run the [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template, which performs account linking to the SDDC.

 When creating a stack, AWS CloudFormation makes underlying service calls to AWS to provision and configure your resources. You can use [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/) (IAM) to manage permissions.

### AWS account management: explore AWS Organizations
<a name="aws-account-management-explore-aws-organizations"></a>

 AWS accounts that host the Connected VPC can belong to [AWS Organizations](https://aws.amazon.com/organizations/). This enables you to centrally govern your AWS Cloud resources.

 If you are using AWS Organizations, you should determine which accounts you want to associate with VMware Cloud on AWS in advance. You can then create an [organization unit (OU)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) and associate those accounts with the account identified for VMware Cloud on AWS.

 The [Connected VPC](https://aws.amazon.com/blogs/apn/account-and-vpc-considerations-for-vmware-cloud-on-aws/) or AWS customer account is owned, operated, and paid for directly by the you, if you choose to utilize any AWS services within that account. To successfully attach the AWS customer-owned account to the SDDC, the AWS account should have at least one VPC within that account. This attachment enables you to use native AWS services to compliment whatever service you use to run on VMware Cloud on AWS.

### Multi-account governance: AWS Control Tower and Landing Zones
<a name="multi-account-governance-aws-control-tower-and-landing-zones"></a>

 You may want to utilize [AWS Control Tower](https://aws.amazon.com/controltower/) to manage the AWS Organization to enforce governance across multi-account environments. In this scenario, create a separate OU for the account to use with VMware Cloud on AWS. On the OU, ensure the guardrail rules you put into place do not restrict CloudFormation from creating the necessary resources in the connected VPC.

 The CloudFormation template used by VMware has the prefix `vmware-sddc-formation`. The CloudFormation stack does the following in the connected VPC within the connected account:
+  It creates immutable IAM roles in the VPC; namely `RemoteRole`, `RemoteRolePlayer`, `RemoveRoleService`, and `BasicLambdaRole`.
+  It creates an IAM policy called `AmazonVPCCrossAccountNetworkOperations` for the above roles.
+  It creates [AWS Lambda](https://aws.amazon.com/lambda/) functions for event notifications.

 whether you use AWS Organizations or AWS Control Tower with landing zones, you need to configure your policies to allow the account that will be associated with VMware Cloud on AWS to complete these operations in the VPC.

### Standalone accounts
<a name="standalone-accounts"></a>

 Standalone accounts can be added to an AWS Organizations or AWS Control Tower landing zone later. When using standalone accounts, ensure you have set your governance policies to allow you to run any native AWS service you may require in your connected VPC.

## VMware Customer Connect account
<a name="myvmware-account"></a>

 You will require a VMware Customer Connect (formerly MyVMware) profile to access the VMware Cloud on AWS service. If you do not have a profile, you can create one at [VMware Customer Connect](https://customerconnect.vmware.com/home).

 Once created, ensure that your account is up-to-date and all required fields are filled in. If required fields are missing, you will not be able to create your first SDDC.

## VMware Cloud on AWS account
<a name="vmware-cloud-on-aws-account"></a>

 During the deal process, your Cloud Sales Specialist or Client Executive requests that you identify a Fund Owner and a Fund User. After your deal is processed, a service welcome email is sent to the Fund Owner and Fund User. This email contains the link you must use to sign up for a VMware Cloud on AWS account. This link can be used only once. The link will redirect you to the VMware Cloud Services Portal (CSP) website where you can log in into the VMware Cloud on AWS service using your VMware Customer Connect credentials.

 VMware Cloud on AWS accounts are based on an Organization, which corresponds to a group or line of business subscribed to VMware Cloud on AWS services. Your VMware Customer Connect account is used to create the Organization and will make you an Organization Owner. Organizational Owners are assigned the Organization Owner’s role and have complete administrative access to their Organization. They grant roles to access the Organization and its services, manage billing and subscription, and file support requests. New users can be assigned the Organization Owner role or the Organization Member role. Both types of users can manage the SDDC cloud, but only those with the Organizational Owner role can invite more users.

 VMware Cloud on AWS has its own set of roles within IAM that need to be enabled manually:
+  Administrator
+  Administrator (delete restricted)
+  NSX Cloud Administrator
+  NSX Cloud Auditor

 The major tasks performed by Organization users include, but are not limited to:
+  Adding hosts to the SDDC
+  Removing hosts from the SDDC
+  Configuring the management network for vCenter access / administration: VPN, DNS, Firewall rules
+  Configuring and maintaining the compute network for workloads: logical networks, firewall rules, NAT, VPN, DNS, Public IP addresses

## Infrastructure preparation and planning
<a name="infrastructure-preparation-and-planning"></a>

 Before you begin, examine the deployment requirements as specified in the following table.

* Table 1 — Design considerations*

<table>
<tbody>
  <tr><td> <b>Area </b></td><td> <b>Description</b> </td></tr>
  <tr><td> Region </td><td> VMware Cloud on AWS isn’t currently supported in all AWS Regions. For a current list of supported Regions for VMware Cloud on AWS, see <a href="https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/com.vmware.vmc-aws-operations/GUID-9708C514-30FE-4D75-A3E4-E358166EEB1F.html">Available AWS Regions</a>. </td></tr>
  <tr><td> Availability Zone (AZ) </td><td> It is good practice to deploy the SDDC to the same Region and AZ as your current or planned native AWS workloads. Traffic between the SDDC and the AWS resources in the same AZ as your customer-owned VPC will not incur cross-AZ traffic charges. Traffic between different AZs in the same Region is billable to the customer-owned AWS account. This is according to the standard <a href="https://aws.amazon.com/pricing/">pricing</a> of AWS. </td></tr>
  <tr><td> VPC and subnet </td><td> Within a Region, a <a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html">VPC and subnet</a> are required to facilitate cross-account linking to the SDDC. Here are some things to consider when selecting these resources: <ul><li>  A new or existing VPC can be leveraged as the Connected VPC. This provides the SDDC with high bandwidth and low latency access to native AWS services.  </li><li>  When <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html#create_vpc">creating new VPC</a>, consider a unique <a href="https://www.ipaddressguide.com/cidr">IPv4 CIDR</a> block which is non-overlapping with the SDDC. This is particularly important if you will be connecting your AWS VPC via a VPN or Direct Connect to your on-premises environment.  </li><li>  The subnet must be in an AWS AZ where VMware Cloud on AWS is available. Start by creating a subnet in every AZ in the AWS Region where the SDDC will be created. This helps you identify all AZs where an SDDC can be deployed, and select the one that best meets your SDDC placement needs. You may want to keep your VMC workloads close to or isolated from your AWS workloads running in a particular AZ, depending on your organization’s security requirements,  <br /> See <a href="https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#AddaSubnet">Creating a subnet in Your VPC</a> to learn how to use the Amazon VPC console to create a subnet in your VPC.  </li><li> As part of the SDDC deployment, a series of <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html">Elastic network interfaces</a> (ENIs) are created for use by the hosts of the SDDC. An ENI is a high bandwidth, private, and dedicated connection which resides inside the customer VPC. An AWS subnet is required to facilitate the account linking. </li><li>  The linked AWS account must have sufficient capacity to create a minimum of 17 ENIs per SDDC cluster in each Region where an SDDC is deployed. Although you cannot provision more than 16 hosts in a cluster, SDDC operations, including planned maintenance and <a href="https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/com.vmware.vmc-aws-operations/GUID-81BD6D29-EB69-4EFF-8060-71ACE4C8F51F.html">Elastic DRS</a>, can require AWS to temporarily add as many as 16 more hosts, so AWS recommends using an AWS account that has sufficient capacity for 34 ENIs per SDDC per Region.  </li><li>  AWS recommends dedicating a /26-CIDR block for each SDDC. Do not use that subnet for any other AWS services or <a href="https://aws.amazon.com/ec2/">Amazon Elastic Compute Cloud</a> (Amazon EC2) instances. Because some of the IP addresses in this block are reserved for internal use, a /26 CIDR block is the smallest subnet that can accommodate the addresses required for an SDDC.  </li><li>  The subnet must exist in the AWS account and not be shared from another account.  </li></ul></td></tr>
  <tr><td> VPC route table </td><td> When VMware Cloud on AWS is connected to your VPC, it always uses the main route table in the VPC. The main route table should be dedicated to VMware Cloud on AWS. Where applicable, the route table is updated by VMware with new networks created within the SDDC. <br /> There are scenarios where customers create separate route tables within a VPC for different reasons. In these instances, remember that the custom route table will <b>not</b> be automatically updated when the main route table is updated based on any network changes within the SDDC. You’ll have to manually update the custom route table in the connected VPC. </td></tr>
  <tr><td> Security groups </td><td> The Cross-account ENIs exist within the customer-owned AWS account, and you have full access to apply security groups to the ENIs, which should otherwise not be touched. These actions can permanently undermine connectivity between the AWS environment and the SDDC. These can be identified in the AWS console with the description <i><b>VMware VMC Interface DO NOT USE</b></i>. </td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">Resources</a> </td><td> If necessary, request <a href="https://console.aws.amazon.com/servicequotas/home?region=us-east-2#!/">service quota increases</a> for the following resources. You might need to do this if an existing deployment uses these resources, and you might exceed the default quotas with this deployment. The <a href="https://console.aws.amazon.com/servicequotas/home?region=us-east-2#!/">Service Quotas console</a> displays your usage and quotas. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">AWS service quotas</a>. The deployment requires the following:
<table>
<thead>
  <tr><th> Resource </th><th> This deployment uses </th></tr>
</thead>
<tbody>
  <tr><td> VPCs </td><td> 1 </td></tr>
  <tr><td> Subnet </td><td> 1 </td></tr>
  <tr><td> ENIs </td><td> 17 </td></tr>
  <tr><td> Route Table </td><td> 1 </td></tr>
</tbody>
</table>
</td></tr>
  <tr><td> IAM permissions </td><td> For a summary of the permissions required to run the CloudFormation template, see <a href="https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/com.vmware.vmc-aws-operations/GUID-DE8E80A3-5EED-474C-AECD-D30534926615.html">AWS Roles and Permissions</a>. Some of the initial permissions required to create the SDDC are removed from the role after the SDDC is has created. These can be seen in the <a href="appendix.md">Appendix</a> of this document. </td></tr>
  <tr><td> SDDC management IP planning </td><td> When you create an SDDC, you are required to specify an IP range for your management network. This IP address range cannot be changed after the SDDC is created. As a result, it is critical to carefully plan out this IP range. In single-AZ deployment, a /23 CIDR can support 27 ESXi hosts, while a /20 can support up to 251, and a /16 up to 4091, but the number of hosts is currently limited to the SDDC maximum of 300. When deploying a multi-AZ (or stretched cluster) SDDC, the limits are 22 hosts, 246 hosts, and the SDDC maximum hosts for /23, /20 and /16 CIDRs, respectively.  <ul><li>  <b>Size</b> — The range needs to be large enough to facilitate all hosts which will be deployed on day one, but also must account for future growth.  </li><li>  <b>Uniqueness</b> — You should provision an IP range which is unique within your organization. This is particularly important if you will be connecting to your SDDC via a VPN or <a href="https://aws.amazon.com/directconnect/">AWS Direct Connect</a>, or if you are cross-linking to a production VPC or other SDDCs.  </li><li>  <b>Ability to summarize</b> — Ideally this block should be a subnet of some larger space which is allocated to the SDDC as a whole. By subnetting a larger dedicated supernet, you will gain the ability to simplify routing between your on-premises environment and the SDDC, and you will potentially simplify network security policies used to secure the SDDC.  </li></ul></td></tr>
  <tr><td> SDDC compute IP planning </td><td> To provision compute workloads within the SDDC, you must create at least one compute network segment. Although it is not required to provision an SDDC, VMware recommends allocating at least one IP address range for the SDDC compute network. After the SDDC has been provisioned, you can create a network segment using this address range. <br /> Compute networks are used for all VM traffic within the SDDC and are defined as individual segments in NSX. VMware Cloud on AWS supports three types of logical network segments: routed, extended, and disconnected. <ul><li>  <b>Routed</b> — Has connectivity to other logical networks in the SDDC and, through the SDDC firewall, to external networks. This is the only segment type that supports DHCP.  </li><li>  <b>Extended</b> — Extends an existing <a href="https://en.wikipedia.org/wiki/Layer_2_MPLS_VPN">Layer 2 MPLS VPN</a> (L2VPN) tunnel, providing a single IP address space that spans the SDDC and an on-premises network.  </li><li>  <b>Disconnected</b> — has no uplink and provides an isolated network accessible only to VMs connected to it. Disconnected segments are created when needed by <a href="https://www.vmware.com/products/hcx.html">VMware HCX</a>.  </li></ul></td></tr>
  <tr><td> Prepare DNS strategy </td><td> VMware Cloud on AWS customers have many options to implement hybrid DNS solutions, ranging from self-hosted to fully managed native services from AWS. <br /> <b>Considerations</b>: <br /> Google DNS servers are set up initially when the SDDC is first deployed. <br /> NSX-T Tier 1 gateways, the management gateway (MGW) and the compute gateway (CGW) in VMware Cloud on AWS, act only as forwarders, relaying the queries from VMs to the actual DNS servers specified. The devices also cache the responses, improving performance. DNS servers configured under the MGW DNS Forwarder are used by the management components such as vCenter to resolve the on-premises fully qualified domain names (FQDNs). Features such as Hybrid Linked Mode (HLM) or Site Recovery may not work until the customer-managed DNS servers are configured here, as the management VMs using Google DNS cannot resolve the on-premises resources by default. <br /> <b>On-premises DNS servers</b> <br /> This is an option for customers who have on-premises DNS servers they wish to leverage. The benefit of this setup is that you can quickly get started, but because the SDDC VMs send DNS queries back to these servers over a IPSEC VPN or Direct Connect (Private VIF), you should be aware that a potential latency can be introduced. <br /> The subnets containing these DNS servers must be permitted or advertised over VPN or Direct Connect. This makes them dependent on the network connectivity. In addition to the network connectivity, both firewalls (VMware Cloud on AWS and the on-premises firewall) must allow DNS traffic UDP/53 and TCP/53). Both the primary and secondary DNS servers should be reachable and provide consistent results. <br /> <b>Local DNS servers</b> <br /> In this configuration, DNS servers reside in one or more logical networks of the VMware Cloud on AWS SDDC. To avoid single points of failure and to prevent traffic going back to the on-premises data center, ensure that additional DNS servers are available in the cloud SDDC. Placing local AD/DNS servers in the SDDC could be a preferred method for increased availability and performance because workloads are catered locally. <br /> If you are syncing with on-premises AD/DNS, both primary and secondary DNS servers should be reachable and provide consistent results. Subnets containing these DNS servers must be permitted or advertised over VPN or Direct Connect along with the firewalls configured to allow DNS traffic (UDP/53 &amp; TCP/53) on the MGW of the SDDC. <br /> <b>DNS server in AWS</b> <br /> In this configuration, customers can leverage DNS servers that reside in AWS. Examples of this are Amazon EC2 instances with DNS configured, or making use of Amazon DNS services. This is useful for customers who already use DNS in their AWS environment. The benefit of this is you can take advantage of cross-VPC connectivity. Take into considerations the DNS design with VMC and the following DNS options, as described in <a href="https://aws.amazon.com/blogs/apn/choosing-the-right-dns-architecture-for-vmware-cloud-on-aws/">this blog</a>. </td></tr>
  <tr><td> Summary of IP Planning </td><td> The following table is an example of how to plan your IP addresses and subnets. <br /> For customers planning to deploy multiple SDDCs, it is important to ensure the CIDRs do not overlap. <br /> When deploying SDDCs into different AZs and subnets, ensure that you plan properly using unique subnets on each site.
<table>
<thead>
  <tr><th> Component </th><th> Value </th><th> </th></tr>
</thead>
<tbody>
  <tr><td> AWS Region </td><td> Frankfurt </td><td> </td></tr>
  <tr><td> VPC Name </td><td> VMC-VPC </td><td> </td></tr>
  <tr><td> VPC CIDR Block </td><td> 172.31.0.0/16 </td><td> </td></tr>
  <tr><td> SDDC Name </td><td> VMC-SDDC01 </td><td> </td></tr>
  <tr><td> SDDC Management CIDR block </td><td> 10.3.0.0/16 </td><td> </td></tr>
  <tr><td> Subnet Purpose </td><td> Availability Zone A </td><td> Availability Zone B </td></tr>
  <tr><td> Connected SDDC </td><td> 172.31.1.0/24 </td><td> 172.31.2.0/24 </td></tr>
</tbody>
</table>
</td></tr>
  <tr><td> NTP planning </td><td> Ensure that your on-premises data center and your cloud SDDC are synchronized to an NTP service or other authoritative time source. </td></tr>
  <tr><td> Security audit </td><td> Because VMware Cloud requires certain permissions within the customer-owned AWS account, you may be required to perform a security audit prior to onboarding. Most typically, security auditors want to review the <a href="https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/com.vmware.vmc-aws-operations/GUID-DE8E80A3-5EED-474C-AECD-D30534926615.html">CloudFormation template</a> used by VMware Cloud. </td></tr>
  <tr><td> Release notes </td><td> VMware Cloud on AWS is able to release new features at a faster pace than traditional on premises software products. Check the release notes page frequently to keep updated on the new features that have been released. <br /> Bookmark the <a href="https://docs.vmware.com/en/VMware-Cloud-on-AWS/0/rn/vmc-on-aws-relnotes.html">VMware Cloud on AWS release notes</a> page. </td></tr>
  <tr><td> Service alerts </td><td> The VMware Cloud Operations team posts updates on planned maintenance events, maintenance start and end times, and service incidents on the VMware Cloud Services status page. <br /> Bookmark the <a href="https://status.vmware-services.io/">VMware Cloud Services Status page</a>. <br /> (Optional) Subscribe to receive real time alerts and updates. </td></tr>
  <tr><td> Service Level Agreement (SLA) </td><td> The Service Level Agreement (SLA) for VMware Cloud on AWS defines the service components that have an availability commitment as well as their associated targets. <br /> You may be eligible for an SLA credit if one of the service components is unavailable and breaches the target SLA. The amount of the SLA credit you may be eligible for is dependent on the monthly uptime percentage for the affected availability component. <br /> Read and bookmark the <a href="https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/support/vmw-cloud-aws-service-level-agreement.pdf">Service Level Agreement for VMware Cloud on AWS</a>. </td></tr>
</tbody>
</table>
