---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_tracking_change_management_resiliency_testing.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL08-BP03 Integrate resiliency testing as part of your deployment
<a name="rel_tracking_change_management_resiliency_testing"></a>

 Resiliency tests (using the [principles of chaos engineering](https://principlesofchaos.org/)) are run as part of the automated deployment pipeline in a pre-production environment.

 These tests are staged and run in the pipeline in a pre-production environment. They should also be run in production as part of [*game days*](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/test-reliability.html#GameDays).

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Integrate resiliency testing as part of your deployment. Use Chaos Engineering, the discipline of experimenting on a workload to build confidence in the workload’s capability to withstand turbulent conditions in production.
  +  Resiliency tests inject faults or resource degradation to assess that your workload responds with its designed resilience.
    +  [Well-Architected lab: Level 300: Testing for Resiliency of EC2 RDS and S3](https://wellarchitectedlabs.com/Reliability/300_Testing_for_Resiliency_of_EC2_RDS_and_S3/README.html)
  +  These tests can be run regularly in pre-production environments in automated deployment pipelines.
  +  They should also be run in production, as part of scheduled game days.
  +  Using Chaos Engineering principles, propose hypotheses about how your workload will perform under various impairments, then test your hypotheses using resiliency testing.
    +  [Principles of Chaos Engineering](https://principlesofchaos.org/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Principles of Chaos Engineering](https://principlesofchaos.org/)
+  [What is AWS Fault Injection Simulator?](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)

 **Related examples:**
+  [Well-Architected lab: Level 300: Testing for Resiliency of EC2 RDS and S3](https://wellarchitectedlabs.com/Reliability/300_Testing_for_Resiliency_of_EC2_RDS_and_S3/README.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
