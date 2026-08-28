---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/automation-access-control.html
---

# Automation and access control
<a name="automation-access-control"></a>

## Automation
<a name="automation"></a>

Pipeline automation is a crucial part of modern data-centric architecture design. To successfully run your production system, we recommend that you have a data pipeline that has a start trigger, connecting steps, and a mechanism for separating failed and passed stages. It's also important to log failures while not hindering the rest of the ETL process.

You can use [AWS Glue workflows](https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html) to create a pipeline. The pipeline supports all AWS Glue jobs, Amazon EventBridge triggers, and crawlers. You can also create workflows from scratch or by using AWS Glue [blueprints](https://docs.aws.amazon.com/glue/latest/dg/blueprints-overview.html). A blueprint provides a framework that helps you get started on reusable use cases. For example, this could be a workflow to import data from Amazon S3 into a DynamoDB table. You can even use parameters to make the blueprint reusable.

If the data pipeline involves more services outside of AWS Glue, then we recommend that you use [AWS Step Functions](https://aws.amazon.com/step-functions/) as the orchestrator. Step Functions can create automated workflows, including manual approval steps for security incident response. You can also use Step Functions for large-scale parallel or sequential processing.

Finally, we recommend using [EventBridge](https://aws.amazon.com/eventbridge/) to insert triggers on schedules, events, or on demand. You can also use EventBridge to create pipelines with filters.

## Access control
<a name="access-control"></a>

We recommend that you use [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) for access control. IAM allows you to specify who or what can access services and resources in AWS and centrally manage fine-grained permissions. Every phase of the lifecycle—from storage to automation to using processing tools—requires the right access permissions. While working with data-centric use cases, you can use [AWS Lake Formation](https://aws.amazon.com/lake-formation/) to simplify the process of making data available for wide-ranging analytics and also across accounts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
