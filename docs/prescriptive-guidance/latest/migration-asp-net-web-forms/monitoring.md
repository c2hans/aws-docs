---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-asp-net-web-forms/monitoring.html
---

# Monitoring and observability for ASP.NET Web Forms applications on AWS
<a name="monitoring"></a>

When you run an ASP.NET Web Forms application on AWS, it's essential to monitor both the underlying infrastructure and the application itself to ensure optimal performance, availability, and operational excellence. AWS provides a comprehensive suite of monitoring tools and services that you can use to achieve this goal.

## Infrastructure monitoring
<a name="infrastructure"></a>

To monitor the infrastructure, such as the EC2 instances for Windows Server, you can track the standard [Amazon EC2 metrics that are available in Amazon CloudWatch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-detailed-monitoring.html). These metrics provide insights into various aspects of your EC2 instances, including CPU utilization, network traffic, disk I/O, and more.

To gain deeper visibility into the performance of your Windows Server instances, you might want to monitor and receive alerts on more granular Windows metrics. To do this, install the CloudWatch agent on the EC2 instances and enable the publishing of [Windows Performance Monitor counters to CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.html). The CloudWatch agent enables you to collect and monitor custom metrics, including Windows-specific metrics such as memory usage, disk space, and other system performance counters.

By monitoring these infrastructure-level metrics, you can proactively identify and address potential issues, such as resource bottlenecks or capacity constraints, before they impact your application's performance or availability.

## Application monitoring
<a name="application"></a>

In addition to monitoring the AWS infrastructure, you should monitor your ASP.NET Web Forms application to gain insights into its performance, error rates, and overall health. AWS provides several tools and services that can assist with application monitoring, including AWS X-Ray.

AWS X-Ray is a distributed tracing service that provides end-to-end visibility into your application's performance and behavior. You can use the [AWS X-Ray SDK for .NET](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-dotnet.html) to instrument your ASP.NET Web Forms application running on .NET Framework 4.5 and later versions to capture detailed information about incoming requests, downstream calls to AWS services, other APIs, and SQL Server databases.

You can use AWS X-Ray to:
+ **Trace request execution**: Visualize the flow of requests through your application, including latencies, errors, and performance bottlenecks.
+ **Identify performance issues**: Pinpoint the root cause of performance issues by analyzing the end-to-end execution path of requests, including external dependencies and database queries.
+ **Monitor error rates**: Monitor and get alerts on application errors, including detailed error messages and stack traces, to quickly identify and resolve issues.
+ **Integrate with other AWS services**: Integrate AWS X-Ray seamlessly with other AWS services, such as AWS Lambda, Amazon ECS, and Amazon EKS, to enable end-to-end monitoring of distributed applications.

In addition to AWS X-Ray, you can use third-party application monitoring tools that provide additional capabilities, such as user experience monitoring, synthetic transaction monitoring, and real-user monitoring.

By combining infrastructure monitoring with application monitoring, you can gain comprehensive visibility into the performance and health of your ASP.NET Web Forms application on AWS. You can proactively identify and resolve issues, optimize resource utilization, and ensure a seamless experience for your application's users.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
