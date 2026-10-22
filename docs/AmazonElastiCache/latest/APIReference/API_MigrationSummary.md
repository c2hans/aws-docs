---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_MigrationSummary.html
---

# MigrationSummary
<a name="API_MigrationSummary"></a>

Provides a summary of the current migration status for a serverless cache.

## Contents
<a name="API_MigrationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CutoverMode **
The cutover configuration for the migration.
Type: String
Required: No

 ** MigrationEndpoint **
The migration endpoint, which is the standard endpoint of the serverless cache. Point your application at this endpoint during the migration. Until cutover, ElastiCache routes requests on this endpoint to your source.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** Status **
The current status of the migration.
Type: String
Required: No

## See Also
<a name="API_MigrationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/MigrationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/MigrationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/MigrationSummary)
