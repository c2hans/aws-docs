---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp01.html
---

# EUCPERF08-BP01 Establish and monitor service metrics and KPIs
<a name="eucperf08-bp01"></a>

 When using an AWS EUC service to deliver a service to your users, it's important to consider the service metrics that are key to the delivery of the service for your organization to verify that the service is operating at the required service levels.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-19"></a>

 Determine service metrics and KPIs for your service. Some examples of key measures to consider are:
+  Service availability
+  Mean time to repair (MTTR)
+  First call resolution (FCR)
+  SLA breach rate
+  User and customer satisfaction (CSAT)
+  Cost per contact
+  Net promoter score
+  Incident volume
+  Problem resolution time

 Consider how metrics available within the AWS EUC services outlined in the following sections can be used to support or determine your service metrics.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
