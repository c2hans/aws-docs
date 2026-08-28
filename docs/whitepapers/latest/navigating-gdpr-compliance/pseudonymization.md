---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/pseudonymization.html
---

# Pseudonymization
<a name="pseudonymization"></a>

AWS provides several approaches and services to help customers implement pseudonymization of personal data. AWS KMS can be used with [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) to create and manage data keys for encrypting specific data fields, while maintaining separate mapping of original values. [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) supports attribute encryption for specific fields, enabling selective pseudonymization of personal data within database records. For application-level pseudonymization, [AWS Lambda](https://aws.amazon.com/lambda/) can be used to create serverless functions that transform data during processing or API calls. [AWS Glue](https://aws.amazon.com/glue/?ams%23interactive-card-vertical%23pattern-data.filter=%257B%2522filters%2522%253A%255B%255D%257D) provides capabilities for data transformation during ETL processes, including the ability to mask or tokenize sensitive fields.

For customers requiring more specialized solutions, [AWS Marketplace](https://aws.amazon.com/marketplace) offers various third-party tools such as Protegrity Data Protection Platform, TokenEx Cloud Data Protection, and the Privacera Data Security Platform, which provide advanced data masking, tokenization, and pseudonymization capabilities. These solutions integrate with AWS services and can be deployed across multiple AWS accounts and regions.

When implementing pseudonymization, customers can use [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) for auditing all pseudonymization operations and [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) to securely store and manage the mapping keys or transformation rules required for re-identification.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
