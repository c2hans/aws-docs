---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateSnapmirrorRelationship.html
---

# UpdateSnapmirrorRelationship

Updates an Amazon FSx for NetApp ONTAP SnapMirror relationship.

## Request Syntax
<a name="API_UpdateSnapmirrorRelationship_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "PolicyId": "{{string}}",
   "SnapmirrorRelationshipId": "{{string}}",
   "State": "{{string}}",
   "ThrottleInKbps": {{number}},
   "TransferSchedule": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSnapmirrorRelationship_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_UpdateSnapmirrorRelationship_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorRelationship-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-za-z0-9_.-]{0,63}$`
Required: No

 ** [PolicyId](#API_UpdateSnapmirrorRelationship_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorRelationship-request-PolicyId"></a>
Specifies the ID of the SnapMirror policy that the SnapMirror relationship uses.
Type: String
Pattern: `^(snapmirrorpol-[0-9a-f]{17})$`
Required: No

 ** [SnapmirrorRelationshipId](#API_UpdateSnapmirrorRelationship_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorRelationship-request-SnapmirrorRelationshipId"></a>
The ID of the SnapMirror relationship that you want to update.
Type: String
Pattern: `^(snapmirror-[0-9a-f]{17})$`
Required: Yes

 ** [State](#API_UpdateSnapmirrorRelationship_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorRelationship-request-State"></a>
Specifies the state to set for the SnapMirror relationship:
+  `SNAPMIRRORED` – Resumes a paused SnapMirror relationship, or resynchronizes a broken-off SnapMirror relationship.
+  `PAUSED` – Pauses SnapMirror transfers for the relationship.
+  `BROKEN_OFF` – Breaks off the SnapMirror relationship, which makes the destination volume writable.
Setting `State` to `SNAPMIRRORED` on a relationship that is `BROKEN_OFF` might resynchronize the relationship. A resync overwrites the destination volume with data from the source volume, and discards any data written to the destination volume that isn't present on the source volume. Use caution when you resynchronize a relationship.
Type: String
Valid Values: `SNAPMIRRORED | PAUSED | BROKEN_OFF`
Required: No

 ** [ThrottleInKbps](#API_UpdateSnapmirrorRelationship_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorRelationship-request-ThrottleInKbps"></a>
Specifies the maximum bandwidth, in kilobytes per second (KBps), that SnapMirror uses to transfer data for the relationship. A value of `0` means that the bandwidth is unlimited. This value overrides the throttle of the SnapMirror policy.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [TransferSchedule](#API_UpdateSnapmirrorRelationship_RequestSyntax) **   <a name="FSx-UpdateSnapmirrorRelationship-request-TransferSchedule"></a>
Specifies the name of the ONTAP schedule that determines when SnapMirror transfers data for the relationship. This schedule overrides the transfer schedule of the SnapMirror policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_:.-]{0,256}$`
Required: No

## Response Syntax
<a name="API_UpdateSnapmirrorRelationship_ResponseSyntax"></a>

```
{
   "SnapmirrorRelationship": {
      "Destination": {
         "Path": "string",
         "VolumeId": "string"
      },
      "ExportedSnapshot": {
         "SnapshotId": "string",
         "SnapshotName": "string"
      },
      "FileSystemId": "string",
      "Healthy": boolean,
      "LagTimeInMinutes": number,
      "Lifecycle": "string",
      "LifecycleTransitionReason": {
         "Message": "string",
         "OntapError": {
            "Code": "string",
            "Message": "string"
         }
      },
      "ResourceARN": "string",
      "SnapmirrorPolicy": {
         "PolicyId": "string",
         "PolicyName": "string"
      },
      "SnapmirrorRelationshipId": "string",
      "Source": {
         "Path": "string"
      },
      "State": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "ThrottleInKbps": number,
      "TransferSchedule": "string",
      "TransferState": {
         "BytesTransferred": number,
         "Duration": "string",
         "EndTime": number,
         "State": "string",
         "Type": "string"
      },
      "UnhealthyReason": "string",
      "UUID": "string"
   }
}
```

## Response Elements
<a name="API_UpdateSnapmirrorRelationship_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapmirrorRelationship](#API_UpdateSnapmirrorRelationship_ResponseSyntax) **   <a name="FSx-UpdateSnapmirrorRelationship-response-SnapmirrorRelationship"></a>
A description of the SnapMirror relationship that was just updated.
Type: [SnapmirrorRelationship](API_SnapmirrorRelationship.md) object

## Errors
<a name="API_UpdateSnapmirrorRelationship_Errors"></a>

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

 ** SnapmirrorRelationshipNotFound **
No Amazon FSx SnapMirror relationships were found based on the supplied parameters.
 ** Message **
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSnapmirrorRelationship_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/UpdateSnapmirrorRelationship)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/UpdateSnapmirrorRelationship)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateSnapmirrorRelationship)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/UpdateSnapmirrorRelationship)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateSnapmirrorRelationship)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/UpdateSnapmirrorRelationship)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/UpdateSnapmirrorRelationship)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/UpdateSnapmirrorRelationship)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/UpdateSnapmirrorRelationship)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateSnapmirrorRelationship)
