---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/monitoring-cloudhsm/next-steps.html
---

# Next steps and resources
<a name="next-steps"></a>

By implementing the monitoring best practices and recommendations in this guide, you can help achieve a high-performing, resilient, efficient, secure, and cost-optimized infrastructure on AWS CloudHSM. Near real-time analysis of the overall health and performance of your AWS CloudHSM cluster provides operational insights over time and helps you prevent issues that affect your workloads.

This guide described many metrics and alarms that you can configure to monitor AWS CloudHSM clusters and hardware security modules (HSMs). At a minimum, consider implementing those that contain "Recommended" in the heading. Review the others and determine whether they are beneficial for your use case or environment.

If you need assistance with increasing AWS service quotas, you can contact [AWS Support](https://aws.amazon.com/premiumsupport/). For assistance implementing the recommended metrics and alarms in this guide, or for assistance optimizing your AWS CloudHSM resources, you can contact [AWS Professional Services](https://aws.amazon.com/professional-services/) or an [AWS Partner](https://aws.amazon.com/partners/work-with-partners/).

## Resources
<a name="next-steps-resources"></a>

The following resources can help you plan and implement the metrics and alarms described in this guide.

### AWS CloudHSM documentation
<a name="9999999999999999hsmlong--documentation.e39398df-36b0-5798-ac9d-e19fcd57b9a4"></a>
+ [Getting CloudWatch metrics for AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-metrics-cw.html)
+ [Monitoring AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/get-logs.html)
+ [Monitoring best practices](https://docs.aws.amazon.com/cloudhsm/latest/userguide/bp-monitoring.html)

### Amazon CloudWatch Logs documentation
<a name="9999999999999999cwllong--documentation.3e8dd48e-f7d6-57c6-b5fc-5cde986a4664"></a>
+ [Creating an alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html)
+ [Creating a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html)

### Amazon EventBridge documentation
<a name="9999999999999999evlong--documentation.cbd326b6-eb07-5ed3-86e4-f74403da92b7"></a>
+ [Creating rules that react to events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html)
+ [Input transformation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
