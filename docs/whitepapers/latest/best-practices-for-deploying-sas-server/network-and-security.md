---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/network-and-security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Network and security
<a name="network-and-security"></a>

 This section covers network and security considerations for SAS deployment on AWS.

 SAS 9.4 can be deployed within a customer’s VPC within a private subnet containing the required EC2 instances and permanent storages devices.

 A public subnet can contain a NAT Gateway that allows instances in a private subnet to connect to the internet or other AWS services, while also preventing outside internet connection to the SAS server.

 A bastion host can be placed within the public subnet, with security group rules, to allow transfix between the public bastion host and the SAS servers placed in the private subnet.

 Internet Gateway can be used for connectivity between the internet and SAS Servers in a VPC for hosting public websites

![Diagram that shows the SAS 9.4 intelligence platform architecture on AWS.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/images/sas-intelligence-platform-on-aws.jpeg)
