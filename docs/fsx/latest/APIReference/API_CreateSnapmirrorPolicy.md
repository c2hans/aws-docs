---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateSnapmirrorPolicy.html
---

# CreateSnapmirrorPolicy

Creates a SnapMirror policy for an Amazon FSx for NetApp ONTAP file system or storage virtual machine (SVM). A SnapMirror policy defines how the SnapMirror relationships that use the policy replicate data, including which snapshots to transfer, the maximum number of snapshots to retain on the destination volume, and when to transfer data.

The `CreateSnapmirrorPolicy` operation returns while the SnapMirror policy's lifecycle state is still `CREATING`. You can check the SnapMirror policy creation status by calling the DescribeSnapmirrorPolicies operation.

## Request Syntax
<a name="API_CreateSnapmirrorPolicy_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "FileSystemId": "{{string}}",
   "Name": "{{string}}",
   "NetworkCompressionEnabled": {{boolean}},
   "RetentionRules": [
      {
         "Count": {{number}},
         "CreationSchedule": "{{string}}",
         "Label": "{{string}}"
      }
   ],
   "SnapshotCopyMode": "{{string}}",
   "StorageVirtualMachineId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ThrottleInKbps": {{number}},
   "TransferSchedule": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateSnapmirrorPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-CreateSnapmirrorPolicy-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-za-z0-9_.-]{0,63}$`
Required: No

 ** [FileSystemId](#API_CreateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-CreateSnapmirrorPolicy-request-FileSystemId"></a>
Specifies the ID of the Amazon FSx for NetApp ONTAP file system on which to create the SnapMirror policy. You must specify either a `FileSystemId` or a `StorageVirtualMachineId`, but not both.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `^(fs-[0-9a-f]{8,})$`
Required: No

 ** [Name](#API_CreateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-CreateSnapmirrorPolicy-request-Name"></a>
Specifies the name of the SnapMirror policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [NetworkCompressionEnabled](#API_CreateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-CreateSnapmirrorPolicy-request-NetworkCompressionEnabled"></a>
Specifies whether SnapMirror compresses data when it transfers the data over the network. This value defaults to `false`.
Type: Boolean
Required: No

 ** [RetentionRules](#API_CreateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-CreateSnapmirrorPolicy-request-RetentionRules"></a>
Specifies the rules that determine which snapshots SnapMirror retains on the destination volume, based on their SnapMirror labels.
Type: Array of [SnapmirrorPolicyRetentionRule](API_SnapmirrorPolicyRetentionRule.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** [SnapshotCopyMode](#API_CreateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-CreateSnapmirrorPolicy-request-SnapshotCopyMode"></a>
Specifies which snapshots SnapMirror transfers to the destination volume:
+  `COPY_ALL_SOURCE_SNAPSHOTS` – SnapMirror copies all snapshots of the source volume to the destination volume on a transfer. You can't specify `RetentionRules` along with this property.
+  `COPY_LATEST_SOURCE_SNAPSHOT` – SnapMirror copies the latest snapshot of the source volume to the destination volume on a transfer. You can't specify `RetentionRules` along with this property.
+  `NO_CREATE_SNAPSHOT_ON_SOURCE` – SnapMirror doesn't create a snapshot on the source volume at beginning of an update or resync operation. You must specify `RetentionRules` along with this property.
If you don't specify a `SnapshotCopyMode`, SnapMirror creates a new snapshot of the source volume and copies it, along with any snapshots that match `RetentionRules`, to the destination volume on a transfer. `RetentionRules` is optional.
Type: String
Valid Values: `COPY_ALL_SOURCE_SNAPSHOTS | COPY_LATEST_SOURCE_SNAPSHOT | NO_CREATE_SNAPSHOT_ON_SOURCE`
Required: No

 ** [StorageVirtualMachineId](#API_CreateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-CreateSnapmirrorPolicy-request-StorageVirtualMachineId"></a>
Specifies the ID of the SVM on which to create the SnapMirror policy. You must specify either a `FileSystemId` or a `StorageVirtualMachineId`, but not both.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^(svm-[0-9a-f]{17,})$`
Required: No

 ** [Tags](#API_CreateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-CreateSnapmirrorPolicy-request-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [ThrottleInKbps](#API_CreateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-CreateSnapmirrorPolicy-request-ThrottleInKbps"></a>
Specifies the maximum bandwidth, in kilobytes per second (KBps), that SnapMirror uses to transfer data. A value of `0` means that the bandwidth is unlimited.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [TransferSchedule](#API_CreateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-CreateSnapmirrorPolicy-request-TransferSchedule"></a>
Specifies the name of the ONTAP schedule that determines when SnapMirror transfers data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_:.-]{0,256}$`
Required: No

## Response Syntax
<a name="API_CreateSnapmirrorPolicy_ResponseSyntax"></a>

```
{
   "SnapmirrorPolicy": {
      "FileSystemId": "string",
      "Lifecycle": "string",
      "LifecycleTransitionReason": {
         "Message": "string",
         "OntapError": {
            "Code": "string",
            "Message": "string"
         }
      },
      "Name": "string",
      "NetworkCompressionEnabled": boolean,
      "ResourceARN": "string",
      "RetentionRules": [
         {
            "Count": number,
            "CreationSchedule": "string",
            "Label": "string"
         }
      ],
      "Scope": "string",
      "SnapmirrorPolicyId": "string",
      "SnapshotCopyMode": "string",
      "StorageVirtualMachineId": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "ThrottleInKbps": number,
      "TransferSchedule": "string",
      "UUID": "string"
   }
}
```

## Response Elements
<a name="API_CreateSnapmirrorPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapmirrorPolicy](#API_CreateSnapmirrorPolicy_ResponseSyntax) **   <a name="FSx-CreateSnapmirrorPolicy-response-SnapmirrorPolicy"></a>
A description of the SnapMirror policy.
Type: [SnapmirrorPolicy](API_SnapmirrorPolicy.md) object

## Errors
<a name="API_CreateSnapmirrorPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **
A generic error indicating a failure with a client request.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** FileSystemNotFound **
No Amazon FSx file systems were found based upon supplied parameters.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** IncompatibleParameterError **
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.
 ** Message **
A detailed error message.
 ** Parameter **
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** InternalServerError **
A generic error indicating a server-side failure.
 ** Message **
A detailed error message.
HTTP Status Code: 500

 ** ServiceLimitExceeded **
An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting AWS Support.
 ** Limit **
Enumeration of the service limit that was exceeded.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** StorageVirtualMachineNotFound **
No FSx for ONTAP SVMs were found based upon the supplied parameters.
 ** Message **
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateSnapmirrorPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateSnapmirrorPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateSnapmirrorPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateSnapmirrorPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateSnapmirrorPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateSnapmirrorPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateSnapmirrorPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateSnapmirrorPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateSnapmirrorPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateSnapmirrorPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateSnapmirrorPolicy)
