---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListSnapshots.html
---

# ListSnapshots
<a name="API_ListSnapshots"></a>

Lists the enhanced snapshots in your account. Snapshots are not scoped to an application. To list the snapshots that were created from a specific application, use the `SourceApplicationName` parameter.

You can specify only one of the following filters in a request: `SourceApplicationName`, `SnapshotInitiator`, `SnapshotInitiatorOperation`, or `SnapshotStatus`. If you specify more than one filter, `InvalidArgumentException` is returned.

The results are sorted in descending order of snapshot creation timestamp. To get detailed information about a specific snapshot, use `DescribeSnapshot`.

## Request Syntax
<a name="API_ListSnapshots_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "SnapshotInitiator": "{{string}}",
   "SnapshotInitiatorOperation": "{{string}}",
   "SnapshotStatus": "{{string}}",
   "SourceApplicationName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSnapshots_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Limit](#API_ListSnapshots_RequestSyntax) **   <a name="APIReference-ListSnapshots-request-Limit"></a>
The maximum number of snapshots to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListSnapshots_RequestSyntax) **   <a name="APIReference-ListSnapshots-request-NextToken"></a>
A pagination token that can be used in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [SnapshotInitiator](#API_ListSnapshots_RequestSyntax) **   <a name="APIReference-ListSnapshots-request-SnapshotInitiator"></a>
Use this parameter to list only the snapshots with the specified initiator.
Type: String
Valid Values: `USER | SYSTEM`
Required: No

 ** [SnapshotInitiatorOperation](#API_ListSnapshots_RequestSyntax) **   <a name="APIReference-ListSnapshots-request-SnapshotInitiatorOperation"></a>
Use this parameter to list only the snapshots that were created by the specified operation.
Type: String
Valid Values: `CreateSnapshot | ImportSnapshot | SystemCreateSnapshot`
Required: No

 ** [SnapshotStatus](#API_ListSnapshots_RequestSyntax) **   <a name="APIReference-ListSnapshots-request-SnapshotStatus"></a>
Use this parameter to list only the snapshots with the specified status.
Type: String
Valid Values: `CREATING | READY | DELETING | FAILED`
Required: No

 ** [SourceApplicationName](#API_ListSnapshots_RequestSyntax) **   <a name="APIReference-ListSnapshots-request-SourceApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_ListSnapshots_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SnapshotInfoList": [
      {
         "SnapshotArn": "string",
         "SnapshotCreationTimestamp": number,
         "SnapshotFormat": "string",
         "SnapshotInitiator": "string",
         "SnapshotInitiatorOperation": "string",
         "SnapshotName": "string",
         "SnapshotStatus": "string",
         "SourceApplicationName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSnapshots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSnapshots_ResponseSyntax) **   <a name="APIReference-ListSnapshots-response-NextToken"></a>
A pagination token that can be used in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [SnapshotInfoList](#API_ListSnapshots_ResponseSyntax) **   <a name="APIReference-ListSnapshots-response-SnapshotInfoList"></a>
A list of `SnapshotInfo` objects.
Type: Array of [SnapshotInfo](API_SnapshotInfo.md) objects

## Errors
<a name="API_ListSnapshots_Errors"></a>

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_ListSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/ListSnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/ListSnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ListSnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/ListSnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ListSnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/ListSnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/ListSnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/ListSnapshots)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/ListSnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ListSnapshots)
