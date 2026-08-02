---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-instance-session-performance.html
---

# Viewing Instance and Session Performance Metrics Using the Console
<a name="monitoring-instance-session-performance"></a>

You can monitor Amazon WorkSpaces Applications fleet instances and session performance using the WorkSpaces Applications console or the CloudWatch console.

Performance metrics are collected at a 5-minute interval. After a new session is provisioned, the first metric data point will show up in 5 minutes. Subsequent metric data points will be available at every 5-minute interval.

**Note**
Performance metrics are currently available only for multi-session fleets

**To view instance and session in the WorkSpaces Applications console**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home).

1. In the left pane, choose **Fleets**.

1. Select a fleet and choose **View Details** and **View Sessions**.

1. Select a session to view the metrics.

1. By default, the graph displays the following metrics:
   + Instance metrics
     + CpuUtilizationInstance
     + MemoryUtilizationInstance
     + PagingFileUtilizationInstance
     + DiskUtilizationInstance
   + Session metrics
     + CpuUtilizationSession
     + MemoryUtilizationSession

**To view instance and session performance in the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left pane, choose **Metrics**.

1. Choose the **AppStream** namespace and then choose **Fleet Instance Metrics** or **Fleet Session Metrics**.

1. Select the metrics to graph.
