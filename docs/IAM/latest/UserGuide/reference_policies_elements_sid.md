---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_sid.html
---

# IAM JSON policy elements: Sid
<a name="reference_policies_elements_sid"></a>

You can provide a `Sid` (statement ID) as an optional identifier for the policy statement. You can assign a `Sid` value to each statement in a statement array. You can use the `Sid` value as a description for the policy statement. In services that let you specify an `ID` element, such as SQS and SNS, the `Sid` value is just a sub-ID of the policy document ID. In IAM, the `Sid` value must be unique within a JSON policy.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "ExampleStatementID",
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    }
  ]
}
```

------

The `Sid` element supports ASCII uppercase letters (A-Z), lowercase letters (a-z), and numbers (0-9).

IAM does not expose the `Sid` in the IAM API. You can't retrieve a particular statement based on this ID.

**Note**
Some AWS services (for example, Amazon SQS or Amazon SNS) might require this element and have uniqueness requirements for it. For service-specific information about writing policies, refer to the documentation for the service you work with.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
