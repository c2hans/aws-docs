---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/granting-permissions-for-mediaconvert-to-access-encrypted-s3-buckets.html
---

# Granting permissions for MediaConvert to access encrypted Amazon S3 buckets
<a name="granting-permissions-for-mediaconvert-to-access-encrypted-s3-buckets"></a>

When you [enable Amazon S3 default encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html#bucket-encryption-how-to-set-up), Amazon S3 automatically encrypts your objects as you upload them. You can optionally choose to use AWS Key Management Service (AWS KMS) to manage the key. This is called SSE-KMS encryption.

If you enable SSE-KMS default encryption on the buckets that hold your AWS Elemental MediaConvert input or output files, you must [add inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console) to your IAM service role. If you don't add inline policies, MediaConvert can't read your input files or write your output files.

Grant these permissions in the following use cases:
+ If your input bucket has SSE-KMS default encryption, grant `kms:Decrypt`.
+ If your output bucket has SSE-KMS default encryption, grant `kms:GenerateDataKey`.

The following example inline policy grants both permissions.

## Example inline policy with kms:Decrypt and kms:GenerateDataKey
<a name="example-inline-policy-kms-decrypt-generatedatakey"></a>

This policy grants permissions for both `kms:Decrypt` and `kms:GenerateDataKey`.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike":

{           "kms:ViaService": "s3.*.amazonaws.com"         }
      }
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
