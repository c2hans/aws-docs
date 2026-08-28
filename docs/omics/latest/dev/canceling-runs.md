---
source_url: https://docs.aws.amazon.com/omics/latest/dev/canceling-runs.html
---

# Cancel a run in HealthOmics
<a name="canceling-runs"></a>

You can cancel a run if its status is `PENDING`, `STARTING`, `RUNNING`, or `STOPPING`.

**Note**
When you cancel a run, HealthOmics doesn't save any of the run outputs.

From the console, follow these steps to cancel a run:

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/).

1.  If required, open the left navigation pane (≡). Choose **Runs**.

1. On the **Runs** page, choose the run to cancel.

1. The console opens the **Run details** page. From the status banner at the top of the page, choose **Stop run**.

1. Enter **confirm** to stop the run.

To cancel a run using the API, use the **CancelRun** API operation.

The following example shows how to cancel a run using the AWS CLI . To run the example, replace the `{{run id}}` with the ID of the run you would like to cancel. If successful, there is no response.

```
aws omics cancel-run --id {{run id}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
