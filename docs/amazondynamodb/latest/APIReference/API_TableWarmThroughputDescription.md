---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableWarmThroughputDescription.html
---

# TableWarmThroughputDescription
<a name="API_TableWarmThroughputDescription"></a>

Represents the warm throughput value (in read units per second and write units per second) of the table. Warm throughput is applicable for DynamoDB Standard-IA tables and specifies the minimum provisioned capacity maintained for immediate data access.

## Contents
<a name="API_TableWarmThroughputDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ReadUnitsPerSecond **   <a name="DDB-Type-TableWarmThroughputDescription-ReadUnitsPerSecond"></a>
Represents the base table's warm throughput value in read units per second.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** Status **   <a name="DDB-Type-TableWarmThroughputDescription-Status"></a>
Represents warm throughput value of the base table.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | INACCESSIBLE_ENCRYPTION_CREDENTIALS | ARCHIVING | ARCHIVED | REPLICATION_NOT_AUTHORIZED`
Required: No

 ** WriteUnitsPerSecond **   <a name="DDB-Type-TableWarmThroughputDescription-WriteUnitsPerSecond"></a>
Represents the base table's warm throughput value in write units per second.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_TableWarmThroughputDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/TableWarmThroughputDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/TableWarmThroughputDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/TableWarmThroughputDescription)
