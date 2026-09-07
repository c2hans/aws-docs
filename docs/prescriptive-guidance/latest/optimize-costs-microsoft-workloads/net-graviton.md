---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-graviton.html
---

# Use Graviton instances and containers
<a name="net-graviton"></a>

## Overview
<a name="net-graviton-overview"></a>

AWS Graviton instances are powered by ARM processors designed by AWS to deliver the best price performance for your cloud workloads running in Amazon Elastic Compute Cloud (Amazon EC2), including containers running in AWS. There are currently three generations of Graviton available for use on Amazon EC2. This guide focuses on the use of Graviton 2 and 3 with .NET applications because there is a significant cost savings when you use the latest versions of Graviton. Keep in mind that Graviton instances only run the Linux operating system. As a result, Graviton instances are a strong offering for .NET running on Linux, but aren't an option for the Windows operating system or legacy .NET Framework applications.

Graviton 3 is 60 percent more efficient over comparable EC2 instances with up to 40 percent better performance. This guide focuses on the cost benefits of using Graviton, but it's important to note that Graviton offers the additional benefits of performance improvements and improved environmental sustainability.

## Cost impact
<a name="net-graviton-cost"></a>

You can achieve up to 45 percent savings when you switch to Graviton. After you refactor any legacy .NET Framework applications to a modern .NET version, you unlock the capability of using Graviton instances. Moving to Graviton is an effective cost optimization technique for .NET developers.

The example in the following table shows the potential for performance improvements that you can achieve by migrating to Graviton instances.

![Graviton performance graph](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/c9fea413-050b-48bf-8e2c-fad5f8fce72c.png)

For a full breakdown and explanation of the benchmarking approach used to create the results in the preceding diagram, see [Powering .NET 5 with AWS Graviton2: Benchmarks](https://aws.amazon.com/blogs/compute/powering-net-5-with-aws-graviton2-benchmark-results/) in the AWS Compute Blog.

One of the reasons for the improved efficiency is the difference in the meaning of vCPU between x86 and Graviton. In the x86 architecture, a vCPU is a logical core achieved by hyperthreading. In Graviton, vCPU equates to a physical core which allows the vCPU to be fully committed to the workload.

The result with Graviton2 is a 40 percent better price performance over comparable x86/x64 instances. Graviton3 offers the following over Graviton2:
+ An increased performance profile with up 25 percent better performance
+ Up to two times higher floating-point performance
+ Up to two times faster cryptographic workload performance
+ Up to three times better machine learning performance

In addition, Graviton3 is the first instance in the cloud to feature DDR5 memory.

The following tables show the difference in cost savings between Graviton-based instances and equivalent x86-based instances.

This table shows Graviton savings of 19.20 percent.

|
|
| Instance type | Architecture | vCPU | Memory (GB) | Hourly cost (on demand) |
| --- |--- |--- |--- |--- |
| t4g.xlarge | ARM | 4 | 16 | $0.1344 |
| t3.xlarge | x86 | 4 | 16 | $0.1664 |

This table shows Graviton savings of 14.99 percent.

|
|
| Instance type | Architecture | vCPU | Memory (GB) | Hourly cost (on demand) |
| --- |--- |--- |--- |--- |
| c7g.4xlarge | ARM | 16 | 32 | $0.5781 |
| c6i.4xlarge | x86 | 16 | 32 | $0.6800 |

It's important to test your application's performance profile when considering Graviton. Graviton isn't a replacement for solid software development practices. You can use testing to verify if you're getting the most out of your underlying compute resources.

## Cost optimization recommendations
<a name="net-graviton-rec"></a>

There are several ways to take advantage of the Graviton processors/instances. This section walk you through the changes required to move from using an x86-architecture machine to Graviton (ARM) instances.

### Change the runtime setting in Lambda
<a name="change-the-runtime-setting-in-9999999999999999lam-.54d1ead6-0c70-54e1-abf0-2f74c0037124"></a>

We recommend that you switch the runtime settings in AWS Lambda. For more information, see [Modifying the runtime environment](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-modify.html) in the Lambda documentation. Since .NET is a compiled language, you must follow a build process to get this working. For an example of how to do this, see .[NET on Graviton](https://github.com/aws/aws-graviton-getting-started/blob/main/dotnet.md) in GitHub.

### Containers
<a name="containers.7bec7f4c-dcc7-5073-be1a-2d63a4b8ec5f"></a>

For a containerized workload, create a multi-architecture container image. You can do this by specifying multiple architectures in the Docker build command. For example:

```
docker buildx build -t "myImageName:latest" --platform linux/amd64,linux/arm64 --push .
```

You can also use a tool such as AWS Cloud Development Kit (AWS CDK) to help [orchestrate the build](https://aws.amazon.com/blogs/devops/build-and-deploy-net-web-applications-to-arm-powered-aws-graviton-2-amazon-ecs-clusters-using-aws-cdk/). For examples from Docker, see [Building Multi-Arch Images for Arm and x86 with Docker Desktops](https://www.docker.com/blog/multi-arch-images/) in the Docker documentation.

### Amazon EC2
<a name="9999999999999999ec2-.c1962cf5-e4ed-5d29-b8b2-f7db7c127cd5"></a>

To migrate to ARM from x86/x64, target the ARM architecture in the compile step. In Visual studio, you can create an ARM64 CPU. For instructions, see [To configure a project to target Arm64 and other platforms](https://learn.microsoft.com/en-us/visualstudio/ide/how-to-configure-projects-to-target-platforms?view=vs-2022) in the Microsoft documentation.

If you're using the .NET CLI, then running the build on an ARM machine produces a Graviton compatible build. To see a demo, watch [Accelerate .NET 6 performance with Arm64 on AWS Graviton2](https://www.youtube.com/watch?v=iMlyZI9NhFw) on YouTube. Dependency issues will result in compile time errors that can then be addressed individually. As long as there are ARM libraries for any dependency, the transition should be relatively straightforward.

## Additional resources
<a name="net-graviton-resources"></a>
+ [How to build your containers for ARM and save with Graviton and Spot instances on Amazon ECS](https://aws.amazon.com/blogs/containers/how-to-build-your-containers-for-arm-and-save-with-graviton-and-spot-instances-on-amazon-ecs/) (AWS blog)
+ [AWS Lambda Functions Powered by AWS Graviton2 Processor – Run Your Functions on Arm and Get Up to 34% Better Price Performance](https://aws.amazon.com/blogs/aws/aws-lambda-functions-powered-by-aws-graviton2-processor-run-your-functions-on-arm-and-get-up-to-34-better-price-performance/) (AWS blog)
+ [Migrating AWS Lambda functions to Arm-based AWS Graviton2 processors](https://aws.amazon.com/blogs/compute/migrating-aws-lambda-functions-to-arm-based-aws-graviton2-processors/) (AWS blog)
+ [Build and deploy .NET web applications to ARM-powered AWS Graviton 2 Amazon ECS Clusters using AWS CDK](https://aws.amazon.com/blogs/devops/build-and-deploy-net-web-applications-to-arm-powered-aws-graviton-2-amazon-ecs-clusters-using-aws-cdk/) (AWS blog)
+ [Graviton Fast Start – A New Program to Help Move Your Workloads to AWS Graviton](https://aws.amazon.com/blogs/aws/graviton-fast-start-a-new-program-to-help-move-your-workloads-to-aws-graviton/) (AWS blog)
+ [Powering .NET 5 with AWS Graviton2: Benchmarks](https://aws.amazon.com/blogs/compute/powering-net-5-with-aws-graviton2-benchmark-results/) (AWS blog)
