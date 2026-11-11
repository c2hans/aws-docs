---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-serverless.html
---

# Consider serverless .NET
<a name="net-serverless"></a>

## Overview
<a name="net-serverless-overview"></a>

Serverless computing has become a popular approach for building and deploying applications. This is mainly because of the scalability and agility that the serverless approach offers when building a modern architecture. However, it's important to consider the cost impact of serverless computing in some scenarios.

[AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) is a serverless compute service that lets developers run code without provisioning or managing servers. Lambda is an option for .NET developers who want to reduce infrastructure costs. With Lambda, .NET developers can develop and deploy applications that are scalable and potentially cost-effective. By using a serverless approach, you no longer provision servers to handle application requests. Instead, you create functions that run on demand. This makes a serverless approach more scalable, easier to manage, and potentially more cost-effective than running, managing, and scaling virtual machines. As a result, you pay only for the resources that your application uses, and you don't have to worry about underutilized resources or server maintenance costs.

Developers can use modern, cross-platform .NET versions to build serverless applications that are fast, efficient, and cost-effective. The .NET Core and newer versions are a free and open-source framework that's better suited to running on serverless platforms over previous .NET Framework versions. This enables developers to reduce development time and increase application performance. Modern .NET also supports a range of programming languages, including C\# and F\#. For this reason, it's an attractive option for developers looking to build modern architectures in the cloud.

This section explains how you can achieve cost savings by using Lambda as a serverless option. You can further optimize costs by fine-tuning the execution profiles of your Lambda functions, right-sizing the memory allocation of your Lambda functions, using [Native AOT](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/?tabs=net7%2Cwindows), and moving to AWS Graviton-based functions.

## Cost impact
<a name="net-serverless-cost"></a>

How much you can reduce costs depends on several factors, including how often your serverless functions run, the amount of memory you allocate, and the duration of each function. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) offers a free tier, which includes one million free requests per month and 400,000 GB-seconds of compute time per month. You can reduce your monthly costs for workloads that stay within these free tier limits.

You might incur additional costs when you use a load balancer with Lambda functions as the target. AWS charges based on the amount of data that the load balancer processes for the [Lambda targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html).

## Cost optimization recommendations
<a name="net-serverless-rec"></a>

### Right size your Lambda functions
<a name="right-size-your-9999999999999999lam--functions.cd4912ce-f4ae-571d-9000-7fcff2369d01"></a>

Right sizing is an important practice for cost optimization in .NET-based [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions. This process involves identifying the memory configuration that balances performance with cost-effectiveness, without requiring changes to the code.

By configuring the memory for a Lambda function, ranging from 128 MB up to 10,240 MB, you also adjust the amount of vCPU available during invocation. This enables memory or CPU-bound applications to access additional resources during execution, leading to a potential reduction in invocation duration and overall cost.

However, identifying the appropriate configuration for your .NET-based Lambda functions can be a manual and time-intensive process, especially if changes are frequent. The [AWS Lambda Power Tuning tool](https://github.com/alexcasalboni/aws-lambda-power-tuning) can help you identify the appropriate configuration by analyzing a set of memory configurations against an example payload.

For example, increasing the memory for a .NET-based Lambda function can lead to improved total invocation time and reduced cost without affecting performance. The appropriate memory configuration for a function can vary. The AWS Lambda Power Tuning tool can help you identify a cost-effective configuration for each function.

In the following example chart, the total invocation time improves as the memory increases for this Lambda function. This reduces the cost of the total execution without affecting the original performance of the function. For this function, 512 MB is an appropriate memory configuration because it provides efficient resource utilization for the total cost of each invocation. This varies per function. Using the tool on your Lambda functions can help you identify whether they benefit from right sizing.

![Graph of invocation time](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/9379cdde-840b-4b97-88c4-9d1c4677ece8.png)

We recommend that you complete this exercise regularly, as part of any integration testing when you release new updates. If you update your functions infrequently, complete this exercise periodically to ensure that your functions are tuned and right sized. After you identify the appropriate memory setting for your Lambda functions, you can add right sizing to your processes. The AWS Lambda Power Tuning tool generates programmatic output that your CI/CD workflows can use during the release of new code. This enables you to automate memory configuration.

You can download the [AWS Lambda Power Tuning tool](https://github.com/alexcasalboni/aws-lambda-power-tuning) for free. For instructions on how to use the tool, see [How to execute the state machine](https://github.com/alexcasalboni/aws-lambda-power-tuning/blob/master/README-EXECUTE.md) in GitHub.

Lambda also supports Native ahead-of-time (AOT) compilation, which enables you to precompile .NET applications. This can help reduce costs by reducing execution times for .NET functions. For more information about creating Native AOT functions, see [.NET functions with native AOT compilation](https://docs.aws.amazon.com/lambda/latest/dg/dotnet-native-aot.html) in the Lambda documentation.

### Avoid idle wait time
<a name="avoid-idle-wait-time.d5735dbe-f76c-5f73-be7b-70574e75fe7b"></a>

Lambda function duration is one dimension used for calculating billing. When function code makes a blocking call, you are billed for the time that it waits to receive a response. This wait time can grow when Lambda functions are chained together, or a function is acting as an orchestrator for other functions. If you have workflows such as batch operations or order delivery systems, this adds management overhead. Additionally, it may not be possible to complete all workflow logic and error handling within the maximum Lambda timeout of 15 minutes.

Instead of handling this logic in function code, we recommend that you rearchitect your solution to use [AWS Step Functions](https://aws.amazon.com/step-functions/) as an orchestrator of the workflow. When using a standard workflow, you are billed for each [state](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-states.html) transition within the workflow rather than the total duration of the workflow. In addition, you can move support for retries, wait conditions, error workflows, and [callbacks](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token) into the state condition to allow your Lambda functions to focus on business logic. For more information, see [Optimizing your AWS Lambda costs – Part 2](https://aws.amazon.com/blogs/compute/optimizing-your-aws-lambda-costs-part-2/) in the AWS Compute Blog.

### Move to Graviton-based functions
<a name="move-to-graviton-based-functions.6c367f4b-93fa-5b90-93ac-62db7bfaf949"></a>

Lambda functions powered by AWS Graviton2 processors are available. Graviton2 functions, which use an ARM-based processor architecture, are designed to deliver up to 19 percent better performance at a 20 percent lower cost for a variety of serverless workloads. With lower latency and better performance, functions powered by Graviton2 processors are designed to support demanding serverless applications.

Migrating to Graviton-based Lambda functions can be a cost-effective option for .NET developers looking to reduce their Lambda costs. Graviton-based functions use ARM-based processors instead of x86 processors. For many workloads, this can lead to cost savings while maintaining performance.

Moving to Graviton-based functions has several benefits, but you must also consider some challenges. For example, Graviton-based functions require the use of Amazon Linux 2, which may not be compatible with all .NET applications. Additionally, third-party libraries or dependencies that aren't compatible with ARM-based processors can cause issues.

If you're running .NET Framework applications and want to take advantage of serverless with Lambda, you can consider porting the applications to modern .NET by using the [Porting Assistant for .NET](https://aws.amazon.com/porting-assistant-dotnet/). This can help you to accelerate the porting of legacy .NET applications to modern .NET, enabling the application to run on Linux.

The following chart compares x86 and ARM/Graviton2 architecture results for a function that computes prime numbers.

![Comparison x86 and ARM/Graviton2 architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/8017c05a-ca63-4bba-82c1-2ebf3138d6c5.png)

The function uses a single thread. The lowest duration for both architectures occurs when memory is configured with 1,769 MB. Above that, Lambda functions have access to more than 1 vCPU, but in this case, the function can't use the additional power. For the same reason, costs are stable with memory up to 1,769 MB. With more memory, costs increase because there are no additional performance benefits for this workload. The Graviton2 processor provides better performance and lower costs for this compute-intensive function.

To configure your function to use an ARM-based processor with Graviton, do the following:

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
