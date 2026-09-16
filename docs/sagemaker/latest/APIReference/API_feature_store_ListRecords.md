---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_ListRecords.html
---

# ListRecords
<a name="API_feature_store_ListRecords"></a>

Lists the `RecordIdentifier` values of all records stored in a `FeatureGroup`'s `OnlineStore`. This enables you to discover which records exist without retrieving the full record data.

## Request Syntax
<a name="API_feature_store_ListRecords_RequestSyntax"></a>

```
POST /FeatureGroup/{{FeatureGroupName}}/ListRecords HTTP/1.1
Content-type: application/json

{
   "IncludeSoftDeletedRecords": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_feature_store_ListRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FeatureGroupName](#API_feature_store_ListRecords_RequestSyntax) **   <a name="sagemaker-feature_store_ListRecords-request-uri-FeatureGroupName"></a>
The name or Amazon Resource Name (ARN) of the feature group to list records from.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/)?([a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63})`
Required: Yes

## Request Body
<a name="API_feature_store_ListRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IncludeSoftDeletedRecords](#API_feature_store_ListRecords_RequestSyntax) **   <a name="sagemaker-feature_store_ListRecords-request-IncludeSoftDeletedRecords"></a>
If set to `true`, the result includes records that have been soft deleted.
Type: Boolean
Required: No

 ** [MaxResults](#API_feature_store_ListRecords_RequestSyntax) **   <a name="sagemaker-feature_store_ListRecords-request-MaxResults"></a>
The maximum number of record identifiers to return in a single page of results. For the `InMemory` tier, this value is a hint and not a strict requirement. The response may contain more or fewer results than the specified `MaxResults`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_feature_store_ListRecords_RequestSyntax) **   <a name="sagemaker-feature_store_ListRecords-request-NextToken"></a>
A token to resume pagination of `ListRecords` results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_feature_store_ListRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RecordIdentifiers": [ "string" ]
}
```

## Response Elements
<a name="API_feature_store_ListRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_feature_store_ListRecords_ResponseSyntax) **   <a name="sagemaker-feature_store_ListRecords-response-NextToken"></a>
A token to resume pagination if the response includes more record identifiers than `MaxResults`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [RecordIdentifiers](#API_feature_store_ListRecords_ResponseSyntax) **   <a name="sagemaker-feature_store_ListRecords-response-RecordIdentifiers"></a>
A list of record identifier values for the records stored in the `OnlineStore`.
Type: Array of strings
Length Constraints: Maximum length of 358400.
Pattern: `.*`

## Errors
<a name="API_feature_store_ListRecords_Errors"></a>

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
<a name="API_feature_store_ListRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-featurestore-runtime-2020-07-01/ListRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-featurestore-runtime-2020-07-01/ListRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/ListRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-featurestore-runtime-2020-07-01/ListRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/ListRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-featurestore-runtime-2020-07-01/ListRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-featurestore-runtime-2020-07-01/ListRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-featurestore-runtime-2020-07-01/ListRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-featurestore-runtime-2020-07-01/ListRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/ListRecords)
