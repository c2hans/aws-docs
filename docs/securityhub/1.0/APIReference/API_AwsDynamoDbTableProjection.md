---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDynamoDbTableProjection.html
---

# AwsDynamoDbTableProjection
<a name="API_AwsDynamoDbTableProjection"></a>

For global and local secondary indexes, identifies the attributes that are copied from the table into the index.

## Contents
<a name="API_AwsDynamoDbTableProjection_Contents"></a>

 ** NonKeyAttributes **   <a name="securityhub-Type-AwsDynamoDbTableProjection-NonKeyAttributes"></a>
The nonkey attributes that are projected into the index. For each attribute, provide the attribute name.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** ProjectionType **   <a name="securityhub-Type-AwsDynamoDbTableProjection-ProjectionType"></a>
The types of attributes that are projected into the index. Valid values are as follows:
+  `ALL`
+  `INCLUDE`
+  `KEYS_ONLY`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsDynamoDbTableProjection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDynamoDbTableProjection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDynamoDbTableProjection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDynamoDbTableProjection)
