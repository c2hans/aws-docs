---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeDatasetSchema.html
---

# DataLakeDatasetSchema
<a name="API_DataLakeDatasetSchema"></a>

The schema details of the dataset. Note that for AWS Supply Chain dataset under **asc** namespace, it may have internal fields like connection\_id that will be auto populated by data ingestion methods.

## Contents
<a name="API_DataLakeDatasetSchema_Contents"></a>

 ** fields **   <a name="supplychain-Type-DataLakeDatasetSchema-fields"></a>
The list of field details of the dataset schema.
Type: Array of [DataLakeDatasetSchemaField](API_DataLakeDatasetSchemaField.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: Yes

 ** name **   <a name="supplychain-Type-DataLakeDatasetSchema-name"></a>
The name of the dataset schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9]+`
Required: Yes

 ** primaryKeys **   <a name="supplychain-Type-DataLakeDatasetSchema-primaryKeys"></a>
The list of primary key fields for the dataset. Primary keys defined can help data ingestion methods to ensure data uniqueness: CreateDataIntegrationFlow's dedupe strategy will leverage primary keys to perform records deduplication before write to dataset; SendDataIntegrationEvent's UPSERT and DELETE can only work with dataset with primary keys. For more details, refer to those data ingestion documentations.
Note that defining primary keys does not necessarily mean the dataset cannot have duplicate records, duplicate records can still be ingested if CreateDataIntegrationFlow's dedupe disabled or through SendDataIntegrationEvent's APPEND operation.
Type: Array of [DataLakeDatasetPrimaryKeyField](API_DataLakeDatasetPrimaryKeyField.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

## See Also
<a name="API_DataLakeDatasetSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataLakeDatasetSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataLakeDatasetSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataLakeDatasetSchema)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
