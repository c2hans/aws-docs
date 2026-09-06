---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/encryption-at-rest.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Encryption of data at rest
<a name="encryption-at-rest"></a>

The telemetry data that an Amazon Inspector Classic agent generates during assessment runs is formatted in JSON files. These files are delivered in near-real-time over TLS to Amazon Inspector Classic, where they are encrypted with a per-assessment-run, ephemeral AWS KMS-derived key.

The files are securely stored in S3 buckets that are dedicated to Amazon Inspector Classic. The rules engine of Amazon Inspector Classic does the following:
+ Accesses the encrypted telemetry data in the S3 bucket
+ Decrypts it in memory
+ Processes the data against the configured assessment rules to generate findings
