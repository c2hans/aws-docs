---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/logging-and-monitoring.html
---

# Logging and monitoring in ARC
<a name="logging-and-monitoring"></a>

Monitoring is an important part of maintaining the availability and performance of ARC and your AWS solutions. You should collect monitoring data from all of the parts of your AWS solution so that you can more easily debug a multi-point failure if one occurs. AWS provides several tools for monitoring your ARC resources and activity, and responding to potential incidents, for example, AWS CloudTrail and Amazon CloudWatch.

For information about monitoring for each capability in ARC, see the following topics:
+ [Logging and monitoring for zonal shift](monitoring-zonal-shift.md)
+ [Logging and monitoring for zonal autoshift](monitoring-zonal-autoshift.md)
+ [Logging and monitoring for routing control](monitoring-routing.md)
+ [Logging and monitoring for Region switch](logging-and-monitoring-rs.md)
+ [Logging and monitoring for readiness check](monitoring-readiness.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
