---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableFastSnapshotRestores.html
---

# DisableFastSnapshotRestores
<a name="API_DisableFastSnapshotRestores"></a>

Disables fast snapshot restores for the specified snapshots in the specified Availability Zones.

## Request Parameters
<a name="API_DisableFastSnapshotRestores_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AvailabilityZone.N**
One or more Availability Zones. For example, `us-east-2a`.
Either `AvailabilityZone` or `AvailabilityZoneId` must be specified in the request, but not both.
Type: Array of strings
Required: No

 **AvailabilityZoneId.N**
One or more Availability Zone IDs. For example, `use2-az1`.
Either `AvailabilityZone` or `AvailabilityZoneId` must be specified in the request, but not both.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SourceSnapshotId.N**
The IDs of one or more snapshots. For example, `snap-1234567890abcdef0`.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_DisableFastSnapshotRestores_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **successful**
Information about the snapshots for which fast snapshot restores were successfully disabled.
Type: Array of [DisableFastSnapshotRestoreSuccessItem](API_DisableFastSnapshotRestoreSuccessItem.md) objects

 **unsuccessful**
Information about the snapshots for which fast snapshot restores could not be disabled.
Type: Array of [DisableFastSnapshotRestoreErrorItem](API_DisableFastSnapshotRestoreErrorItem.md) objects

## Errors
<a name="API_DisableFastSnapshotRestores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DisableFastSnapshotRestores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisableFastSnapshotRestores)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisableFastSnapshotRestores)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisableFastSnapshotRestores)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisableFastSnapshotRestores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisableFastSnapshotRestores)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisableFastSnapshotRestores)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisableFastSnapshotRestores)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisableFastSnapshotRestores)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisableFastSnapshotRestores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisableFastSnapshotRestores)
