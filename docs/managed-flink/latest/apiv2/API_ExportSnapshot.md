---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ExportSnapshot.html
---

# ExportSnapshot
<a name="API_ExportSnapshot"></a>

Exports the data of an enhanced snapshot to an Amazon S3 location. Managed Service for Apache Flink assumes the IAM role that you specify in `ExportDestinationConfiguration` to write the snapshot data. The snapshot must be in the `READY` status.

This operation is asynchronous. To track the progress of the export, use `DescribeSnapshotOperation`.

A snapshot can have only one export in progress at a time. If an export of the snapshot is already in progress, `LimitExceededException` is returned.

For more information, see [Import and export](https://docs.aws.amazon.com/managed-flink/latest/java/snapshots-import-export.html).

## Request Syntax
<a name="API_ExportSnapshot_RequestSyntax"></a>

```
{
   "ExportDestinationConfiguration": {
      "DestinationEncryptionConfiguration": {
         "KeyId": "{{string}}",
         "KeyType": "{{string}}"
      },
      "DestinationS3PrefixLocation": {
         "BucketARN": "{{string}}",
         "KeyPrefix": "{{string}}"
      },
      "DestinationType": "{{string}}",
      "ExportRoleArn": "{{string}}"
   },
   "SnapshotName": "{{string}}"
}
```

## Request Parameters
<a name="API_ExportSnapshot_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ExportDestinationConfiguration](#API_ExportSnapshot_RequestSyntax) **   <a name="APIReference-ExportSnapshot-request-ExportDestinationConfiguration"></a>
Describes the location, IAM role, and encryption configuration of the export destination.
Type: [ExportDestinationConfiguration](API_ExportDestinationConfiguration.md) object
Required: Yes

 ** [SnapshotName](#API_ExportSnapshot_RequestSyntax) **   <a name="APIReference-ExportSnapshot-request-SnapshotName"></a>
The name of the enhanced snapshot to export.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_ExportSnapshot_ResponseSyntax"></a>

```
{
   "SnapshotOperationId": "string",
   "SnapshotOperationStatus": "string"
}
```

## Response Elements
<a name="API_ExportSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotOperationId](#API_ExportSnapshot_ResponseSyntax) **   <a name="APIReference-ExportSnapshot-response-SnapshotOperationId"></a>
The ID of the snapshot operation. You can use this value with `DescribeSnapshotOperation` to track the progress of the export.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [SnapshotOperationStatus](#API_ExportSnapshot_ResponseSyntax) **   <a name="APIReference-ExportSnapshot-response-SnapshotOperationStatus"></a>
The status of the snapshot operation.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | CANCELLED`

## Errors
<a name="API_ExportSnapshot_Errors"></a>

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application or snapshot. This error can be the result of attempting to modify an application without using the current application ID.
HTTP Status Code: 400

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The number of allowed resources has been exceeded.
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
<a name="API_ExportSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/ExportSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/ExportSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ExportSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/ExportSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ExportSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/ExportSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/ExportSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/ExportSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/ExportSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ExportSnapshot)
