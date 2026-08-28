---
source_url: https://docs.aws.amazon.com/omics/latest/dev/deleting-runs.html
---

# Delete a run in HealthOmics
<a name="deleting-runs"></a>

When you no longer need a run, you can delete it using the AWS CLI, API, or console. You can delete a run when its status is `COMPLETED` or `CANCELED`.

From the console, follow these steps to delete a run:

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/).

1.  If required, open the left navigation pane (≡). Choose **Runs**.

1. On the **Runs** page, select one or more runs to delete.

1. From the action menu above the table, choose **Delete**.

1. In the modal form, type **confirm** to confirm the deletion.

The following AWS CLI command deletes a run. To run the example, replace the `{{run id}}` with the ID of the run you want to delete. There is no response if the run is successfully deleted.

```
aws omics delete-run --id {{run id}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
