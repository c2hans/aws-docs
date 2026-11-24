---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateSnapmirrorPolicy.html
---

# UpdateSnapmirrorPolicy

Updates an Amazon FSx for NetApp ONTAP SnapMirror policy.

## Request Syntax
<a name="API_UpdateSnapmirrorPolicy_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "NetworkCompressionEnabled": {{boolean}},
   "RetentionRules": [
      {
         "Count": {{number}},
         "CreationSchedule": "{{string}}",
         "Label": "{{string}}"
      }
   ],
   "SnapmirrorPolicyId": "{{string}}",
   "ThrottleInKbps": {{number}},
   "TransferSchedule": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSnapmirrorPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_UpdateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorPolicy-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-za-z0-9_.-]{0,63}$`
Required: No

 ** [NetworkCompressionEnabled](#API_UpdateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorPolicy-request-NetworkCompressionEnabled"></a>
Specifies whether SnapMirror compresses data when it transfers the data over the network.
Type: Boolean
Required: No

 ** [RetentionRules](#API_UpdateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorPolicy-request-RetentionRules"></a>
Specifies the rules that determine which snapshots SnapMirror retains on the destination volume, based on their SnapMirror labels. The rules that you specify replace all the SnapMirror policy's existing retention rules. To keep an existing rule, include it in the list. To remove all retention rules, specify an empty list.
Type: Array of [SnapmirrorPolicyRetentionRule](API_SnapmirrorPolicyRetentionRule.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** [SnapmirrorPolicyId](#API_UpdateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorPolicy-request-SnapmirrorPolicyId"></a>
The ID of the SnapMirror policy that you want to update.
Type: String
Pattern: `^(snapmirrorpol-[0-9a-f]{17})$`
Required: Yes

 ** [ThrottleInKbps](#API_UpdateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorPolicy-request-ThrottleInKbps"></a>
Specifies the maximum bandwidth, in kilobytes per second (KBps), that SnapMirror uses to transfer data. A value of `0` means that the bandwidth is unlimited.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [TransferSchedule](#API_UpdateSnapmirrorPolicy_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorPolicy-request-TransferSchedule"></a>
Specifies the name of the ONTAP schedule that determines when SnapMirror transfers data. To remove the transfer schedule, specify an empty string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_:.-]{0,256}$`
Required: No

## Response Syntax
<a name="API_UpdateSnapmirrorPolicy_ResponseSyntax"></a>

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
<a name="API_UpdateSnapmirrorPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapmirrorPolicy](#API_UpdateSnapmirrorPolicy_ResponseSyntax) **   <a name="FSx-UpdateSnapmirrorPolicy-response-SnapmirrorPolicy"></a>
A description of the SnapMirror policy that was just updated.
Type: [SnapmirrorPolicy](API_SnapmirrorPolicy.md) object

## Errors
<a name="API_UpdateSnapmirrorPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **
A generic error indicating a failure with a client request.
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

 ** SnapmirrorPolicyNotFound **
No Amazon FSx SnapMirror policies were found based on the supplied parameters.
 ** Message **
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSnapmirrorPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/UpdateSnapmirrorPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/UpdateSnapmirrorPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateSnapmirrorPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/UpdateSnapmirrorPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateSnapmirrorPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/UpdateSnapmirrorPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/UpdateSnapmirrorPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/UpdateSnapmirrorPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/UpdateSnapmirrorPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateSnapmirrorPolicy)
