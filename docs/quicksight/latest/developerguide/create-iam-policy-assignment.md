---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/create-iam-policy-assignment.html
---

# CreateIAMPolicyAssignment
<a name="create-iam-policy-assignment"></a>

Use the `CreateIAMPolicyAssignment` API operation to create an assignment with one specified IAM policy, identified by its Amazon Resource Name (ARN). This policy assignment is attached to the specified groups or users of Amazon Quick Sight. Assignment names are unique for each AWS account. To avoid overwriting rules in other namespaces, use assignment names that are unique.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-iam-policy-assignment
    --aws-account-id {{AWSACCOUNTID}}
    --assignment-name {{ASSIGNMENT}}
    --assignment-status {{ENABLED}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-iam-policy-assignment
    --cli-input-json file://{{createiampolicyassignment}}.json
```

------

For more information about the `CreateIAMPolicyAssignment` API operation, see [CreateIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateIAMPolicyAssignment.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
