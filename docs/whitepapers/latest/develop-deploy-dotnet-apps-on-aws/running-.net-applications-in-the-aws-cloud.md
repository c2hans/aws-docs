---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/running-.net-applications-in-the-aws-cloud.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Running .NET Applications in the AWS Cloud
<a name="running-.net-applications-in-the-aws-cloud"></a>

The AWS Cloud provides a number of benefits, including elasticity, scalability, and flexibility, but many legacy applications were designed with the server hardware and infrastructure as critical aspects of the application’s design.

Architects and software engineers had little choice but to shape .NET applications into existing deployment environments, which generally involved a fixed set of resources that often needed to be shared across a number of applications or services.

For the many legacy .NET applications, the most suitable compute choice for running applications in AWS is using virtual machines, using either [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) or [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2). In some cases, it’s also possible to run .NET applications in Windows containers, and you can also run .NET applications on Amazon EC2 bare metal instances, either by running directly on the Windows OS of the host instance, or by [running Hyper-V](https://aws.amazon.com/blogs/compute/running-hyper-v-on-amazon-ec2-bare-metal-instances/) on the instance.

In contrast, with the advent of .NET Core, modern .NET Core applications can be designed to take advantage of all the cloud benefits. Modern applications can use the traditional set of compute choices, and also target various types of serverless environment, including AWS Fargate or AWS Lambda.

.NET 5 now also allows performant hosting of workloads on [ARM64](https://en.wikipedia.org/wiki/AArch64) EC2 instances such as the [Graviton2](https://aws.amazon.com/ec2/graviton/) EC2 families. This enables access to the latest generation of processors available on Amazon EC2, meaning your applications can be hosted on compute specialized to your workload type, such as video encoding, web servers, and high-performance computing (HPC).

![A chart depicting AWS deployment targets for compute workloads.](http://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/images/dotnet-apps4.png)

* AWS deployment targets for compute workloads *

For new applications, consider serverless options for innovative and highly-elastic workloads, and then consider the various container options or virtual machines when there are specific dependencies on the environment or when more precise control over the infrastructure is needed.

For legacy .NET applications, virtual machines are often considered the natural choice, although the integration of [Docker with Windows](https://docs.docker.com/docker-for-windows/install/) means the use of containers is increasingly common. Containers have a number of benefits, including immutable deployment and improved resource utilization.

Subsequent sections cover each of these compute choices in more detail. However, prior to choosing a compute environment, you must choose an operating system for hosting an application, and choose a suitable architectural style.
