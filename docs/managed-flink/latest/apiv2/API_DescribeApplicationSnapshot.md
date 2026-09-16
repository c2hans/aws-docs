---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplicationSnapshot.html
---

# DescribeApplicationSnapshot
<a name="API_DescribeApplicationSnapshot"></a>

Returns information about a snapshot of application state data.

## Request Syntax
<a name="API_DescribeApplicationSnapshot_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "SnapshotName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeApplicationSnapshot_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_DescribeApplicationSnapshot_RequestSyntax) **   <a name="APIReference-DescribeApplicationSnapshot-request-ApplicationName"></a>
The name of an existing application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [SnapshotName](#API_DescribeApplicationSnapshot_RequestSyntax) **   <a name="APIReference-DescribeApplicationSnapshot-request-SnapshotName"></a>
The identifier of an application snapshot. You can retrieve this value using [ListApplicationSnapshots](API_ListApplicationSnapshots.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeApplicationSnapshot_ResponseSyntax"></a>

```
{
   "SnapshotDetails": {
      "ApplicationEncryptionConfigurationDescription": {
         "KeyId": "string",
         "KeyType": "string"
      },
      "ApplicationVersionId": number,
      "RuntimeEnvironment": "string",
      "SnapshotCreationTimestamp": number,
      "SnapshotName": "string",
      "SnapshotStatus": "string"
   }
}
```

## Response Elements
<a name="API_DescribeApplicationSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotDetails](#API_DescribeApplicationSnapshot_ResponseSyntax) **   <a name="APIReference-DescribeApplicationSnapshot-response-SnapshotDetails"></a>
An object containing information about the application snapshot.
Type: [SnapshotDetails](API_SnapshotDetails.md) object

## Errors
<a name="API_DescribeApplicationSnapshot_Errors"></a>

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_DescribeApplicationSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DescribeApplicationSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DescribeApplicationSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DescribeApplicationSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DescribeApplicationSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DescribeApplicationSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DescribeApplicationSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DescribeApplicationSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DescribeApplicationSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DescribeApplicationSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DescribeApplicationSnapshot)
