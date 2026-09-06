---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RestoreImageFromRecycleBin.html
---

# RestoreImageFromRecycleBin
<a name="API_RestoreImageFromRecycleBin"></a>

Restores an AMI from the Recycle Bin. For more information, see [Recover deleted Amazon EBS snapshots and EBS-back AMIs with Recycle Bin](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_RestoreImageFromRecycleBin_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageId**
The ID of the AMI to restore.
Type: String
Required: Yes

## Response Elements
<a name="API_RestoreImageFromRecycleBin_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_RestoreImageFromRecycleBin_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_RestoreImageFromRecycleBin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RestoreImageFromRecycleBin)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RestoreImageFromRecycleBin)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RestoreImageFromRecycleBin)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RestoreImageFromRecycleBin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RestoreImageFromRecycleBin)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RestoreImageFromRecycleBin)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RestoreImageFromRecycleBin)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RestoreImageFromRecycleBin)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RestoreImageFromRecycleBin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RestoreImageFromRecycleBin)
