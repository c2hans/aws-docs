---
source_url: https://docs.aws.amazon.com/kms/latest/developerguide/ct-attestation.html
---

# Monitoring attested requests
<a name="ct-attestation"></a>

You can use your AWS CloudTrail logs to monitor [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt), [DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret), [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey), [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair), and [GenerateRandom](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateRandom) operations that use attestation. In these log entries, the `additionalEventData` field has a `recipient` field with information from the attestation document in the request. These fields are included only when the `Recipient` parameter in the request specifies a signed attestation document.

The specific information included in the CloudTrail log depends on the attestation method used.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
