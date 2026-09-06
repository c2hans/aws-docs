---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_detect_investigate_events_actionable_events.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC04-BP04 Implement actionable security events
<a name="sec_detect_investigate_events_actionable_events"></a>

 Create alerts that are sent to and can be actioned by your team. Ensure that alerts include relevant information for the team to take action. For each detective mechanism you have, you should also have a process, in the form of a [runbook](https://wa.aws.amazon.com/wat.concept.runbook.en.html) or [playbook](https://wa.aws.amazon.com/wat.concept.playbook.en.html), to investigate. For example, when you use [Amazon GuardDuty](http://aws.amazon.com/guardduty), it generates different [findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html). You should have a runbook entry for each finding type, for example, if a [trojan](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_trojan.html) is discovered, your runbook has simple instructions that instruct someone to investigate and remediate.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Discover metrics available for AWS services: Discover the metrics that are available through Amazon CloudWatch for the services that you are using.
  +  [AWS service documentation](https://aws.amazon.com/documentation/)
  +  [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
+  Configure Amazon CloudWatch alarms.
  +  [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+ [ Amazon CloudWatch ](https://aws.amazon.com/cloudwatch/)
+  [Amazon EventBridge ](https://aws.amazon.com/eventbridge)
+  [Security Partner Solutions: Logging and Monitoring](https://aws.amazon.com/security/partner-solutions/#logging-monitoring)

 **Related videos:**
+ [ Centrally Monitoring Resource Configuration and Compliance ](https://youtu.be/kErRv4YB_T4)
+  [Remediating Amazon GuardDuty and AWS Security Hub CSPM Findings ](https://youtu.be/nyh4imv8zuk)
+ [ Threat management in the cloud: Amazon GuardDuty and AWS Security Hub CSPM](https://youtu.be/vhYsm5gq9jE)
