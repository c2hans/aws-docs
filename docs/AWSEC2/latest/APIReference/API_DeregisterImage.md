---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterImage.html
---

# DeregisterImage
<a name="API_DeregisterImage"></a>

Deregisters the specified AMI. A deregistered AMI can't be used to launch new instances.

If a deregistered EBS-backed AMI matches a Recycle Bin retention rule, it moves to the Recycle Bin for the specified retention period. It can be restored before its retention period expires, after which it is permanently deleted. If the deregistered AMI doesn't match a retention rule, it is permanently deleted immediately. For more information, see [Recover deleted Amazon EBS snapshots and EBS-backed AMIs with Recycle Bin](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin.html) in the *Amazon EBS User Guide*.

When deregistering an EBS-backed AMI, you can optionally delete its associated snapshots at the same time. However, if a snapshot is associated with multiple AMIs, it won't be deleted even if specified for deletion, although the AMI will still be deregistered.

Deregistering an AMI does not delete the following:
+ Instances already launched from the AMI. You'll continue to incur usage costs for the instances until you terminate them.
+ For EBS-backed AMIs: Snapshots that are associated with multiple AMIs. You'll continue to incur snapshot storage costs.
+ For instance store-backed AMIs: The files uploaded to Amazon S3 during AMI creation. You'll continue to incur S3 storage costs.

For more information, see [Deregister an Amazon EC2 AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DeregisterImage_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DeleteAssociatedSnapshots**
Specifies whether to delete the snapshots associated with the AMI during deregistration.
If a snapshot is associated with multiple AMIs, it is not deleted, regardless of this setting.
Default: The snapshots are not deleted.
Type: Boolean
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageId**
The ID of the AMI.
Type: String
Required: Yes

## Response Elements
<a name="API_DeregisterImage_ResponseElements"></a>

The following elements are returned by the service.

 **deleteSnapshotResultSet**
The deletion result for each snapshot associated with the AMI, including the snapshot ID and its success or error code.
Type: Array of [DeleteSnapshotReturnCode](API_DeleteSnapshotReturnCode.md) objects

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_DeregisterImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeregisterImage_Examples"></a>

### Example
<a name="API_DeregisterImage_Example_1"></a>

This example request deregisters the specified AMI.

#### Sample Request
<a name="API_DeregisterImage_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeregisterImage
&ImageId=ami-4fa54026
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeregisterImage_Example_1_Response"></a>

```
<DeregisterImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <return>true</return>
</DeregisterImageResponse>
```

## See Also
<a name="API_DeregisterImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeregisterImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeregisterImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeregisterImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeregisterImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeregisterImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeregisterImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeregisterImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeregisterImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeregisterImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeregisterImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
