---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/high-density-deployments.html
---

# High-density deployments without Elastic IPs
<a name="high-density-deployments"></a>

If you need highly dense deployments, then you can operate in the performance metrics and these applications do not require the use of Elastic IPs. This is referred to as an "alien IP."

An alien IP is a network or subnet range that is external to the VPC CIDR block and to which F5 maps virtual services. Alien IP addresses do not work in all scenarios, but can be used for a high density of virtual servers. Before an alien IP can be used, the following resources are required.
+ One subnet to host the applications
+ An F5 BIG-IP deployment with a Cloud Failover Extension to manage the routes
+ A route in the AWS route tables pointing to the elastic network interfaces

Using alien IP addresses does have implications for how you interconnect VPCs to other VPCs, as well as how you can interconnect VPCs to your data centers. The following diagram helps determine if an alien IP address is required.

![Process flow for identifying if you require an alien IP address.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/images/guide-img/migration-f5-big-ip/images/F5-alien-address.png)
