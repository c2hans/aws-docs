---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_telemetry_dependency_telemetry.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS04-BP04 Implement dependency telemetry
<a name="ops_telemetry_dependency_telemetry"></a>

 Design and configure your workload to emit information about the status (for example, reachability or response time) of resources it depends on. Examples of external dependencies can include, external databases, DNS, and network connectivity. Use this information to determine when a response is required.

 **Common anti-patterns:**
+  You are unable to determine if the reason your application is unreachable is a DNS issue without manually performing a check to see if your DNS provider is working.
+  Your shopping cart application is unable to complete transactions. You are unable to determine if it's a problem with your credit card processing provider without contacting them to verify.

 **Benefits of establishing this best practice:** Understanding the health of your dependencies enables you to respond if necessary.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement dependency telemetry: Design and configure your workload to emit information about the state and status of systems it depends on. Some examples include: external databases, DNS, network connectivity, and external credit card processing services.
  +  [Amazon CloudWatch Agent with AWS Systems Manager integration - unified metrics & log collection for Linux & Windows](https://aws.amazon.com/blogs/aws/new-amazon-cloudwatch-agent-with-aws-systems-manager-integration-unified-metrics-log-collection-for-linux-windows/)
  +  [Collect metrics and logs from Amazon EC2 instances and on-premises servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon CloudWatch Agent with AWS Systems Manager integration - unified metrics & log collection for Linux & Windows](https://aws.amazon.com/blogs/aws/new-amazon-cloudwatch-agent-with-aws-systems-manager-integration-unified-metrics-log-collection-for-linux-windows/)
+  [Collect metrics and logs from Amazon EC2 instances and on-premises servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

   **Related examples:**
+  [Well-Architected Labs – Dependency Monitoring](https://wellarchitectedlabs.com/operational-excellence/100_labs/100_dependency_monitoring/)
