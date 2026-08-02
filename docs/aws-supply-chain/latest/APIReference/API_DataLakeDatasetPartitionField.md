---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeDatasetPartitionField.html
---

# DataLakeDatasetPartitionField
<a name="API_DataLakeDatasetPartitionField"></a>

The detail of the partition field.

## Contents
<a name="API_DataLakeDatasetPartitionField_Contents"></a>

 ** name **   <a name="supplychain-Type-DataLakeDatasetPartitionField-name"></a>
The name of the partition field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9_]+`
Required: Yes

 ** transform **   <a name="supplychain-Type-DataLakeDatasetPartitionField-transform"></a>
The transformation of the partition field. A transformation specifies how to partition on a given field. For example, with timestamp you can specify that you'd like to partition fields by day, e.g. data record with value 2025-01-03T00:00:00Z in partition field is in 2025-01-03 partition. Also noted that data record without any value in optional partition field is in NULL partition.
Type: [DataLakeDatasetPartitionFieldTransform](API_DataLakeDatasetPartitionFieldTransform.md) object
Required: Yes

## See Also
<a name="API_DataLakeDatasetPartitionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataLakeDatasetPartitionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataLakeDatasetPartitionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataLakeDatasetPartitionField)
