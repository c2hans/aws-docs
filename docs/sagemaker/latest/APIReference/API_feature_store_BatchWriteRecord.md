---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchWriteRecord.html
---

# BatchWriteRecord
<a name="API_feature_store_BatchWriteRecord"></a>

Writes a batch of `Records` to one or more `FeatureGroup`s. Use this API for bulk ingestion of records into the `OnlineStore` and `OfflineStore`.

You can set the ingested records to expire at a given time to live (TTL) duration after the record's event time by specifying the `TtlDuration` parameter. A request level `TtlDuration` applies to all entries that do not specify their own `TtlDuration`.

## Request Syntax
<a name="API_feature_store_BatchWriteRecord_RequestSyntax"></a>

```
POST /BatchWriteRecord HTTP/1.1
Content-type: application/json

{
   "Entries": [
      {
         "FeatureGroupName": "{{string}}",
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
   ],
   "TtlDuration": {
      "Unit": "{{string}}",
      "Value": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_feature_store_BatchWriteRecord_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_feature_store_BatchWriteRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Entries](#API_feature_store_BatchWriteRecord_RequestSyntax) **   <a name="sagemaker-feature_store_BatchWriteRecord-request-Entries"></a>
A list of records to write. Each entry specifies the `FeatureGroup`, the record data, and optionally target stores and a TTL duration.
Type: Array of [BatchWriteRecordEntry](API_feature_store_BatchWriteRecordEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

 ** [TtlDuration](#API_feature_store_BatchWriteRecord_RequestSyntax) **   <a name="sagemaker-feature_store_BatchWriteRecord-request-TtlDuration"></a>
Time to live duration applied to all entries in the batch that do not specify their own `TtlDuration`; `ExpiresAt` = `EventTime` \+ `TtlDuration`. For information on HardDelete, see the [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html) API in the Amazon SageMaker API Reference guide.
Type: [TtlDuration](API_feature_store_TtlDuration.md) object
Required: No

## Response Syntax
<a name="API_feature_store_BatchWriteRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "Entry": {
            "FeatureGroupName": "string",
            "Record": [
               {
                  "FeatureName": "string",
                  "ValueAsString": "string",
                  "ValueAsStringList": [ "string" ]
               }
            ],
            "TargetStores": [ "string" ],
            "TtlDuration": {
               "Unit": "string",
               "Value": number
            }
         },
         "ErrorCode": "string",
         "ErrorMessage": "string"
      }
   ],
   "UnprocessedEntries": [
      {
         "FeatureGroupName": "string",
         "Record": [
            {
               "FeatureName": "string",
               "ValueAsString": "string",
               "ValueAsStringList": [ "string" ]
            }
         ],
         "TargetStores": [ "string" ],
         "TtlDuration": {
            "Unit": "string",
            "Value": number
         }
      }
   ]
}
```

## Response Elements
<a name="API_feature_store_BatchWriteRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_feature_store_BatchWriteRecord_ResponseSyntax) **   <a name="sagemaker-feature_store_BatchWriteRecord-response-Errors"></a>
A list of errors that occurred when writing records in the batch.
Type: Array of [BatchWriteRecordError](API_feature_store_BatchWriteRecordError.md) objects
Array Members: Minimum number of 0 items.

 ** [UnprocessedEntries](#API_feature_store_BatchWriteRecord_ResponseSyntax) **   <a name="sagemaker-feature_store_BatchWriteRecord-response-UnprocessedEntries"></a>
A list of entries that were not processed. These entries can be retried.
Type: Array of [BatchWriteRecordEntry](API_feature_store_BatchWriteRecordEntry.md) objects
Array Members: Minimum number of 0 items.

## Errors
<a name="API_feature_store_BatchWriteRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessForbidden **
You do not have permission to perform an action.
HTTP Status Code: 403

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
<a name="API_feature_store_BatchWriteRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecord)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecord)
