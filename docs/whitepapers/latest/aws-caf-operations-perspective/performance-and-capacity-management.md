---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/performance-and-capacity-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Performance and capacity management
<a name="performance-and-capacity-management"></a>

** Monitor workload performance and ensure that capacity meets current and future demands. **

 To ensure that your applications fulfil their business purpose, it’s essential to measure performance and ensure that you do not reach capacity limits. Although the AWS Cloud can allow you to scale to unparalleled levels, it’s important to understand that there are performance considerations and [service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) that need to be measured and acted upon.

## Start
<a name="start-44"></a>

 Many AWS services publish metrics to Amazon CloudWatch that should form the basis of the absolute minimum metrics you should be monitoring and alerting upon. As stated in the observability section of this whitepaper, you should also monitor and alert upon metrics collected from AWS using the [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) or [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) for Amazon EC2 instances as well as managed services. For large scale applications, ensure that you load test your application in pre-production environments to gauge where you may reach performance limits.

 While the cloud offers virtually infinite scalability, even for the largest organizations and applications, it’s important to remember that managed services have [quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) (formerly referred to as limits) that are designed to help guarantee the availability of AWS resources, and prevent accidental provisioning of more resources than needed. You must anticipate these quotas by running load tests in pre-production environments, to anticipate demand in production. These tests are vital to ensure that you do not encounter any unanticipated service quotas or hit any limits encountered by the design of your application.

 Use Amazon CloudWatch metrics that are provided by AMS, as well as metrics provided by your EC2 instances through the CloudWatch agent, to ensure that your application will respond according to your business requirements. It is vital that you test these against service quotas in pre-production before deploying to production, but you must also continuously monitor these metrics in production. It is possible, and often desirable, that your actual demand will outstrip your anticipated demand. If this is the case, you need to have mechanisms that alert you to such changes so that you can respond accordingly.

 [AWS Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) is a service that enables you to view and manage your quotas for AWS services from a central location. Along with looking up the quota values, you can also request a quota increase, monitor the usage of specific services API actions, and create alerts for them directly from the Service Quotas console. [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) gives you additional insight as to whether or not you are approaching or breaching limits.

## Advance
<a name="advance-44"></a>

 To make full use of the tools available to you to measure performance, you need to monitor your metrics and make use of AWS services that give you enhanced insights. To gain full visibility into your applications’ performance, you need to implement distributed tracing, one of the three pillars of observability.

 [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) is a distributed tracing system that can help you gain insights into how your applications communicate between each other, measure performance of [functions or lines of code](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-subsegments), and provide analytics capabilities correlated with other signals, such as metrics and logs. Additionally, [CloudWatch Log Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html), [Lambda Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights.html), [Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html), and [Metric Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html) enable you to use enhanced insights into how your application is performing.

While load testing gives you an idea of how well your application sustains its performance at certain amount of traffic and its associated infrastructure capacity, your infrastructure will probably not always be performing at that level. This is why it’s vital that you implement Auto Scaling for horizontal scaling wherever possible to allow your infrastructure to scale according to the traffic. [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-a-scaling-plan.html) helps your application scale by monitoring and adjusting capacity using metrics and user-defined thresholds.

 Multiple AWS services provide [serverless](https://aws.amazon.com/serverless/) offerings, where AWS shifts the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) from you to AWS. AWS takes most of the work such as scaling, servers/systems patching, and management. This lets you focus on your business use case and spend more time on innovation. When working with databases, AWS offers more than 15 [purpose-built, fully managed database engines](https://aws.amazon.com/products/databases/) to choose from according to your use cases. Orchestrating containers at scale can be daunting and that’s why AWS offers Amazon EKS, Amazon ECS, AWS Fargate, and [other container services](https://aws.amazon.com/containers/) to make it easier to manage your underlying infrastructure. Choosing the right service and architecture for the job helps you achieve better performance and less management overhead.

## Excel
<a name="excel-44"></a>

 Use testing to evaluate performance and capacity limits, and use scaling mechanisms to help you sustain your customer traffic and growth. You should adopt flexible architectures that enable you to scale globally. Extending your infrastructure to multiple regions can give you that extra mile of capacity. Using the tools discussed in the Observability section of this whitepaper, such as CloudWatch RUM, you can understand the performance impact on your customers around the globe and deploy accordingly.

 Testing your applications should not be a one-time event before going to production. Continuously testing your applications helps you detect customer impact when issues occur and can surface issues before technical metrics become available. Use [CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) and CloudWatch RUM as described in the Observability section to continuously monitor application performance, including when you have no active users. Build experimentations and design your applications around failures to help recover quickly. AWS FIS is a fully managed service to help you run experiments safely and easily implement [chaos engineering](https://aws.amazon.com/blogs/mt/chaos-engineering-leveraging-aws-fault-injection-simulator-in-a-multi-account-aws-environment/). Chaos engineering is the practice of stressing an application in testing or production environments by creating disruptive events, such as sudden increase in CPU or memory consumption, observing how the system responds, and implementing improvements.
