---
source_url: https://docs.aws.amazon.com/whitepapers/latest/deploying-oracle-soa-suite-12c/securing-your-environment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Securing your environment
<a name="securing-your-environment"></a>

 AWS provides a secure global infrastructure, plus a range of features that you can use to help secure your systems and data in the cloud. To learn more about AWS Security, refer to the [AWS Security Center](https://aws.amazon.com/security/).

## AWS security group configuration
<a name="aws-security-group-configuration"></a>

 A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. For each security group, you add rules that control the inbound traffic to instances, and a separate set of rules that control the outbound traffic. For more information on security groups, refer to [Amazon EC2 security groups for Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html).

 The following table includes some of the recommended security group rules related to Oracle SOA Suite 12c. This list is not an exhaustive list of inbound rules it is only meant to serve as a reference.

 *Table 2: Suggested Security Group rules for Oracle SOA Suite 12c *

|  Security Group  |  Inbound traffic type  |  Inbound port (example\*)  |
| --- | --- | --- |
|  Load Balancer Security Group  |  ELB http  |  80  |
|   |  ELB https (SSL)  |  443  |
|  Application Security Group  |  SOA Admin Server  |  7001  |
|   |  SOA Managed servers  |  7003, 7005, 7007  |
|   |  OSB Admin server  |  8001  |
|   |  OSB Managed servers  |  8003  |
|   |  ADF Admin server  |  9001  |
|   |  ADF Managed servers  |  9003, 9005  |
|   |  BPM Admin Server  |  10001  |
|   |  BPM Managed Servers  |  10003, 10005, 10007  |
|   |  Any other SOA component  |  <Add as per your configuration>  |
|   |  Oracle Coherence port  |  9991  |
|   |  WebLogic Node manager  |  5555 - 5558  |
|  Database Security Group  |  Oracle Database  |  1521  |
|  Web Security Group  |  Oracle HTTP Server (OHS)  |  7777  |

 *\*The port numbers might change depending on your configuration.*
