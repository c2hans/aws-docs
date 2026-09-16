---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySnapshotAttribute.html
---

# ModifySnapshotAttribute
<a name="API_ModifySnapshotAttribute"></a>

Adds or removes permission settings for the specified snapshot. You may add or remove specified AWS account IDs from a snapshot's list of create volume permissions, but you cannot do both in a single operation. If you need to both add and remove account IDs for a snapshot, you must use multiple operations. You can make up to 500 modifications to a snapshot in a single operation.

Encrypted snapshots and snapshots with AWS Marketplace product codes cannot be made public. Snapshots encrypted with your default KMS key cannot be shared with other accounts.

For more information about modifying snapshot permissions, see [Share a snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modifying-snapshot-permissions.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_ModifySnapshotAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The snapshot attribute to modify. Only volume creation permissions can be modified.
Type: String
Valid Values: `productCodes | createVolumePermission`
Required: No

 **CreateVolumePermission**
A JSON representation of the snapshot attribute modification.
Type: [CreateVolumePermissionModifications](API_CreateVolumePermissionModifications.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **OperationType**
The type of operation to perform to the attribute.
Type: String
Valid Values: `add | remove`
Required: No

 **SnapshotId**
The ID of the snapshot.
Type: String
Required: Yes

 **UserGroup.N**
The group to modify for the snapshot.
Type: Array of strings
Required: No

 **UserId.N**
The account ID to modify for the snapshot.
Type: Array of strings
Required: No

## Response Elements
<a name="API_ModifySnapshotAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ModifySnapshotAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifySnapshotAttribute_Examples"></a>

### Example
<a name="API_ModifySnapshotAttribute_Example_1"></a>

This example makes the `snap-1234567890abcdef0` snapshot public, and gives the account with ID `111122223333` permission to create volumes from the snapshot.

#### Sample Request
<a name="API_ModifySnapshotAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifySnapshotAttribute
&SnapshotId=snap-1234567890abcdef0
&CreateVolumePermission.Add.1.UserId=111122223333
&CreateVolumePermission.Add.1.Group=all
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifySnapshotAttribute_Example_1_Response"></a>

```
<ModifySnapshotAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</ModifySnapshotAttributeResponse>
```

### Example
<a name="API_ModifySnapshotAttribute_Example_2"></a>

This example makes the `snap-1234567890abcdef0` snapshot public, and removes the account with ID `111122223333` from the list of users with permission to create volumes from the snapshot.

#### Sample Request
<a name="API_ModifySnapshotAttribute_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifySnapshotAttribute
&SnapshotId=snap-1234567890abcdef0
&CreateVolumePermission.Remove.1.UserId=111122223333
&CreateVolumePermission.Add.1.Group=all
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifySnapshotAttribute_Example_2_Response"></a>

```
<ModifySnapshotAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</ModifySnapshotAttributeResponse>
```

## See Also
<a name="API_ModifySnapshotAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifySnapshotAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifySnapshotAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifySnapshotAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifySnapshotAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifySnapshotAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifySnapshotAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifySnapshotAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifySnapshotAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifySnapshotAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifySnapshotAttribute)
