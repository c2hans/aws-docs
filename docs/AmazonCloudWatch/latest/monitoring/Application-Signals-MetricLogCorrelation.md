---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Application-Signals-MetricLogCorrelation.html
---

# Enable metric to log correlation
<a name="Application-Signals-MetricLogCorrelation"></a>

If you publish application logs to log groups in CloudWatch Logs, you can enable *metric to application log correlation* in Application Signals. With metric log correlation, the Application Signals console automatically displays the relevant log groups associated with a metric.

For example, suppose you notice a spike in a latency graph. You can choose a point on the graph to load the diagnostics information for that point in time. The diagnostics information will show the relevant application log groups that are associated with the current service and metric. Then you can choose a button to run a CloudWatch Logs Insights query on those log groups. Depending on the information contained in the application logs, this might help you to investigate the cause of the latency spike.

Depending on the architecture that your application runs on, you might have to also set an environment variable to enable metric to application log correlation.
+ On Amazon EKS, no further steps are needed.
+ On Amazon ECS, no further steps are needed.
+ On Amazon EC2, see step 4 in the procedure in [Step 3: Instrument your application and start it](CloudWatch-Application-Signals-Enable-EC2Main.md#CloudWatch-Application-Signals-Enable-Other-instrument).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
