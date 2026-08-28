---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-deactivate-pipeline.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Deactivating Your Pipeline
<a name="dp-deactivate-pipeline"></a>

Deactivating a running pipeline pauses the pipeline execution. To resume pipeline execution, you can activate the pipeline. This enables you to make changes. For example, if you are writing data to a database that is scheduled to undergo maintenance, you can deactivate the pipeline, wait for the maintenance to complete, and then activate the pipeline.

When you deactivate a pipeline, you can specify what happens to running activities. By default, these activities are canceled immediately. Alternatively, you can have AWS Data Pipeline wait until the activities finish before deactivating the pipeline.

When you activate a deactivated pipeline, you can specify when it resumes. Using the AWS CLI or the API, the pipeline resumes from the last completed execution by default, or you can specify the date and time to resume the pipeline.

## Deactivate Your Pipeline Using the AWS CLI
<a name="dp-deactivate-pipeline-cli"></a>

Use the following [deactivate-pipeline](https://docs.aws.amazon.com/cli/latest/reference/datapipeline/deactivate-pipeline.html) command to deactivate a pipeline:

```
aws datapipeline deactivate-pipeline --pipeline-id {{df-00627471SOVYZEXAMPLE}}
```

To deactivate the pipeline only after all running activities finish, add the `--no-cancel-active` option, as follows:

```
aws datapipeline deactivate-pipeline --pipeline-id {{df-00627471SOVYZEXAMPLE}} --no-cancel-active
```

When you are ready, you can resume the pipeline execution where it left off using the following [activate-pipeline](https://docs.aws.amazon.com/cli/latest/reference/datapipeline/activate-pipeline.html) command:

```
aws datapipeline activate-pipeline --pipeline-id {{df-00627471SOVYZEXAMPLE}}
```

To start the pipeline from a specific date and time, add the `--start-timestamp` option, as follows:

```
aws datapipeline activate-pipeline --pipeline-id {{df-00627471SOVYZEXAMPLE}} --start-timestamp {{YYYY}}-{{MM}}-{{DD}}T{{HH}}:{{MM}}:{{SS}}Z
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
