---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-group-membership.html
---

# DescribeGroupMembership
<a name="describe-group-membership"></a>

Use the `DescribeGroupMembership` API operation to determine if a user is a member of the specified group. If the user exists and is a member of the specified group, an associated `GroupMember` object is returned.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

CLI Input:

```
aws quicksight describe-group-membership
    --region {{us-west-2}}
    --aws-account-id {{AWSACCOUNTID}}
    --namespace {{NAMESPACE}}
    --group-name {{Marketing-East}}
    --member-name {{MEMBERNAME}}
```

------

For more information about the `ListGroups` API operation, see [DescribeGroupMembership](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeGroupMembership.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
