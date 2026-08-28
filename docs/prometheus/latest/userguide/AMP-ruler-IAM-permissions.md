---
source_url: https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-IAM-permissions.html
---

# Understanding IAM permissions needed for using rules
<a name="AMP-ruler-IAM-permissions"></a>

You must give users permissions to use rules in Amazon Managed Service for Prometheus. Create an AWS Identity and Access Management (IAM) policy with the following permissions, and assign the policy to your users, groups, or roles.

**Note**
For more information about IAM, see [Identity and Access Management for Amazon Managed Service for Prometheus](security-iam.md).

**Policy to give access to use rules**

The following policy gives access to use rules for all resources in your account.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "aps:CreateRuleGroupsNamespace",
                "aps:ListRuleGroupsNamespaces",
                "aps:DescribeRuleGroupsNamespace",
                "aps:PutRuleGroupsNamespace",
                "aps:DeleteRuleGroupsNamespace"
            ],
            "Resource": "*"
        }
    ]
}
```

------

**Policy to give access to only one namespace**

You can also create policy that gives access to only specific policies. The following sample policy gives access only to the `RuleGroupNamespace` specified. To use this policy, replace {{<account>}}, {{<region>}}, {{<workspace-id>}}, and {{<namespace-name>}} with appropriate values for your account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
