---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html
---

# ModifyImageAttribute
<a name="API_ModifyImageAttribute"></a>

Modifies the specified attribute of the specified AMI. You can specify only one attribute at a time.

To specify the attribute, you can use the `Attribute` parameter, or one of the following parameters: `Description`, `ImdsSupport`, or `LaunchPermission`.

Images with an AWS Marketplace product code cannot be made public.

To enable the SriovNetSupport enhanced networking attribute of an image, enable SriovNetSupport on an instance and create an AMI from the instance.

## Request Parameters
<a name="API_ModifyImageAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The name of the attribute to modify.
Valid values: `description` \| `imdsSupport` \| `launchPermission`
Type: String
Required: No

 **Description**
A new description for the AMI.
Type: [AttributeValue](API_AttributeValue.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageId**
The ID of the AMI.
Type: String
Required: Yes

 **ImdsSupport**
Set to `v2.0` to indicate that IMDSv2 is specified in the AMI. Instances launched from this AMI will have `HttpTokens` automatically set to `required` so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, `HttpPutResponseHopLimit` is set to `2`. For more information, see [Configure the AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) in the *Amazon EC2 User Guide*.
Do not use this parameter unless your AMI software supports IMDSv2. After you set the value to `v2.0`, you can't undo it. The only way to “reset” your AMI is to create a new AMI from the underlying snapshot.
Type: [AttributeValue](API_AttributeValue.md) object
Required: No

 **LaunchPermission**
A new launch permission for the AMI.
Type: [LaunchPermissionModifications](API_LaunchPermissionModifications.md) object
Required: No

 **OperationType**
The operation type. This parameter can be used only when the `Attribute` parameter is `launchPermission`.
Type: String
Valid Values: `add | remove`
Required: No

 **OrganizationalUnitArn.N**
The Amazon Resource Name (ARN) of an organizational unit (OU). This parameter can be used only when the `Attribute` parameter is `launchPermission`.
Type: Array of strings
Required: No

 **OrganizationArn.N**
The Amazon Resource Name (ARN) of an organization. This parameter can be used only when the `Attribute` parameter is `launchPermission`.
Type: Array of strings
Required: No

 **ProductCode.N**
Not supported.
Type: Array of strings
Required: No

 **UserGroup.N**
The user groups. This parameter can be used only when the `Attribute` parameter is `launchPermission`.
Type: Array of strings
Required: No

 **UserId.N**
The AWS account IDs. This parameter can be used only when the `Attribute` parameter is `launchPermission`.
Type: Array of strings
Required: No

 **Value**
The value of the attribute being modified. This parameter can be used only when the `Attribute` parameter is `description` or `imdsSupport`.
Type: String
Required: No

## Response Elements
<a name="API_ModifyImageAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ModifyImageAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyImageAttribute_Examples"></a>

### Example 1
<a name="API_ModifyImageAttribute_Example_1"></a>

This example makes the AMI public (for example, so any AWS account can use it).

#### Sample Request
<a name="API_ModifyImageAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyImageAttribute
&ImageId=ami-61a54008
&LaunchPermission.Add.1.Group=all
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyImageAttribute_Example_1_Response"></a>

```
<ModifyImageAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <return>true</return>
</ModifyImageAttributeResponse>
```

### Example 2
<a name="API_ModifyImageAttribute_Example_2"></a>

This example makes the AMI private (for example, so that only you as the owner can use it).

#### Sample Request
<a name="API_ModifyImageAttribute_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyImageAttribute
&ImageId=ami-61a54008
&LaunchPermission.Remove.1.Group=all
&AUTHPARAMS
```

### Example 3
<a name="API_ModifyImageAttribute_Example_3"></a>

This example grants launch permission to the AWS account with ID `111122223333`.

#### Sample Request
<a name="API_ModifyImageAttribute_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyImageAttribute
&ImageId=ami-61a54008
&LaunchPermission.Add.1.UserId=111122223333
&AUTHPARAMS
```

### Example 4
<a name="API_ModifyImageAttribute_Example_4"></a>

This example adds the `774F4FF8` product code to the `ami-61a54008` AMI.

#### Sample Request
<a name="API_ModifyImageAttribute_Example_4_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyImageAttribute
&ImageId=ami-61a54008
&ProductCode.1=774F4FF8
&AUTHPARAMS
```

### Example 5
<a name="API_ModifyImageAttribute_Example_5"></a>

This example changes the description of the AMI to `New Description`.

#### Sample Request
<a name="API_ModifyImageAttribute_Example_5_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyImageAttribute
&ImageId=ami-61a54008
&Description.Value=New Description
&AUTHPARAMS
```

### Example 6
<a name="API_ModifyImageAttribute_Example_6"></a>

This example sets the AMI to IMDSv2 only. Instances created from this AMI will require that IMDSv2 is used when requesting instance metadata.

Note that after you set the value to `v2.0`, you can't undo it.

#### Sample Request
<a name="API_ModifyImageAttribute_Example_6_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyImageAttribute
&ImageId=ami-61a54008
&ImdsSupport.Value=v2.0
&AUTHPARAMS
```

## See Also
<a name="API_ModifyImageAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyImageAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyImageAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyImageAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyImageAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyImageAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyImageAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyImageAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyImageAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyImageAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyImageAttribute)
