---
source_url: https://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/swift-environment-protection.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Requirement 1 - SWIFT environment protection
<a name="swift-environment-protection"></a>

## SWIFT environment protection
<a name="swift-environment-protection1"></a>

### Overall design for environment segmentation
<a name="overall-design-for-environment-segmentation"></a>

 SWIFT mandates the various connectivity components (messaging interface, SwiftNet link (SNL), hardware security model (HSM), SWIFT connector, jump server, operator PC) to be deployed in a “secure zone”: a segmented and controlled environment that is bounded to the CSP control framework. Several AWS services can help you design and implement the secure zone. The following sections detail recommendations and guidance to help you meet the CSP control objectives using a combination of different AWS services.

#### Scope of the secure zone
<a name="scope-of-the-secure-zone"></a>

![Example of a SWIFT secure zone architected by AWS .](https://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/images/swift-secure-zone.jpeg)

 SWIFT provides general guidance on which components should be in scope for the secure zone depending on the architecture the customers select to satisfy their business requirements. The preceding diagram shows an example of a SWIFT secure zone architected on AWS.

 From the perspective of environment segregation, customers should use a dedicated AWS Account that is governed by [AWS Organizations](https://aws.amazon.com/organizations/) for running the SWIFT secure zone in a production environment. From the [Well-Architected Security Pillar](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.pillar.security.en.html):

 “We recommend that you organize workloads in separate accounts and group accounts based on function, compliance requirements, or a common set of controls rather than mirroring your organization’s reporting structure. In AWS, accounts are a hard boundary, zero trust container for your resources. For example, account-level separation is strongly recommended for isolating production workloads from development and test workloads.”

 Account separation helps to ensure the ease of auditing and clear environment separation from back-office applications and other SWIFT connectivity stacks (Dev/Test).

 Another important aspect of the scoping is that the SWIFT secure zone should contain only the resources that are intended to be deployed and run. On the preventative side, you can leverage [AWS Organization Service Control Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCP) to restrict the resource instantiation to the intended AWS services. You can create a dedicated deployment [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) role with a least privilege policy and assign it to the infrastructure deployment pipeline to perform the infrastructure deployment.

 On the detective side, you can use [AWS Config](https://aws.amazon.com/config/) to help you detect drifts and alterations that have happened in the SWIFT secure zone, and you can monitor [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) for any unintended changes. If you use [AWS CloudFormation](https://aws.amazon.com/cloudformation/) for infrastructure as code deployment, you can leverage the drift detection functionality in CloudFormation to detect unintended deployment in the SWIFT secure zone.

 You can leverage a landing zone to manage and govern the SWIFT secure zone accounts. A landing zone is a well-architected, multi-account AWS environment that is scalable and secure. This is a starting point from which your organization can quickly launch and deploy workloads and applications with confidence in their security and infrastructure environment. Building a landing zone involves making technical and business decisions across account structure, networking, security, and access management in accordance with your organization’s growth and business goals for the future.

 You have a few options for creating your landing zone on AWS. You can choose a managed service to orchestrate your environment, or work with an AWS Partner to build your own. AWS offers [AWS Control Tower](https://aws.amazon.com/controltower/), a managed service that sets up a landing zone based on multi-account best practices, centralizes identity and access management, and establishes pre-configured governance rules for security and compliance.

#### Protection of the secure zone — boundary protection
<a name="protection-of-the-secure-zone-boundary-protection"></a>

 [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) enables you to provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. Security Groups act as a stateful firewall for resources within an Amazon VPC, controlling both inbound and outbound traffic at the virtual network interface. Security Groups can be used to restrict traffic by IP address, port, and protocol, and can help satisfy elements of CSP 1.1. By default, Security Groups allow all outbound connections; you are responsible for configuring specific outbound connection rules for CSP compliance. [Network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) (ACLs) are an additional layer of security for VPCs that acts as a stateless firewall for controlling traffic in and out of one or more subnets.

 For example, the [AWS Quick Start guide for SWIFT client connectivity](https://aws.amazon.com/quickstart/architecture/swift-client-connectivity/) provides these Security Groups:

* Table 1 – Security Groups in SWIFT on AWS Quick Start reference deployment *

|  Security Group  |  Inbound (Port)  |  Outbound (Port)  |
| --- | --- | --- |
|  Alliance Message Hub (AMH)  |  AMH Admin Desktop IP (8443)  |  SAG/SNL (48002/3), Amazon MQ (61617), RDS (1521)  |
|  Alliance Gateway (SAG) / SNL  |  AMH (48002/3)  |  SWIFT IP range (0-65536), HSM IPs (1792)  |
|  Amazon MQ  |  AMH (61617)  |  n/a  |
|  Amazon RDS  |  AMH (1521)  |  n/a  |
|  VPC Endpoint  |  AMH (443), SAG/SNL (443)  |  n/a  |

#### Access to the secure zone systems
<a name="access-to-the-secure-zone-systems"></a>

 Traditionally, jump servers are deployed to the SWIFT secure zone for accessing various SWIFT components. Creating, maintaining, managing access, security hardening, and patching on these jump servers becomes undifferentiated heavy lifting. Access to the secure zone systems is simplified with [AWS System Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html), as it removes the need for the jump server in the secure zone. Session Manager is a fully managed AWS capability that enables you to manage your Amazon EC2 instances, on-premises instances, and virtual machines (VMs) through an interactive, one-click, browser-based shell, or through the AWS Command Line Interface (AWS CLI) without the need for a [bastion](https://aws.amazon.com/blogs/security/tag/bastion-host/) or jump server.

 If you prefer a traditional jump server setup and GUI access, [Amazon WorkSpaces](https://aws.amazon.com/workspaces/) is the preferred choice. Amazon WorkSpaces enables you to provision virtual, cloud- based Microsoft Windows or Amazon Linux desktops, called Workspaces, for your users. Amazon WorkSpaces eliminates the need to procure and deploy hardware or install complex software. You can quickly add or remove users as your needs change. Users can access their virtual desktops from multiple devices or web browsers. This Amazon Workspace virtual desktop would be deployed to the secure zone VPC and act as a bastion host to access the rest of the secure zone’s components. This virtual desktop can be restricted such that it can be accessed through the corporate network only. For example, you could use IP access control to only allow certain IP addresses to access the virtual desktop. Refer to [How to secure your Amazon WorkSpaces for external users](https://aws.amazon.com/blogs/security/how-to-secure-your-amazon-workspaces-for-external-users/). Various components in the SWIFT secure zone can be accessed from the virtual desktop.

#### Segregation from general enterprise IT services
<a name="segregation-from-general-enterprise-it-services"></a>

 The guidance of using your AWS account to achieve segregation is detailed in the [Scope of the secure zone](#scope-of-the-secure-zone) section of this document.

## Operating system privileged account control
<a name="operating-system-privileged-account-control"></a>

 The goal for this control is to prevent individual users from having excess privilege to exploit the operating system on the host. The general best practice is to prevent human access to the EC2 host directly, except in a break glass situation. (“Break glass” refers to a quick means for a person who does not have access privileges to gain access when necessary.)

 Ideally, installation and configuration of the SWIFT software should not be run manually on the EC2 host itself. Software installation should be done through an automated AMI pipeline. Per the Well-Architected Framework: [Financial Service Industry Lens](https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/use-immutable-infrastructure-with-no-human-access.html):

 “Adopt immutable infrastructure practices with no human access to better meet your audit and compliance needs. You will be able to version control your infrastructure and handling failure will be a routine and continuous way of doing business.”

 You can leverage [Amazon EC2 Image Builder](https://aws.amazon.com/image-builder/) as part of the AMI pipeline implementation for building the SWIFT application AMIs. If regular operation and maintenance tasks are required to be performed on the EC2 host, AWS Systems Manager Document Automation and Run Command can be used. Proper IAM role and least privilege policies should be assigned for individuals or groups who need to perform such functions.

## Virtualization platform protection
<a name="virtualization-platform-protection"></a>

 Customer environments are logically segregated to prevent users and customers from accessing resources not assigned to them. You maintain full control over who has access to your data. Services such as EC2, that provide virtualized operational environments, ensure that customers are segregated from one another and prevent cross-tenant privilege escalation and information disclosure via [hypervisors](https://en.wikipedia.org/wiki/Hypervisor#%3A~%3Atext%3DA%20hypervisor%20(or%20virtual%20machine%2Cis%20called%20a%20guest%20machine) and instance isolation.

 Different instances running on the same physical machine are isolated from each other via the hypervisor. The Amazon EC2 firewall resides within the hypervisor layer, between the physical network interface and the instance's virtual interface. All packets must pass through this layer, so an instance’s neighbors have no more access to that instance than to any other host on the internet, and can be treated as if they are on separate physical hosts. The physical random access memory (RAM) is separated using similar mechanisms.

 Customer instances have no access to physical disk devices, but instead are presented with virtualized disks. The AWS proprietary disk virtualization layer automatically erases every block of storage before making it available for use, which protects one customer’s data from being unintentionally exposed to another. Customers can further protect their data using traditional file system encryption mechanisms, or, in the case of [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) volumes, by enabling AWS managed disk encryption.

 The [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) is the underlying platform for the next generation of EC2 instances that enable AWS to innovate faster, further reduce cost for customers, and deliver added benefits such as increased security and new instance types.

 The Nitro System provides enhanced security that continuously monitors, protects, and verifies the instance hardware and firmware. Virtualization resources are offloaded to dedicated hardware and software, minimizing the attack surface. Nitro System's security model is locked down and prohibits administrative access, eliminating the possibility of human error and tampering.

 [Nitro is currently available across many different EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances).

## Restriction of internet access
<a name="restriction-of-internet-access"></a>

 This control objective is designed to limit exposure to an internet-based attack. This is a common security control, and best practice for many organizations. There are many well-established patterns to restrict internet access.

 One simple measure that can help you meet this control objective is to completely disable internet access for the SWIFT secure zone. The SWIFT secure zone can be operated without internet access. In AWS terms, the VPC in the secure zone does not have an internet gateway attached to the VPC. An SCP can be implemented to disallow internet gateway and prevent additional components for getting internet access. Refer to the example service control policy, [prevent any VPC that doesn't already have internet access from getting it](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html#examples_vpc).

 If internet access is required, customers can consider leveraging different traffic filtering solutions like [Gateway Load Balancer](https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/), [AWS Network Firewall](https://aws.amazon.com/network-firewall/), or open-source [Squid proxy](https://aws.amazon.com/blogs/security/how-to-add-dns-filtering-to-your-nat-instance-with-squid/). These solutions can filter unnecessary egress traffic to the internet and prevent unintentional internet ingress traffic.

 Advanced adversaries may attempt to use DNS-based [data exfiltration](https://en.wikipedia.org/wiki/Data_exfiltration) to leak data or perform command and control within a VPC that is otherwise removed from the internet. Use [Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html) to control internet name resolution, in conjunction with Amazon GuardDuty rules for DNS tunneling. [Amazon Route 53 Resolver DNS Firewall](https://aws.amazon.com/blogs/aws/how-to-get-started-with-amazon-route-53-resolver-dns-firewall-for-amazon-vpc/) is a managed firewall that enables customers to block DNS queries made for known malicious domains and to allow queries for trusted domains. DNS Firewall provides more granular control over the DNS querying behavior of resources within your Amazon VPCs.

 [Amazon GuardDuty](https://aws.amazon.com/guardduty/) is a continuous security monitoring service that analyzes and processes the following [data sources](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html#guardduty_data-sources.title):
+  VPC Flow Logs
+  AWS CloudTrail management event logs
+  CloudTrail S3 data event logs
+  DNS logs

 If you use AWS DNS resolvers for your EC2 instances (the default setting), then GuardDuty can access and process your request and response DNS logs through the internal AWS DNS resolvers. For example, the `Trojan:EC2/DNSDataExfiltration` ([https://docs.aws.amazon.com/guardduty/latest/ug/guardduty\_finding-types-ec2.html\#trojan-ec2-dnsdataexfiltration](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-dnsdataexfiltration)) finding informs you that the listed EC2 instance in your AWS environment is running malware that uses DNS queries for outbound data transfers.
