---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-outbound-network-traffic/restricting-outbound-traffic.html
---

# Restricting a VPC's outbound traffic
<a name="restricting-outbound-traffic"></a>

## Restricting a VPC's outbound traffic by using security groups
<a name="restricting-outbound-traffic-security-groups"></a>

After you assess your architecture's outbound traffic requirements, start modifying your VPC's security group rules to meet your organization's security needs. Make sure that you add all of the necessary ports, protocols, and destination IP addresses to your security groups' allow lists.

For instructions, see [Control traffic to resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon VPC User Guide*.

**Important**
After updating your VPC's security group rules in your test environment, make sure that you confirm your application is still operating as expected. For more information, see the **Best practices for analyzing your VPC's outbound traffic when using VPC Flow Logs **section of this guide.

### Key security group considerations for specific AWS services
<a name="key-security-group-considerations-for-specific-aws-services.7204f38a-93fe-5e4d-b28c-461c3c05e1a1"></a>

**Amazon Elastic Compute Cloud (Amazon EC2)**

When you create a VPC, it comes with a [default security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/default-custom-security-groups.html#default-security-group) that allows all outbound traffic. Amazon Elastic Compute Cloud (Amazon EC2) instances use this default security group unless you create your own [custom security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/default-custom-security-groups.html#creating-your-own-security-groups).

**Important**
To mitigate the risk of your Amazon EC2 instance using the default security group unintentionally, remove all the group's outbound rules. For more information, see **Delete security group rules** in the [Work with security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#working-with-security-group-rules) section of the *Amazon VPC User Guide*.

**Amazon Relational Database Service (Amazon RDS)**

All outbound security group rules for an Amazon RDS DB instance can be removed unless the database acts as a client. For more information, see [Overview of VPC security groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html#Overview.RDSSecurityGroups.VPCSec) in the *Amazon RDS User Guide*.

**Amazon ElastiCache**

All outbound security group rules for Amazon ElastiCache (Redis OSS) and Amazon ElastiCache (Memcached) instances can be removed unless the instance acts as a client. For more information, see the following:
+ [Security groups: EC2-Classic](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/SecurityGroups.html) (*Amazon ElastiCache (Redis OSS) User Guide*)
+ [Understanding ElastiCache and Amazon VPCs](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/VPCs.EC.html) (*Amazon ElastiCache (Memcached) User Guide*)

## Restricting a VPC's outbound traffic by using AWS Network Firewall and DNS hostnames
<a name="restricting-outbound-traffic-network-firewall-hostnames"></a>

When an application uses dynamic IP addresses, it's a best practice to filter its VPC's outbound traffic by using DNS hostnames instead of IP addresses. For example, if an application is using an Application Load Balancer, the application's associated IP addresses will change because the nodes continually scale. In this type of situation, it's more secure to use DNS hostnames to filter outbound network traffic than static IP addresses.

You can use [AWS Network Firewall](https://aws.amazon.com/network-firewall/) to restrict your VPC's outbound internet access to a set of hostnames provided by the [Server Name Indication (SNI)](https://https.cio.gov/sni/) in the HTTPS traffic.

For more information and example Network Firewall policy rules, see [Domain filtering](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-examples.html#suricata-example-domain-filtering) in the *AWS Network Firewall Developer Guide*. For detailed instructions, see the following AWS Prescriptive Guidance (APG) pattern: [Use Network Firewall to capture the DNS domain names from the Server Name Indication (SNI) for outbound traffic](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic.html).

**Note**
SNI is an extension to TLS that remains unencrypted in the traffic flow. It indicates the destination hostname a client is attempting to access over HTTPS.

**Important**
After updating the Network Firewall stateful rules in your test environment, make sure that your application is still working as expected. Make sure that none of the necessary DNS domain names provided by the SNI are blocked.

### Architecture example
<a name="architecture-example.a02c8282-349f-5b3e-ba7d-2048c9417a70"></a>

The following diagram shows an example architecture for using AWS Network Firewall to filter a VPC's outbound traffic using DNS hostnames:

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-outbound-network-traffic/images/guide-img/bce22483-dc0a-4eb3-b027-d2b6a2a1a92a/images/32feaac9-8496-4718-86c8-3ea25291597d.png)

The diagram shows the following workflow:

1. The outbound request originates within the private subnet and is sent to the NAT gateway in the protected subnet.

1. The HTTPS traffic received by the NAT gateway is routed to an AWS Network Firewall endpoint in the public subnet.

1. AWS Network Firewall inspects the request and applies the configured firewall policy rules to either accept or decline the request to pass to the internet gateway.

1. Approved outbound requests are sent to the internet gateway.

1. Approved traffic from the internet gateway is sent to the internet to access the intended URL (provided by SNI in the non-encrypted HTTPS header).
