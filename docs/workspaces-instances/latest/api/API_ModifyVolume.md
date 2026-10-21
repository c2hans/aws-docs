---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ModifyVolume.html
---

# ModifyVolume
<a name="API_ModifyVolume"></a>

Modifies the size, volume type, IOPS (input/output operations per second), or throughput of a volume. When you modify a volume, you must specify at least one of these parameters. You can modify a volume only after any previous modification for that volume has finished.

To track the progress of a modification, use the Amazon EC2 [DescribeVolumesModifications](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumesModifications.html) operation. For more information, see [Monitor the progress of Amazon EBS volume modifications](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-modifications.html) in the *Amazon EBS User Guide*.

After you increase the size of a volume, you must extend the partition and file system to use the new storage capacity. For more information, see [Extend the file system after resizing an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/recognize-expanded-volume-linux.html) in the *Amazon EBS User Guide*, which covers both [Linux](https://docs.aws.amazon.com/ebs/latest/userguide/recognize-expanded-volume-linux.html#extend-linux) and [Windows](https://docs.aws.amazon.com/ebs/latest/userguide/recognize-expanded-volume-linux.html#extend-windows) instances.

## Request Syntax
<a name="API_ModifyVolume_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Iops": {{number}},
   "SizeInGB": {{number}},
   "Throughput": {{number}},
   "VolumeId": "{{string}}",
   "VolumeType": "{{string}}"
}
```

## Request Parameters
<a name="API_ModifyVolume_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_ModifyVolume_RequestSyntax) **   <a name="workspacesinstances-ModifyVolume-request-ClientToken"></a>
Unique token to ensure idempotent volume modification, preventing duplicate volume modifications.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x20-\x7E]+`
Required: No

 ** [Iops](#API_ModifyVolume_RequestSyntax) **   <a name="workspacesinstances-ModifyVolume-request-Iops"></a>
Specifies the target IOPS rate of the volume. This parameter is valid only for `gp3`, `io1`, and `io2` volumes. If you don't specify IOPS and keep the same volume type, the current IOPS rate is retained.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [SizeInGB](#API_ModifyVolume_RequestSyntax) **   <a name="workspacesinstances-ModifyVolume-request-SizeInGB"></a>
Specifies the target size of the volume, in GiB. The target size must be greater than or equal to the current size of the volume. If you don't specify a size, the current size is retained.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 16384.
Required: No

 ** [Throughput](#API_ModifyVolume_RequestSyntax) **   <a name="workspacesinstances-ModifyVolume-request-Throughput"></a>
Specifies the target throughput of the volume, in MiB/s. This parameter is valid only for `gp3` volumes. If you don't specify throughput and the volume remains `gp3`, the current throughput is retained.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [VolumeId](#API_ModifyVolume_RequestSyntax) **   <a name="workspacesinstances-ModifyVolume-request-VolumeId"></a>
Specifies the identifier of the volume to modify.
Type: String
Pattern: `vol-[0-9a-zA-Z]{1,63}`
Required: Yes

 ** [VolumeType](#API_ModifyVolume_RequestSyntax) **   <a name="workspacesinstances-ModifyVolume-request-VolumeType"></a>
Specifies the target Amazon Elastic Block Store (Amazon EBS) volume type. If you don't specify a volume type, the current volume type is retained.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

## Response Syntax
<a name="API_ModifyVolume_ResponseSyntax"></a>

```
{
   "TargetIops": number,
   "TargetSize": number,
   "TargetThroughput": number,
   "TargetVolumeType": "string",
   "VolumeId": "string"
}
```

## Response Elements
<a name="API_ModifyVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TargetIops](#API_ModifyVolume_ResponseSyntax) **   <a name="workspacesinstances-ModifyVolume-response-TargetIops"></a>
Specifies the target IOPS rate of the volume.
Type: Integer
Valid Range: Minimum value of 0.

 ** [TargetSize](#API_ModifyVolume_ResponseSyntax) **   <a name="workspacesinstances-ModifyVolume-response-TargetSize"></a>
Specifies the target size of the volume, in GiB.
Type: Integer
Valid Range: Minimum value of 0.

 ** [TargetThroughput](#API_ModifyVolume_ResponseSyntax) **   <a name="workspacesinstances-ModifyVolume-response-TargetThroughput"></a>
Specifies the target throughput of the volume, in MiB/s.
Type: Integer
Valid Range: Minimum value of 0.

 ** [TargetVolumeType](#API_ModifyVolume_ResponseSyntax) **   <a name="workspacesinstances-ModifyVolume-response-TargetVolumeType"></a>
Specifies the target Amazon EBS volume type.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`

 ** [VolumeId](#API_ModifyVolume_ResponseSyntax) **   <a name="workspacesinstances-ModifyVolume-response-VolumeId"></a>
Specifies the identifier of the modified volume.
Type: String
Pattern: `vol-[0-9a-zA-Z]{1,63}`

## Errors
<a name="API_ModifyVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Indicates insufficient permissions to perform the requested action.
 ** Message **
Detailed explanation of the access denial.
HTTP Status Code: 403

 ** ConflictException **
Signals a conflict with the current state of the resource.
 ** Message **
Description of the conflict encountered.
 ** ResourceId **
Identifier of the conflicting resource.
 ** ResourceType **
Type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
Indicates an unexpected server-side error occurred.
 ** Message **
Description of the internal server error.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Indicates the requested resource could not be found.
 ** Message **
Details about the missing resource.
 ** ResourceId **
Identifier of the resource that was not found.
 ** ResourceType **
Type of the resource that was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Indicates that a service quota has been exceeded.
 ** Message **
Description of the quota limitation.
 ** QuotaCode **
Specific code for the exceeded quota.
 ** ResourceId **
Identifier of the resource related to the quota.
 ** ResourceType **
Type of resource related to the quota.
 ** ServiceCode **
Code identifying the service with the quota limitation.
HTTP Status Code: 402

 ** ThrottlingException **
Indicates the request rate has exceeded limits.
 ** Message **
Description of the throttling event.
 ** QuotaCode **
Specific code for the throttling quota.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
 ** ServiceCode **
Code identifying the service experiencing throttling.
HTTP Status Code: 429

 ** ValidationException **
Indicates invalid input parameters in the request.
 ** FieldList **
List of fields that failed validation.
 ** Message **
Overall description of validation failures.
 ** Reason **
Specific reason for the validation failure.
HTTP Status Code: 400

 ** VolumeModificationRateExceededException **
The volume has a previous modification that is still in progress, or has reached the limit of four modifications in a rolling 24-hour period. Wait for the current modification to finish, or wait until the time indicated in the error message, and then retry the request.
 ** Message **
Specifies the reason that the modification request was rejected.
 ** ResourceId **
Specifies the identifier of the volume for which the modification request was rejected.
 ** ResourceType **
Specifies the type of the resource for which the modification request was rejected.
HTTP Status Code: 429

## See Also
<a name="API_ModifyVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-instances-2022-07-26/ModifyVolume)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-instances-2022-07-26/ModifyVolume)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/ModifyVolume)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-instances-2022-07-26/ModifyVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/ModifyVolume)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-instances-2022-07-26/ModifyVolume)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-instances-2022-07-26/ModifyVolume)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-instances-2022-07-26/ModifyVolume)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-instances-2022-07-26/ModifyVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/ModifyVolume)
