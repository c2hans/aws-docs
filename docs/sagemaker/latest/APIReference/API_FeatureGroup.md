---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FeatureGroup.html
---

# FeatureGroup
<a name="API_FeatureGroup"></a>

Amazon SageMaker Feature Store stores features in a collection called Feature Group. A Feature Group can be visualized as a table which has rows, with a unique identifier for each row where each column in the table is a feature. In principle, a Feature Group is composed of features and values per features.

## Contents
<a name="API_FeatureGroup_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-FeatureGroup-CreationTime"></a>
The time a `FeatureGroup` was created.
Type: Timestamp
Required: No

 ** Description **   <a name="sagemaker-Type-FeatureGroup-Description"></a>
A free form description of a `FeatureGroup`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** EventTimeFeatureName **   <a name="sagemaker-Type-FeatureGroup-EventTimeFeatureName"></a>
The name of the feature that stores the `EventTime` of a Record in a `FeatureGroup`.
A `EventTime` is point in time when a new event occurs that corresponds to the creation or update of a `Record` in `FeatureGroup`. All `Records` in the `FeatureGroup` must have a corresponding `EventTime`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`
Required: No

 ** FailureReason **   <a name="sagemaker-Type-FeatureGroup-FailureReason"></a>
The reason that the `FeatureGroup` failed to be replicated in the `OfflineStore`. This is failure may be due to a failure to create a `FeatureGroup` in or delete a `FeatureGroup` from the `OfflineStore`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** FeatureDefinitions **   <a name="sagemaker-Type-FeatureGroup-FeatureDefinitions"></a>
A list of `Feature`s. Each `Feature` must include a `FeatureName` and a `FeatureType`.
Valid `FeatureType`s are `Integral`, `Fractional` and `String`.
 `FeatureName`s cannot be any of the following: `is_deleted`, `write_time`, `api_invocation_time`.
You can create up to 2,500 `FeatureDefinition`s per `FeatureGroup`.
Type: Array of [FeatureDefinition](API_FeatureDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2500 items.
Required: No

 ** FeatureGroupArn **   <a name="sagemaker-Type-FeatureGroup-FeatureGroupArn"></a>
The Amazon Resource Name (ARN) of a `FeatureGroup`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/.*`
Required: No

 ** FeatureGroupName **   <a name="sagemaker-Type-FeatureGroup-FeatureGroupName"></a>
The name of the `FeatureGroup`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63}`
Required: No

 ** FeatureGroupStatus **   <a name="sagemaker-Type-FeatureGroup-FeatureGroupStatus"></a>
A `FeatureGroup` status.
Type: String
Valid Values: `Creating | Created | CreateFailed | Deleting | DeleteFailed`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-FeatureGroup-LastModifiedTime"></a>
A timestamp indicating the last time you updated the feature group.
Type: Timestamp
Required: No

 ** LastUpdateStatus **   <a name="sagemaker-Type-FeatureGroup-LastUpdateStatus"></a>
A value that indicates whether the feature group was updated successfully.
Type: [LastUpdateStatus](API_LastUpdateStatus.md) object
Required: No

 ** OfflineStoreConfig **   <a name="sagemaker-Type-FeatureGroup-OfflineStoreConfig"></a>
The configuration of an `OfflineStore`.
Provide an `OfflineStoreConfig` in a request to `CreateFeatureGroup` to create an `OfflineStore`.
To encrypt an `OfflineStore` using at rest data encryption, specify AWS Key Management Service (KMS) key ID, or `KMSKeyId`, in `S3StorageConfig`.
Type: [OfflineStoreConfig](API_OfflineStoreConfig.md) object
Required: No

 ** OfflineStoreStatus **   <a name="sagemaker-Type-FeatureGroup-OfflineStoreStatus"></a>
The status of `OfflineStore`.
Type: [OfflineStoreStatus](API_OfflineStoreStatus.md) object
Required: No

 ** OnlineStoreConfig **   <a name="sagemaker-Type-FeatureGroup-OnlineStoreConfig"></a>
Use this to specify the AWS Key Management Service (KMS) Key ID, or `KMSKeyId`, for at rest data encryption. You can turn `OnlineStore` on or off by specifying the `EnableOnlineStore` flag at General Assembly.
The default value is `False`.
Type: [OnlineStoreConfig](API_OnlineStoreConfig.md) object
Required: No

 ** RecordIdentifierFeatureName **   <a name="sagemaker-Type-FeatureGroup-RecordIdentifierFeatureName"></a>
The name of the `Feature` whose value uniquely identifies a `Record` defined in the `FeatureGroup` `FeatureDefinitions`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`
Required: No

 ** RoleArn **   <a name="sagemaker-Type-FeatureGroup-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM execution role used to create the feature group.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** Tags **   <a name="sagemaker-Type-FeatureGroup-Tags"></a>
Tags used to define a `FeatureGroup`.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_FeatureGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FeatureGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FeatureGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FeatureGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
