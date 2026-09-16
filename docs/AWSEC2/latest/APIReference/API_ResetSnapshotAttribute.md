---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetSnapshotAttribute.html
---

# ResetSnapshotAttribute
<a name="API_ResetSnapshotAttribute"></a>

Resets permission settings for the specified snapshot.

For more information about modifying snapshot permissions, see [Share a snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modifying-snapshot-permissions.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_ResetSnapshotAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The attribute to reset. Currently, only the attribute for permission to create volumes can be reset.
Type: String
Valid Values: `productCodes | createVolumePermission`
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SnapshotId**
The ID of the snapshot.
Type: String
Required: Yes

## Response Elements
<a name="API_ResetSnapshotAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ResetSnapshotAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ResetSnapshotAttribute_Examples"></a>

### Example
<a name="API_ResetSnapshotAttribute_Example_1"></a>

This example resets the permissions for `snap-1234567890abcdef0`, making it a private snapshot that can only be used by the account that created it.

#### Sample Request
<a name="API_ResetSnapshotAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ResetSnapshotAttribute
&SnapshotId=snap-1234567890abcdef0
&Attribute=createVolumePermission
&AUTHPARAMS
```

#### Sample Response
<a name="API_ResetSnapshotAttribute_Example_1_Response"></a>

```
<ResetSnapshotAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <return>true</return>
</ResetSnapshotAttributeResponse>
```

## See Also
<a name="API_ResetSnapshotAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ResetSnapshotAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ResetSnapshotAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ResetSnapshotAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ResetSnapshotAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ResetSnapshotAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ResetSnapshotAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ResetSnapshotAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ResetSnapshotAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ResetSnapshotAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ResetSnapshotAttribute)
