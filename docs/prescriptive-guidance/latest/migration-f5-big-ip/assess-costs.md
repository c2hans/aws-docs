---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/assess-costs.html
---

# Evaluating migration costs and skills PDF RSS
<a name="assess-costs"></a>

Before you decide to migrate your F5 BIG-IP security and traffic management solutions to the AWS Cloud, you need to assess the costs of the migration and evaluate what skills are required.

The following sections provide a summary of potential migration costs, as well as an overview of the knowledge of AWS and F5 products and services that your team will need.

**Topics**
+ [Assessing license and instance costs](#assess-license-and-instances-costs)
+ [Evaluating AWS and F5 knowledge base](#evaluate-team-skills-expertise)

## Assessing license and instance costs
<a name="assess-license-and-instances-costs"></a>

The cost of running F5 BIG-IP workloads in the AWS Cloud will vary based on your combined license and instance costs. When you migrate to the AWS Cloud, you will need to match your existing licenses and turn on features from your source system to the destination system.

F5 products have multiple license models, but your business and technical requirements will typically intersect with the following models: Bring Your Own License (BYOL), marketplace, private offer, subscription, and enterprise license agreements (ELA).

The migration cost will also vary depending on if you use pay-as-you-go, annually priced instances, or have an individual agreement with AWS. Importantly, the cost of an F5 license can also change based on the model and your individual requirements.

You can use the [AWS Pricing Calculator](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/getting-started.html) to estimate your potential running cost. The following three examples provide insight into the costs of AWS instances and infrastructure.
+ [F5 BIG-IP small – 100 Mbps](https://calculator.s3.amazonaws.com/index.html#r=IADs=EC2&key=files/calc-5b0f57475ed81d2e9e1e4ee31eee4fec13caf8cc&v=ver20200107wD)
+ [F5 BIG-IP medium – 200 Mbps](https://calculator.s3.amazonaws.com/index.html#r=IAD&s=EC2&key=files/calc-d4362355aed7d553d6175a115e0e24b59fe5f894&v=ver20200107wD)
+ [F5 BIG-IP large – 800 Mbps](https://calculator.s3.amazonaws.com/index.html#r=IAD&s=EC2&key=files/calc-45f93d5443e2fa064f9c4c08e0ea774c7cc411cd&v=ver20200107wD)

## Evaluating AWS and F5 knowledge base
<a name="evaluate-team-skills-expertise"></a>

Before you begin to migrate your F5 BIG-IP workload, you should make sure that your team has knowledge of the following AWS and F5 products and services.

**AWS products and services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/cloudformation/index.html) helps you to create and provision AWS infrastructure deployments predictably and repeatedly.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/index.html) provides a reliable, scalable, and flexible monitoring solution that you can start using within minutes.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/index.html) is a web service that provides resizable computing capacity for you to build and host your software systems.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/iam/index.html) is a web service for securely controlling access to AWS services.
+ [AWS Landing Zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html) is a solution that helps customers quickly set up a secure, multi-account AWS environment based on AWS best practices.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) helps you request temporary, limited-privilege credentials for users.
+ [AWS Transit Gateway](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-transit-gateway.html) is a highly available and scalable service to consolidate the Amazon VPC routing configuration for an AWS Region with a hub-and-spoke architecture.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/index.html) helps you launch AWS resources into a virtual network that you've defined.

|
|
| Important: Your team should understand the different ways to connect one or several virtual private clouds (VPCs) to existing data centers, as well as how to create resources in your AWS infrastructure. For more information about this, see [Network-to-Amazon VPC connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html) in the Amazon VPC documentation. |
| --- |

**F5 products and services**
+ [Traffic Management Operating System (F5 TMOS)](https://www.f5.com/pdf/white-papers/tmos-wp.pdf) is the software foundation for all of F5's network or traffic products.
+ [Local Traffic Manager (F5 LTM)](https://www.f5.com/products/big-ip-services/local-traffic-manager) helps you to control network traffic, selecting the right destination based on server performance, security, and availability.
+ *Global Traffic Manager (F5 GTM)* distributes DNS and user application requests based on business policies, data center and cloud service conditions, user location, and application performance.
+ [Access Policy Manager (F5 APM)](https://www.f5.com/products/big-ip-services/access-policy-manager) secures, simplifies, and centralizes access to apps, APIs, and data, no matter where users and their apps are located.
+ [Application Security Manager (F5 ASM)](https://www.f5.com/pdf/products/big-ip-application-security-manager-overview.pdf) is a flexible web application firewall that secures web applications in traditional, virtual, and private cloud environments.
+ [Advanced Firewall Manager (F5 AFM)](https://www.f5.com/products/big-ip-services/advanced-firewall-manager) mitigates network threats before they disrupt critical data center resources.
+ [F5 BIG-IQ](https://www.f5.com/products/automation-and-orchestration/big-iq) provides a central point of control for F5 physical and virtual devices, and for the solutions that run on them.
