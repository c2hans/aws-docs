---
source_url: https://docs.aws.amazon.com/glue/latest/dg/orchestrate-using-blueprints.html
---

# Developing blueprints in AWS Glue
<a name="orchestrate-using-blueprints"></a>

Your organization might have a set of similar ETL use cases that could benefit from being able to parametrize a single workflow to handle them all. To address this need, AWS Glue enables you to define *blueprints*, which you can use to generate workflows. A blueprint accepts parameters, so that from a single blueprint, a data analyst can create different workflows to handle similar ETL use cases. After you create a blueprint, you can reuse it for different departments, teams, and projects.

**Topics**
+ [Overview of blueprints in AWS Glue](blueprints-overview.md)
+ [Developing blueprints in AWS Glue](developing-blueprints.md)
+ [Registering a blueprint in AWS Glue](registering-blueprints.md)
+ [Viewing blueprints in AWS Glue](viewing_blueprints.md)
+ [Updating a blueprint in AWS Glue](updating_blueprints.md)
+ [Creating a workflow from a blueprint in AWS Glue](creating_workflow_blueprint.md)
+ [Viewing blueprint runs in AWS Glue](viewing_blueprint_runs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
