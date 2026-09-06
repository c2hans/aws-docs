---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/amazon-elastic-compute-cloud-ec2-instances.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon Elastic Compute Cloud (EC2) Instances
<a name="amazon-elastic-compute-cloud-ec2-instances"></a>

Amazon EC2 provides a flexible compute service with a wide variety of virtual machines and [bare metal](https://en.wikipedia.org/wiki/Bare-metal_server) instance types.

AWS is responsible for operating all levels up to hypervisor and host OS, giving you full access and control over the guest operating system. AWS also provides tools, features, and services that enable you to create a fully automated and self-managing infrastructure, such as [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) and [AWS Systems Manager](https://aws.amazon.com/systems-manager/). You are responsible for patching, updating, securing, and maintaining the Windows or Linux OS, application server, web server, and any application code, either using AWS-provided tools or features, or any other custom methods. Because you have full control of your environment, you also have complete flexibility to configure your environment as needed. For example, you may want to use [Nginx](https://www.nginx.com/) or [Apache HTTP Server](https://httpd.apache.org/) instead of IIS as your web server.

Amazon EC2 instances provide the highest level of flexibility and control in the cloud. This flexibility often proves essential for legacy applications, but can also be useful for many modern applications. You have the choice of x86 (32-bit), x64 (64-bit), and Arm-based platforms in Amazon EC2. You also have access to most popular Linux versions and all Windows Server versions, from Windows Server 2008 to Windows Server 2019. For modern Windows applications, you can also use Semi-Annual Channel Windows releases, including 1709, 1803, 1809 and 1903.

For any of these, you can choose from [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMIs) provided by AWS, numerous community and AWS Partner AMIs available in the [AWS Marketplace](https://aws.amazon.com/marketplace), or you can create or import your own images.

You can also benefit from various features such as automatic scaling, self-healing, and deep integration with other services, such as [AWS Identity and Access Management](https://aws.amazon.com/iam/) (AWS IAM), [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS), or [Amazon Elastic Block Storage](https://aws.amazon.com/ebs/) (Amazon EBS).

There are a variety of ways you can deploy your .NET applications on Amazon EC2 instances, from manual deployments to using Infrastructure as Code with [AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates and Continuous Integration / Continuous Deployment pipelines.
