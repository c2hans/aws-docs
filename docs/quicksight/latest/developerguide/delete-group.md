---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-group.html
---

# DeleteGroup
<a name="delete-group"></a>

Use the `DeleteGroup` API operation to remove a user group from Amazon Quick Sight. You can find a group name by calling the `ListGroups` API operation.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-group
    --group-name {{GROUPNAME}}
    --aws-account-id {{AWSACCOUNTID}}
    --namespace {{default}}
```

------

For more information about the `DeleteGroup` API operation, see [DeleteGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteGroup.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
