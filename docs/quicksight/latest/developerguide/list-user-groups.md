---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/list-user-groups.html
---

# ListUserGroups
<a name="list-user-groups"></a>

Use the `ListUserGroups` operation to list the Quick Sight groups that an Quick Sight user is a member of. To use this operation, you need the ID of the user whose group memberships you want to know. You can use the `ListUsers` operation to list all users and their corresponding user IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-user-groups
    --user-name {{USERNAME}}
    --aws-account-id {{AWSACCOUNTID}}
    --namespace {{default}}
    --max-results {{100}}
```

------

For more information about `ListUserGroups` operation, see [ListUserGroups](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListUserGroups.html)in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
