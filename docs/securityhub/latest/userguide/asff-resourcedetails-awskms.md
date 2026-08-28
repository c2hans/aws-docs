---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/asff-resourcedetails-awskms.html
---

# AwsKms resources in ASFF
<a name="asff-resourcedetails-awskms"></a>

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsKms` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md).

## AwsKmsKey
<a name="asff-resourcedetails-awskmskey"></a>

The `AwsKmsKey` object provides details about an AWS KMS key.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsKmsKey` object. To view descriptions of `AwsKmsKey` attributes, see [AwsKmsKeyDetails](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsKmsKeyDetails.html) in the *AWS Security Hub API Reference*.

**Example**

```
"AwsKmsKey": {
                        "AWSAccountId": "string",
                        "CreationDate": "string",
                        "Description": "string",
                        "KeyId": "string",
                        "KeyManager": "string",
                        "KeyRotationStatus": boolean,
                        "KeyState": "string",
                        "Origin": "string"
                    }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
