---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-containerize.html
---

# Containerize .NET apps
<a name="net-containerize"></a>

## Overview
<a name="net-containerize-overview"></a>

Containers are a lightweight and efficient way to package and deploy applications in a consistent and reproducible manner. This section explains how you can use AWS Fargate, a serverless container service, to reduce the costs of your .NET applications while also providing scalable and reliable infrastructure.

## Cost impact
<a name="net-containerize-cost"></a>

Some factors that influence the effectiveness of using containers for cost savings include the size and complexity of the application, the number of applications that need to be deployed, and the level of traffic and demand on the applications. For small or simple applications, containers may not provide significant cost savings compared to traditional infrastructure approaches because the overhead of managing the containers and the associated services may actually increase costs. However, for larger or more complex applications, using containers can provide cost savings by improving resource utilization and reducing the number of required instances.

We recommend that you keep the following in mind when using containers for cost savings:
+ **Application size and complexity** – Larger and more complex applications are better suited for containerization because they tend to require more resources and can benefit more from improved resource utilization.
+ **Number of applications** – The more applications that your organization must deploy, the more cost savings can be achieved through containerization.
+ **Traffic and demand** – Applications that experience high traffic and demand can benefit from the scalability and elasticity that containers provide. This can lead to cost savings.

Different architectures and operating systems affect container costs. If you're using Windows containers, costs may not decrease because of licensing considerations. Licensing costs are lower or absent with Linux containers. The following chart uses a basic configuration on AWS Fargate in the US East (Ohio) Region with the following settings: 30 tasks per month each running for 12 hours with 4 vCPUs and 8 GB of memory allocated.

You can choose from two primary compute platforms to run your containers on AWS: [EC2-based container hosts and serverless](https://catalog.us-east-1.prod.workshops.aws/workshops/1de8014a-d598-4cb5-a119-801576492564/en-US/module2-ecs/lab1-deploy-ecs-cluster) or [AWS Fargate](https://aws.amazon.com/blogs/containers/running-windows-containers-with-amazon-ecs-on-aws-fargate/). If you use Amazon Elastic Container Service (Amazon ECS) instead of Fargate, then you must maintain running compute (instances) to allow the placement engine to instantiate containers when needed. If you use Fargate instead, only the compute capacity that is needed is provisioned.

The following chart shows the difference for equivalent containers using Fargate versus Amazon EC2. Because of the flexibility of Fargate, tasks for an application can run 12 hours per day, with zero utilization during off hours. However, for Amazon ECS, you must control compute capacity by using an [Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) of EC2 instances. This can lead to capacity running 24 hours a day, which can ultimately increase costs.

![Fargate monthly costs vs EC2 monthly costs](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/aa2ad113-7e74-45d3-b547-1974eb8f473c.png)

## Cost optimization recommendations
<a name="net-containerize-rec"></a>

### Use Linux containers rather than Windows
<a name="use-linux-containers-rather-than-windows.0c5fc93d-8a36-5d2c-bf81-a56ec23060d3"></a>

You can achieve significant savings if you use Linux containers instead of Windows containers. For example, you can achieve an approximately 45 percent savings on compute costs if you run the .NET Core on EC2 Linux instead of running the .NET Framework on EC2 Windows. You can get an additional 40 percent savings if you use the ARM architecture (AWS Graviton) instead of x86.

If you plan to run Linux-based containers for existing .NET Framework applications, you must port these applications to modern, cross-platform versions of .NET ([such as .NET 6.0](https://learn.microsoft.com/en-us/dotnet/core/releases-and-support)) in order to use Linux containers. A major consideration is weighing the cost of refactoring compared with the cost savings gained through the reduced cost of Linux containers. For more information about porting your applications to modern .NET, see [Porting Assistant for .NET](https://aws.amazon.com/porting-assistant-dotnet/) in the AWS documentation.

Another benefit of moving to modern .NET (that is, away from the .NET Framework) is that additional modernization opportunities become available. For instance, you can consider rearchitecting your application to a microservices-based architecture that's more scalable, agile, and cost effective.

The following diagram illustrates the decision-making process for exploring modernization opportunities.

![Replatforming decision tree](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/bdfdad39-96e2-454f-a366-a53efa3ad2d4.png)

### Take advantage of Savings Plans
<a name="take-advantage-of-9999999999999999sps-.6405f365-7438-5374-8731-b782e44f3dc2"></a>

Containers can help you take advantage of [Compute Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/) to reduce your Fargate costs. The flexible discount model offers the same discounts as Convertible Reserved Instances. Fargate pricing is based on the vCPU and memory resources used from the time you start to download your container image until the Amazon ECS task terminates (rounded up to the nearest second). [Savings Plans for Fargate](https://aws.amazon.com/fargate/pricing/) offer savings of up to 50 percent on Fargate usage in exchange for a commitment to use a specific amount of compute usage (measured in dollars per hour) for a one-year or three-year term. You can use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) to help you choose a Savings Plans.

It's important to understand that Compute Savings Plans are applied to the usage that gets you the largest savings first. For example, if you're running a t3.medium Linux instance in `us-east-2` and an identical Windows t3.medium instance, the Linux instance receives the Savings Plans benefit first. This is because the Linux instance has a 50 percent savings potential whereas the same Windows instance has a 35 percent savings potential. If you have other Savings Plans eligible resources running in your AWS account, such as Amazon EC2 or Lambda, then it's not necessary for your Savings Plans to be applied to Fargate first. For more information, see [Understanding how Savings Plans apply to your AWS usage](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-applying.html) in the Savings Plans documentation and the [Optimize spending for Windows on Amazon EC2](savings-plans.md) section of this guide.

### Right size Fargate tasks
<a name="right-size-9999999999999999fargate--tasks.732cb19b-2d85-50b2-82d0-0d64f6df8a49"></a>

It's important to ensure that Fargate tasks are correctly sized to achieve the maximum degree of cost optimization. Frequently, developers don't have all the necessary usage information when initially determining the configurations for the Fargate tasks used in their applications. This can lead to overprovisioning of tasks and then result in unnecessary spending. To avoid this, we recommend that you load test applications running on Fargate to understand how a specific task configuration performs under different usage scenarios. You can use the load testing results, vCPU, memory allocation of the tasks, and auto scaling policies to find the right balance between performance and cost.

The following diagram shows how Compute Optimizer generates recommendations for the optimal task and container size.

![Compute Optimizer recommendations for task and container size](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/c98dbd1d-849a-4a2a-8b09-c550be6579d1.png)

One approach is to use a load testing tool, such as the one described in [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/), to establish a baseline for vCPU and memory utilization. After you run the load test to simulate a typical application load, then you can fine-tune the vCPU and memory configuration for the task until the baseline utilization is achieved.

## Additional resources
<a name="net-containerize-resources"></a>
+ [Cost Optimization Checklist for Amazon ECS and AWS Fargate](https://aws.amazon.com/blogs/containers/cost-optimization-checklist-for-ecs-fargate/) (AWS Containers blog post)
+ [Theoretical cost optimization by Amazon ECS launch type: Fargate vs EC2](https://aws.amazon.com/blogs/containers/theoretical-cost-optimization-by-amazon-ecs-launch-type-fargate-vs-ec2/) (AWS Containers blog post)
+ [Porting Assistant for .NET](https://aws.amazon.com/porting-assistant-dotnet/) (AWS documentation)
+ [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) (AWS Solutions Library)
+ [AWS Compute Optimizer launches support for Amazon ECS services on AWS Fargate](https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-compute-optimizer-launches-support-for-amazon-ecs-services-on-aws-fargate/) (AWS Cloud Financial Management blog post)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
