---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-sensitive-data-types-credentials.html
---

# Amazon SNS sensitive data types: Credentials
<a name="sns-message-data-protection-sensitive-data-types-credentials"></a>

The following table lists and describes the types of credentials that Amazon SNS can detect using managed data identifiers.

| Detection type | Managed data identifier ID | Keyword required | Countries and regions |
| --- | --- | --- | --- |
| AWS secret access key | AwsSecretKey | aws\_secret\_access\_key, credentials, secret access key, secret key, set-awscredential | Any |
| OpenSSH private key | OpenSshPrivateKey | No | Any |
| PGP private key | PgpPrivateKey | No | Any |
| Public-Key Cryptography Standard (PKCS) private key | PkcsPrivateKey | No | Any |
| PuTTY private key | PuttyPrivateKey | No | Any |

## Data identifier ARNs for credential data types
<a name="sns-message-data-protection-credentials-arns"></a>

The following lists the Amazon Resource Names (ARNs) for the data identifiers that you can add to your data protection policies.

| Credential data identifier ARNs |
| --- |
| arn:aws:dataprotection::aws:data-identifier/AwsSecretKey |
| arn:aws:dataprotection::aws:data-identifier/OpenSshPrivateKey |
| arn:aws:dataprotection::aws:data-identifier/PgpPrivateKey |
| arn:aws:dataprotection::aws:data-identifier/PkcsPrivateKey |
| arn:aws:dataprotection::aws:data-identifier/PuttyPrivateKey |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
