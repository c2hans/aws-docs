---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus04-bp01.html
---

# EUCSUS04-BP01 Implement a scaling methodology in WorkSpaces Applications
<a name="eucsus04-bp01"></a>

 Scaling policies improve resource utilization and cost management for application streaming workloads.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-98"></a>

 Either fleet type (On-Demand or Always-On) requires a methodology to verify that the appropriate number of instances are available when users initiate a connection.

 A combination of step scaling, scheduled scaling, or target tracking scaling is recommended to match each fleet usage. To avoid extra consumption of instances, monitor your fleet usage and modify your scaling policies accordingly. The following resources describe in further detail the differences between the types of scaling and how to configure them to align with the pattern of usage for the applications being delivered. Keep in mind that the fleet type choice is only available during the fleet creation process.
+  [WorkSpaces Applications Fleet Types ](https://docs.aws.amazon.com/appstream2/latest/developerguide/fleet-type.html)
+  [Fleet Auto Scaling for Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling.html)
+  [Scaling Your Desktop Application Streams with Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/compute/scaling-your-desktop-application-streams-with-amazon-appstream-2-0/)
+  [Scale your Amazon WorkSpaces Applications fleets](https://aws.amazon.com/blogs/desktop-and-application-streaming/scale-your-amazon-appstream-2-0-fleets/)
+  [Monitoring Amazon WorkSpaces Applications Resources ](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
