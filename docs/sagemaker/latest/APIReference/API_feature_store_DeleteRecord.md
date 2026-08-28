---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html
---

# DeleteRecord
<a name="API_feature_store_DeleteRecord"></a>

Deletes a `Record` from a `FeatureGroup` in the `OnlineStore`. Feature Store supports both `SoftDelete` and `HardDelete`. For `SoftDelete` (default), feature columns are set to `null` and the record is no longer retrievable by `GetRecord` or `BatchGetRecord`. For `HardDelete`, the complete `Record` is removed from the `OnlineStore`. In both cases, Feature Store appends the deleted record marker to the `OfflineStore`. The deleted record marker is a record with the same `RecordIdentifer` as the original, but with `is_deleted` value set to `True`, `EventTime` set to the delete input `EventTime`, and other feature values set to `null`.

Note that the `EventTime` specified in `DeleteRecord` should be set later than the `EventTime` of the existing record in the `OnlineStore` for that `RecordIdentifer`. If it is not, the deletion does not occur:
+ For `SoftDelete`, the existing (not deleted) record remains in the `OnlineStore`, though the delete record marker is still written to the `OfflineStore`.
+  `HardDelete` returns `EventTime`: `400 ValidationException` to indicate that the delete operation failed. No delete record marker is written to the `OfflineStore`.

When a record is deleted from the `OnlineStore`, the deleted record marker is appended to the `OfflineStore`. If you have the Iceberg table format enabled for your `OfflineStore`, you can remove all history of a record from the `OfflineStore` using Amazon Athena or Apache Spark. For information on how to hard delete a record from the `OfflineStore` with the Iceberg table format enabled, see [Delete records from the offline store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-delete-records.html#feature-store-delete-records-offline-store).

## Request Syntax
<a name="API_feature_store_DeleteRecord_RequestSyntax"></a>

```
DELETE /FeatureGroup/{{FeatureGroupName}}?DeletionMode={{DeletionMode}}&EventTime={{EventTime}}&RecordIdentifierValueAsString={{RecordIdentifierValueAsString}}&TargetStores={{TargetStores}} HTTP/1.1
```

## URI Request Parameters
<a name="API_feature_store_DeleteRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeletionMode](#API_feature_store_DeleteRecord_RequestSyntax) **   <a name="sagemaker-feature_store_DeleteRecord-request-uri-DeletionMode"></a>
The name of the deletion mode for deleting the record. By default, the deletion mode is set to `SoftDelete`.
Valid Values: `SoftDelete | HardDelete`

 ** [EventTime](#API_feature_store_DeleteRecord_RequestSyntax) **   <a name="sagemaker-feature_store_DeleteRecord-request-uri-EventTime"></a>
Timestamp indicating when the deletion event occurred. `EventTime` can be used to query data at a certain point in time.
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: Yes

 ** [FeatureGroupName](#API_feature_store_DeleteRecord_RequestSyntax) **   <a name="sagemaker-feature_store_DeleteRecord-request-uri-FeatureGroupName"></a>
The name or Amazon Resource Name (ARN) of the feature group to delete the record from.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/)?([a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63})`
Required: Yes

 ** [RecordIdentifierValueAsString](#API_feature_store_DeleteRecord_RequestSyntax) **   <a name="sagemaker-feature_store_DeleteRecord-request-uri-RecordIdentifierValueAsString"></a>
The value for the `RecordIdentifier` that uniquely identifies the record, in string format.
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: Yes

 ** [TargetStores](#API_feature_store_DeleteRecord_RequestSyntax) **   <a name="sagemaker-feature_store_DeleteRecord-request-uri-TargetStores"></a>
A list of stores from which you're deleting the record. By default, Feature Store deletes the record from all of the stores that you're using for the `FeatureGroup`.
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `OnlineStore | OfflineStore`

## Request Body
<a name="API_feature_store_DeleteRecord_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_feature_store_DeleteRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_feature_store_DeleteRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_feature_store_DeleteRecord_Errors"></a>

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
<a name="API_feature_store_DeleteRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-featurestore-runtime-2020-07-01/DeleteRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-featurestore-runtime-2020-07-01/DeleteRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/DeleteRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-featurestore-runtime-2020-07-01/DeleteRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/DeleteRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-featurestore-runtime-2020-07-01/DeleteRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-featurestore-runtime-2020-07-01/DeleteRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-featurestore-runtime-2020-07-01/DeleteRecord)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-featurestore-runtime-2020-07-01/DeleteRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/DeleteRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
