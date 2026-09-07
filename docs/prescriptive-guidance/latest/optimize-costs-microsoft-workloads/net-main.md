---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-main.html
---

# .NET
<a name="net-main"></a>

Developing and deploying .NET applications is an important key in helping you achieve the scale and agility offered by cloud computing. For many legacy .NET applications, the most suitable compute choice for running applications in AWS is using virtual machines, either through AWS Elastic Beanstalk or Amazon Elastic Compute Cloud (Amazon EC2). It's also possible to run .NET applications in Windows and Linux containers.

The introduction of .NET core enables you to design modern .NET applications that take advantage of all the cloud benefits. Modern applications can use the traditional set of compute choices and also target various types of serverless environments, including AWS Fargate or AWS Lambda. .NET 6\+ now offers performant hosting of workloads on ARM64 EC2 instances such as the Graviton2 EC2 families. This enables access to the latest generation of processors available on Amazon EC2. This means that your applications can be hosted on compute specialized to your workload type, such as video encoding, web servers, and high-performance computing (HPC).

![Optmizing .NET costs for Microsoft workloads](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/932312a7-4ef4-455e-9c4a-1c8dc7284bb2.png)

This section provides recommendations for helping you adapt your .NET applications to take advantage of the benefits of the cloud with a focus on cost efficiency. This section covers the following topics:
+ [Refactor to modern .NET and move to Linux](net-refactor-linux.md)
+ [Containerize .NET apps](net-containerize.md)
+ [Use Graviton instances and containers](net-graviton.md)
+ [Support dynamic scaling for static .NET framework apps](net-static.md)
+ [Use caching to reduce database demand](net-caching.md)
+ [Consider serverless .NET](net-serverless.md)
+ [Consider purpose-built databases](net-purpose.md)
