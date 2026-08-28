---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-iam-policy-assignment.html
---

# DescribeIAMPolicyAssignment
<a name="describe-iam-policy-assignment"></a>

Use the `DescribeIAMPolicyAssignment` API operation to describe an existing IAM policy assignment.

To find a policy assignment name, call the `ListIAMPolicyAssignments` or `ListIAMPolicyAssignmentsForUser` API operation.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-iam-policy-assignment
    --aws-account-id {{AWSACCOUNTID}}
    --assignment-name {{ASSIGNMENT}}
    --namespace {{default}}
```

------

For more information about the `DescribeIAMPolicyAssignment` API operation, see [DescribeIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeIAMPolicyAssignment.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
