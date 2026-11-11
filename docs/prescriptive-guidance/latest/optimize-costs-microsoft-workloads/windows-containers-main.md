---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/windows-containers-main.html
---

# Move Windows applications to containers
<a name="windows-containers-main"></a>

## Overview
<a name="windows-containers-overview"></a>

According to the [CNCF Annual Survey 2021](https://www.cncf.io/reports/cncf-annual-survey-2021/), 96 percent of organizations are either using or evaluating containers to modernize their infrastructure. This is because containers can help your organization reduce risk, increase operational efficiency and speed, and enable agility. You can also use containers to reduce the cost of running your applications. This section offers recommendations for cost-effectively running containers across AWS container services, including [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/), and [AWS Fargate](https://aws.amazon.com/fargate/).

## Cost benefits
<a name="windows-containers-cost-benefits"></a>

The following infographic shows the cost savings that a business can achieve by consolidating their ASP.NET Framework applications onto Amazon Elastic Compute Cloud (Amazon EC2) instances based on an [AWS Optimization and Licensing Assessment (AWS OLA)](https://aws.amazon.com/optimization-and-licensing-assessment/) recommendation. The following infographic shows what additional savings can be achieved by moving applications to a Windows container.

![ASP.NET consolidation](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/cc4e3b59-96d6-406d-9f53-01d065d1e6e0.png)

The AWS OLA recommended that the business rehost (lift and shift) its applications on individual t3.small instances. The business could accomplish these savings by running seven ASP.NET applications on on-premises servers, as the following performance utilization analysis shows.

![Performance utilization analysis](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/b149d628-4b57-4aaa-b242-e47ee573dcd2.png)

Further analysis revealed that the business could save even more on costs by running its workloads on containers. Containers reduce the operating system overhead on system resources like CPU, RAM, and disk usage (explained in the next section). In this scenario, the business could consolidate all seven applications onto one t3.large instance and still have 3 GB of RAM available. Migrating to containers can help the business achieve an average of 64 percent cost savings across compute and storage by using containers instead of Amazon EC2 instances.

## Cost optimization recommendations
<a name="windows-containers-rec"></a>

The following section offers recommendations for optimizing costs by consolidating applications and using containers.

### Reduce your Windows on Amazon EC2 footprint
<a name="reduce-your-windows-on-9999999999999999ec2--footprint.4c7b7451-cc4d-5105-b653-4f60f1eb1ab2"></a>

Windows containers can reduce your Windows on Amazon EC2 footprint by enabling you to consolidate more applications onto fewer EC2 instances. For example, assume that you have 500 ASP.NET applications. If you're running one core per one application for Windows on Amazon EC2, that equals 500 Windows instances (t3.small). If you assume a 1:7 ratio (which can significantly increase depending on EC2 instance type/size) for using Windows containers (with t3.large), then you only need approximately 71 Windows instances. That represents an 85.8 percent decrease in your Windows on Amazon EC2 footprint.

### Reduce Windows licensing costs
<a name="reduce-windows-licensing-costs.b447fd38-c430-5eb1-b058-7fc799f7cbc4"></a>

If you license a Windows instance, you don't need to license containers running on that instance. As a result, consolidating your ASP.NET applications using Windows containers can significantly reduce your Windows licensing costs.

### Reduce your storage footprint
<a name="reduce-your-storage-footprint.b55b0350-a4ed-5934-89fd-f88349573ed0"></a>

Every time you launch a new EC2 instance, you create and pay for a new Amazon Elastic Block Store (Amazon EBS) volume to house the operating system. As this scales, the cost scales with it. If you use containers, you can reduce storage costs because all the containers share the same base operating system. Additionally, containers use the concept of layers to reuse immutable portions of a container image for all running containers based on that image. In the preceding example scenario, all the containers are running .NET Framework and therefore all share the intermediate and immutable ASP.NET framework layer.

### Migrate end-of-support servers to containers
<a name="migrate-end-of-support-servers-to-containers.85f24d96-98ed-5db4-98af-e16c33a12269"></a>

Support for Windows Server 2012 and Windows Server 2012 R2 ended on October 10, 2023. You can migrate your applications running on Windows Server 2012 or previous versions by containerizing them to run on new operating systems. This way, you avoid running your applications on unsupported operating systems while taking advantage of the cost efficiencies, reduced risk, operational efficiency, speed, and agility that containers provide.

A caveat to consider with this approach is if your application requires specific APIs related to the operating system version currently in use (COM Interop, for example). In this case, you must test moving your application to a newer Windows version. Windows containers align their base container image (for example, Windows Server 2019) with the operating system of the container host (for example, Windows Server 2019). Testing and moving to containers can enable easier operating system upgrades in the future by changing the base image within your Dockerfile and deploying to a fresh set of hosts running the latest version of Windows.

### Remove third-party management tools and licenses
<a name="remove-third-party-management-tools-and-licenses.4c7addfb-ca9b-5c28-aa66-ac7e251c15ec"></a>

Managing your server fleet requires using several third-party system operation tools for patching and configuration management. These tools can make infrastructure management complex, and you often incur third-party licensing costs. If you use containers on AWS, you reduce the need to manage the operating system directly. The container runtime manages the containers. This means the underlying host is ephemeral and you can replace it quickly. You can run your containers without directly managing the container host. Additionally, you can use tools like AWS Systems Manager Session Manager to access the host and troubleshoot issues.

### Improve control and portability
<a name="improve-control-and-portability.238242ed-1d6d-588a-a3ec-d4520f77ec7b"></a>

Containers give you more granular control over server resources like CPU and RAM than you have over EC2 instances. For EC2 instances, you can control CPU and RAM by selecting an instance family, instance type, and [CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html). However, with containers, you can define how much CPU or RAM you want to allocate to a container in your task definitions for [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) or to [pods in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/fargate-pod-configuration.html). We recommend [specifying container-level CPU and memory](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_definitions.html) for Windows containers. This level of granularity can provide cost benefits. Consider the following example code:

```
json
{
    "taskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:task-definition/demo-service:1",
    "containerDefinitions": [
        {
            "name": "demo-service",
            "image": "mcr.microsoft.com/dotnet/framework/samples:aspnetapp-windowsservercore-ltsc2019",
            "cpu": 512,
            "memory": 512,
            "links": [],
            "portMappings": [
                {
                    "containerPort": 80,
                    "hostPort": 0,
                    "protocol": "tcp"
                }
            ],
```

### Accelerate innovation
<a name="accelerate-innovation.5cb35535-dcd5-5ef3-8342-e496903e9858"></a>

Moving to containers makes it easier to automate stages of the development lifecycle that include building, testing, and deploying applications. If you automate these processes, then you give your development and operations teams more time to focus on innovating.

### Reduce TCO
<a name="reduce-tco.10e01a34-0bcb-57b9-ac33-7b0769b2f2c2"></a>

Moving to containers often reduces the reliance on license management and endpoint protection tools. Because containers are ephemeral units of compute, you can automate and simplify management tasks such as patching, scaling, and backup and restore. This can reduce the total cost of ownership (TCO) of administering and operating container-based workloads. Compared to virtual machines, containers can be more efficient because they help you place more applications on the same infrastructure, which increases the utilization of your infrastructure resources.

### Close the skills gap
<a name="close-the-skills-gap.538ef4d9-ae37-56ee-9f94-39d5dc3ebc68"></a>

AWS offers programs and immersion days to upskill customer development teams on containers and DevOps technology. This includes hands-on consulting and enablement.

### Refactor to .NET 5\+ and use Linux containers
<a name="refactor-to-.net-5--and-use-linux-containers.9eb970cf-a962-5b89-820e-b5a50ed9d25b"></a>

While you can reduce costs by moving your .NET Framework applications to containers, you can realize even further cost savings when you refactor legacy .NET applications to cloud-native alternatives on AWS.

### Remove licensing costs
<a name="remove-licensing-costs.f21d8880-4a39-5210-bf33-4e5405a416ac"></a>

Refactoring your application from .NET Framework on Windows to .NET Core on Linux can result in cost savings of approximately 45 percent, depending on your workload.

### Access the latest enhancements
<a name="access-the-latest-enhancements.85c938cb-3f50-5772-8ed8-23f04dd46931"></a>

Refactoring your applications from .NET Framework on Windows to .NET Core on Linux gives you access to the latest enhancements such as AWS Graviton2 processors. AWS Graviton2 processors offer up to 40 percent better price performance than comparable x86-based instances.

### Improve security and performance
<a name="improve-security-and-performance.201b0312-c1cf-50fd-a9e8-be8ba2a110e2"></a>

Refactoring your application from .NET Framework on Windows to .NET Core on Linux containers can improve security and performance. You get the latest security patches, benefit from container isolation, and have access to new features.

### Use Windows containers instead of running many applications on one instance of IIS
<a name="use-windows-containers-instead-of-running-many-applications-on-one-instance-of-iis.5efa1518-e8a2-5a54-baef-2f8262bfd37d"></a>

Consider the following advantages of using Windows containers instead of running multiple applications on one EC2 Windows instance with Internet Information Services (IIS):
+ **Security** – Containers provide a level of isolation by default that isn't achieved at the IIS level. If one IIS website or application is compromised, the other hosted sites might also be affected. Container escape is rare and is harder to exploit than gaining control of a server through a web vulnerability.
+ **Flexibility** – The ability to run containers in process isolation, each with its own instance, allows for more granular networking options. Containers also support flexible distribution methods across many EC2 instances. You don't get these benefits when you consolidate applications on a single IIS instance.
+ **Management overhead** – Server Name Indication (SNI) creates overhead that requires management and automation. Also, you must handle typical operating system management operations such as patching, troubleshooting Blue Screen of Death (BSOD) errors (if Auto Scaling isn't in place), and endpoint protection. Configuring IIS sites according to [security best practices](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj635855(v=ws.11)) is a time-consuming and ongoing activity. You might also need to set up [trust levels](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831532(v=ws.11)), which adds to management overhead. Containers are designed to be stateless and immutable. As a result, your deployments can be faster, more secure, and repeatable if you use Windows containers instead.

## Next steps
<a name="windows-containers-next-steps"></a>

Investing in modern infrastructure to run your legacy workloads can benefit your organization. AWS container services help you manage your underlying infrastructure, whether on premises or in the cloud, so you can focus on innovation and your business needs. AWS provides a broad set of container services for many use cases. To get started, see [Containers at AWS](https://aws.amazon.com/containers/).

## Additional resources
<a name="windows-containers-resources"></a>
+ [Optimize cost for container workloads with ECS capacity providers and EC2 Spot Instances](https://aws.amazon.com/blogs/containers/optimize-cost-for-container-workloads-with-ecs-capacity-providers-and-ec2-spot-instances/) (AWS Blog)
+ [Cost Optimization Checklist for Amazon ECS and AWS Fargate](https://aws.amazon.com/blogs/containers/cost-optimization-checklist-for-ecs-fargate/) (AWS Blog)
+ [Amazon EKS on AWS Graviton2 generally available: considerations on multi-architecture apps](https://aws.amazon.com/blogs/containers/eks-on-graviton-generally-available/) (AWS Blog)
+ [Cost optimization for Kubernetes on AWS](https://aws.amazon.com/blogs/containers/cost-optimization-for-kubernetes-on-aws/) (AWS Blog)
+ [Optimizing your Kubernetes compute costs with Karpenter consolidation](https://aws.amazon.com/blogs/containers/optimizing-your-kubernetes-compute-costs-with-karpenter-consolidation/) (AWS Blog)
