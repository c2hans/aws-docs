---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/update-data-source-permissions.html
---

# UpdateDataSourcePermissions
<a name="update-data-source-permissions"></a>

Use the `UpdateDataSourcePermissions` API operation to update the resource permissions for a data source. You can grant or revoke permissions in the same command. To use this operation, you need the ID of the data source whose permissions you want to update. The data source ID is part of the data source URL in Quick Sight. You can also use the `ListDataSources` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-data-source-permissions
    --aws-account-id {{AWSACCOUNTID}}
    --data-source-id {{DATASOURCEID}}
    --grant-permissions Principal=arn:aws:quicksight:{{us-east-1}}:{{AWSACCOUNTID}}:user/default/{{USER{{NAME}}}},Actions=quicksight:DescribeDataSource,quicksight:DescribeDataSourcePermissions,quicksight:PassDataSource
    --revoke-permissions Principal=arn:aws:quicksight:{{us-east-1}}:{{AWSACCOUNTID}}:user/default/{{USER{{NAME}}}},Actions=quicksight:DescribeDataSource,quicksight:DescribeDataSourcePermissions,quicksight:PassDataSource
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-data-source-permissions
    --cli-input-json file://{{updatedatasourcepermissions}}.json
```

------

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information about the `UpdateDataSourcePermissions` API operation, see [UpdateDataSourcePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSourcePermissions.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
