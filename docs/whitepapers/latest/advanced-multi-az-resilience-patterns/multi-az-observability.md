---
source_url: https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/multi-az-observability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Multi-AZ observability
<a name="multi-az-observability"></a>

 To be able to evacuate an Availability Zone during an event that is isolated to a single Availability Zone, you first must be able to detect that the failure is, in fact, isolated to a single Availability Zone. This requires high-fidelity visibility into how the system is behaving in each Availability Zone. Many AWS services provide out-of-the-box metrics that provide operational insights about your resources. For example, Amazon EC2 provides numerous metrics such as CPU utilization, disk reads and writes, and network traffic in and out.

 However, as you build workloads that use these services, you need more visibility than just those standard metrics. You want visibility into the customer experience being provided by your workload. Additionally, you need your metrics to be aligned to the Availability Zones where they are being produced. This is the insight you need to detect differentially observable gray failures. That level of visibility requires instrumentation.

 Instrumentation requires writing explicit code. This code should do things such as record how long tasks take, count how many items succeeded or failed, collect metadata about the requests, and so on. You also need to define thresholds ahead of time to define what is considered normal and what isn’t. You should outline objectives and different severity thresholds for latency, availability, and error counts in your workload. The Amazon Builders’ Library article [Instrumenting distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/) provides a number of best practices.

 Metrics should both be generated from the server-side as well as the client-side. A best practice for generating client-side metrics and understanding the customer experience is using [canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html), software that regularly probes your workload and records metrics.

 In addition to producing these metrics, you also need to understand their context. One way to do this is by using [dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension). Dimensions give a metric a unique identity, and help explain what the metrics are telling you. For metrics that are used to identify failure in your workload (for example, latency, availability, or error count), you need to use dimensions that align to your [fault isolation boundaries](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/use-fault-isolation-to-protect-your-workload.html).

 For example, if you are running a web service in one Region, across multiple Availability Zones, using a [Model-view-controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) (MVC) web framework, you should use `Region`, [`Availability Zone ID`](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html), `Controller`, `Action`, and `InstanceId` as the dimensions for your dimension sets (if you were using microservices, you might use the service name and HTTP method instead of the controller and action names). This is because you expect different types of failures to be isolated by these boundaries. You wouldn’t expect a bug in your web service’s code that affects its ability to list products to also impact the home page. Similarly, you wouldn’t expect a full EBS volume on a single EC2 instance to affect other EC2 instances from serving your web content. The Availability Zone ID dimension is what enables you to identify Availability Zone-related impacts consistently across AWS accounts. You can find the Availability Zone ID in your workloads in a number of different ways. Refer to [Appendix A – Getting the Availability Zone ID](appendix-a-getting-the-availability-zone-id.md) for some examples.

 While this document mainly uses Amazon EC2 as the compute resource in the examples, `InstanceId` could be replaced with a container ID for [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS) and [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) compute resources as components of your dimensions.

 Your canaries can also use `Controller`, `Action`, `AZ-ID`, and `Region` as dimensions in their metrics if you have zonal endpoints for your workload. In this case, align your canaries to run in the Availability Zone that they are testing. This ensures that if an isolated Availability Zone event is impacting the Availability Zone in which your canary is running, it doesn’t record metrics that make a different Availability Zone it is testing appear unhealthy. For example, your canary can test each zonal endpoint for a service behind a Network Load Balancer (NLB) or Application Load Balancer (ALB) using its [zonal DNS names](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#dns-name).

![Diagram showing a canary running on CloudWatch Synthetics or an AWS Lambda function testing each zonal endpoint of an NLB](http://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/images/canary-testing-for-zonal-impact.png)

 By producing metrics with these dimensions, you can establish [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) that notify you when changes in availability or latency occur within those boundaries. You can also quickly analyze that data using [dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). To use both metrics and logs efficiently, Amazon CloudWatch offers the [embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html) (EMF) that enables you to embed custom metrics with log data. CloudWatch automatically extracts the custom metrics so you can visualize and alarm on them. AWS provides several [client libraries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Libraries.html) for different programming languages that make it easy to get started with EMF. They can be used with Amazon EC2, Amazon ECS, Amazon EKS, [AWS Lambda](https://aws.amazon.com/lambda/), and on-premises environments. With metrics embedded into your logs, you can also use [Amazon CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) to create time series graphs that display contributor data. In this scenario, we could display data grouped by dimensions like `AZ-ID`, `InstanceId`, or `Controller` as well as any other field in the log like `SuccessLatency` or `HttpResponseCode`.

```
{
  "_aws": {
    "Timestamp": 1634319245221,
    "CloudWatchMetrics": [
      {
        "Namespace": "workloadname/frontend",
        "Metrics": [
          { "Name": "2xx", "Unit": "Count" },
          { "Name": "3xx", "Unit": "Count" },
          { "Name": "4xx", "Unit": "Count" },
          { "Name": "5xx", "Unit": "Count" },
          { "Name": "SuccessLatency", "Unit": "Milliseconds" }
        ],
        "Dimensions": [
          [ "Controller", "Action", "Region", "AZ-ID", "InstanceId"],
          [ "Controller", "Action", "Region", "AZ-ID"],
          [ "Controller", "Action", "Region"]
        ]
      }
    ],
    "LogGroupName": "/loggroupname"
  },
  "CacheRefresh": false,
  "Host": "use1-az2-name.example.com",
  "SourceIp": "34.230.82.196",
  "TraceId": "|e3628548-42e164ee4d1379bf.",
  "Path": "/home",
  "OneBox": false,
  "Controller": "Home",
  "Action": "Index",
  "Region": "us-east-1",
  "AZ-ID": "use1-az2",
  "InstanceId": "i-01ab0b7241214d494",
  "LogGroupName": "/loggroupname",
  "HttpResponseCode": 200,
  "2xx": 1,
  "3xx": 0,
  "4xx": 0,
  "5xx": 0,
  "SuccessLatency": 20
}
```

This log has three sets of dimensions. They progress in order of granularity, from instance to Availability Zone to Region (`Controller` and `Action` are always included in this example). They support creating alarms across your workload that indicate when there is impact to a specific controller action in a single instance, in a single Availability Zone, or within a whole AWS Region. These dimensions are used for the count of 2xx, 3xx, 4xx, and 5xx HTTP response metrics, as well as the latency for successful request metrics (if the request failed, it would also record a metric for failed request latency). The log also records other information such as the HTTP path, the source IP of the requestor, and whether this request required the local cache to be refreshed. These data points can then be used to calculate the availability and latency of each API the workload provides.

**A note on using HTTP response codes for availability metrics**
Typically, you can consider 2xx and 3xx responses as successful, and 5xx as failures. 4xx response codes fall somewhere in the middle. Usually, they are produced due to a client error. Maybe a parameter is out of range leading to a [400 response](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes), or they’re requesting something that doesn’t exist, resulting in a 404 response. You wouldn’t count these responses against your workload’s availability. However, this could also be the result of a bug in the software.
For example, if you’ve introduced stricter input validation that rejects a request that would have succeeded before, the 400 response might count as a drop in availability. Or maybe you’re throttling the customer and returning a 429 response. While throttling a customer protects your service to maintain its availability, from the customer’s perspective, the service isn’t available to process their request. You’ll need to decide whether or not 4xx response codes are part of your availability calculation.

While this section has outlined using CloudWatch as a way to collect and analyze metrics, it’s not the only solution you can use. You might choose to also send metrics into Amazon Managed Service for Prometheus and Amazon Managed Grafana, an Amazon DynamoDB table, or use a third-party monitoring solution. The key is that the metrics your workload produces must contain context about the fault isolation boundaries of your workload.

With workloads that produce metrics with dimensions aligned to fault isolation boundaries, you can create observability that detects Availability Zone isolated failures. The following sections describe three complimentary approaches for detecting failures that arise from the impairment of a single Availability Zone.

**Topics**
+ [Failure detection with CloudWatch composite alarms](failure-detection-with-cloudwatch-composite-alarms.md)
+ [Failure detection using outlier detection](failure-detection-using-outlier-detection.md)
+ [Failure detection of single instance zonal resources](failure-detection-of-single-instance-zonal-resources.md)
+ [Summary](summary.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
