---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-user.html
---

# DescribeUser
<a name="describe-user"></a>

Use the `DescribeUser` operation to return information about a user, given the user name. Following is an example AWS CLI command for this operation. To use this operation, you need the ID of the user that you want to describe. You can also use the `ListUsers` operation to list all users and their corresponding user IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-user
    --aws-account-id {{AWSACCOUNTID}}
    --namespace {{default}}
```

------

For more information about the `DescribeUser` operation, see [DescribeUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeUser.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
