---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-data-source.html
---

# DeleteDataSource
<a name="delete-data-source"></a>

Use the `DeleteDataSource` API operation to permanently delete a data source from Amazon Quick Sight. To use this operation, you need the ID of the data source that you want to delete. The data source ID is part of the data source URL in Quick Sight. You can also use the `ListDataSources` API operation to get the ID.

**Note**
Deleting a data source breaks all datasets that reference it.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-data-source
    --aws-account-id {{AWSACCOUNTID}}
    --data-source-id {{DATASOURCEID}}
```

------

For more information about the `DeleteDataSource` API operation, see [DeleteDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteDataSource.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
