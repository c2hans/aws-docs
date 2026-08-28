---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import-cancelling-import.html
---

# Canceling an import task
<a name="bulk-import-cancelling-import"></a>

 You can cancel a running import task by using the [ CancelImportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CancelImportTask.html) API.

```
aws neptune-graph cancel-import-task \
--task-id <task-id>
```

 The import task will will be canceled and all changes rolled back. The state of the import task will switch to `CANCELING` after `cancel-import-task` API is called and eventually the state will be `CANCELED` when rollback finishes. You can check the current state of your import task using the [GetImportTask](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import-checking-details.html) API.

```
aws neptune-graph get-import-task \
--task-id <task-id>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
