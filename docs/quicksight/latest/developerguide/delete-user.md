---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-user.html
---

# DeleteUser
<a name="delete-user"></a>

Use the `DeleteUser` operation to delete the Quick Sight user that is associated with the identity of the IAM user or role that's making the call. The IAM user isn't deleted as a result of this call. To use this operation, you need the ID of the user that you want to delete. You can also use the `ListUsers` operation to list all users and their corresponding user IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-user
    --user-name {{USERNAME}}
    --aws-account-id {{AWSACCOUNTID}}
    --namespace {{default}}
```

------

For more information about the `DeleteUser` operation, see [DeleteUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteUser.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
