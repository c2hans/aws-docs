---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_GetRecord.html
---

# GetRecord
<a name="API_feature_store_GetRecord"></a>

Use for `OnlineStore` serving from a `FeatureStore`. Only the latest records stored in the `OnlineStore` can be retrieved. If no Record with `RecordIdentifierValue` is found, then an empty result is returned.

## Request Syntax
<a name="API_feature_store_GetRecord_RequestSyntax"></a>

```
GET /FeatureGroup/{{FeatureGroupName}}?ExpirationTimeResponse={{ExpirationTimeResponse}}&FeatureName={{FeatureNames}}&RecordIdentifierValueAsString={{RecordIdentifierValueAsString}} HTTP/1.1
```

## URI Request Parameters
<a name="API_feature_store_GetRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExpirationTimeResponse](#API_feature_store_GetRecord_RequestSyntax) **   <a name="sagemaker-feature_store_GetRecord-request-uri-ExpirationTimeResponse"></a>
Parameter to request `ExpiresAt` in response. If `Enabled`, `GetRecord` will return the value of `ExpiresAt`, if it is not null. If `Disabled` and null, `GetRecord` will return null.
Valid Values: `Enabled | Disabled`

 ** [FeatureGroupName](#API_feature_store_GetRecord_RequestSyntax) **   <a name="sagemaker-feature_store_GetRecord-request-uri-FeatureGroupName"></a>
The name or Amazon Resource Name (ARN) of the feature group from which you want to retrieve a record.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/)?([a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63})`
Required: Yes

 ** [FeatureNames](#API_feature_store_GetRecord_RequestSyntax) **   <a name="sagemaker-feature_store_GetRecord-request-uri-FeatureNames"></a>
List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned.
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`

 ** [RecordIdentifierValueAsString](#API_feature_store_GetRecord_RequestSyntax) **   <a name="sagemaker-feature_store_GetRecord-request-uri-RecordIdentifierValueAsString"></a>
The value that corresponds to `RecordIdentifier` type and uniquely identifies the record in the `FeatureGroup`.
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: Yes

## Request Body
<a name="API_feature_store_GetRecord_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_feature_store_GetRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ExpiresAt": "string",
   "Record": [
      {
         "FeatureName": "string",
         "ValueAsString": "string",
         "ValueAsStringList": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_feature_store_GetRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExpiresAt](#API_feature_store_GetRecord_ResponseSyntax) **   <a name="sagemaker-feature_store_GetRecord-response-ExpiresAt"></a>
The `ExpiresAt` ISO string of the requested record.
Type: String

 ** [Record](#API_feature_store_GetRecord_ResponseSyntax) **   <a name="sagemaker-feature_store_GetRecord-response-Record"></a>
The record you requested. A list of `FeatureValues`.
Type: Array of [FeatureValue](API_feature_store_FeatureValue.md) objects
Array Members: Minimum number of 1 item.

## Errors
<a name="API_feature_store_GetRecord_Errors"></a>

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
<a name="API_feature_store_GetRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-featurestore-runtime-2020-07-01/GetRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-featurestore-runtime-2020-07-01/GetRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/GetRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-featurestore-runtime-2020-07-01/GetRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/GetRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-featurestore-runtime-2020-07-01/GetRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-featurestore-runtime-2020-07-01/GetRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-featurestore-runtime-2020-07-01/GetRecord)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-featurestore-runtime-2020-07-01/GetRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/GetRecord)
