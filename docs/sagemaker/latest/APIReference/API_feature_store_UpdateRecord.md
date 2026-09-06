---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html
---

# UpdateRecord
<a name="API_feature_store_UpdateRecord"></a>

Updates one or more feature values for an existing record in the specified feature group. Features that you do not include in the request remain unchanged. You can update up to 100 features per call.

**Important**
This operation requires the online store. It is available only for feature groups that use the [`Standard_V2`](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-storage-configurations-online-store.html#feature-store-storage-configurations-online-store-standard-v2-tier) or `InMemory` online store type.

The record you want to update must already exist in the online store. When you ingest a record, the `TargetStores` parameter must include the `OnlineStore`. You can specify `OnlineStore` alone, or both `OnlineStore` and `OfflineStore`. Records written only to the `OfflineStore` can't be updated.

The record must already exist. If the record does not exist or has been soft-deleted, the operation returns a `ResourceNotFound` error. To create a record, use `PutRecord`.

If you provide an `EventTime` that is older than the record's current `EventTime`, the service rejects the update with a `ConflictException`. If the `EventTime` is equal to or newer than the current value, the service applies the update. If you omit `EventTime`, the service keeps the record's existing `EventTime` and applies the update.

If you specify a `TtlDuration`, you must also provide an `EventTime` in the request. Otherwise, the operation returns a `ValidationError`.

## Request Syntax
<a name="API_feature_store_UpdateRecord_RequestSyntax"></a>

```
POST /FeatureGroup/{{FeatureGroupName}}/Record HTTP/1.1
Content-type: application/json

{
   "Features": [
      {
         "FeatureName": "{{string}}",
         "ValueAsString": "{{string}}",
         "ValueAsStringList": [ "{{string}}" ]
      }
   ],
   "RecordIdentifierValueAsString": "{{string}}",
   "TargetStores": [ "{{string}}" ],
   "TtlDuration": {
      "Unit": "{{string}}",
      "Value": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_feature_store_UpdateRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FeatureGroupName](#API_feature_store_UpdateRecord_RequestSyntax) **   <a name="sagemaker-feature_store_UpdateRecord-request-uri-FeatureGroupName"></a>
The identifier for the feature group that contains the record to update. You can specify one of the following:
+ The feature group name.
+ The feature group Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/)?([a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63})`
Required: Yes

## Request Body
<a name="API_feature_store_UpdateRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Features](#API_feature_store_UpdateRecord_RequestSyntax) **   <a name="sagemaker-feature_store_UpdateRecord-request-Features"></a>
The feature values to write to the record.
Type: Array of [FeatureValue](API_feature_store_FeatureValue.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [RecordIdentifierValueAsString](#API_feature_store_UpdateRecord_RequestSyntax) **   <a name="sagemaker-feature_store_UpdateRecord-request-RecordIdentifierValueAsString"></a>
The value that uniquely identifies the record in the feature group. This must match the value defined by the feature group's record identifier feature.
Type: String
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: Yes

 ** [TargetStores](#API_feature_store_UpdateRecord_RequestSyntax) **   <a name="sagemaker-feature_store_UpdateRecord-request-TargetStores"></a>
The target stores for the record update. By default, Amazon SageMaker Feature Store updates the record in all stores associated with the `FeatureGroup`. This list must include the `OnlineStore`, because `UpdateRecord` operates on the online store.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `OnlineStore | OfflineStore`
Required: No

 ** [TtlDuration](#API_feature_store_UpdateRecord_RequestSyntax) **   <a name="sagemaker-feature_store_UpdateRecord-request-TtlDuration"></a>
The time-to-live (TTL) duration for the record. Amazon SageMaker Feature Store deletes the record when `EventTime` \+ `TtlDuration` elapses. If you omit this parameter, the record's existing TTL setting remains unchanged. For information about `HardDelete`, see the [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html) operation in the Amazon SageMaker API Reference.
Type: [TtlDuration](API_feature_store_TtlDuration.md) object
Required: No

## Response Syntax
<a name="API_feature_store_UpdateRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_feature_store_UpdateRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_feature_store_UpdateRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessForbidden **
You do not have permission to perform an action.
HTTP Status Code: 403

 ** ConflictException **
The service rejected the update because the provided `EventTime` is older than the record's current `EventTime`. To persist the update, retrieve the record's latest `EventTime` and resubmit the request with an `EventTime` that is equal to or newer than the current value.
HTTP Status Code: 409

 ** InternalFailure **
An internal failure occurred. Try your request again. If the problem persists, contact AWS customer support.
HTTP Status Code: 500

 ** ResourceNotFound **
A resource that is required to perform an action was not found.
HTTP Status Code: 404

 ** ServiceUnavailable **
The service is currently unavailable.
HTTP Status Code: 503

 ** ValidationError **
There was an error validating your request.
HTTP Status Code: 400

## See Also
<a name="API_feature_store_UpdateRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-featurestore-runtime-2020-07-01/UpdateRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-featurestore-runtime-2020-07-01/UpdateRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/UpdateRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-featurestore-runtime-2020-07-01/UpdateRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/UpdateRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-featurestore-runtime-2020-07-01/UpdateRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-featurestore-runtime-2020-07-01/UpdateRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-featurestore-runtime-2020-07-01/UpdateRecord)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-featurestore-runtime-2020-07-01/UpdateRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/UpdateRecord)
