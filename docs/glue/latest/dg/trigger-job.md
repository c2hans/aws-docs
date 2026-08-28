---
source_url: https://docs.aws.amazon.com/glue/latest/dg/trigger-job.html
---

# Starting jobs and crawlers using triggers
<a name="trigger-job"></a>

In AWS Glue, you can create Data Catalog objects called triggers, which you can use to either manually or automatically start one or more crawlers or extract, transform, and load (ETL) jobs. Using triggers, you can design a chain of dependent jobs and crawlers.

**Note**
You can accomplish the same thing by defining *workflows*. Workflows are preferred for creating complex multi-job ETL operations. For more information, see [Performing complex ETL activities using blueprints and workflows in AWS Glue](orchestrate-using-workflows.md).

**Topics**
+ [AWS Glue triggers](about-triggers.md)
+ [Adding triggers](console-triggers.md)
+ [Activating and deactivating triggers](activate-triggers.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
