---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/vpc.html
---

# Amazon Virtual Private Cloud
<a name="vpc"></a>

[Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you've defined. This virtual network resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

Consider the following encryption best practices for this service:
+ Encrypt traffic between information assets and systems within the corporate network and VPCs by using one of the following:
  + AWS Site-to-Site VPN connections
  + A combination of AWS Site-to-Site VPN and AWS Direct Connect connections, which provides an IPsec-encrypted private connection
  + AWS Direct Connect connections that support MAC Security (MACsec) to encrypt data from corporate networks to the AWS Direct Connect location
+ Use VPC endpoints in AWS PrivateLink to privately connect your VPCs to supported AWS services without using an internet gateway. You can use AWS Direct Connect or Site-to-Site VPN services to establish this connection. Traffic between your VPC and the other service does not leave the AWS network. For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html).
+ Configure [security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html) that allow traffic only from ports associated with secure protocols, such as HTTPS over TCP/443. Periodically audit security groups and their rules.
