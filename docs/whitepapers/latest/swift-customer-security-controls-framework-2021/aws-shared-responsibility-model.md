---
source_url: https://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/aws-shared-responsibility-model.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Shared Responsibility model
<a name="aws-shared-responsibility-model"></a>

 Security and Compliance is a [shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) between AWS and the customer. This shared model can help relieve the customer’s operational burden as AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates.

![A diagram depicting the AWS Shared Responsibility security model.](http://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/images/shared-responsibility.jpeg)

 AWS is responsible for the security and compliance **of** the cloud, or the infrastructure that runs all of the services offered in the AWS Cloud. Cloud security at AWS is the highest priority. AWS customers benefit from a data center and network architecture that are built to meet the requirements of the most security-sensitive organizations and compliance frameworks. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services. This includes controls that maintain separation between customer resources and data, along with numerous other administrative, compliance, and security-related controls.

 Customers are responsible for the security and compliance **in** the cloud, or the customer-configured systems and services provisioned on AWS. The customer assumes responsibility and management of the guest operating system (including updates and security patches) and other associated application software, as well as the configuration of the AWS-provided security group firewall. This includes, but is not limited to, the following, as the customer’s responsibility will depend on the services used, the integration of those services into their IT environment, and applicable laws and regulations:
+  Customers are responsible for the compliant configuration of all system components, to include AWS resources and services, included in or connected to their cardholder data environments (CDE).
+  Customers are responsible for the operating systems and installed applications on [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2), and network routing and configuration of associated virtual networking components.
