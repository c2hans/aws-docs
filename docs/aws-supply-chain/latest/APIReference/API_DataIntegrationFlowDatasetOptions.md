---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowDatasetOptions.html
---

# DataIntegrationFlowDatasetOptions
<a name="API_DataIntegrationFlowDatasetOptions"></a>

The dataset options used in dataset source and target configurations.

## Contents
<a name="API_DataIntegrationFlowDatasetOptions_Contents"></a>

 ** dedupeRecords **   <a name="supplychain-Type-DataIntegrationFlowDatasetOptions-dedupeRecords"></a>
The option to perform deduplication on data records sharing same primary key values. If disabled, transformed data with duplicate primary key values will ingest into dataset, for datasets within **asc** namespace, such duplicates will cause ingestion fail. If enabled without dedupeStrategy, deduplication is done by retaining a random data record among those sharing the same primary key values. If enabled with dedupeStragtegy, the deduplication is done following the strategy.
Note that target dataset may have partition configured, when dedupe is enabled, it only dedupe against primary keys and retain only one record out of those duplicates regardless of its partition status.
Type: Boolean
Required: No

 ** dedupeStrategy **   <a name="supplychain-Type-DataIntegrationFlowDatasetOptions-dedupeStrategy"></a>
The deduplication strategy to dedupe the data records sharing same primary key values of the target dataset. This strategy only applies to target dataset with primary keys and with dedupeRecords option enabled. If transformed data still got duplicates after the dedupeStrategy evaluation, a random data record is chosen to be retained.
Type: [DataIntegrationFlowDedupeStrategy](API_DataIntegrationFlowDedupeStrategy.md) object
Required: No

 ** loadType **   <a name="supplychain-Type-DataIntegrationFlowDatasetOptions-loadType"></a>
The target dataset's data load type. This only affects how source S3 files are selected in the S3-to-dataset flow.
+  **REPLACE** - Target dataset will get replaced with the new file added under the source s3 prefix.
+  **INCREMENTAL** - Target dataset will get updated with the up-to-date content under S3 prefix incorporating any file additions or removals there.
Type: String
Valid Values: `INCREMENTAL | REPLACE`
Required: No

## See Also
<a name="API_DataIntegrationFlowDatasetOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlowDatasetOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlowDatasetOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlowDatasetOptions)
