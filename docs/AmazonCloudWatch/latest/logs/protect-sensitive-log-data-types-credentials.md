---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types-credentials.html
---

# Credentials
<a name="protect-sensitive-log-data-types-credentials"></a>

CloudWatch Logs data protection can find the following types of credentials.

| Type of data | Data identifier ID | Keyword required | Countries and regions |
| --- | --- | --- | --- |
| AWS secret access key | `AwsSecretKey` | `aws_secret_access_key`, `credentials`, `secret access key`, `secret key`, `set-awscredential` | All |
| OpenSSH private key | `OpenSSHPrivateKey` | None | All |
| PGP private key | `PgpPrivateKey` | None | All |
| Pkcs Private Key | `PkcsPrivateKey` | None | All |
| PuTTY private key | `PuttyPrivateKey` | None | All |

## Data identifier ARNs for credential data types
<a name="cwl-data-protection-credentials-arns"></a>

The following lists the Amazon Resource Names (ARNs) for the data identifiers that you can add to your data protection policies.

| Credential data identifier ARNs |
| --- |
| arn:aws:dataprotection::aws:data-identifier/AwsSecretKey |
| arn:aws:dataprotection::aws:data-identifier/OpenSshPrivateKey |
| arn:aws:dataprotection::aws:data-identifier/PgpPrivateKey |
| arn:aws:dataprotection::aws:data-identifier/PkcsPrivateKey |
| arn:aws:dataprotection::aws:data-identifier/PuttyPrivateKey |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
