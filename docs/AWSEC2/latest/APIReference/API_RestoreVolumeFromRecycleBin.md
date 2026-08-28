---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RestoreVolumeFromRecycleBin.html
---

# RestoreVolumeFromRecycleBin
<a name="API_RestoreVolumeFromRecycleBin"></a>

Restores a volume from the Recycle Bin. For more information, see [Restore volumes from the Recycle Bin](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-working-with-volumes.html#recycle-bin-restore-volumes) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_RestoreVolumeFromRecycleBin_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VolumeId**
The ID of the volume to restore.
Type: String
Required: Yes

## Response Elements
<a name="API_RestoreVolumeFromRecycleBin_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_RestoreVolumeFromRecycleBin_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_RestoreVolumeFromRecycleBin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RestoreVolumeFromRecycleBin)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RestoreVolumeFromRecycleBin)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RestoreVolumeFromRecycleBin)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RestoreVolumeFromRecycleBin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RestoreVolumeFromRecycleBin)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RestoreVolumeFromRecycleBin)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RestoreVolumeFromRecycleBin)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RestoreVolumeFromRecycleBin)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RestoreVolumeFromRecycleBin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RestoreVolumeFromRecycleBin)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
