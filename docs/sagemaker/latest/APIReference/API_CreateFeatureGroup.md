---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateFeatureGroup.html
---

# CreateFeatureGroup
<a name="API_CreateFeatureGroup"></a>

Create a new `FeatureGroup`. A `FeatureGroup` is a group of `Features` defined in the `FeatureStore` to describe a `Record`.

The `FeatureGroup` defines the schema and features contained in the `FeatureGroup`. A `FeatureGroup` definition is composed of a list of `Features`, a `RecordIdentifierFeatureName`, an `EventTimeFeatureName` and configurations for its `OnlineStore` and `OfflineStore`. Check [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) to see the `FeatureGroup`s quota for your AWS account.

Note that it can take approximately 10-15 minutes to provision an `OnlineStore` `FeatureGroup` with the `InMemory` `StorageType`.

**Important**
You must include at least one of `OnlineStoreConfig` and `OfflineStoreConfig` to create a `FeatureGroup`.

## Request Syntax
<a name="API_CreateFeatureGroup_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "EventTimeFeatureName": "{{string}}",
   "FeatureDefinitions": [
      {
         "CollectionConfig": { ... },
         "CollectionType": "{{string}}",
         "FeatureName": "{{string}}",
         "FeatureType": "{{string}}"
      }
   ],
   "FeatureGroupName": "{{string}}",
   "OfflineStoreConfig": {
      "DataCatalogConfig": {
         "Catalog": "{{string}}",
         "Database": "{{string}}",
         "TableName": "{{string}}"
      },
      "DisableGlueTableCreation": {{boolean}},
      "S3StorageConfig": {
         "KmsKeyId": "{{string}}",
         "ResolvedOutputS3Uri": "{{string}}",
         "S3Uri": "{{string}}"
      },
      "TableFormat": "{{string}}"
   },
   "OnlineStoreConfig": {
      "EnableOnlineStore": {{boolean}},
      "SecurityConfig": {
         "KmsKeyId": "{{string}}"
      },
      "StorageType": "{{string}}",
      "TtlDuration": {
         "Unit": "{{string}}",
         "Value": {{number}}
      }
   },
   "RecordIdentifierFeatureName": "{{string}}",
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ThroughputConfig": {
      "ProvisionedReadCapacityUnits": {{number}},
      "ProvisionedWriteCapacityUnits": {{number}},
      "ThroughputMode": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateFeatureGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateFeatureGroup_RequestSyntax) **   <a name="sagemaker-CreateFeatureGroup-request-Description"></a>
A free-form description of a `FeatureGroup`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [EventTimeFeatureName](#API_CreateFeatureGroup_RequestSyntax) **   <a name="sagemaker-CreateFeatureGroup-request-EventTimeFeatureName"></a>
The name of the feature that stores the `EventTime` of a `Record` in a `FeatureGroup`.
An `EventTime` is a point in time when a new event occurs that corresponds to the creation or update of a `Record` in a `FeatureGroup`. All `Records` in the `FeatureGroup` must have a corresponding `EventTime`.
An `EventTime` can be a `String` or `Fractional`.
+  `Fractional`: `EventTime` feature values must be a Unix timestamp in seconds.
+  `String`: `EventTime` feature values must be an ISO-8601 string in the format. The following formats are supported `yyyy-MM-dd'T'HH:mm:ssZ` and `yyyy-MM-dd'T'HH:mm:ss.SSSZ` where `yyyy`, `MM`, and `dd` represent the year, month, and day respectively and `HH`, `mm`, `ss`, and if applicable, `SSS` represent the hour, month, second and milliseconds respsectively. `'T'` and `Z` are constants.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** [FeatureDefinitions](#API_CreateFeatureGroup_RequestSyntax) **   <a name="sagemaker-CreateFeatureGroup-request-FeatureDefinitions"></a>
A list of `Feature` names and types. `Name` and `Type` is compulsory per `Feature`.
Valid feature `FeatureType`s are `Integral`, `Fractional` and `String`.
 `FeatureName`s cannot be any of the following: `is_deleted`, `write_time`, `api_invocation_time`
You can create up to 2,500 `FeatureDefinition`s per `FeatureGroup`.
Type: Array of [FeatureDefinition](API_FeatureDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2500 items.
Required: Yes

 ** [FeatureGroupName](#API_CreateFeatureGroup_RequestSyntax) **   <a name="sagemaker-CreateFeatureGroup-request-FeatureGroupName"></a>
The name of the `FeatureGroup`. The name must be unique within an AWS Region in an AWS account.
The name:
+ Must start with an alphanumeric character.
+ Can only include alphanumeric characters, underscores, and hyphens. Spaces are not allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** [OfflineStoreConfig](#API_CreateFeatureGroup_RequestSyntax) **   <a name="sagemaker-CreateFeatureGroup-request-OfflineStoreConfig"></a>
Use this to configure an `OfflineFeatureStore`. This parameter allows you to specify:
+ The Amazon Simple Storage Service (Amazon S3) location of an `OfflineStore`.
+ A configuration for an AWS Glue or AWS Hive data catalog.
+ An KMS encryption key to encrypt the Amazon S3 location used for `OfflineStore`. If KMS encryption key is not specified, by default we encrypt all data at rest using AWS KMS key. By defining your [bucket-level key](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) for SSE, you can reduce AWS KMS requests costs by up to 99 percent.
+ Format for the offline store table. Supported formats are Glue (Default) and [Apache Iceberg](https://iceberg.apache.org/).
To learn more about this parameter, see [OfflineStoreConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OfflineStoreConfig.html).
Type: [OfflineStoreConfig](API_OfflineStoreConfig.md) object
Required: No

 ** [OnlineStoreConfig](#API_CreateFeatureGroup_RequestSyntax) **   <a name="sagemaker-CreateFeatureGroup-request-OnlineStoreConfig"></a>
You can turn the `OnlineStore` on or off by specifying `True` for the `EnableOnlineStore` flag in `OnlineStoreConfig`.
You can also include an AWS KMS key ID (`KMSKeyId`) for at-rest encryption of the `OnlineStore`.
The default value is `False`.
Type: [OnlineStoreConfig](API_OnlineStoreConfig.md) object
Required: No

 ** [RecordIdentifierFeatureName](#API_CreateFeatureGroup_RequestSyntax) **   <a name="sagemaker-CreateFeatureGroup-request-RecordIdentifierFeatureName"></a>
The name of the `Feature` whose value uniquely identifies a `Record` defined in the `FeatureStore`. Only the latest record per identifier value will be stored in the `OnlineStore`. `RecordIdentifierFeatureName` must be one of feature definitions' names.
You use the `RecordIdentifierFeatureName` to access data in a `FeatureStore`.
This name:
+ Must start with an alphanumeric character.
+ Can only contains alphanumeric characters, hyphens, underscores. Spaces are not allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** [RoleArn](#API_CreateFeatureGroup_RequestSyntax) **   <a name="sagemaker-CreateFeatureGroup-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM execution role used to persist data into the `OfflineStore` if an `OfflineStoreConfig` is provided.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [Tags](#API_CreateFeatureGroup_RequestSyntax) **   <a name="sagemaker-CreateFeatureGroup-request-Tags"></a>
Tags used to identify `Features` in each `FeatureGroup`.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [ThroughputConfig](#API_CreateFeatureGroup_RequestSyntax) **   <a name="sagemaker-CreateFeatureGroup-request-ThroughputConfig"></a>
Used to set feature group throughput configuration. There are two modes: `ON_DEMAND` and `PROVISIONED`. With on-demand mode, you are charged for data reads and writes that your application performs on your feature group. You do not need to specify read and write throughput because Feature Store accommodates your workloads as they ramp up and down. You can switch a feature group to on-demand only once in a 24 hour period. With provisioned throughput mode, you specify the read and write capacity per second that you expect your application to require, and you are billed based on those limits. Exceeding provisioned throughput will result in your requests being throttled.
Note: `PROVISIONED` throughput mode is supported only for feature groups that are offline-only, or use the [`Standard`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig-StorageType) tier online store.
Type: [ThroughputConfig](API_ThroughputConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateFeatureGroup_ResponseSyntax"></a>

```
{
   "FeatureGroupArn": "string"
}
```

## Response Elements
<a name="API_CreateFeatureGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FeatureGroupArn](#API_CreateFeatureGroup_ResponseSyntax) **   <a name="sagemaker-CreateFeatureGroup-response-FeatureGroupArn"></a>
The Amazon Resource Name (ARN) of the `FeatureGroup`. This is a unique identifier for the feature group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/.*`

## Errors
<a name="API_CreateFeatureGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateFeatureGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateFeatureGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateFeatureGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateFeatureGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateFeatureGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateFeatureGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateFeatureGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateFeatureGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateFeatureGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateFeatureGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateFeatureGroup)
