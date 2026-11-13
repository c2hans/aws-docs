---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeSnapshotOperation.html
---

# DescribeSnapshotOperation
<a name="API_DescribeSnapshotOperation"></a>

Provides a detailed description of a specified operation that was performed on an enhanced snapshot. To see a list of the operations of a snapshot, use `ListSnapshotOperations`.

Snapshot operations are available for 90 days after they are created.

## Request Syntax
<a name="API_DescribeSnapshotOperation_RequestSyntax"></a>

```
{
   "SnapshotName": "{{string}}",
   "SnapshotOperationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSnapshotOperation_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [SnapshotName](#API_DescribeSnapshotOperation_RequestSyntax) **   <a name="APIReference-DescribeSnapshotOperation-request-SnapshotName"></a>
The name of the enhanced snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [SnapshotOperationId](#API_DescribeSnapshotOperation_RequestSyntax) **   <a name="APIReference-DescribeSnapshotOperation-request-SnapshotOperationId"></a>
The ID of the snapshot operation. You can retrieve this value using `ListSnapshotOperations`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_DescribeSnapshotOperation_ResponseSyntax"></a>

```
{
   "SnapshotOperationInfoDetails": {
      "ApplicationOperationDescription": {
         "ApplicationName": "string",
         "ApplicationOperationId": "string"
      },
      "DestinationEncryptionConfigurationDescription": {
         "KeyId": "string",
         "KeyType": "string"
      },
      "EndTime": number,
      "SnapshotArn": "string",
      "SnapshotDestinationLocationDescription": {
         "LocationType": "string",
         "S3PrefixLocation": {
            "BucketARN": "string",
            "ExportedPrefix": "string",
            "KeyPrefix": "string"
         }
      },
      "SnapshotOperation": "string",
      "SnapshotOperationFailureDetails": {
         "ErrorInfo": {
            "ErrorCode": "string",
            "ErrorString": "string"
         }
      },
      "SnapshotOperationId": "string",
      "SnapshotOperationStatus": "string",
      "SnapshotSourceLocationDescription": {
         "LocationType": "string",
         "S3PrefixLocation": {
            "BucketARN": "string",
            "ExportedPrefix": "string",
            "KeyPrefix": "string"
         }
      },
      "SourceEncryptionConfigurationDescription": {
         "KeyId": "string",
         "KeyType": "string"
      },
      "StartTime": number
   }
}
```

## Response Elements
<a name="API_DescribeSnapshotOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotOperationInfoDetails](#API_DescribeSnapshotOperation_ResponseSyntax) **   <a name="APIReference-DescribeSnapshotOperation-response-SnapshotOperationInfoDetails"></a>
An object containing information about the snapshot operation.
Type: [SnapshotOperationInfoDetails](API_SnapshotOperationInfoDetails.md) object

## Errors
<a name="API_DescribeSnapshotOperation_Errors"></a>

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified application, snapshot, or snapshot operation can't be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSnapshotOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DescribeSnapshotOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DescribeSnapshotOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DescribeSnapshotOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DescribeSnapshotOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DescribeSnapshotOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DescribeSnapshotOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DescribeSnapshotOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DescribeSnapshotOperation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DescribeSnapshotOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DescribeSnapshotOperation)
