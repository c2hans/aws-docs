---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListSnapshotOperations.html
---

# ListSnapshotOperations
<a name="API_ListSnapshotOperations"></a>

Lists the operations that were performed on the specified enhanced snapshot, such as `CreateSnapshot`, `ImportSnapshot`, and `ExportSnapshot`. The response includes a summary of each operation.

You can specify only one of the `SnapshotOperation` or `SnapshotOperationStatus` filters in a request. If you specify both, `InvalidArgumentException` is returned.

To get the complete description of a specific operation, use `DescribeSnapshotOperation`. Snapshot operations are available for 90 days after they are created.

## Request Syntax
<a name="API_ListSnapshotOperations_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "SnapshotName": "{{string}}",
   "SnapshotOperation": "{{string}}",
   "SnapshotOperationStatus": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSnapshotOperations_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Limit](#API_ListSnapshotOperations_RequestSyntax) **   <a name="APIReference-ListSnapshotOperations-request-Limit"></a>
The maximum number of snapshot operations to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListSnapshotOperations_RequestSyntax) **   <a name="APIReference-ListSnapshotOperations-request-NextToken"></a>
A pagination token that can be used in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [SnapshotName](#API_ListSnapshotOperations_RequestSyntax) **   <a name="APIReference-ListSnapshotOperations-request-SnapshotName"></a>
The name of the enhanced snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [SnapshotOperation](#API_ListSnapshotOperations_RequestSyntax) **   <a name="APIReference-ListSnapshotOperations-request-SnapshotOperation"></a>
Use this parameter to list only the operations of the specified type.
Type: String
Valid Values: `CreateSnapshot | DeleteSnapshot | ImportSnapshot | ExportSnapshot | SystemCreateSnapshot`
Required: No

 ** [SnapshotOperationStatus](#API_ListSnapshotOperations_RequestSyntax) **   <a name="APIReference-ListSnapshotOperations-request-SnapshotOperationStatus"></a>
Use this parameter to list only the operations with the specified status.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | CANCELLED`
Required: No

## Response Syntax
<a name="API_ListSnapshotOperations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SnapshotOperationInfoList": [
      {
         "EndTime": number,
         "SnapshotOperation": "string",
         "SnapshotOperationId": "string",
         "SnapshotOperationStatus": "string",
         "StartTime": number
      }
   ]
}
```

## Response Elements
<a name="API_ListSnapshotOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSnapshotOperations_ResponseSyntax) **   <a name="APIReference-ListSnapshotOperations-response-NextToken"></a>
A pagination token that can be used in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [SnapshotOperationInfoList](#API_ListSnapshotOperations_ResponseSyntax) **   <a name="APIReference-ListSnapshotOperations-response-SnapshotOperationInfoList"></a>
A list of `SnapshotOperationInfo` objects.
Type: Array of [SnapshotOperationInfo](API_SnapshotOperationInfo.md) objects

## Errors
<a name="API_ListSnapshotOperations_Errors"></a>

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
<a name="API_ListSnapshotOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/ListSnapshotOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/ListSnapshotOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ListSnapshotOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/ListSnapshotOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ListSnapshotOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/ListSnapshotOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/ListSnapshotOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/ListSnapshotOperations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/ListSnapshotOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ListSnapshotOperations)
