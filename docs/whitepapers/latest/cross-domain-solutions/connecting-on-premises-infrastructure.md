---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cross-domain-solutions/connecting-on-premises-infrastructure.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Connecting On-Premises Infrastructure
<a name="connecting-on-premises-infrastructure"></a>

 AWS provides service offerings to help you connect your existing on-premises infrastructures. As noted earlier, you can use many of the same services on premises. One service that is useful for on-premises is AWS Direct Connect.

## AWS Direct Connect
<a name="aws-direct-connect"></a>

 Using AWS Direct Connect, you can establish private connectivity between AWS and your datacenter, office, or colocation environment. AWS Direct Connect enables you to establish a dedicated network connection between your network and one of the AWS Direct Connect locations. Using industry standard 802.1q VLANs, this dedicated connection can be partitioned into multiple virtual interfaces. This enables you to use the same connection to access public resources, such as objects stored in Amazon S3 using public IP address space, and private resources such as Amazon EC2 instances running within Amazon VPC using private IP address space, while maintaining network separation between the public and private environments.

 You can reconfigure virtual interfaces at any time to meet your changing needs.
