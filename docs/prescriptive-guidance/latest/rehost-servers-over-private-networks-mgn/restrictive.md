---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/restrictive.html
---

# Replication over private networks only
<a name="restrictive"></a>

The following diagram displays the architecture of the most restrictive scenario, where all traffic goes over the private channel (AWS VPN or AWS Direct Connect) between the source environment and AWS.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/images/guide-img/db816b63-918e-424c-861e-0630fc54fedf/images/e7418ef1-d0ff-4c73-aa2c-00c6bb1a8dad.png)

The main components of this architecture are:
+ *Source environment* in the corporate data center (on the left). This is the environment to migrate from.
+ *Staging environment* in AWS with private virtual private cloud (VPC) and subnet (in the middle). This is the environment that AWS Transform MGN will use to create replication-related resources. These resources might include replication servers, conversion servers, and related Amazon Elastic Block Store (Amazon EBS) volumes and their Amazon Simple Storage Service (Amazon S3) snapshots.
+ *VPN connection* from the source environment to the staging VPC and subnet(s) to handle three types of traffic:
  + HTTPS/TCP port 443 for API communication
  + TCP port 1500 for data transfer
  + Domain Name System (DNS) traffic over UDP port 53
+ *Target environment* in AWS (on the right). This can be a completely isolated VPC or a subnet in the staging environment.
**Note**
There's no network connectivity requirement from the staging environment subnet to the target subnets.
+ *Amazon VPC interface endpoints* for MGN, Amazon Elastic Compute Cloud (Amazon EC2), and Amazon S3 created in the staging environment, and an *Amazon S3 VPC gateway endpoint* that is accessible from the staging subnet.
+ And finally, [DNS resolver inbound endpoint ](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-network-to-vpc)in the staging subnet. This is required for the source systems to resolve the fully qualified domain names (FQDNs) of the VPC endpoints into private IPs.
