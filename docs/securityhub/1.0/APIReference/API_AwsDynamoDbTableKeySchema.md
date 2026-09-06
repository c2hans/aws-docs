---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDynamoDbTableKeySchema.html
---

# AwsDynamoDbTableKeySchema
<a name="API_AwsDynamoDbTableKeySchema"></a>

A component of the key schema for the DynamoDB table, a global secondary index, or a local secondary index.

## Contents
<a name="API_AwsDynamoDbTableKeySchema_Contents"></a>

 ** AttributeName **   <a name="securityhub-Type-AwsDynamoDbTableKeySchema-AttributeName"></a>
The name of the key schema attribute.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KeyType **   <a name="securityhub-Type-AwsDynamoDbTableKeySchema-KeyType"></a>
The type of key used for the key schema attribute. Valid values are `HASH` or `RANGE`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsDynamoDbTableKeySchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDynamoDbTableKeySchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDynamoDbTableKeySchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDynamoDbTableKeySchema)
