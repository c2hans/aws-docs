---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/api-permissions-reference.html
---

# DynamoDB API permissions: Actions, resources, and conditions reference
<a name="api-permissions-reference"></a>

When you are setting up [Identity and Access Management for Amazon DynamoDB](security-iam.md) and writing a permissions policy that you can attach to an IAM identity (identity-based policies), you can use the list of [Actions, resources, and condition keys for Amazon DynamoDB](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondynamodb.html) in the *IAM User Guide* as a reference. The page lists each DynamoDB API operation, the corresponding actions for which you can grant permissions to perform the action, and the AWS resource for which you can grant the permissions. You specify the actions in the policy's `Action` field, and you specify the resource value in the policy's `Resource` field.

You can use AWS-wide condition keys in your DynamoDB policies to express conditions. For a complete list of AWS-wide keys, see the [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*.

In addition to the AWS-wide condition keys, DynamoDB has its own specific keys that you can use in conditions. For more information, see [Using IAM policy conditions for fine-grained access control](specifying-conditions.md).

## Related topics
<a name="w2aac39c21c15c15b9"></a>
+  [Identity and Access Management for Amazon DynamoDB](security-iam.md)
+ [Using IAM policy conditions for fine-grained access control](specifying-conditions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
