---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateSnapshotPolicy.html
---

# CreateSnapshotPolicy

Creates a snapshot policy for an Amazon FSx for NetApp ONTAP file system or storage virtual machine (SVM). A snapshot policy defines the schedules on which ONTAP automatically creates snapshots of the volumes that use the policy, and the maximum number of snapshots to retain for each schedule.

The `CreateSnapshotPolicy` operation returns while the snapshot policy's lifecycle state is still `CREATING`. You can check the snapshot policy creation status by calling the DescribeSnapshotPolicies operation.

## Request Syntax
<a name="API_CreateSnapshotPolicy_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "Enabled": {{boolean}},
   "FileSystemId": "{{string}}",
   "Name": "{{string}}",
   "Schedules": [
      {
         "Count": {{number}},
         "Name": "{{string}}",
         "Prefix": "{{string}}",
         "RetentionPeriod": {
            "Type": "{{string}}",
            "Value": {{number}}
         },
         "SnapmirrorLabel": "{{string}}"
      }
   ],
   "StorageVirtualMachineId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateSnapshotPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateSnapshotPolicy_RequestSyntax) **   <a name="FSx-CreateSnapshotPolicy-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-za-z0-9_.-]{0,63}$`
Required: No

 ** [Enabled](#API_CreateSnapshotPolicy_RequestSyntax) **   <a name="FSx-CreateSnapshotPolicy-request-Enabled"></a>
Specifies whether the snapshot policy is enabled. This value defaults to `true`.
Type: Boolean
Required: No

 ** [FileSystemId](#API_CreateSnapshotPolicy_RequestSyntax) **   <a name="FSx-CreateSnapshotPolicy-request-FileSystemId"></a>
Specifies the ID of the Amazon FSx for NetApp ONTAP file system on which to create the snapshot policy. You must specify either a `FileSystemId` or a `StorageVirtualMachineId`, but not both.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `^(fs-[0-9a-f]{8,})$`
Required: No

 ** [Name](#API_CreateSnapshotPolicy_RequestSyntax) **   <a name="FSx-CreateSnapshotPolicy-request-Name"></a>
Specifies the name of the snapshot policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Schedules](#API_CreateSnapshotPolicy_RequestSyntax) **   <a name="FSx-CreateSnapshotPolicy-request-Schedules"></a>
Specifies the schedules on which ONTAP creates snapshots for the snapshot policy.
Type: Array of [SnapshotPolicySchedule](API_SnapshotPolicySchedule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** [StorageVirtualMachineId](#API_CreateSnapshotPolicy_RequestSyntax) **   <a name="FSx-CreateSnapshotPolicy-request-StorageVirtualMachineId"></a>
Specifies the ID of the SVM on which to create the snapshot policy. You must specify either a `FileSystemId` or a `StorageVirtualMachineId`, but not both.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^(svm-[0-9a-f]{17,})$`
Required: No

 ** [Tags](#API_CreateSnapshotPolicy_RequestSyntax) **   <a name="FSx-CreateSnapshotPolicy-request-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateSnapshotPolicy_ResponseSyntax"></a>

```
{
   "SnapshotPolicy": {
      "Enabled": boolean,
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
      "ResourceARN": "string",
      "Schedules": [
         {
            "Count": number,
            "Name": "string",
            "Prefix": "string",
            "RetentionPeriod": {
               "Type": "string",
               "Value": number
            },
            "SnapmirrorLabel": "string"
         }
      ],
      "Scope": "string",
      "SnapshotPolicyId": "string",
      "StorageVirtualMachineId": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "UUID": "string"
   }
}
```

## Response Elements
<a name="API_CreateSnapshotPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotPolicy](#API_CreateSnapshotPolicy_ResponseSyntax) **   <a name="FSx-CreateSnapshotPolicy-response-SnapshotPolicy"></a>
A description of the snapshot policy.
Type: [SnapshotPolicy](API_SnapshotPolicy.md) object

## Errors
<a name="API_CreateSnapshotPolicy_Errors"></a>

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
<a name="API_CreateSnapshotPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateSnapshotPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateSnapshotPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateSnapshotPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateSnapshotPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateSnapshotPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateSnapshotPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateSnapshotPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateSnapshotPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateSnapshotPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateSnapshotPolicy)
