---
source_url: https://docs.aws.amazon.com/glue/latest/dg/activate-triggers.html
---

# Activating and deactivating triggers
<a name="activate-triggers"></a>

You can activate or deactivate a trigger using the AWS Glue console, the AWS Command Line Interface (AWS CLI), or the AWS Glue API.

**To activate or deactivate a trigger (console)**

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. In the navigation pane, under **ETL**, choose **Triggers**.

1. Select the check box next to the desired trigger, and on the **Action** menu choose **Enable trigger** to activate the trigger or **Disable trigger** to deactivate the trigger.

**To activate or deactivate a trigger (AWS CLI)**
+ Enter one of the following commands.

  ```
  aws glue start-trigger --name MyTrigger

  aws glue stop-trigger --name MyTrigger
  ```

  Starting a trigger activates it, and stopping a trigger deactivates it. When you activate an on-demand trigger, it fires immediately.

For more information, see [AWS Glue triggers](about-triggers.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
