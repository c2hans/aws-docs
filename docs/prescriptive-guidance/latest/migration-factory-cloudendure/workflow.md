---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/workflow.html
---

# The Cloud Migration Factory workflow
<a name="workflow"></a>

Cloud Migration Factory comes with a predefined process that includes three phases: pre-migration, migration implementation, and post-migration, as shown in the following diagram.

![The Cloud Migration Factory workflow](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/images/guide-img/3ff8a3b6-fa4d-412f-ba5f-3d8aad3942a7/images/1e7db694-72a6-450f-b8c1-2e5254792baf.png)

In the **pre-migration phase**, your migration team is responsible for preparing the implementation environment. This includes deploying Cloud Migration Factory, building a migration execution server, and setting up AWS Transform MGN (AWS MGN).

During the **migration implementation phase**, the migration team is responsible for running predefined tasks that automate the migration process. These tasks can include:
+ Verifying prerequisites
+ Pushing the replication agent to the source machines for a given wave
+ Verifying replication status
+ Launching servers for boot-up testing
+ Scheduling a window for application cutover

Migration tasks are scheduled in *waves*. Each wave consists of a group of applications and servers that have the same cutover date. As shown in the following diagram, each wave should be completed in a predefined period. For example, in the three-week period shown, week 1 is the build stage, week 2 is the validate and boot-up testing stage, and week 3 is the cutover stage. All the waves run in parallel.

![Scheduling migrations in waves with Cloud Migration Factory](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/images/guide-img/3ff8a3b6-fa4d-412f-ba5f-3d8aad3942a7/images/e0aff81f-9488-45b9-97f0-3d897ed56c91.png)

**Post-migration tasks** depend on the specific migration scenario and your requirements. These tasks might include removing servers from the source CMDB, decommissioning source machines, and optimizing performance for the target Amazon Elastic Compute Cloud (Amazon EC2) instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
