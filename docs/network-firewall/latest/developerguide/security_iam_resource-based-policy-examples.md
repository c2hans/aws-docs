---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/security_iam_resource-based-policy-examples.html
---

# Resource-based policy examples for AWS Network Firewall
<a name="security_iam_resource-based-policy-examples"></a>

The Network Firewall service supports only one type of resource-based policy called a *resource policy*, which is attached to a shared firewall policy or rule group. This policy defines which principals can share firewall policies and rule groups between accounts.

To learn how to attach a resource policy to a shared rule group or firewall policy, see [Sharing AWS Network Firewall resources](sharing.md).

**Topics**
+ [Enable sharing of a firewall policy with an account](#security_iam_resource-based-policy-examples-put-resource-policy)

## Enable sharing of a firewall policy with an account
<a name="security_iam_resource-based-policy-examples-put-resource-policy"></a>

The following example grants permissions to the service principal to create or update a resource policy for a firewall policy that's shared across accounts. In the resource policy, you specify the accounts that you want to share the resource with and the operations that you want the accounts to be able to perform.

For information about sharing resources in Network Firewall, see [Sharing AWS Network Firewall resources](sharing.md).

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "{{123456789012}}"
            },
            "Action": [
                "network-firewall:AssociateFirewallPolicy",
                "network-firewall:ListFirewallPolicies"
            ],
            "Resource": "arn:aws:network-firewall:{{us-east-1}}:{{123456789012}}:firewall-policy/{{test-action}}"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
