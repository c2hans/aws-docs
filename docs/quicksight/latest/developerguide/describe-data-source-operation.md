---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-data-source-operation.html
---

# DescribeDataSourcePermissions
<a name="describe-data-source-operation"></a>

Use the `DescribeDataSourcePermissions` API operation to describe the resource permissions for a data source. To use this operation, you need the ID of the data source whose permissions you want to view. The data source ID is part of the data source URL in Quick Sight. You can also use the `ListDataSources` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-data-source-permissions
    --aws-account-id {{AWSACCOUNTID}}
    --data-source-id {{DATASOURCEID}}
```

------

For more information about the `DescribeDataSourcePermissions` API operation, see [DescribeDataSourcePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDataSourcePermissions.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
