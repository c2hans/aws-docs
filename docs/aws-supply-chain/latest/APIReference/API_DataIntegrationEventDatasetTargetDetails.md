---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationEventDatasetTargetDetails.html
---

# DataIntegrationEventDatasetTargetDetails
<a name="API_DataIntegrationEventDatasetTargetDetails"></a>

The target dataset details for a DATASET event type.

## Contents
<a name="API_DataIntegrationEventDatasetTargetDetails_Contents"></a>

 ** datasetIdentifier **   <a name="supplychain-Type-DataIntegrationEventDatasetTargetDetails-datasetIdentifier"></a>
The datalake dataset ARN identifier.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1011.
Pattern: `arn:aws:scn:([a-z0-9-]+):([0-9]+):instance/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/namespaces/[^/]+/datasets/[^/]+`
Required: Yes

 ** datasetLoadExecution **   <a name="supplychain-Type-DataIntegrationEventDatasetTargetDetails-datasetLoadExecution"></a>
The target dataset load execution.
Type: [DataIntegrationEventDatasetLoadExecutionDetails](API_DataIntegrationEventDatasetLoadExecutionDetails.md) object
Required: Yes

 ** operationType **   <a name="supplychain-Type-DataIntegrationEventDatasetTargetDetails-operationType"></a>
The target dataset load operation type. The available options are:
+  **APPEND** - Add new records to the dataset. Noted that this operation type will just try to append records as-is without any primary key or partition constraints.
+  **UPSERT** - Modify existing records in the dataset with primary key configured, events for datasets without primary keys are not allowed. If event data contains primary keys that match records in the dataset within same partition, then those existing records (in that partition) will be updated. If primary keys do not match, new records will be added. Note that if dataset contain records with duplicate primary key values in the same partition, those duplicate records will be deduped into one updated record.
+  **DELETE** - Remove existing records in the dataset with primary key configured, events for datasets without primary keys are not allowed. If event data contains primary keys that match records in the dataset within same partition, then those existing records (in that partition) will be deleted. If primary keys do not match, no actions will be done. Note that if dataset contain records with duplicate primary key values in the same partition, all those duplicates will be removed.
Type: String
Valid Values: `APPEND | UPSERT | DELETE`
Required: Yes

## See Also
<a name="API_DataIntegrationEventDatasetTargetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationEventDatasetTargetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationEventDatasetTargetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationEventDatasetTargetDetails)
