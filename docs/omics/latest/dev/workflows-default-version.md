---
source_url: https://docs.aws.amazon.com/omics/latest/dev/workflows-default-version.html
---

# Default workflow version
<a name="workflows-default-version"></a>

After you create one or more versions of a workflow, HealthOmics treats the original workflow as the default version. When you start a run, you can optionally specify a workflow version for the run. If you don't specify a version when you start a run, HealthOmics uses the default version.

In the console, HealthOmics indicates the original workflow with a **Default version** label. The console uses this label only after you create one or more workflow versions. The original workflow always remains the default version. You can't assign any other version to be the default.

You can't delete a workflow's default version if there are other versions associated with the workflow. For more information, see [Delete a private workflow](delete-private-workflow.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
