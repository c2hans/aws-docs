---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ImportFileEnrichment.html
---

# ImportFileEnrichment
<a name="API_ImportFileEnrichment"></a>

Details about an import file enrichment job.

## Contents
<a name="API_ImportFileEnrichment_Contents"></a>

 ** checksum **   <a name="mgn-Type-ImportFileEnrichment-checksum"></a>
The checksum of the enriched file for integrity verification.
Type: [Checksum](API_Checksum.md) object
Required: No

 ** createdAt **   <a name="mgn-Type-ImportFileEnrichment-createdAt"></a>
The timestamp when the enrichment job was created.
Type: Timestamp
Required: No

 ** endedAt **   <a name="mgn-Type-ImportFileEnrichment-endedAt"></a>
The timestamp when the enrichment job completed or failed.
Type: Timestamp
Required: No

 ** jobID **   <a name="mgn-Type-ImportFileEnrichment-jobID"></a>
The unique identifier of the import file enrichment job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** s3BucketTarget **   <a name="mgn-Type-ImportFileEnrichment-s3BucketTarget"></a>
The target S3 configuration for the enriched import file.
Type: [EnrichmentTargetS3Configuration](API_EnrichmentTargetS3Configuration.md) object
Required: No

 ** status **   <a name="mgn-Type-ImportFileEnrichment-status"></a>
The current status of the import file enrichment job.
Type: String
Valid Values: `PENDING | STARTED | FAILED | SUCCEEDED | SUCCEEDED_WITH_WARNINGS`
Required: No

 ** statusDetails **   <a name="mgn-Type-ImportFileEnrichment-statusDetails"></a>
Detailed status information about the enrichment job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

## See Also
<a name="API_ImportFileEnrichment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ImportFileEnrichment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ImportFileEnrichment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ImportFileEnrichment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
