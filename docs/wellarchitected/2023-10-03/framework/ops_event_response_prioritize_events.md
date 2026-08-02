---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/ops_event_response_prioritize_events.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS10-BP03 Prioritize operational events based on business impact
<a name="ops_event_response_prioritize_events"></a>

 Ensure that when multiple events require intervention, those that are most significant to the business are addressed first. Impacts can include loss of life or injury, financial loss, or damage to reputation or trust.

 **Common anti-patterns:**
+  You receive a support request to add a printer configuration for a user. While working on the issue, you receive a support request stating that your retail site is down. After completing the printer configuration for your user, you start work on the website issue.
+  You get notified that both your retail website and your payroll system are down. You don't know which one should get priority.

 **Benefits of establishing this best practice:** Prioritizing responses to the incidents with the greatest impact on the business notifies your management of that impact.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Prioritize operational events based on business impact: Ensure that when multiple events require intervention, those that are most significant to the business are addressed first. Impacts can include loss of life or injury, financial loss, regulatory violations, or damage to reputation or trust.
