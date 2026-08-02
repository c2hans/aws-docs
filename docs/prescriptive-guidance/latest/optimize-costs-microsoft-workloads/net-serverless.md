---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-serverless.html
---

# Consider serverless .NET
<a name="net-serverless"></a>

## Overview
<a name="net-serverless-overview"></a>

Serverless computing has become a popular approach for building and deploying applications. This is mainly because of the scalability and agility that the serverless approach offers when building a modern architecture. However, it's important to consider the cost impact of serverless computing in some scenarios.

Lambda is a serverless computing platform that enables developers to run code without the need for dedicated servers. Lambda is a particularly attractive option for .NET developers looking to reduce infrastructure costs. With Lambda, .NET developers can develop and deploy applications that are highly scalable and potentially cost-effective. By using a serverless approach, developers no longer provision servers to handle application requests. Instead, developers can create functions that are executed on-demand. This makes a serverless approach more scalable, manageable, and potentially more cost-effective than running, managing, and scaling virtual machines. As a result, you only pay for the resources used by the application, without having to worry about underutilized resources or server maintenance costs.

Developers can use modern, cross-platform .NET versions to build serverless applications that are fast, efficient, and cost-effective. The .NET Core and newer versions are a free and open-source framework that's better suited to running on serverless platforms over previous .NET Framework versions. This enables developers to reduce development time and increase application performance. Modern .NET also supports a range of programming languages, including C\# and F\#. For this reason, it's an attractive option for developers looking to build modern architectures in the cloud.

This section explains how you can achieve costs savings by using Lambda as a serverless option. You can further optimize costs by fine-tuning the execution profiles of your Lambda functions, right sizing the memory allocation of your Lambda functions, using [Native AOT](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/?tabs=net7%2Cwindows), and moving to Graviton-based functions.

## Cost impact
<a name="net-serverless-cost"></a>

How much you can reduce costs depends on several factors, including how many executions your serverless functions will execute in addition to the amount of memory allocated and duration of each function. AWS Lambda offers a free tier, which includes one million free requests per month and 400,000 GB seconds of compute time per month. You can significantly reduce your monthly costs for workloads that are on or around these free tier limits.

There may also be additional costs when using a load balancer with Lambda functions as the target. This is calculated as the amount of data processed by the load balancer for the [Lambda targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html).

## Cost optimization recommendations
<a name="net-serverless-rec"></a>

### Right size your Lambda functions
<a name="right-size-your-9999999999999999lam--functions.473c63f8-85a0-50aa-b7a5-9a87d4a16ffd"></a>

Right sizing is an essential practice for cost optimization in .NET-based Lambda functions. This process involves identifying the optimal memory configuration that balances performance with cost-effectiveness, without requiring changes to the code.

By configuring the memory for a Lambda function, ranging from 128 MB up to 10,240 MB, you also adjust the amount of vCPU available during invocation. This enables memory or CPU-bound applications to access additional resources during execution, leading to a potential reduction in invocation duration and overall cost.

However, identifying the optimal configuration for your .NET-based Lambda functions can be a manual and time-intensive process, especially if changes are frequent. The [AWS Lambda Power Tuning tool](https://github.com/alexcasalboni/aws-lambda-power-tuning) can help you identify the appropriate configuration by analyzing a set of memory configurations against an example payload.

For example, increasing the memory for a .NET-based Lambda function can lead to improved total invocation time and reduced cost without affecting performance. The optimal memory configuration for a function can vary. The AWS Lambda Power Tuning tool can help identify the most cost-effective configuration for each function.

In the following example chart, the total invocation time improves as the memory increases for this Lambda function. This leads to a reduction in the cost for the total execution without affecting the original performance of the function. For this function, the optimal memory configuration for the function is 512 MB, as this is where the resource utilization is most efficient for the total cost of each invocation. This varies per function, and using the tool on your Lambda functions can identify if they benefit from right sizing.

![Graph of invocation time](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/9379cdde-840b-4b97-88c4-9d1c4677ece8.png)

We recommend that you complete this exercise regularly, as part of any integration testing when new updates are released. If infrequently updated, then do this exercise periodically to ensure functions are tuned and right sized. After you have identified the appropriate memory setting for your Lambda functions, you can add right sizing to your processes. The AWS Lambda Power Tuning tool generates programmatic output that can be used by your CI/CD workflows during the release of new code. This enables you to automate memory configuration.

You can download the [AWS Lambda Power Tuning tool](https://github.com/alexcasalboni/aws-lambda-power-tuning) for free. For instructions on how to use the tool, see [How to execute the state machine](https://github.com/alexcasalboni/aws-lambda-power-tuning/blob/master/README-EXECUTE.md) in GitHub.

Lambda also supports native AOT, which enables .NET applications to be pre-compiled. This can help reduce costs by reducing execution times for .NET functions. For more information about creating Native AOT functions, see [.NET functions with native AOT compilation](https://docs.aws.amazon.com/lambda/latest/dg/dotnet-native-aot.html) in the Lambda documentation.

### Avoid idle wait time
<a name="avoid-idle-wait-time.31a2277d-b25f-59f8-98a9-b3932c4e301d"></a>

Lambda function duration is one dimension used for calculating billing. When function code makes a blocking call, you are billed for the time that it waits to receive a response. This wait time can grow when Lambda functions are chained together, or a function is acting as an orchestrator for other functions. If you have workflows such as batch operations or order delivery systems, this adds management overhead. Additionally, it may not be possible to complete all workflow logic and error handling within the maximum Lambda timeout of 15 minutes.

Instead of handling this logic in function code, we recommend that you re-architect your solution to use [AWS Step Functions](https://aws.amazon.com/step-functions/) as an orchestrator of the workflow. When using a standard workflow, you are billed for each [state](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-states.html) transition within the workflow rather than the total duration of the workflow. In addition, you can move support for retries, wait conditions, error workflows, and [callbacks](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token) into the state condition to allow your Lambda functions to focus on business logic. For more information, see [Optimizing your AWS Lambda costs – Part 2](https://aws.amazon.com/blogs/compute/optimizing-your-aws-lambda-costs-part-2/) in the AWS Compute Blog.

### Move to Graviton-based functions
<a name="move-to-graviton-based-functions.bf48a61c-656e-5009-9b70-8de6ad318fbd"></a>

Lambda functions powered by next-generation Graviton2 processors are now generally available. Graviton2 functions, using an ARM-based processor architecture, are designed to deliver up to 19 percent better performance at a 20 percent lower cost for a variety of serverless workloads. With lower latency and better performance, functions powered by Graviton2 processors are ideal for powering mission-critical serverless applications.

Migrating to Graviton-based Lambda functions can be a cost-effective option for .NET developers looking to optimize their Lambda costs. Graviton-based functions use ARM-based processors instead of traditional x86 processors. This can lead to significant cost savings without sacrificing performance.

While there are several benefits to moving to Graviton-based functions, there are also several challenges and considerations that we recommend you consider. For example, Graviton-based functions require the use of Amazon Linux 2, which may not be compatible with all .NET applications. Additionally, there may be compatibility issues with third-party libraries or dependencies that aren't compatible with ARM-based processors.

If you're running .NET Framework applications and want to take advantage of serverless with Lambda, you can consider porting the applications to modern .NET by using the [Porting Assistant for .NET](https://aws.amazon.com/porting-assistant-dotnet/). This can help you to accelerate the porting of legacy .NET applications to modern .NET, enabling the application to run on Linux.

The following chart compares x86 and ARM/Graviton2 architecture results for a function that computes prime numbers.

![Comparison x86 and ARM/Graviton2 architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/8017c05a-ca63-4bba-82c1-2ebf3138d6c5.png)

The function is using a single thread. The lowest duration for both architectures is reported when memory is configured with 1.8 GB. Above that, Lambda functions have access to more than 1 vCPU, but in this case, the function can't use the additional power. For the same reason, costs are stable with memory up to 1.8 GB. With more memory, costs increase because there are no additional performance benefits for this workload. The Graviton2 processor is clearly providing better performance and lower costs for this compute-intensive function.

To configure your function to use and ARM-based processor with Graviton, do the following:

1. Sign in to the AWS Management Console and then open the [Lambda console](https://console.aws.amazon.com/lambda/).

1. Choose **Create function**.

1. For **Function name**, enter a name.

1. For **Runtime**, choose **.NET 6 (C\#/PowerShell)**.

1. For **Architecture**, select **arm64**.

1. Make any additional configurations that you require, and then choose **Create function**.

## Additional resources
<a name="net-serverless-resources"></a>
+ [Lambda functions as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html) (AWS documentation)
+ [Optimizing AWS Lambda cost and performance using AWS Compute Optimizer](https://aws.amazon.com/blogs/compute/optimizing-aws-lambda-cost-and-performance-using-aws-compute-optimizer/) (AWS Compute Blog)
+ [Optimizing your AWS Lambda costs – Part 1](https://aws.amazon.com/blogs/compute/optimizing-your-aws-lambda-costs-part-1/) (AWS Compute Blog)
+ [Optimizing your AWS Lambda costs – Part 2](https://aws.amazon.com/blogs/compute/optimizing-your-aws-lambda-costs-part-2/) (AWS Compute Blog)
+ [Building serverless .NET applications on AWS Lambda using .NET 7](https://aws.amazon.com/blogs/compute/building-serverless-net-applications-on-aws-lambda-using-net-7/) (AWS Compute Blog)
