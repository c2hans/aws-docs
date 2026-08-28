---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/encryption-with-kms.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Encryption with AWS KMS
<a name="encryption-with-kms"></a>

Amazon SageMaker AI automatically encrypts model artifacts and storage volumes attached to training instances with AWS managed encryption key. All network traffic within the SageMaker AI service account and between the service account and your VPC is encrypted-in-transit using Transport Layer Security (TLS 1.2).

For regulated workloads with highly sensitive data, you might require data encryption using an [AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-cmk-keystore.html) (formerly CMK). The following set of AWS services provide data encryption support with a KMS key.
+ SageMaker AI Processing, SageMaker AI Training (including AutoPilot), SageMaker AI Hosting (including Model Monitoring), SageMaker AI Batch Transform, SageMaker AI Notebook instance, SageMaker AI Feature Store, Amazon S3, AWS Glue, Amazon ECR, AWS CodeBuild, AWS Step Functions, AWS Lambda, Amazon EFS.

[AWS KMS](https://aws.amazon.com/kms/) provides organizations with a fully managed service to centrally control their encryption keys. With AWS KMS, you can ensure your encryption keys are secure and available for the different services in the ML platform. If compliance needs dictate that keys must be frequently rotated, you can manually rotate the CMK with a new CMK. AWS KMS also rotates CMKs automatically once a year.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
