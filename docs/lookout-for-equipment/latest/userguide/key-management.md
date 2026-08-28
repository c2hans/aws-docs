---
source_url: https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/key-management.html
---

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/).

# Key management
<a name="key-management"></a>

Amazon Lookout for Equipment encrypts your data using one of the following types of keys:
+ An AWS owned key. This is the default.
+ A customer managed key. You can create the key when you create an Amazon Lookout for Equipment dataset, model, or inference, or you can create the key using the AWS Key Management Service (AWS KMS) console. Choose a symmetric customer managed key, Amazon Lookout for Equipment doesn't support asymmetric customer managed keys. For more information, see [Using symmetric and asymmetric keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.

When you create a key using the AWS KMS console, you can give the key the following policy, which enables users or roles to use the key with Amazon Lookout for Equipment. For more information, see [Using key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *AWS Key Management Service Developer Guide*.

```
{
    "Effect": "Allow",
    "Sid": "Allow to use the key with Amazon Lookout for Equipment",
    "Principal": {
        "AWS": "IAM USER OR ROLE ARN"
    },
    "Action": [
        "kms:DescribeKey",
        "kms:CreateGrant",
        "kms:RetireGrant"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": [
                "lookoutequipment.{{Region}}.amazonaws.com"
            ]
        }
    }
},
{
    "Effect": "Allow",
    "Sid": "Allow to view the key in the console"
    "Principal": {
        "AWS": "IAM USER OR ROLE ARN"
    },
    "Action": [
        "kms:DescribeKey"
    ],
    "Resource": "*"
},
{
    "Effect": "Allow",
    "Sid": "Allow inference scheduler pass-in role to encrypt output data"
    "Principal": {
        "AWS": "INFERENCE SCHEDULER PASS-IN ROLE ARN"
    },
    "Action": [
        "kms:GenerateDataKey"
    ],
    "Resource": "*"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lookout for Equipment. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lookout-for-equipment` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
