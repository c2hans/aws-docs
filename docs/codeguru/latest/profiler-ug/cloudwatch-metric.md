---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/cloudwatch-metric.html
---

# Monitoring profiling groups with CloudWatch metrics
<a name="cloudwatch-metric"></a>

 You can view Amazon CodeGuru Profiler metrics in the Amazon CloudWatch console. <a name="cloudswatch-console-procedure"></a>

**To access profiling group metrics**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1.  In the navigation pane, choose **Metrics**.

1.  On the **All metrics** tab, choose **AWS/CodeGuruProfiler**.

1.  Choose **ProfilingGroupName**. Metrics for recommendations for all selected profiling groups are displayed in the graph on the page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
