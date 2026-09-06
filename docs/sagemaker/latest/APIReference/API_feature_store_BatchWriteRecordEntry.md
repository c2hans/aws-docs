---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchWriteRecordEntry.html
---

# BatchWriteRecordEntry
<a name="API_feature_store_BatchWriteRecordEntry"></a>

An entry to write as part of a `BatchWriteRecord` request.

## Contents
<a name="API_feature_store_BatchWriteRecordEntry_Contents"></a>

 ** FeatureGroupName **   <a name="sagemaker-Type-feature_store_BatchWriteRecordEntry-FeatureGroupName"></a>
The name or Amazon Resource Name (ARN) of the `FeatureGroup` to write the record to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/)?([a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63})`
Required: Yes

 ** Record **   <a name="sagemaker-Type-feature_store_BatchWriteRecordEntry-Record"></a>
List of FeatureValues to be inserted. This will be a full over-write.
Type: Array of [FeatureValue](API_feature_store_FeatureValue.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** TargetStores **   <a name="sagemaker-Type-feature_store_BatchWriteRecordEntry-TargetStores"></a>
A list of stores to which you're adding the record. By default, Feature Store adds the record to all of the stores that you're using for the `FeatureGroup`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `OnlineStore | OfflineStore`
Required: No

 ** TtlDuration **   <a name="sagemaker-Type-feature_store_BatchWriteRecordEntry-TtlDuration"></a>
Time to live duration for this entry, where the record is hard deleted after the expiration time is reached; `ExpiresAt` = `EventTime` \+ `TtlDuration`. This overrides the request level `TtlDuration`.
Type: [TtlDuration](API_feature_store_TtlDuration.md) object
Required: No

## See Also
<a name="API_feature_store_BatchWriteRecordEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecordEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecordEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecordEntry)
