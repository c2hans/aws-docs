---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FeatureGroupSummary.html
---

# FeatureGroupSummary
<a name="API_FeatureGroupSummary"></a>

The name, ARN, `CreationTime`, `FeatureGroup` values, `LastUpdatedTime` and `EnableOnlineStorage` status of a `FeatureGroup`.

## Contents
<a name="API_FeatureGroupSummary_Contents"></a>

 ** FeatureGroupArn **   <a name="sagemaker-Type-FeatureGroupSummary-FeatureGroupArn"></a>
Unique identifier for the `FeatureGroup`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/.*`
Required: Yes

 ** FeatureGroupName **   <a name="sagemaker-Type-FeatureGroupSummary-FeatureGroupName"></a>
The name of `FeatureGroup`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** FeatureGroupStatus **   <a name="sagemaker-Type-FeatureGroupSummary-FeatureGroupStatus"></a>
The status of a FeatureGroup. The status can be any of the following: `Creating`, `Created`, `CreateFail`, `Deleting` or `DetailFail`.
Type: String
Valid Values: `Creating | Created | CreateFailed | Deleting | DeleteFailed`
Required: No

 ** OfflineStoreStatus **   <a name="sagemaker-Type-FeatureGroupSummary-OfflineStoreStatus"></a>
Notifies you if replicating data into the `OfflineStore` has failed. Returns either: `Active` or `Blocked`.
Type: [OfflineStoreStatus](API_OfflineStoreStatus.md) object
Required: No

## See Also
<a name="API_FeatureGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FeatureGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FeatureGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FeatureGroupSummary)
