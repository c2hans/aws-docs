---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDynamoDbTableLocalSecondaryIndex.html
---

# AwsDynamoDbTableLocalSecondaryIndex
<a name="API_AwsDynamoDbTableLocalSecondaryIndex"></a>

Information about a local secondary index for a DynamoDB table.

## Contents
<a name="API_AwsDynamoDbTableLocalSecondaryIndex_Contents"></a>

 ** IndexArn **   <a name="securityhub-Type-AwsDynamoDbTableLocalSecondaryIndex-IndexArn"></a>
The ARN of the index.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IndexName **   <a name="securityhub-Type-AwsDynamoDbTableLocalSecondaryIndex-IndexName"></a>
The name of the index.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KeySchema **   <a name="securityhub-Type-AwsDynamoDbTableLocalSecondaryIndex-KeySchema"></a>
The complete key schema for the index.
Type: Array of [AwsDynamoDbTableKeySchema](API_AwsDynamoDbTableKeySchema.md) objects
Required: No

 ** Projection **   <a name="securityhub-Type-AwsDynamoDbTableLocalSecondaryIndex-Projection"></a>
Attributes that are copied from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.
Type: [AwsDynamoDbTableProjection](API_AwsDynamoDbTableProjection.md) object
Required: No

## See Also
<a name="API_AwsDynamoDbTableLocalSecondaryIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDynamoDbTableLocalSecondaryIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDynamoDbTableLocalSecondaryIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDynamoDbTableLocalSecondaryIndex)
