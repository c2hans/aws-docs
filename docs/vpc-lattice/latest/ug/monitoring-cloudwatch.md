---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-cloudwatch.html
---

# CloudWatch metrics for Amazon VPC Lattice
<a name="monitoring-cloudwatch"></a>

Amazon VPC Lattice sends data related to your target groups and services to Amazon CloudWatch, and processes it into readable, near real-time metrics. These metrics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. You can also set alarms that watch for certain thresholds and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com//AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

Amazon VPC Lattice uses a service-linked role in your AWS account to send metrics to Amazon CloudWatch. For more information, see [Using service-linked roles for Amazon VPC Lattice](using-service-linked-roles.md).

**Topics**
+ [View Amazon CloudWatch metrics](#monitoring-cloudwatch-view)
+ [Target group metrics](#monitoring-cloudwatch-tg)
+ [Service metrics](#monitoring-cloudwatch-service)

## View Amazon CloudWatch metrics
<a name="monitoring-cloudwatch-view"></a>

You can view the Amazon CloudWatch metrics for your target groups and services using the CloudWatch console or AWS CLI.

**To view metrics using the CloudWatch console**

1. Open the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Select the `AWS/VpcLattice` namespace.

1. (Optional) To view a metric across all dimensions, enter its name in the search field.

1. (Optional) To filter by dimension, select one of the following:
   + To display only the metrics reported for your target groups, choose **Target groups**. To view the metrics for a single target group, enter its name in the search field.
   + To display only the metrics reported for your services, choose **Services**. To view the metrics for a single service, enter its name in the search field.

**To view metrics using the AWS CLI**

Use the following [CloudWatch list-metrics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) AWS CLI command to list the available metrics:

`aws cloudwatch list-metrics --namespace AWS/VpcLattice`

For information about each of the metrics and their dimensions, see [Target group metrics](#monitoring-cloudwatch-tg) and [Service metrics](#monitoring-cloudwatch-service).

## Target group metrics
<a name="monitoring-cloudwatch-tg"></a>

VPC Lattice automatically stores metrics related to target groups in the `AWS/VpcLattice` [Amazon CloudWatch namespace](https://docs.aws.amazon.com//AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace). For more information about target groups, see [Target groups in VPC Lattice](target-groups.md).

**Dimensions**

To filter the metrics for target groups, use the following dimensions:
+ `AvailabilityZone`
+ `TargetGroup`

| Metric | Description | TargetGroup Protocol |
| --- | --- | --- |
|  TotalConnectionCount  | Total connections.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  |
|  ActiveConnectionCount  | Active connections.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  |
|  ConnectionErrorCount  | Total connection failures.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  |
|  HTTP1\_ConnectionCount  | Total HTTP/1.1 connections.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS  |
|  HTTP2\_ConnectionCount  | Total HTTP/2 connections.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS  |
|  ConnectionTimeoutCount  | Total connection connect timeouts.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  |
|  TotalReceivedConnectionBytes  | Total received connection bytes.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  |
|  TotalSentConnectionBytes  | Total sent connection bytes.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  |
|  TotalRequestCount  | Total requests.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS  |
|  ActiveRequestCount  | Total active requests.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS  |
|  RequestTime  | Request time to the last byte in milliseconds.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistics are `Average` and `pNN.NN` (percentiles).  |  HTTP, HTTPS  |
|  HTTPCode\_2XX\_Count, HTTPCode\_3XX\_Count, HTTPCode\_4XX\_Count, HTTPCode\_5XX\_Count  | Aggregate HTTP response codes.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS  |
|  TLSConnectionErrorCount  | Total TLS connection errors not including failed certificate verifications.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  |
|  TotalTLSConnectionHandshakeCount  | Total successful TLS connection handshakes.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  |

## Service metrics
<a name="monitoring-cloudwatch-service"></a>

VPC Lattice automatically stores metrics related to services in the `AWS/VpcLattice` [Amazon CloudWatch namespace](https://docs.aws.amazon.com//AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace). For more information about services, see [Services in VPC Lattice](services.md).

**Dimensions**

To filter the metrics for target groups, use the following dimensions:
+ `AvailabilityZone`
+ `Service`

| Metric | Description |
| --- | --- |
|  RequestTimeoutCount  | Total requests that timed out waiting for a response.+  Always reported (whether it's a zero or nonzero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |
|  TotalRequestCount  | Total requests.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |
|  RequestTime  | Request time in milliseconds.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistics are `Average` and `pNN.NN` (percentiles).  |
|  HTTPCode\_2XX\_Count, HTTPCode\_3XX\_Count, HTTPCode\_4XX\_Count, HTTPCode\_5XX\_Count  | Aggregate HTTP response codes.+  Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.  +  Once a minute. +  The most useful statistic is `Sum`.  |
