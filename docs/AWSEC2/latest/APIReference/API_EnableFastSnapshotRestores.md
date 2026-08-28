---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableFastSnapshotRestores.html
---

# EnableFastSnapshotRestores
<a name="API_EnableFastSnapshotRestores"></a>

Enables fast snapshot restores for the specified snapshots in the specified Availability Zones.

You get the full benefit of fast snapshot restores after they enter the `enabled` state.

To get the current state of fast snapshot restores, use [DescribeFastSnapshotRestores](API_DescribeFastSnapshotRestores.md). To disable fast snapshot restores, use [DisableFastSnapshotRestores](API_DisableFastSnapshotRestores.md).

For more information, see [Amazon EBS fast snapshot restore](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fast-snapshot-restore.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_EnableFastSnapshotRestores_RequestParameters"></a>

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
The IDs of one or more snapshots. For example, `snap-1234567890abcdef0`. You can specify a snapshot that was shared with you from another AWS account.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_EnableFastSnapshotRestores_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **successful**
Information about the snapshots for which fast snapshot restores were successfully enabled.
Type: Array of [EnableFastSnapshotRestoreSuccessItem](API_EnableFastSnapshotRestoreSuccessItem.md) objects

 **unsuccessful**
Information about the snapshots for which fast snapshot restores could not be enabled.
Type: Array of [EnableFastSnapshotRestoreErrorItem](API_EnableFastSnapshotRestoreErrorItem.md) objects

## Errors
<a name="API_EnableFastSnapshotRestores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_EnableFastSnapshotRestores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableFastSnapshotRestores)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableFastSnapshotRestores)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableFastSnapshotRestores)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableFastSnapshotRestores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableFastSnapshotRestores)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableFastSnapshotRestores)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableFastSnapshotRestores)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableFastSnapshotRestores)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableFastSnapshotRestores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableFastSnapshotRestores)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
