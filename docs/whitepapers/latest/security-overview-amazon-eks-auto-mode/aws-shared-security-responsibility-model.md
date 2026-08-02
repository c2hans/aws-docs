---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-eks-auto-mode/aws-shared-security-responsibility-model.html
---

# AWS Shared Security Responsibility Model
<a name="aws-shared-security-responsibility-model"></a>

Security and compliance is a shared responsibility between AWS and the customer. The [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) can help relieve the customer's operational burden because AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates.

With EKS Auto Mode, AWS is responsible for the configuration, patching, and health of the EC2 instances so that customers can focus on the [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc) and cluster configuration, and the application containers that they are running.

EKS Auto Mode accomplishes this by using [EC2 managed](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.html) instances. Using managed instances, customers can delegate operational control over the instances to the Amazon EKS service. EKS is then responsible for patching the components that are delivered as part of the AMI. This combines with the 21-day maximum node lifetime for Auto Mode, so that nodes are regularly replaced with newer nodes running the most recently released version of the AMI, containing the latest patches.

![Figure 2: Shared Responsibility Model with EKS Auto Mode](http://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-eks-auto-mode/images/image2.jpg)

Figure 1: Shared Responsibility Model with EKS Auto Mode
