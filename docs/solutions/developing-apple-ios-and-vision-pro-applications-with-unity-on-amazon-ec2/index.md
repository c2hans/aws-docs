---
source_url: https://docs.aws.amazon.com/solutions/developing-apple-ios-and-vision-pro-applications-with-unity-on-amazon-ec2/index.html
---

---
title: 'Guidance for Developing Apple iOS and Vision Pro Applications with Unity on Amazon EC2'
canonical_url: https://docs.aws.amazon.com/solutions/developing-apple-ios-and-vision-pro-applications-with-unity-on-amazon-ec2/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Developing Apple iOS and Vision Pro Applications with Unity on Amazon EC2

## Overview

This Guidance demonstrates how developers can build applications on mobile iOS and Apple Vision Pro in the AWS Cloud using Unity—a widely-used game engine and development platform where developers can create immersive 2D and 3D interactive experiences. Amazon EC2 Mac instances are used to provide the necessary macOS environment to run Xcode, allowing developers to use Apple tools and workflows required to build, compile, and package applications for iOS and visionOS platforms. By automating the build process on scalable and cost-efficient AWS infrastructure, developers can significantly reduce the time and effort required to package applications for mobile and extended reality devices.

## How it works

This architecture diagram shows how to build Unity-based Apple Vision Pro and mobile projects for iOS in the AWS Cloud. The build process uses a two-step approach, using an auto-scaled fleet of Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances and Amazon EC2 Mac Instances, to achieve flexibility and cost-efficiency within the pipeline.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/developing-apple-ios-and-vision-pro-applications-with-unity-on-amazon-ec2.pdf)

![Architecture diagram](/images/solutions/developing-apple-ios-and-vision-pro-applications-with-unity-on-amazon-ec2/images/developing-apple-ios-and-vision-pro-applications-with-unity-on-amazon-ec2-1.png)

1. **Step 1**: Code Repository and Jenkins Integration: The source code is stored in a Git code repository. Jenkins pulls the source code from the repository to initiate a build. Developers access the Jenkins Controller interface through an Application Load Balancer.
1. **Step 2**: Developer and Administrator Access: Developers and system administrators access Amazon EC2 Mac Instances through an Apple Remote Desktop (ARD). They access Linux agents through SSH, and the Unity Accelerator through HTTP using AWS Systems Manager.
1. **Step 3**: Infrastructure Management: System Administrators deploy and manage the infrastructure using the AWS Cloud Development Kit (AWS CDK).
1. **Step 4**: Jenkins Controller Deployment: The Jenkins Controller is deployed on AWS Fargate for Amazon Elastic Container Service (Amazon ECS) using the AWS CDK. Amazon Elastic File Service (Amazon EFS) is to support redundancy.
1. **Step 5**: Build Stage on Spot Instances: The first build stage, which involves generating the Xcode project from the Unity source code, is run on Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances. The Spot Instances are placed into an Amazon EC2 Auto Scaling group for scalability and redundancy.
1. **Step 6**: Jenkins Agent Instances and Caching: Jenkins agent instances use Amazon Elastic Block Storage (Amazon EBS) volumes and Amazon Simple Storage Service (Amazon S3) for repository and build asset caching mechanics. The Unity Accelerator can also be used for Unity asset caching.
1. **Step 7**: Final Build and Artifact Storage: The resulting Xcode project is transferred to a Jenkins worker hosted on one of the Amazon EC2 Mac Instances to finalize, sign the build, and export the artifact. The .ipa or Xcode archive file is exported as a Jenkins artifact and stored in an Amazon S3 bucket.
1. **Step 8**: Secure Storage of Credentials: Certificates, private keys, and provisioning profiles are stored in AWS Secrets Manager and dynamically pulled onto the Mac instances during the build process.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-developing-apple-vision-pro-applications-with-unity-on-amazon-ec2/?target=_blank)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses Amazon CloudWatch, AWS CDK, and Amazon Key Management Service (AWS KMS) to provide a consistent and repeatable way to deploy the Amazon EC2 and Jenkins resources, reducing human error and lead time. For example, AWS CDK allows defining the entire deployment, from the Amazon EC2 instances to the Jenkins setup, in a programmatic manner. This enables version control, testing, and easy updates of the pipeline infrastructure. Additionally, AWS CDK simplifies the management and upgrades of the pipeline components over time, reducing operational overhead and helping to ensure the environment stays up-to-date. Additionally, CloudWatch provides observability on the workloads to proactively identify issues, while AWS KMS is used to create encryption keys and store secrets for the pipeline, encrypting data at rest. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The capabilities of Amazon Virtual Private Cloud (Amazon VPC), AWS KMS, AWS PrivateLink, and Systems Manager help ensure the certificates and provisioning profiles are securely stored and accessed only during the build process. Container images are restricted within the private Amazon VPC, and PrivateLink controls Amazon S3 bucket access. Lastly, Systems Manager provides controlled access to the pipeline resources and stores audit logs. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The Application Load Balancer, EC2 Auto Scaling groups, Amazon EFS, and Fargate are services that collectively offer consistent ingress to the Jenkins web UI. The Jenkins UI uses Amazon EFS for shared storage and runs on Fargate for automatic restarts. Moreover, EC2 Auto Scaling groups with mixed Spot Instances handle worker node failures and interruptions. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance leverages a variety of AWS services to optimize the performance and cost-efficiency of the build process. For instance, Amazon Elastic Container Registry (Amazon ECR) simplifies container image storage and delivery, eliminating the need to manage separate registries. EC2 Auto Scaling groups are used to automatically scale the build workloads on cost-effective Spot Instances, taking advantage of unused capacity. Additionally, Amazon EBS volumes and the Unity Accelerator provide caching mechanisms to reduce overall build times by reusing critical build repositories, artifacts, and assets. By integrating these AWS services, this Guidance is able to improve the performance and cost-efficiency of developing Apple Vision Pro applications with Unity. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance minimizes compute costs by strategically using Amazon EC2Mac Instances and Spot Instances. This is done by using Spot Instances for the initial project build phase and reserving the more powerful EC2 Mac instances for the final Xcode build step. Additionally, the EC2 Auto Scaling groups automatically scale the resources based on demand, and AWS Savings Plans help optimize costs for the services. By combining these cost-saving AWS capabilities, this Guidance is able to significantly reduce the overall compute expenditure for developing Apple Vision Pro applications with Unity. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

EC2 Auto Scaling automatically scales resources up and down based on demand, minimizing excess capacity and reducing energy consumption. This Guidance also uses managed services like Amazon S3, Amazon EFS, and Systems Manager, which distribute the environmental impact across many users rather than requiring dedicated infrastructure. Additionally, it takes advantage of AWS Graviton Processors, which can improve the price-performance ratio and further minimize the hardware requirements, contributing to a more sustainable architecture. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Implementing a Build Pipeline for Unity Mobile Apps**: This blog demonstrates how to create custom build pipelines in Unity to efficiently build applications for diverse platforms while reducing build times.

[Read the blog](https://aws.amazon.com/blogs/gametech/implementing-a-build-pipeline-for-unity-mobile-apps/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
