---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/list-iam-policy-assignments.html
---

# ListIAMPolicyAssignments
<a name="list-iam-policy-assignments"></a>

Use the `ListIAMPolicyAssignments` API operation to list IAM policy assignments in the current Amazon Quick Sight account. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-iam-policy-assignments
    --aws-account-id {{AWSACCOUNTID}}
    --assignment-status {{ENABLED}}
    --namespace {{default}}
    --max-results {{100}}
```

------

For more information about the `ListIAMPolicyAssignments` API operation, see [ListIAMPolicyAssignments](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListIAMPolicyAssignments.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
