---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_PutRecord.html
---

# PutRecord
<a name="API_feature_store_PutRecord"></a>

The `PutRecord` API is used to ingest a list of `Records` into your feature group.

If a new record’s `EventTime` is greater, the new record is written to both the `OnlineStore` and `OfflineStore`. Otherwise, the record is a historic record and it is written only to the `OfflineStore`.

You can specify the ingestion to be applied to the `OnlineStore`, `OfflineStore`, or both by using the `TargetStores` request parameter.

You can set the ingested record to expire at a given time to live (TTL) duration after the record’s event time, `ExpiresAt` = `EventTime` \+ `TtlDuration`, by specifying the `TtlDuration` parameter. A record level `TtlDuration` is set when specifying the `TtlDuration` parameter using the `PutRecord` API call. If the input `TtlDuration` is `null` or unspecified, `TtlDuration` is set to the default feature group level `TtlDuration`. A record level `TtlDuration` supersedes the group level `TtlDuration`.

## Request Syntax
<a name="API_feature_store_PutRecord_RequestSyntax"></a>

```
PUT /FeatureGroup/{{FeatureGroupName}} HTTP/1.1
Content-type: application/json

{
   "Record": [
      {
         "FeatureName": "{{string}}",
         "ValueAsString": "{{string}}",
         "ValueAsStringList": [ "{{string}}" ]
      }
   ],
   "TargetStores": [ "{{string}}" ],
   "TtlDuration": {
      "Unit": "{{string}}",
      "Value": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_feature_store_PutRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FeatureGroupName](#API_feature_store_PutRecord_RequestSyntax) **   <a name="sagemaker-feature_store_PutRecord-request-uri-FeatureGroupName"></a>
The name or Amazon Resource Name (ARN) of the feature group that you want to insert the record into.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/)?([a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63})`
Required: Yes

## Request Body
<a name="API_feature_store_PutRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Record](#API_feature_store_PutRecord_RequestSyntax) **   <a name="sagemaker-feature_store_PutRecord-request-Record"></a>
A list of FeatureValues to insert. This is a full overwrite. To update individual feature values without overwriting the entire record, use the [UpdateRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_UpdateRecord.html) operation.
Type: Array of [FeatureValue](API_feature_store_FeatureValue.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [TargetStores](#API_feature_store_PutRecord_RequestSyntax) **   <a name="sagemaker-feature_store_PutRecord-request-TargetStores"></a>
A list of stores to which you're adding the record. By default, Feature Store adds the record to all of the stores that you're using for the `FeatureGroup`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `OnlineStore | OfflineStore`
Required: No

 ** [TtlDuration](#API_feature_store_PutRecord_RequestSyntax) **   <a name="sagemaker-feature_store_PutRecord-request-TtlDuration"></a>
Time to live duration, where the record is hard deleted after the expiration time is reached; `ExpiresAt` = `EventTime` \+ `TtlDuration`. For information on HardDelete, see the [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html) API in the Amazon SageMaker API Reference guide.
Type: [TtlDuration](API_feature_store_TtlDuration.md) object
Required: No

## Response Syntax
<a name="API_feature_store_PutRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_feature_store_PutRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_feature_store_PutRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessForbidden **
You do not have permission to perform an action.
HTTP Status Code: 403

 ** InternalFailure **
An internal failure occurred. Try your request again. If the problem persists, contact AWS customer support.
HTTP Status Code: 500

 ** ServiceUnavailable **
The service is currently unavailable.
HTTP Status Code: 503

 ** ValidationError **
There was an error validating your request.
HTTP Status Code: 400

## See Also
<a name="API_feature_store_PutRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-featurestore-runtime-2020-07-01/PutRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-featurestore-runtime-2020-07-01/PutRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/PutRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-featurestore-runtime-2020-07-01/PutRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/PutRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-featurestore-runtime-2020-07-01/PutRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-featurestore-runtime-2020-07-01/PutRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-featurestore-runtime-2020-07-01/PutRecord)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-featurestore-runtime-2020-07-01/PutRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/PutRecord)
