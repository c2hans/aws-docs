---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/monitoring.html
---

# Monitoring
<a name="monitoring"></a>

Monitoring is the process of collecting different metrics, such as CPU and memory, and storing them in a time-series database such as Amazon Managed Service for Prometheus. The monitoring system can be push based or pull based. In push-based systems, the source pushes metrics periodically to the time-series data base. In pull-based systems, the scraper scrapes metrics from various sources and stores them in the time-series database. Developers can analyze the metrics, filter the metrics, and plot them over time to visualize performance. Implementing monitoring successfully can be split into two broad areas: application and infrastructure.

For application developers, the following metrics are critical:
+ **Latency** – The time taken to receive a response
+ **Request throughput** – The total number of requests handled per second
+ **Request error rate** – The total number of errors

Capture resource utilization, saturation, and error counts for each resource (such as the application container, the database) that's involved in the business transaction. For example, when monitoring CPU usage, you can track average CPU utilization, average load, and peak load during the performance-test run. When a resource reaches saturation during stress testing, but it might not reach saturation during a performance run for a shorter period of time.

## Metrics
<a name="metrics"></a>

Applications can use different actuators such, as spring boot actuators, to monitor their applications. These production-grade libraries generally expose a REST endpoint for monitoring information about the running applications. The libraries can monitor the underlying infrastructure, application platforms, and other resources. If any of the default metrics don't meet the requirements, the developer must implement custom metrics. Custom metrics can help track business key performance indicators (KPIs) that can't be tracked through data from default implementations. For example, you might want to track a business operation such as third-party API integration latency or the total number of transactions completed.

### Cardinality
<a name="cardinality.a5b9e890-a2a1-5536-be8b-2d484e92d9ed"></a>

Cardinality refers to number of unique time-series of a metric. Metrics are labeled to provide additional information. For example, a REST-based application that tracks the request count for a particular API indicates a cardinality of 1. If you add a user label to identify the request count per user, the cardinality increases proportionally to the number of users. By adding labels that create cardinality, you can slice and dice metrics by various groups. It's important to use the right labels for the right use case because cardinality increases the number of metrics series in the backend monitoring time-series database.

### Resolution
<a name="resolution.0b8b0127-102c-53de-ae4b-4ff9eed659f9"></a>

In a typical monitoring setup, the monitoring application is configured to scrape the metrics from the application periodically. The periodicity of scraping defines the granularity of the monitoring data. Metrics collected at shorter interval tends to provide a more accurate view of the performance because more data points are available. However, the load on the time-series database increases as more entries are stored. Typically a granularity of 60 seconds is standard resolution and 1 second is high resolution.

## DevOps team
<a name="monitoring-devops-team"></a>

Application developers often ask DevOps engineers to set up a monitoring environment for visualizing metrics of the infrastructure and applications. The DevOps engineer must set up an environment that is scalable and supports the data-visualization tools used by the application developer. This involves scraping monitoring data from different sources and sending the data to a central time-series database such as [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html).

### Monitoring backend
<a name="monitoring-backend.596d4c33-d053-5bbd-b6e8-7a25e434a5e0"></a>

A monitoring backend service supports the collection, storage, querying, and visualization of metrics data. It's typically a time-series database such as Amazon Managed Service for Prometheus or InfluxData InfluxDB. Using a service-discovery mechanism, the monitoring collector can collect metrics from different sources and store them. While performance testing, it's important to store the metrics data so that it can be searched at a later time. We recommend saving at least 15 days of data for metrics. However, storing the metrics for a longer duration doesn't add significant benefits and leads to unnecessary storage costs. Because the performance test can generate a large volume of metrics, it's important for the metrics infrastructure to scale while providing fast query performance. The monitoring backend service provides a query language which can be used to view the metrics data.

### Visualization
<a name="visualization.eed7da42-a7d6-5021-996d-f46201e9058d"></a>

Provide visualization tools that can display the application data to provide meaningful insights. The DevOps engineer and the application developer should learn the query language for the monitoring backend and work closely to generate a dashboard template that  can be reused. On the dashboards, include latency, and errors while also displaying resource utilization and saturation across the infrastructure and the application resources.

### Automating the monitoring infrastructure
<a name="automating-the-monitoring-infrastructure.3d12d52f-98cd-57ea-91f0-6a521331bcf6"></a>

Similar to logging, it's important to automate installation and operation of the monitoring infrastructure so that you can accommodate the different requirements of different applications. Use IaC tools to provision the monitoring infrastructure's backend. Then you can provision the monitoring infrastructure either as a shared service or as an independent bespoke deployment for a particular application.

Use CD pipelines to automate the following:
+ Deploy the monitoring infrastructure on demand and tear it down when it isn't required.
+ Update the monitoring configuration to filter or aggregate metrics.
+ Deploy application dashboards.

## Monitoring tools
<a name="monitoring-tools"></a>

Amazon Managed Service for Prometheus is a [Prometheus](https://prometheus.io/)-compatible monitoring service for container infrastructure and application metrics for containers that you can use to securely monitor container environments at scale. For more information, see the blog post [Getting Started with Amazon Managed Service for Prometheus](https://aws.amazon.com/blogs/mt/getting-started-amazon-managed-service-for-prometheus/).

Amazon CloudWatch provides full-stack monitoring on AWS. CloudWatch supports both AWS native and open source solutions so that you can understand what is happening across your technology stack at any time.

Native AWS tools include the following:
+ [Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)
+ [CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html)
+ [CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
+ [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

Amazon CloudWatch offers purpose-built features that address specific use cases such as container monitoring through CloudWatch Container Insights. These features are built-into CloudWatch so that you can set up logs, metrics collection, and monitoring.

For your containerized applications and microservices, use Container Insights to collect, aggregate, and summarize metrics and logs. Container Insights is available for Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), and Kubernetes platforms on Amazon Elastic Compute Cloud (Amazon EC2). Container Insights collects data as performance log events in the [embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html). These performance log event entries use a structured JSON schema that supports high-cardinality data ingestion and storage at scale.

For information about implementing Container Insights with Amazon EKS, see the blog post [Introducing Amazon CloudWatch Container Insights for Amazon EKS Fargate using AWS Distro for OpenTelemetry](https://aws.amazon.com/blogs/containers/introducing-amazon-cloudwatch-container-insights-for-amazon-eks-fargate-using-aws-distro-for-opentelemetry/).
