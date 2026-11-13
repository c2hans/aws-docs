---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ImportSnapshot.html
---

# ImportSnapshot
<a name="API_ImportSnapshot"></a>

Imports an Apache Flink savepoint from an Amazon S3 location as an enhanced snapshot. Managed Service for Apache Flink assumes the IAM role that you specify in `ImportSourceConfiguration` to read the savepoint data.

This operation is asynchronous. The response returns the snapshot ARN with the `CREATING` status. To track the progress of the import, use `DescribeSnapshotOperation`.

For more information, see [Import and export](https://docs.aws.amazon.com/managed-flink/latest/java/snapshots-import-export.html).

## Request Syntax
<a name="API_ImportSnapshot_RequestSyntax"></a>

```
{
   "DestinationEncryptionConfiguration": {
      "KeyId": "{{string}}",
      "KeyType": "{{string}}"
   },
   "ImportSourceConfiguration": {
      "ImportRoleArn": "{{string}}",
      "SourceEncryptionConfiguration": {
         "KeyId": "{{string}}",
         "KeyType": "{{string}}"
      },
      "SourceS3PrefixLocation": {
         "BucketARN": "{{string}}",
         "KeyPrefix": "{{string}}"
      },
      "SourceType": "{{string}}"
   },
   "SnapshotDescription": "{{string}}",
   "SnapshotFormat": "{{string}}",
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
<a name="API_ImportSnapshot_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DestinationEncryptionConfiguration](#API_ImportSnapshot_RequestSyntax) **   <a name="APIReference-ImportSnapshot-request-DestinationEncryptionConfiguration"></a>
The encryption configuration of the imported snapshot. If you don't specify this parameter, the snapshot is encrypted using a key of type `AWS_OWNED_KEY`. If you specify a KMS key, you must specify the key ARN.
Type: [SnapshotEncryptionConfiguration](API_SnapshotEncryptionConfiguration.md) object
Required: No

 ** [ImportSourceConfiguration](#API_ImportSnapshot_RequestSyntax) **   <a name="APIReference-ImportSnapshot-request-ImportSourceConfiguration"></a>
Describes the location, IAM role, and encryption configuration of the savepoint data to import.
Type: [ImportSourceConfiguration](API_ImportSourceConfiguration.md) object
Required: Yes

 ** [SnapshotDescription](#API_ImportSnapshot_RequestSyntax) **   <a name="APIReference-ImportSnapshot-request-SnapshotDescription"></a>
A summary description of the snapshot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\u0000-\u001F\u007F]*`
Required: No

 ** [SnapshotFormat](#API_ImportSnapshot_RequestSyntax) **   <a name="APIReference-ImportSnapshot-request-SnapshotFormat"></a>
The format of the snapshot being imported.
Type: String
Valid Values: `CANONICAL`
Required: No

 ** [SnapshotName](#API_ImportSnapshot_RequestSyntax) **   <a name="APIReference-ImportSnapshot-request-SnapshotName"></a>
The name of the enhanced snapshot. The name must be unique among the snapshots in your account and Region. You can't reuse the name of an existing snapshot, including a snapshot in the `FAILED` status, until you delete that snapshot. Names that begin with `SYSTEMSNAPSHOT` are reserved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Tags](#API_ImportSnapshot_RequestSyntax) **   <a name="APIReference-ImportSnapshot-request-Tags"></a>
A list of one or more tags to assign to the snapshot. A tag is a key-value pair that identifies a snapshot. For more information, see [Using Tagging](https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_ImportSnapshot_ResponseSyntax"></a>

```
{
   "SnapshotArn": "string",
   "SnapshotOperationId": "string",
   "SnapshotOperationStatus": "string",
   "SnapshotStatus": "string"
}
```

## Response Elements
<a name="API_ImportSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotArn](#API_ImportSnapshot_ResponseSyntax) **   <a name="APIReference-ImportSnapshot-response-SnapshotArn"></a>
The ARN of the enhanced snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [SnapshotOperationId](#API_ImportSnapshot_ResponseSyntax) **   <a name="APIReference-ImportSnapshot-response-SnapshotOperationId"></a>
The ID of the snapshot operation. You can use this value with `DescribeSnapshotOperation` to track the progress of the import.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [SnapshotOperationStatus](#API_ImportSnapshot_ResponseSyntax) **   <a name="APIReference-ImportSnapshot-response-SnapshotOperationStatus"></a>
The status of the snapshot operation.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | CANCELLED`

 ** [SnapshotStatus](#API_ImportSnapshot_ResponseSyntax) **   <a name="APIReference-ImportSnapshot-response-SnapshotStatus"></a>
The status of the snapshot. When Managed Service for Apache Flink accepts the request, the status is `CREATING`.
Type: String
Valid Values: `CREATING | READY | DELETING | FAILED`

## Errors
<a name="API_ImportSnapshot_Errors"></a>

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

 ** TooManyTagsException **
Application created with too many tags, or too many tags added to an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_ImportSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/ImportSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/ImportSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ImportSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/ImportSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ImportSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/ImportSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/ImportSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/ImportSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/ImportSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ImportSnapshot)
