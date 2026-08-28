---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/adduserstogroups.html
---

# Add users to groups
<a name="adduserstogroups"></a>

Use the following procedure to add users as members of a group that you previously created in your Identity Center directory. Alternatively, you can call the AWS API operation [CreateGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroupMembership.html) to add a user as a member of a group.

------
#### [ Console ]

**To add a user as a member of a group**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Groups**.

1. Choose the **group name** that you want to update.

1. On the group details page, under **Users in this group**, choose **Add users to group**.

1. On the **Add users to group** page, under **Other users**, locate the users you want to add as members. Then, select the check box next to each of them.

1. Choose **Add users**.

------
#### [ AWS CLI ]

**To add a user as a member of a group**
The following `create-group-membership` command adds a user to a group in your Identity Center directory.

```
aws identitystore create-group-membership \
    --identity-store-id d-1234567890 \
    --group-id a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 \
    --member-id UserId=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

Output:

```
{
    "MembershipId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "IdentityStoreId": "d-1234567890"
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
