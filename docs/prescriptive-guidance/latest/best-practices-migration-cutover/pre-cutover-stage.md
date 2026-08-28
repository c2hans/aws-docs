---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/pre-cutover-stage.html
---

# Pre-cutover stage
<a name="pre-cutover-stage"></a>

Your cutover options depend on various factors, including what migration pattern you're using and the tools, technologies, and configurations of both your source and target environment. For example, the cutover options are different for migrating a VMware environment to AWS compared to building a completely new stack.

Fundamentally, all cutovers strive to achieve the same outcome—moving a workload to another location. It's important to understand where servers or applications have moved to so that you can configure upstream and downstream dependencies to connect to the new endpoint.

Depending on the nature of the service, the existing databases and its connections to other systems that move to the new location can be complex. The synchronization of databases to ensure consistent data in both locations can increase complexity. In addition, multiple services require that you either adjust your network configuration or cut over multiple services at the same time.

## Developing a cutover plan
<a name="cutover-plan"></a>

To reduce the risk of delay, rework, unplanned outages, data loss, performance issues, and a poor user experience, you can develop a cutover plan, create a cutover workbook, and practice rehearsing your cutover. We recommend that your cutover plan includes contingency plans and risk mitigation strategies for failure in the event of an unsuccessful cutover. Be sure to document a rollback procedure as part of the cutover plan.

We recommend that you analyze and assess the following critical items as part of your pre-cutover planning process:
+ Downtime required, including:
  + Impact to the business (for example, on revenue or trust) of an overrun of the allocated downtime window
  + Contingency for "fix forward" activities in the event of unforeseen events
  + Rollback time in the event of a failure
+ User connectivity
+ Application and system dependencies
+ Infrastructure changes
+ Operational changes
+ Testing plans, including:
  + Functional testing
  + Performance testing with baseline testing and post-cutover testing
  + Integration and connectivity testing for dependent applications, systems, and services
  + Strategies testing during the cutover and warranty period
+ Deployment changes related to tooling and strategy

Finally, consider incorporating the following into your plan:
+ Task definitions and duration
+ Task owners
+ Sequence of stages and tasks

## Creating a cutover runbook
<a name="cutover-runbook"></a>

We recommend that you create a cutover runbook that your migration team can use to track activities, including their respective planned start and end times, sequence, and owners. You can use a RACI matrix to assign responsibilities to the appropriate team members. A cutover runbook can provide the following benefits:
+ Reduced risk by proactively aligning diﬀerent stakeholders
+ Increased productivity by reusing a proven mechanism for migrating applications to the AWS Cloud
+ Increased velocity of application migration by using a structured template for cutover planning
+ Providing a framework so that required processes are followed
+ Providing a mechanism where changes to processes can be communicated to all teams

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
