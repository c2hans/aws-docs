---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateSnapshot.html
---

# CreateSnapshot
<a name="API_CreateSnapshot"></a>

Creates an enhanced snapshot of the state data of a running Managed Service for Apache Flink application. The application must be in the `RUNNING` status, use Apache Flink version 1.20 or later, and use the `ENHANCED_SNAPSHOTS` snapshot mode.

This operation is asynchronous. The response returns the snapshot ARN with the `CREATING` status. To check the status of the snapshot, use `DescribeSnapshot`. To track the progress of the operation, use `DescribeSnapshotOperation`.

An application can have only one `CreateSnapshot` operation in progress at a time. For information about limits, see [Managed Service for Apache Flink Quotas](https://docs.aws.amazon.com/managed-flink/latest/java/limits.html). For more information about snapshots, see [Enhanced Snapshots](https://docs.aws.amazon.com/managed-flink/latest/java/how-snapshots.html).

## Request Syntax
<a name="API_CreateSnapshot_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "SnapshotDescription": "{{string}}",
   "SnapshotName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateSnapshot_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_CreateSnapshot_RequestSyntax) **   <a name="APIReference-CreateSnapshot-request-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [SnapshotDescription](#API_CreateSnapshot_RequestSyntax) **   <a name="APIReference-CreateSnapshot-request-SnapshotDescription"></a>
A summary description of the snapshot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\u0000-\u001F\u007F]*`
Required: No

 ** [SnapshotName](#API_CreateSnapshot_RequestSyntax) **   <a name="APIReference-CreateSnapshot-request-SnapshotName"></a>
The name of the enhanced snapshot. The name must be unique among the snapshots in your account and Region. You can't reuse the name of an existing snapshot, including a snapshot in the `FAILED` status, until you delete that snapshot. Names that begin with `SYSTEMSNAPSHOT` are reserved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Tags](#API_CreateSnapshot_RequestSyntax) **   <a name="APIReference-CreateSnapshot-request-Tags"></a>
A list of one or more tags to assign to the snapshot. A tag is a key-value pair that identifies a snapshot. For more information, see [Using Tagging](https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateSnapshot_ResponseSyntax"></a>

```
{
   "SnapshotArn": "string",
   "SnapshotOperationId": "string",
   "SnapshotOperationStatus": "string",
   "SnapshotStatus": "string"
}
```

## Response Elements
<a name="API_CreateSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotArn](#API_CreateSnapshot_ResponseSyntax) **   <a name="APIReference-CreateSnapshot-response-SnapshotArn"></a>
The ARN of the enhanced snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [SnapshotOperationId](#API_CreateSnapshot_ResponseSyntax) **   <a name="APIReference-CreateSnapshot-response-SnapshotOperationId"></a>
The ID of the snapshot operation. You can use this value with `DescribeSnapshotOperation` to track the progress of the operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [SnapshotOperationStatus](#API_CreateSnapshot_ResponseSyntax) **   <a name="APIReference-CreateSnapshot-response-SnapshotOperationStatus"></a>
The status of the snapshot operation.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | CANCELLED`

 ** [SnapshotStatus](#API_CreateSnapshot_ResponseSyntax) **   <a name="APIReference-CreateSnapshot-response-SnapshotStatus"></a>
The status of the snapshot. When Managed Service for Apache Flink accepts the request, the status is `CREATING`.
Type: String
Valid Values: `CREATING | READY | DELETING | FAILED`

## Errors
<a name="API_CreateSnapshot_Errors"></a>

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application or snapshot. This error can be the result of attempting to modify an application without using the current application ID.
HTTP Status Code: 400

 ** InvalidApplicationConfigurationException **
The user-provided application configuration is not valid.
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

 ** TooManyTagsException **
Application created with too many tags, or too many tags added to an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_CreateSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/CreateSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/CreateSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CreateSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/CreateSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CreateSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/CreateSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/CreateSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/CreateSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/CreateSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CreateSnapshot)
