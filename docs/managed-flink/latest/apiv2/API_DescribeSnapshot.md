---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeSnapshot.html
---

# DescribeSnapshot
<a name="API_DescribeSnapshot"></a>

Returns information about an enhanced snapshot. To see a list of the snapshots in your account, use `ListSnapshots`.

## Request Syntax
<a name="API_DescribeSnapshot_RequestSyntax"></a>

```
{
   "SnapshotName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSnapshot_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [SnapshotName](#API_DescribeSnapshot_RequestSyntax) **   <a name="APIReference-DescribeSnapshot-request-SnapshotName"></a>
The name of the enhanced snapshot. You can retrieve this value using `ListSnapshots`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeSnapshot_ResponseSyntax"></a>

```
{
   "SnapshotInfoDetails": {
      "RuntimeEnvironment": "string",
      "SnapshotArn": "string",
      "SnapshotCreationTimestamp": number,
      "SnapshotDescription": "string",
      "SnapshotEncryptionConfigurationDescription": {
         "KeyId": "string",
         "KeyType": "string"
      },
      "SnapshotFormat": "string",
      "SnapshotInitiator": "string",
      "SnapshotInitiatorOperation": "string",
      "SnapshotName": "string",
      "SnapshotSizeInBytes": number,
      "SnapshotSourceDescription": {
         "S3PrefixLocation": {
            "BucketARN": "string",
            "KeyPrefix": "string"
         },
         "SourceApplicationDescription": {
            "ApplicationCreationTimestamp": number,
            "ApplicationName": "string",
            "ApplicationVersionId": number
         }
      },
      "SnapshotStatus": "string"
   }
}
```

## Response Elements
<a name="API_DescribeSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotInfoDetails](#API_DescribeSnapshot_ResponseSyntax) **   <a name="APIReference-DescribeSnapshot-response-SnapshotInfoDetails"></a>
An object containing information about the enhanced snapshot.
Type: [SnapshotInfoDetails](API_SnapshotInfoDetails.md) object

## Errors
<a name="API_DescribeSnapshot_Errors"></a>

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
<a name="API_DescribeSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DescribeSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DescribeSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DescribeSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DescribeSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DescribeSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DescribeSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DescribeSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DescribeSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DescribeSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DescribeSnapshot)
