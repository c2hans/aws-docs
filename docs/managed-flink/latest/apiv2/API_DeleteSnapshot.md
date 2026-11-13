---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteSnapshot.html
---

# DeleteSnapshot
<a name="API_DeleteSnapshot"></a>

Deletes an enhanced snapshot. Snapshots are not scoped to an application, so you can delete a snapshot independently of the application that it was created from.

This operation is asynchronous. The response returns the snapshot ARN with the `DELETING` status. To track the progress of the operation, use `DescribeSnapshotOperation`.

You can delete a snapshot in the `READY` or `FAILED` status. If a snapshot operation, such as an export, uses the snapshot, Managed Service for Apache Flink waits for that operation to finish before it deletes the snapshot. For a snapshot in any other status, `ResourceInUseException` is returned.

## Request Syntax
<a name="API_DeleteSnapshot_RequestSyntax"></a>

```
{
   "SnapshotCreationTimestamp": {{number}},
   "SnapshotName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSnapshot_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [SnapshotCreationTimestamp](#API_DeleteSnapshot_RequestSyntax) **   <a name="APIReference-DeleteSnapshot-request-SnapshotCreationTimestamp"></a>
The creation timestamp of the enhanced snapshot to delete. Use the `DescribeSnapshot` operation to get this value.
Type: Timestamp
Required: Yes

 ** [SnapshotName](#API_DeleteSnapshot_RequestSyntax) **   <a name="APIReference-DeleteSnapshot-request-SnapshotName"></a>
The name of the enhanced snapshot to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteSnapshot_ResponseSyntax"></a>

```
{
   "SnapshotArn": "string",
   "SnapshotOperationId": "string",
   "SnapshotOperationStatus": "string",
   "SnapshotStatus": "string"
}
```

## Response Elements
<a name="API_DeleteSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotArn](#API_DeleteSnapshot_ResponseSyntax) **   <a name="APIReference-DeleteSnapshot-response-SnapshotArn"></a>
The ARN of the enhanced snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [SnapshotOperationId](#API_DeleteSnapshot_ResponseSyntax) **   <a name="APIReference-DeleteSnapshot-response-SnapshotOperationId"></a>
The ID of the snapshot operation. You can use this value with `DescribeSnapshotOperation` to track the progress of the operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [SnapshotOperationStatus](#API_DeleteSnapshot_ResponseSyntax) **   <a name="APIReference-DeleteSnapshot-response-SnapshotOperationStatus"></a>
The status of the snapshot operation.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | CANCELLED`

 ** [SnapshotStatus](#API_DeleteSnapshot_ResponseSyntax) **   <a name="APIReference-DeleteSnapshot-response-SnapshotStatus"></a>
The status of the snapshot. When Managed Service for Apache Flink accepts the request, the status is `DELETING`. If a snapshot operation, such as an export, uses the snapshot, the status stays `DELETING` until that operation finishes and Managed Service for Apache Flink deletes the snapshot.
Type: String
Valid Values: `CREATING | READY | DELETING | FAILED`

## Errors
<a name="API_DeleteSnapshot_Errors"></a>

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application or snapshot. This error can be the result of attempting to modify an application without using the current application ID.
HTTP Status Code: 400

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** ResourceInUseException **
The application or snapshot is not available for this operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified application, snapshot, or snapshot operation can't be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DeleteSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DeleteSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DeleteSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DeleteSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DeleteSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DeleteSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DeleteSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DeleteSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DeleteSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DeleteSnapshot)
