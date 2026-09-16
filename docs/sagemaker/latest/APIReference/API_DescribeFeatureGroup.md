---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureGroup.html
---

# DescribeFeatureGroup
<a name="API_DescribeFeatureGroup"></a>

Use this operation to describe a `FeatureGroup`. The response includes information on the creation time, `FeatureGroup` name, the unique identifier for each `FeatureGroup`, and more.

## Request Syntax
<a name="API_DescribeFeatureGroup_RequestSyntax"></a>

```
{
   "FeatureGroupName": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFeatureGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FeatureGroupName](#API_DescribeFeatureGroup_RequestSyntax) **   <a name="sagemaker-DescribeFeatureGroup-request-FeatureGroupName"></a>
The name or Amazon Resource Name (ARN) of the `FeatureGroup` you want described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group\/)?([a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63})`
Required: Yes

 ** [NextToken](#API_DescribeFeatureGroup_RequestSyntax) **   <a name="sagemaker-DescribeFeatureGroup-request-NextToken"></a>
A token to resume pagination of the list of `Features` (`FeatureDefinitions`). 2,500 `Features` are returned by default.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_DescribeFeatureGroup_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "Description": "string",
   "EventTimeFeatureName": "string",
   "FailureReason": "string",
   "FeatureDefinitions": [
      {
         "CollectionConfig": { ... },
         "CollectionType": "string",
         "FeatureName": "string",
         "FeatureType": "string"
      }
   ],
   "FeatureGroupArn": "string",
   "FeatureGroupName": "string",
   "FeatureGroupStatus": "string",
   "LastModifiedTime": number,
   "LastUpdateStatus": {
      "FailureReason": "string",
      "Status": "string"
   },
   "NextToken": "string",
   "OfflineStoreConfig": {
      "DataCatalogConfig": {
         "Catalog": "string",
         "Database": "string",
         "TableName": "string"
      },
      "DisableGlueTableCreation": boolean,
      "S3StorageConfig": {
         "KmsKeyId": "string",
         "ResolvedOutputS3Uri": "string",
         "S3Uri": "string"
      },
      "TableFormat": "string"
   },
   "OfflineStoreStatus": {
      "BlockedReason": "string",
      "Status": "string"
   },
   "OnlineStoreConfig": {
      "EnableOnlineStore": boolean,
      "SecurityConfig": {
         "KmsKeyId": "string"
      },
      "StorageType": "string",
      "TtlDuration": {
         "Unit": "string",
         "Value": number
      }
   },
   "OnlineStoreTotalSizeBytes": number,
   "RecordIdentifierFeatureName": "string",
   "RoleArn": "string",
   "ThroughputConfig": {
      "ProvisionedReadCapacityUnits": number,
      "ProvisionedWriteCapacityUnits": number,
      "ThroughputMode": "string"
   }
}
```

## Response Elements
<a name="API_DescribeFeatureGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-CreationTime"></a>
A timestamp indicating when SageMaker created the `FeatureGroup`.
Type: Timestamp

 ** [Description](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-Description"></a>
A free form description of the feature group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [EventTimeFeatureName](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-EventTimeFeatureName"></a>
The name of the feature that stores the `EventTime` of a Record in a `FeatureGroup`.
 An `EventTime` is a point in time when a new event occurs that corresponds to the creation or update of a `Record` in a `FeatureGroup`. All `Records` in the `FeatureGroup` have a corresponding `EventTime`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`

 ** [FailureReason](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-FailureReason"></a>
The reason that the `FeatureGroup` failed to be replicated in the `OfflineStore`. This is failure can occur because:
+ The `FeatureGroup` could not be created in the `OfflineStore`.
+ The `FeatureGroup` could not be deleted from the `OfflineStore`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [FeatureDefinitions](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-FeatureDefinitions"></a>
A list of the `Features` in the `FeatureGroup`. Each feature is defined by a `FeatureName` and `FeatureType`.
Type: Array of [FeatureDefinition](API_FeatureDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2500 items.

 ** [FeatureGroupArn](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-FeatureGroupArn"></a>
The Amazon Resource Name (ARN) of the `FeatureGroup`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/.*`

 ** [FeatureGroupName](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-FeatureGroupName"></a>
he name of the `FeatureGroup`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63}`

 ** [FeatureGroupStatus](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-FeatureGroupStatus"></a>
The status of the feature group.
Type: String
Valid Values: `Creating | Created | CreateFailed | Deleting | DeleteFailed`

 ** [LastModifiedTime](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-LastModifiedTime"></a>
A timestamp indicating when the feature group was last updated.
Type: Timestamp

 ** [LastUpdateStatus](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-LastUpdateStatus"></a>
A value indicating whether the update made to the feature group was successful.
Type: [LastUpdateStatus](API_LastUpdateStatus.md) object

 ** [NextToken](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-NextToken"></a>
A token to resume pagination of the list of `Features` (`FeatureDefinitions`).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [OfflineStoreConfig](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-OfflineStoreConfig"></a>
The configuration of the offline store. It includes the following configurations:
+ Amazon S3 location of the offline store.
+ Configuration of the Glue data catalog.
+ Table format of the offline store.
+ Option to disable the automatic creation of a Glue table for the offline store.
+ Encryption configuration.
Type: [OfflineStoreConfig](API_OfflineStoreConfig.md) object

 ** [OfflineStoreStatus](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-OfflineStoreStatus"></a>
The status of the `OfflineStore`. Notifies you if replicating data into the `OfflineStore` has failed. Returns either: `Active` or `Blocked`
Type: [OfflineStoreStatus](API_OfflineStoreStatus.md) object

 ** [OnlineStoreConfig](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-OnlineStoreConfig"></a>
The configuration for the `OnlineStore`.
Type: [OnlineStoreConfig](API_OnlineStoreConfig.md) object

 ** [OnlineStoreTotalSizeBytes](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-OnlineStoreTotalSizeBytes"></a>
The size of the `OnlineStore` in bytes.
Type: Long

 ** [RecordIdentifierFeatureName](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-RecordIdentifierFeatureName"></a>
The name of the `Feature` used for `RecordIdentifier`, whose value uniquely identifies a record stored in the feature store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`

 ** [RoleArn](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM execution role used to persist data into the OfflineStore if an OfflineStoreConfig is provided.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [ThroughputConfig](#API_DescribeFeatureGroup_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureGroup-response-ThroughputConfig"></a>
Active throughput configuration of the feature group. There are two modes: `ON_DEMAND` and `PROVISIONED`. With on-demand mode, you are charged for data reads and writes that your application performs on your feature group. You do not need to specify read and write throughput because Feature Store accommodates your workloads as they ramp up and down. You can switch a feature group to on-demand only once in a 24 hour period. With provisioned throughput mode, you specify the read and write capacity per second that you expect your application to require, and you are billed based on those limits. Exceeding provisioned throughput will result in your requests being throttled.
Note: `PROVISIONED` throughput mode is supported only for feature groups that are offline-only, or use the [`Standard`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig-StorageType) tier online store.
Type: [ThroughputConfigDescription](API_ThroughputConfigDescription.md) object

## Errors
<a name="API_DescribeFeatureGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeFeatureGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeFeatureGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeFeatureGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeFeatureGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeFeatureGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeFeatureGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeFeatureGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeFeatureGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeFeatureGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeFeatureGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeFeatureGroup)
