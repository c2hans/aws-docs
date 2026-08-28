---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshotAttribute.html
---

# DescribeSnapshotAttribute
<a name="API_DescribeSnapshotAttribute"></a>

Describes the specified attribute of the specified snapshot. You can specify only one attribute at a time.

For more information about EBS snapshots, see [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_DescribeSnapshotAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The snapshot attribute you would like to view.
Type: String
Valid Values: `productCodes | createVolumePermission`
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SnapshotId**
The ID of the EBS snapshot.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeSnapshotAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **createVolumePermission**
The users and groups that have the permissions for creating volumes from the snapshot.
Type: Array of [CreateVolumePermission](API_CreateVolumePermission.md) objects

 **productCodes**
The product codes.
Type: Array of [ProductCode](API_ProductCode.md) objects

 **requestId**
The ID of the request.
Type: String

 **snapshotId**
The ID of the EBS snapshot.
Type: String

## Errors
<a name="API_DescribeSnapshotAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeSnapshotAttribute_Examples"></a>

### Example
<a name="API_DescribeSnapshotAttribute_Example_1"></a>

This example describes the create volume permissions for the specified snapshot.

#### Sample Request
<a name="API_DescribeSnapshotAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSnapshotAttribute
&SnapshotId=snap-1234567890abcdef0
&Attribute=createVolumePermission
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeSnapshotAttribute_Example_1_Response"></a>

```
<DescribeSnapshotAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <snapshotId>snap-1234567890abcdef0</snapshotId>
   <createVolumePermission>
      <item>
         <group>all</group>
      </item>
   </createVolumePermission>
</DescribeSnapshotAttributeResponse>
```

## See Also
<a name="API_DescribeSnapshotAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeSnapshotAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeSnapshotAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeSnapshotAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeSnapshotAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeSnapshotAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeSnapshotAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeSnapshotAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeSnapshotAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeSnapshotAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeSnapshotAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
