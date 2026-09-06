---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/zookeeper-quorum.html
---

# ZooKeeper quorum
<a name="zookeeper-quorum"></a>

The guidance sets up a ZooKeeper [quorum](concepts-and-definitions.md), consisting of the specified number of instances as defined in the CDK configuration. Metrics from these ZooKeeper instances are gathered and sent to CloudWatch under the metric namespace `AWSSolutions/Druid`.

The guidance additionally allocates an extra Elastic Network Interface (ENI) for each instance, enabling Druid to establish connections with ZooKeeper through static IP addresses.
