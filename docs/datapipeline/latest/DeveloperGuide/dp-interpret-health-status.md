---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-interpret-health-status.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Interpreting Pipeline and Component Health State
<a name="dp-interpret-health-status"></a>

Each pipeline and component within that pipeline returns a health status of `HEALTHY`, `ERROR`, `"-"`, `No Completed Executions`, or `No Health Information Available`. A pipeline only has a health state after a pipeline component has completed its first execution or if component preconditions have failed. The health status for components aggregates into a pipeline health status in that error states are visible first when you view your pipeline execution details.Pipeline Health States

`HEALTHY`
The aggregate health status of all components is `HEALTHY`. This means at least one component must have successfully completed. You can click on the `HEALTHY` status to see the most recent successfully completed pipeline component instance on the **Execution Details** page.

`ERROR`
At least one component in the pipeline has a health status of `ERROR`. You can click on the `ERROR` status to see the most recent failed pipeline component instance on the **Execution Details** page.

`No Completed Executions` or `No Health Information Available`.
No health status was reported for this pipeline.

**Note**
While components update their health status almost immediately, it may take up to five minutes for a pipeline health status to update.Component Health States

`HEALTHY`
A component (`Activity` or `DataNode`) has a health status of `HEALTHY` if it has completed a successful execution where it was marked with a status of `FINISHED` or `MARK_FINISHED`. You can click on the name of the component or the `HEALTHY` status to see the most recent successfully completed pipeline component instances on the **Execution Details** page.

`ERROR`
An error occurred at the component level or one of its preconditions failed. Statuses of `FAILED`, `TIMEOUT`, or `CANCELED` trigger this error. You can click on the name of the component or the `ERROR` status to see the most recent failed pipeline component instance on the **Execution Details** page.

`No Completed Executions` or `No Health Information Available`
No health status was reported for this component.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
