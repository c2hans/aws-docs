---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/networking-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Networking architecture
<a name="networking-architecture"></a>

Enterprise ML platforms built on AWS normally have requirements to access on-premises resources, such as on-premises code repositories or databases. Secure communications such as [AWS Direct Connect](https://aws.amazon.com/directconnect/) or VPN should be established. To enable flexible network routing across different AWS accounts and the on-prem network, consider using the [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) service. If you want all internet traffic to go through your corporate network, configure an internet egress route to allow internet traffic to go through the on-premises network. The following figure shows a network design with multiple accounts and an on-premises environment.

![A diagram showing networking design.](http://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-5.png)

* Networking design*

 For enhanced network security, you can configure resources in different AWS accounts to communicate via the [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc) (VPC) using VPC endpoints. A VPC endpoint enables private connections between your VPC and supported AWS services. There are different types of VPC endpoints such as [interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) and [gateway endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-gateway.html). An interface endpoint is an elastic network interface (ENI) with a private IP address from the IP address range of your subnet that you can control network access using a VPC security group. To access resources inside a VPC, you need to establish a route to the subnet where your interface endpoint is located. A gateway endpoint is a gateway that you specify as a target for a route in your route table. You can control access to resources behind a VPC endpoint using a [VPC endpoint policy](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html).

 For data scientists to use [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), AWS recommend the following VPC endpoints:
+  [Amazon S3](https://aws.amazon.com/s3/)
+  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) (to call SageMaker APIs)
+  [Amazon SageMaker AI Runtime](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_SageMaker_Runtime.html) (only use this in accounts which have permissions to invoke SageMaker endpoints)
+  [Amazon SageMaker AI Feature Store Runtime](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Types_Amazon_SageMaker_Feature_Store_Runtime.html)
+  [Amazon Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) (STS)
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) (for logging)
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) (for auditing API calls made by the service)
+  [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) (ECR)
+  [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
+  [AWS CodeBuild](https://aws.amazon.com/codebuild/)
+  [AWS CodeArtifact](https://aws.amazon.com/codeartifact/)

 The following figure shows the networking architecture for SageMaker AI with private endpoints for all the dependent services.

![A diagram showing networking architecture for Amazon SageMaker AI Studio inside a VPC.](http://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-6.png)

* Networking architecture for Amazon SageMaker AI Studio inside a VPC (Not all VPC endpoints are shown for simplicity) *

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
