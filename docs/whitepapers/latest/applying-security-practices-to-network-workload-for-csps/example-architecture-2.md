---
source_url: https://docs.aws.amazon.com/whitepapers/latest/applying-security-practices-to-network-workload-for-csps/example-architecture-2.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Example architecture \#2
<a name="example-architecture-2"></a>

An example architecture of a 5GC workload with AWS Outposts. The 5G control plane and user plane are running on-premises.

![5GC architecture with control plane in AWS Region and user plane on AWS Outposts premises.](http://docs.aws.amazon.com/whitepapers/latest/applying-security-practices-to-network-workload-for-csps/images/architecture-5g-core-outposts.png)

**Security description of the example architecture of 5G core network function on AWS Outposts: **

1.  *VPC routing tables*. As an example, customers can direct the user plane or internet traffic to on-premises network using the AWS Outposts local gateway.

1.  Traffic going in and out of the instances are filtered using security groups.  In addition, there are network ACL rules that can filter traffic on a subnet level. Network ACLs are stateless firewall rules.

1.  Nitro hardware-based instances.

1.  Persistent data at rest stored in EBS volumes.

1.  Access to AWS services that do not reside inside the VPC is through VPC endpoints.

1.  Snapshots, AMIs, manifest files, or backup data can be stored in Amazon S3 storage. Data at rest is encrypted using AWS KMS, and access to data can be restricted with IAM policies.

1.  AWS Direct Connect instances.

1.  AWS KMS for management of encryption keys.

1.  AWS Certificate Manager to manage imported SSL/TLS certificates.

1.  Amazon ECR is used to store container images.

1.  Amazon EKS service is used for Kubernetes-based container orchestration.

1.  AWS CloudTrail helps enable governance, and supports operational and risk auditing of an AWS account.

1.  Amazon CloudWatch monitors AWS resources and applications that run on AWS in near real-time.

1.  AWS Config provides a detailed view of the configuration of AWS resources in an AWS account.

1.  AWS CloudFormation helps set up AWS resources automatically.

1.  AWS WAF helps protect application endpoints or APIs against common web exploits and bots.

1.  AWS IAM helps to securely control access to AWS resources.

1.  AWS Control Tower provides a simple way to set up and govern a secure, multi-account AWS environment.

1.  VRF devices, virtual router, and forwarding devices are used to segregate the VPN.

1.  Customer SEGs are entities on the borders of the IP security domains used for securing native IP based protocols.

1.  Customer owned on-premises HSM to generate cryptographic keys for importing to AWS KMS or use with AWS KMS XKS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
