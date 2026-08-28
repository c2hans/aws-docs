---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/key-policy.html
---

# Key policy for voice analytics
<a name="key-policy"></a>

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, with policy statements that determine who can use the key and how they can use it. When you create your key, you can specify a key policy. For more information, see [ Working with key policies](https://docs.aws.amazon.com/kms/latest/developerguide/programming-key-policies.html) in the *AWS Key Management Service Developer Guide*.

------
#### [ JSON ]

****

```
{
"Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "Allow key access to Chime SDK voice analytics.",
            "Effect": "Allow",
            "Principal": {
            "AWS": "arn:aws:iam::{{111122223333}}:user/{{UserNameWithPath}}"
            },
            "Action": [
                "kms:CreateGrant",
                "kms:Decrypt",
                "kms:DescribeKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": [
                       "chime.{{us-east-1}}.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

------

For information about specifying permissions in a policy, see [ Specifying KMS keys in IAM policy statements](https://docs.aws.amazon.com/kms/latest/developerguide/cmks-in-iam-policies.html) in the *AWS Key Management Service Developer Guide*.

For information about troubleshooting key access, see [Troubleshooting key access](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html) in the *AWS Key Management Service Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
