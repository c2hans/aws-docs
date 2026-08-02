---
source_url: https://docs.aws.amazon.com/whitepapers/latest/applying-security-practices-to-network-workload-for-csps/example-architecture-1.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Example architecture \#1
<a name="example-architecture-1"></a>

 An example architecture of a 5GC workload running in an AWS Region. The 5G Control Plane and User Plane are running in the Region and interconnected with an on-premises environment.

![Network architecture diagram showing public and private subnets, NAT gateways, and on-premises connections for 5G workloads.](http://docs.aws.amazon.com/whitepapers/latest/applying-security-practices-to-network-workload-for-csps/images/architecture-5g-core.png)

**Security description of the AWS services used in the example architecture of 5G core deployment on the Region:**

1.  [AWS Direct Connect](https://aws.amazon.com/directconnect) instances are physical links that connect the customer’s on-premises network to AWS over a standard Ethernet fiber-optic cable. AWS Direct Connect connections support MACsec to encrypt data between on-premises facilities to the AWS Direct Connect location. MAC Security (MACsec) is an IEEE standard that provides data confidentiality, data integrity, and data origin authenticity. Network traffic is to be encrypted over an AWS Direct Connect line using IPSEC or TLS encryption, as indicated on 3GPP TS 33.210, to secure a network domain.

1.  *VPC routing tables* are route tables used to control where network traffic is directed. Customers can remove direct routing towards the internet from the compute nodes.

1.  Traffic going in and out of the instances are filtered using [security groups](https://docs.aws.amazon.com/managedservices/latest/userguide/about-security-groups.html). Security groups are stateful firewall rules that filter inbound traffic based on source address. In addition, there are network ACL rules that can filter traffic on a subnet level. Network ACLs are stateless firewall rules.

1.  Nitro hardware-based instances are the compute or worker nodes where applications or network functions are deployed.

1.  Persistent data at rest stored in EBS volumes are encrypted by a data key managed by AWS KMS. This verifies that data such as CDRs and subscriber profiles are protected.

1.  Access to AWS services that do not reside inside the VPC is through VPC endpoints. These are endpoints that enable you to privately connect to an AWS service without traversing the internet.

1.  Use [AWS Key Management Service](https://aws.amazon.com/kms) for management of encryption keys — AWS KMS supports BYOK. Alternatively, connect to on-premises HSM using AWS KMS XKS.

1.  Use [AWS Certificate Manager](https://aws.amazon.com/certificate-manager) to manage imported SSL/TLS certificates. Certificates are for encrypting data in transit to support 3GPP TS 33.210.

1.  Snapshots, [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) , manifest files, or backup data can be stored in Amazon S3 storage. Data at rest is encrypted using AWS KMS, and access to data is restricted with IAM policies.

1.  [Amazon EKS](https://aws.amazon.com/eks) is used for Kubernetes-based container orchestration. Amazon EKS is a service used to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes. For more information on security concepts using EKS, refer to [Security in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/security).

1.  [Amazon ECR](https://aws.amazon.com/ecr) is used to store container images. Amazon ECR can also be used to scan images for security vulnerabilities. Images are encrypted using AWS KMS.

1.  [AWS CloudTrail](https://aws.amazon.com/cloudtrail) helps enable governance and supports operational and risk auditing of an AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs.

1.  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) monitors AWS resources and applications that run on AWS in near real-time. Amazon CloudWatch can be used to collect and track metrics, which are variables that can be measured for resources and applications. Logs from Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) firewall applications can be forwarded to CloudWatch and can be used for future investigations.

1.  [AWS AppConfig](https://aws.amazon.com/config) provides a detailed view of the configuration of AWS resources in an AWS account. This includes how the resources are related to one another, and how they were configured in the past so that customers can see how the configurations and relationships change over time. AWS Config rules are used to evaluate the configuration settings of AWS resources. When AWS Config detects that a resource violates the conditions in one of its rules, AWS Config flags the resource as non-compliant and sends a notification. AWS Config nearly continuously evaluates AWS resources as they are created, changed, or deleted. As an example, AWS Config can detect changes in the security groups and flag them as non-compliant.

1.  [Amazon CloudFront](https://aws.amazon.com/cloudformation) is an infrastructure as a code (IaaC) service that helps set up AWS resources automatically. Using IaaC templates helps eliminate human errors caused by manually configuring resources, security and networking rules.

1.  [AWS Identity and Access Management](https://aws.amazon.com/iam) helps to securely control access to AWS resources. IAM is used to control who is authenticated (signed in) and authorized (has permissions) to use AWS resources.

1.  [AWS WAF](https://aws.amazon.com/waf) is a firewall that helps protect application endpoints or APIs against common web exploits and bots that may affect availability, compromise security, or consume excessive resources.

1.  [AWS Control Tower](https://aws.amazon.com/controltower) provides the simplest way to set up and govern a secure, multi-account AWS environment.

1.  A customer-owned on-premises HSM generates cryptographic keys for importing to AWS KMS, or use with AWS KMS XKS.

1.  Customer security gateways (SEGs) are entities on the borders of the IP security domains used for securing native IP-based protocols.

1.  Virtual routing and forwarding (VRF) devices, virtual router, and forwarding devices are used to segregate the VPN.
