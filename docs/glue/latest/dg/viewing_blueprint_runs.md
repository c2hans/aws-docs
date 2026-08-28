---
source_url: https://docs.aws.amazon.com/glue/latest/dg/viewing_blueprint_runs.html
---

# Viewing blueprint runs in AWS Glue
<a name="viewing_blueprint_runs"></a>

View a blueprint run to see the following information:
+ Name of the workflow that was created.
+ blueprint parameter values that were used to create the workflow.
+ Status of the workflow creation operation.

You can view a blueprint run by using the AWS Glue console, AWS Glue API, or AWS Command Line Interface (AWS CLI).

**To view a blueprint run (console)**

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. In the navigation pane, choose **blueprints**.

1. On the **blueprints** page, select a blueprint. Then on the **Actions** menu, choose **View**.

1. At the bottom of the **Blueprint Details** page, select a blueprint run, and on the **Actions** menu, choose **View**.

**To view a blueprint run (AWS CLI)**
+ Enter the following command. Replace {{<blueprint-name>}} with the name of the blueprint. Replace {{<blueprint-run-id>}} with the blueprint run ID.

  ```
  aws glue get-blueprint-run --blueprint-name {{<blueprint-name>}} --run-id {{<blueprint-run-id>}}
  ```

**See also:**
[Overview of blueprints in AWS Glue](blueprints-overview.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
