---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-program-implementation/preparation.html
---

# Preparation
<a name="preparation"></a>

The preparation stage of the migration consists of these steps:

1. Set up two 2-pizza teams as scrum teams. These teams are made up of internal resources from workstreams that are deﬁned in the readiness and planning phase. Group the teams based on the underlying functional/technical roles. Together these teams are responsible for driving adoption, enabling initial migrations, and preparing the organization for running enterprise-scale migrations.
   + *2-Pizza Team 1* structure and resources – advisory, business case, program governance, people skills, and center of excellence (CoE).
   + *2-Pizza Team 2* structure and resources – app discovery/migrations, landing zone, security, and operations integration.

1. Kick oﬀ a planning meeting with both scrum teams to review the results from the migration readiness assessment.

1. Identify 10 to 30 applications to migrate from on premises to AWS in Wave 1.

1. Set up a backlog. Prioritize the use of "pre-baked" epics for all workstreams from existing migration patterns. Here are a few examples:

![Backlog example.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-program-implementation/images/guide-img/c368ac72-b4ba-4de5-80d0-24d311a6c244/images/40f22208-eef7-489b-9a3a-14fe9ded0e51.png)

1. Assign a scrum leader and a product owner, who are responsible for managing the backlog.

1. Set up eight two-week sprints for migrating applications.

1. Build a migration plan with resources, a backlog (epics, user stories), a risk/mitigation log, and a roles and responsibilities matrix (for example, a RACI matrix). You can use this plan to manage the risks that occur during the project, and to identify ownership for each resource involved.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
