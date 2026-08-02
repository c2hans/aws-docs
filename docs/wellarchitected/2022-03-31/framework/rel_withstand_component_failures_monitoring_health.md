---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_monitoring_health.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL11-BP01 Monitor all components of the workload to detect failures
<a name="rel_withstand_component_failures_monitoring_health"></a>

 Continuously monitor the health of your workload so that you and your automated systems are aware of degradation or failure as soon as they occur. Monitor for key performance indicators (KPIs) based on business value.

 All recovery and healing mechanisms must start with the ability to detect problems quickly. Technical failures should be detected first so that they can be resolved. However, availability is based on the ability of your workload to deliver business value, so key performance indicators (KPIs) that measure this need to be a part of your detection and remediation strategy.

 **Common anti-patterns:**
+  No alarms have been configured, so outages occur without notification.
+  Alarms exist, but at thresholds that don't provide adequate time to react.
+  Metrics are not collected often enough to meet the recovery time objective (RTO).
+  Only the customer facing tier of the workload is actively monitored.
+  Only collecting technical metrics, no business function metrics.
+  No metrics measuring the user experience of the workload.

 **Benefits of establishing this best practice:** Having appropriate monitoring at all layers enables you to reduce recovery time by reducing time to detection.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Determine the collection interval for your components based on your recovery goals.
  +  Your monitoring interval is dependent on how quickly you must recover. Your recovery time is driven by the time it takes to recover, so you must determine the frequency of collection by accounting for this time and your recovery time objective (RTO).
+  Configure detailed monitoring for components.
  +  Determine if detailed monitoring for EC2 instances and Auto Scaling is necessary. Detailed monitoring provides 1-min interval metrics, and default monitoring provides 5-minute interval metrics.
    +  [Enable or Disable Detailed Monitoring for Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html)
    +  [Monitoring Your Auto Scaling Groups and Instances Using Amazon CloudWatch](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html)
  +  Determine if enhanced monitoring for RDS is necessary. Enhanced monitoring uses an agent on the RDS instances to get useful information about different process or threads on an RDS instance.
    +  [Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)
+  Create custom metrics to measure business key performance indicators (KPIs). Workloads implement key business functions. These functions should be used as KPIs that help identify when an indirect problem happens.
  +  [Publishing Custom Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
+  Monitor the user experience for failures using user canaries. Synthetic transaction testing (also known as canary testing, but not to be confused with canary deployments) that can run and simulate customer behavior is among the most important testing processes. Run these tests constantly against your workload endpoints from diverse remote locations.
  +  [Amazon CloudWatch Synthetics enables you to create user canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
+  Create custom metrics that track the user's experience. If you can instrument the experience of the customer, you can determine when the consumer experience degrades.
  +  [Publishing Custom Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
+  Set alarms to detect when any part of your workload is not working properly, and to indicate when to Auto Scale resources. Alarms can be visually displayed on dashboards, send alerts via Amazon SNS or email, and work with Auto Scaling to scale up or down the resources for a workload.
  +  [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
+  Create dashboards to visualize your metrics. Dashboards can be used to visually see trends, outliers, and other indicators of potential problems, or to provide an indication of problems you may want to investigate.
  +  [Using CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon CloudWatch Synthetics enables you to create user canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
+  [Enable or Disable Detailed Monitoring for Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html)
+  [Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)
+  [Monitoring Your Auto Scaling Groups and Instances Using Amazon CloudWatch](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html)
+  [Publishing Custom Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
+  [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
+  [Using CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)

 **Related examples:**
+  [Well-Architected lab: Level 300: Implementing Health Checks and Managing Dependencies to Improve Reliability](https://wellarchitectedlabs.com/Reliability/300_Health_Checks_and_Dependencies/README.html)
