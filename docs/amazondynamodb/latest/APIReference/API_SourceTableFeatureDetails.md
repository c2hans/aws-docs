---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SourceTableFeatureDetails.html
---

# SourceTableFeatureDetails
<a name="API_SourceTableFeatureDetails"></a>

Contains the details of the features enabled on the table when the backup was created. For example, LSIs, GSIs, streams, TTL.

## Contents
<a name="API_SourceTableFeatureDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GlobalSecondaryIndexes **   <a name="DDB-Type-SourceTableFeatureDetails-GlobalSecondaryIndexes"></a>
Represents the GSI properties for the table when the backup was created. It includes the IndexName, KeySchema, Projection, and ProvisionedThroughput for the GSIs on the table at the time of backup.
Type: Array of [GlobalSecondaryIndexInfo](API_GlobalSecondaryIndexInfo.md) objects
Required: No

 ** LocalSecondaryIndexes **   <a name="DDB-Type-SourceTableFeatureDetails-LocalSecondaryIndexes"></a>
Represents the LSI properties for the table when the backup was created. It includes the IndexName, KeySchema and Projection for the LSIs on the table at the time of backup.
Type: Array of [LocalSecondaryIndexInfo](API_LocalSecondaryIndexInfo.md) objects
Required: No

 ** SSEDescription **   <a name="DDB-Type-SourceTableFeatureDetails-SSEDescription"></a>
The description of the server-side encryption status on the table when the backup was created.
Type: [SSEDescription](API_SSEDescription.md) object
Required: No

 ** StreamDescription **   <a name="DDB-Type-SourceTableFeatureDetails-StreamDescription"></a>
Stream settings on the table when the backup was created.
Type: [StreamSpecification](API_StreamSpecification.md) object
Required: No

 ** TimeToLiveDescription **   <a name="DDB-Type-SourceTableFeatureDetails-TimeToLiveDescription"></a>
Time to Live settings on the table when the backup was created.
Type: [TimeToLiveDescription](API_TimeToLiveDescription.md) object
Required: No

 ** VectorIndexes **   <a name="DDB-Type-SourceTableFeatureDetails-VectorIndexes"></a>
The vector index properties for the table at the time the backup was created, including the index name, vector attribute, dimensions, distance function, search schema, and projection.
Type: Array of [VectorIndexInfo](API_VectorIndexInfo.md) objects
Required: No

## See Also
<a name="API_SourceTableFeatureDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/SourceTableFeatureDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/SourceTableFeatureDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/SourceTableFeatureDetails)
