---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-data-set.html
---

# DeleteDataSet
<a name="delete-data-set"></a>

Use the `DeleteDataSet` API operation to delete a dataset. To use this operation, you need the ID of the dataset that you want to delete. The dataset ID is part of the dataset URL in Quick Sight. You can also use the `ListDataSets` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-data-set
    --aws-account-id {{AWSACCOUNTID}}
    --data-set-id {{DATASETID}}
```

------

For more information about the `DeleteDataSet` API operation, see [DeleteDataSet](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteDataSet.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
