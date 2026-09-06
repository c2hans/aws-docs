---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_process_culture_automation_remediate_issues.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP05 Use automation to proactively remediate performance-related issues
<a name="perf_process_culture_automation_remediate_issues"></a>

 Use key performance indicators (KPIs), combined with monitoring and alerting systems, to proactively address performance-related issues.

 **Common anti-patterns:**
+  You only allow operations staff the ability to make operational changes to the workload.
+  You let all alarms filter to the operations team with no proactive remediation.

 **Benefits of establishing this best practice:** Proactive remediation of alarm actions allows support staff to concentrate on those items that are not automatically actionable. This helps operations staff handle all alarms without being overwhelmed and instead focus only on critical alarms.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 Use alarms to trigger automated actions to remediate issues where possible. Escalate the alarm to those able to respond if automated response is not possible. For example, you may have a system that can predict expected key performance indicator (KPI) values and alarm when they breach certain thresholds, or a tool that can automatically halt or roll back deployments if KPIs are outside of expected values.

 Implement processes that provide visibility into performance as your workload is running. Build monitoring dashboards and establish baseline norms for performance expectations to determine if the workload is performing optimally.

### Implementation steps
<a name="implementation-steps"></a>
+  Identify and understand the performance issue that can be remediated automatically. Use AWS monitoring solutions such as [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) or AWS X-Ray to help you better understand the root cause of the issue.
+  Create a step-by-step remediation plan and process that can be used to automatically fix the issue.
+  Configure the trigger to automatically initiate the remediation process. For example, you can define a trigger to automatically restart an instance when it reaches a certain threshold of CPU utilization.
+  Use AWS services and technologies to automate the remediation process. For example, [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) provides a secure and scalable way to automate the remediation process.
+  Test the automated remediation process in a pre-production environment.
+  After testing, implement the remediation process in production environment and continually monitor to identify areas for improvement.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [Monitoring, Logging, and Performance AWS Partner Network Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance)
+  [X-Ray Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
+  [Using Alarms and Alarm Actions in CloudWatch](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cw-example-using-alarm-actions.html)

 **Related videos:**
+  [Intelligently automating cloud operations](https://www.youtube.com/watch?v=m0S8eAF0l54)
+  [Setting up controls at scale in your AWS environment](https://www.youtube.com/watch?v=NkE9_okfPG8)
+  [Automating patch management and compliance using AWS](https://www.youtube.com/watch?v=gL3baXQJvc0)
+  [How Amazon uses better metrics for improved website performance](https://www.youtube.com/watch?v=_uaaCiyJCFA&ab_channel=AWSEvents)

 **Related examples:**
+  [CloudWatch Logs Customize Alarms](https://github.com/awslabs/cloudwatch-logs-customize-alarms)
