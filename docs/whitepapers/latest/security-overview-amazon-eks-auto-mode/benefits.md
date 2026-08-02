---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-eks-auto-mode/benefits.html
---

# Benefits
<a name="benefits"></a>

EKS Auto Mode is a new operating model for Amazon EKS. In addition to the reduced operational responsibility, there are several technical changes to further improve the security posture of Auto Mode nodes.
+ **EC2 managed instances:** EKS Auto Mode uses [Amazon Elastic Compute Cloud (Amazon EC2) managed instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.html) to provide the compute that backs an Auto Mode node. This allows Auto Mode to provide the full breadth of Amazon EC2 capabilities while delegating operational control to Amazon EKS.
+ **Minimal container optimized OS:** The operating system used on Auto Mode nodes is a variant of [Bottlerocket](https://aws.amazon.com/bottlerocket/), which is optimized solely for running containers.
+ **Minimal permissions on the node role:** Auto Mode has been designed to require fewer permissions on the node's [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) role.
+ **Amazon EKS managed compute, networking, and storage capabilities**: Auto Mode provides managed capabilities for these functions, which shifts the responsibility for health and patching of the components that normally provide them to AWS.
+ **Frequent patching**: AWS is responsible for patching the components hosted on AWS infrastructure and the components in the Auto Mode node Amazon Machine Image (AMI).
+ **Limited node lifetime:** It's a best practice to treat Kubernetes nodes as ephemeral compute providers. Auto Mode builds upon that by stopping nodes from living longer than 21 days.
