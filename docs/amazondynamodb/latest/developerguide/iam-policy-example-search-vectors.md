---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-example-search-vectors.html
---

# IAM policy to grant access to search a vector index
<a name="iam-policy-example-search-vectors"></a>

The following policy grants permissions to perform `SearchVectors` operations on a specific vector index. The resource ARN for a vector index uses the same format as other DynamoDB indexes.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "dynamodb:SearchVectors",
            "Resource": "arn:aws:dynamodb:us-west-2:123456789012:table/Products/index/ProductEmbeddingIndex"
        }
    ]
}
```

To grant `SearchVectors` access to all indexes on a table, use a wildcard character (\*) for the index name.

```
"Resource": "arn:aws:dynamodb:us-west-2:123456789012:table/Products/index/*"
```

**No additional permissions required**
No additional IAM permissions are required to create or delete vector indexes. The existing `dynamodb:CreateTable` and `dynamodb:UpdateTable` permissions are sufficient.

**FGAC condition keys not supported for SearchVectors**
Fine-grained access control (FGAC) condition keys are not supported for the `SearchVectors` API. You cannot use `dynamodb:LeadingKeys`, `dynamodb:Attributes`, or `dynamodb:Select` condition keys to restrict `SearchVectors` access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
