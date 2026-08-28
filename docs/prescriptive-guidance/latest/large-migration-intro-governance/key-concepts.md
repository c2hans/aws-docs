---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-intro-governance/key-concepts.html
---

# Key concepts for large migrations
<a name="key-concepts"></a>

Large migrations of more than 300 servers pose unique challenges. The scale of the project requires that you adopt a strategic approach with well-defined phases, workstreams, and processes. This section contains the following topics:
+ [Workstreams in a large migration](#workstreams)
+ [Adopting an agile approach](#agile-approach)

|
|
| Note If you have not done so already, we recommend that you read the [Guide for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/welcome.html), which introduces the phases, migration strategies, and other important information about large migrations. |
| --- |

## Workstreams in a large migration
<a name="workstreams"></a>

AWS recommends that you establish *workstreams*, which are dedicated to completing certain tasks. The following are the four core workstreams in the migration phase of the project, and you can create additional, supporting workstreams as needed to support your use case:
+ **Foundation workstream** – This workstream is focused on preparing the people and platform for the large migration.
+ **Project governance workstream** – This workstream manages the overall migration project, facilitates communication, and focuses on completing the project within budget and on time.
+ **Portfolio workstream** – The teams in this workstream collect metadata to support the migration, prioritize applications, and perform wave planning.
+ **Migration workstream** – Using the wave plan and collected metadata from the portfolio workstream, the teams in this workstream migrate and cutover the applications and servers.

For more information, see [Workstreams in a large migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/workstreams.html) in the *Foundation playbook for AWS large migrations*. Your governance model should be designed to report workstream progress, establish common goals and transparent expectations, facilitate communication between the workstreams, and resolve any issues that arise during the migration project.

## Adopting an agile approach
<a name="agile-approach"></a>

By establishing an agile approach, the project team can remain flexible and quickly adapt to change during the migration. We recommend adopting a Scrum framework for a large migration. Using this framework, you assign applications to *waves*, which is a group of related applications. You then assign waves to sprints, which is a fixed period of time (typically two weeks) in which the migration team works on all waves within that sprint. For more information, see [Establishing an agile approach](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/managing-large-migration.html#establish-agile-approach) in the *Project governance playbook for AWS large migrations*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
