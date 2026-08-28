---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-troubleshoot-locate-errors.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Locating Errors in Pipelines
<a name="dp-troubleshoot-locate-errors"></a>

The AWS Data Pipeline console is a convenient tool to visually monitor the status of your pipelines and easily locate any errors related to failed or incomplete pipeline runs.

**To locate errors about failed or incomplete runs with the console**

1. On the **List Pipelines** page, if the **Status** column of any of your pipeline instances shows a status other than **FINISHED**, either your pipeline is waiting for some precondition to be met or it has failed and you need to troubleshoot the pipeline.

1. On the **List Pipelines** page, locate the instance pipeline and select the triangle to the left of it, to expand the details.

1. At the bottom of this panel, choose **View execution details**; the **Instance summary** panel opens to show the details of the selected instance.

1. In the **Instance summary** panel, select the triangle next to the instance to see additional details of the instance, and choose **Details**, **More...** If the status of your selected instance is **FAILED**, the details box has entries for the error message, the `errorStackTrace` and other information. You can save this information into a file. Choose **OK**.

1. In the **Instance summary** pane, choose **Attempts**, to see details for each attempt row.

1. To take an action on your incomplete or failed instance, select the check box next the instance. This activates the actions. Then, select an action (`Rerun|Cancel|Mark Finished`).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
