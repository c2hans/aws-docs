---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/list-users.html
---

# ListUsers
<a name="list-users"></a>

Use the `ListUsers` operation to return a list of all of the Quick Sight users belonging to this account.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-users
    --aws-account-id {{AWSACCOUNTID}}
    --max-results {{100}}
    --namespace {{default}}
```

------

For more information about `ListUsers` operation, see [ListUsers](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListUsers.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
