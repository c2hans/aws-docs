---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/kms-key-policy-configuration.html
---

# Set customer managed key policy
<a name="kms-key-policy-configuration"></a>

**Note**
Currently we don’t support configuring CMK on token vault through console.

To use a customer managed key, your key must trust an Amazon Bedrock AgentCore Identity service principal to perform encryption and decryption operations on the key. Configure the [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) of your KMS key as shown in the following example. The IAM principal that writes this policy must have write access to your KMS key, with `kms:PutKeyPolicy` permission.

```
{
    "Id": "identity-service-cmk-policy",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "BedrockAgentCoreIdentityKMSAccess",
            "Effect": "Allow",
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:GenerateDataKeyWithoutPlaintext"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "bedrock-agentcore-identity.*.amazonaws.com"
                },
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                },
                "ArnLike": {
                    "kms:EncryptionContext:aws-crypto-ec:aws:bedrock-agentcore-identity:token-vault-arn": "arn:aws:bedrock-agentcore:*:*:token-vault/default"
                }
            }
        },
        {
            "Sid": "BedrockAgentCoreIdentityDescribeKeyKMSAccess",
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                },
                "StringLike": {
                    "kms:ViaService": "bedrock-agentcore-identity.*.amazonaws.com"
                }
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
