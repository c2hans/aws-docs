---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-group-membership.html
---

# DeleteGroupMembership
<a name="delete-group-membership"></a>

Use the `DeleteGroupMembership` API operation to remove a user from a group so that the user is no longer a member of the group. You can find users in a certain group by calling the `ListGroups` API operation, and then the `ListGroupMemberships` operation on the group that you choose.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-group-membership
    --member-name {{USERNAME}}
    --group-name {{GROUPNAME}}
    --aws-account-id {{AWSACCOUNTID}}
    --namespace {{NAMESPACE}}
```

------

For more information about the `DeleteGroupMembership` API operation, see [DeleteGroupMembership](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteGroupMembership.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
