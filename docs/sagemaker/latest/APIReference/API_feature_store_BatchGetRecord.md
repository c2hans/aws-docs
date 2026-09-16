---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchGetRecord.html
---

# BatchGetRecord
<a name="API_feature_store_BatchGetRecord"></a>

Retrieves a batch of `Records` from a `FeatureGroup`.

## Request Syntax
<a name="API_feature_store_BatchGetRecord_RequestSyntax"></a>

```
POST /BatchGetRecord HTTP/1.1
Content-type: application/json

{
   "ExpirationTimeResponse": "{{string}}",
   "Identifiers": [
      {
         "FeatureGroupName": "{{string}}",
         "FeatureNames": [ "{{string}}" ],
         "RecordIdentifiersValueAsString": [ "{{string}}" ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_feature_store_BatchGetRecord_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_feature_store_BatchGetRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ExpirationTimeResponse](#API_feature_store_BatchGetRecord_RequestSyntax) **   <a name="sagemaker-feature_store_BatchGetRecord-request-ExpirationTimeResponse"></a>
Parameter to request `ExpiresAt` in response. If `Enabled`, `BatchGetRecord` will return the value of `ExpiresAt`, if it is not null. If `Disabled` and null, `BatchGetRecord` will return null.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** [Identifiers](#API_feature_store_BatchGetRecord_RequestSyntax) **   <a name="sagemaker-feature_store_BatchGetRecord-request-Identifiers"></a>
A list containing the name or Amazon Resource Name (ARN) of the `FeatureGroup`, the list of names of `Feature`s to be retrieved, and the corresponding `RecordIdentifier` values as strings.
Type: Array of [BatchGetRecordIdentifier](API_feature_store_BatchGetRecordIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_feature_store_BatchGetRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "FeatureGroupName": "string",
         "RecordIdentifierValueAsString": "string"
      }
   ],
   "Records": [
      {
         "ExpiresAt": "string",
         "FeatureGroupName": "string",
         "Record": [
            {
               "FeatureName": "string",
               "ValueAsString": "string",
               "ValueAsStringList": [ "string" ]
            }
         ],
         "RecordIdentifierValueAsString": "string"
      }
   ],
   "UnprocessedIdentifiers": [
      {
         "FeatureGroupName": "string",
         "FeatureNames": [ "string" ],
         "RecordIdentifiersValueAsString": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_feature_store_BatchGetRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_feature_store_BatchGetRecord_ResponseSyntax) **   <a name="sagemaker-feature_store_BatchGetRecord-response-Errors"></a>
A list of errors that have occurred when retrieving a batch of Records.
Type: Array of [BatchGetRecordError](API_feature_store_BatchGetRecordError.md) objects
Array Members: Minimum number of 0 items.

 ** [Records](#API_feature_store_BatchGetRecord_ResponseSyntax) **   <a name="sagemaker-feature_store_BatchGetRecord-response-Records"></a>
A list of Records you requested to be retrieved in batch.
Type: Array of [BatchGetRecordResultDetail](API_feature_store_BatchGetRecordResultDetail.md) objects
Array Members: Minimum number of 0 items.

 ** [UnprocessedIdentifiers](#API_feature_store_BatchGetRecord_ResponseSyntax) **   <a name="sagemaker-feature_store_BatchGetRecord-response-UnprocessedIdentifiers"></a>
A unprocessed list of `FeatureGroup` names, with their corresponding `RecordIdentifier` value, and Feature name.
Type: Array of [BatchGetRecordIdentifier](API_feature_store_BatchGetRecordIdentifier.md) objects
Array Members: Minimum number of 0 items.

## Errors
<a name="API_feature_store_BatchGetRecord_Errors"></a>

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
<a name="API_feature_store_BatchGetRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecord)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecord)
