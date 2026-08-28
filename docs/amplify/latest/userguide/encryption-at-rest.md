---
source_url: https://docs.aws.amazon.com/amplify/latest/userguide/encryption-at-rest.html
---

# Encryption at rest
<a name="encryption-at-rest"></a>

Encryption at rest refers to protecting your data from unauthorized access by encrypting data while stored. Amplify encrypts an app's build artifacts by default using AWS KMS keys for Amazon S3 that are managed by the AWS Key Management Service.

Amplify uses Amazon CloudFront to serve your app to your customers. CloudFront uses SSDs which are encrypted for edge location points of presence (POPs), and encrypted EBS volumes for Regional Edge Caches (RECs). Function code and configuration in CloudFront Functions is always stored in an encrypted format on the encrypted SSDs on the edge location POPs, and in other storage locations used by CloudFront.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
