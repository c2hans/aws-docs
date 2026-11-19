---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/appstream-well-architected-framework/performance-efficiency.html
---

# Performance efficiency pillar

The [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html) of the AWS Well-Architected Framework focuses on optimizing the use of cloud resources to meet performance goals while adapting to fluctuating demands and emerging technologies. It emphasizes continuously fine-tuning systems to maintain efficiency in a dynamic cloud environment.

Key focus areas for applying this pillar to your WorkSpaces Applications streaming environment include:
+ Instance type selection and optimization
+ Streaming performance optimization
+ Fleet capacity management

## Democratize advanced technologies
<a name="pe-advanced"></a>

Use AWS managed services for complex technologies so your team can focus on product development instead of infrastructure management.
+ Configure instance types based on application requirements:
  + Select GPU-enabled instances for graphics-intensive applications.
  + Choose [GPU families](https://docs.aws.amazon.com/appstream2/latest/developerguide/instance-types.html) (such as Graphics G4dn or Graphics G5) based on application needs.
+ Choose and configure one of the following authentication methods:
  + Set up integration with a SAML 2.0-based identity provider.
  + Configure user pool settings.
  + Integrate with [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html).
+ Enable and configure storage options based on user needs:
  + Set up home folders in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) for Windows-based fleets.
  + Set up shared file systems in [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) for Linux-based fleets.
  + Configure persistent storage permissions.
  + Enable application settings persistence.

## Go global in minutes
<a name="pe-global"></a>

Use multi-Region deployment to improve global user experiences through reduced latency.
+ Configure fleets in multiple AWS Regions by deploying them in the Regions closest to your users, and create a separate stack for each Region.
+ Implement cross-Region redirection to automatically redirect WorkSpaces Applications users to the WorkSpaces Applications stacks closest to their current location.
+ If you use optional features in WorkSpaces Applications, such as application settings persistence, home folders, or elastic fleets, configure Amazon S3 cross-Region replication for user data for Windows-based fleets, and configure cross-Region replication for Linux-based fleets.
+ Replicate images across Regions. For more information, see [Copy an image that you own to another AWS Region in Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/copy-image-different-region.html) in the AWS documentation.
+ For domain-joined fleets, set up Active Directory infrastructure in the other Regions, including Active Directory Federation Services (AD FS) (unless you use SAML 2.0 and Amazon Cognito as an alternative). Use [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) for multi-Region replication capabilities.
+ Direct users to the lowest-latency WorkSpaces Applications endpoints. For more information, see the AWS blog post [Optimize user experience with latency-based routing for Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/optimize-user-experience-with-latency-based-routing-for-amazon-appstream-2-0/).

## Use serverless architectures
<a name="pe-serverless"></a>

Serverless architectures can reduce server management overhead and help lower costs by using managed services for compute functions.

Use AWS serverless services such as the following:
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) to automate tasks and integrate custom logic through event-driven functions
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) to provide scalable storage for WorkSpaces Applications user data, application files, and session artifacts
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to provide monitoring, logging, and alerting for WorkSpaces Applications performance and usage metrics
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) to facilitate user authentication and access control for WorkSpaces Applications applications
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) to create RESTful APIs to interface between WorkSpaces Applications and other services or custom applications

## Experiment more often
<a name="pe-experiment"></a>

Cloud infrastructure enables rapid testing of various resource configurations to optimize performance and cost.
+ Test different instance types to optimize performance and cost:
  + Compare stream performance across different instance families.
  + Compare GPU instances with non-GPU instances for graphics applications.
  + Test memory-optimized instances for memory-intensive applications.
+ Test application configurations by using Image Builder:
  + Create test images with different application configurations.
  + Validate application performance before deployment.
  + Test application compatibility with different instance types.
+ Test fleet settings, including capacity configurations (minimum and maximum capacity), scaling policies, and session settings (maximum session duration and disconnect timeout).

## Consider mechanical sympathy
<a name="pe-sympathy"></a>

Choose cloud services based on your workload's specific requirements and usage patterns to help improve performance and efficiency.
+ Choose Graphics G5 instances for graphics-intensive applications, such as applications that require DirectX, OpenGL, OpenCL, or 3D visualization software.
+ Select `stream.standard` instances for business applications, web browsers, and light graphics applications.
+ Monitor and adjust the streaming protocol based on CloudWatch metrics such as `StreamingSessionLatency`.
+ Configure WorkSpaces Applications in Amazon VPC networks that are closest to your users, and choose network bandwidth that meets your application's requirements.
+ Choose the fleet type based on application behavior. For example, choose single-session fleets for applications that require dedicated resources and multi-session fleets for applications that can share resources efficiently.
+ Consider application compatibility with multi-session environments.
+ Use the [file system redirection feature](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-file-system-redirection.html) to handle the interactions between remote and local applications. For more information, see the AWS blog post [Launching local applications from an Amazon WorkSpaces Applications streaming session](https://aws.amazon.com/blogs/desktop-and-application-streaming/launching-local-applications-from-an-amazon-appstream-2-0-streaming-session/).
