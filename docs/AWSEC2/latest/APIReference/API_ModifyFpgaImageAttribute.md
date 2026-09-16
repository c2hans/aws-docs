---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFpgaImageAttribute.html
---

# ModifyFpgaImageAttribute
<a name="API_ModifyFpgaImageAttribute"></a>

Modifies the specified attribute of the specified Amazon FPGA Image (AFI).

## Request Parameters
<a name="API_ModifyFpgaImageAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The name of the attribute.
Type: String
Valid Values: `description | name | loadPermission | productCodes`
Required: No

 **Description**
A description for the AFI.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FpgaImageId**
The ID of the AFI.
Type: String
Required: Yes

 **LoadPermission**
The load permission for the AFI.
Type: [LoadPermissionModifications](API_LoadPermissionModifications.md) object
Required: No

 **Name**
A name for the AFI.
Type: String
Required: No

 **OperationType**
The operation type.
Type: String
Valid Values: `add | remove`
Required: No

 **ProductCode.N**
The product codes. After you add a product code to an AFI, it can't be removed. This parameter is valid only when modifying the `productCodes` attribute.
Type: Array of strings
Required: No

 **UserGroup.N**
The user groups. This parameter is valid only when modifying the `loadPermission` attribute.
Type: Array of strings
Required: No

 **UserId.N**
The AWS account IDs. This parameter is valid only when modifying the `loadPermission` attribute.
Type: Array of strings
Required: No

## Response Elements
<a name="API_ModifyFpgaImageAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **fpgaImageAttribute**
Information about the attribute.
Type: [FpgaImageAttribute](API_FpgaImageAttribute.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyFpgaImageAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyFpgaImageAttribute_Examples"></a>

### Example
<a name="API_ModifyFpgaImageAttribute_Example_1"></a>

This example adds load permissions for account ID `123456789012`.

#### Sample Request
<a name="API_ModifyFpgaImageAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyFpgaImageAttribute
&FpgaImageId=afi-0d123e21abcc85abc
&Attribute=loadPermission
&LoadPermission.Add.1.UserId=123456789012
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyFpgaImageAttribute_Example_1_Response"></a>

```
<ModifyFpgaImageAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>75837959-edf9-4183-ad01-6cb1example</requestId>
    <fpgaImageAttribute>
        <fpgaImageId>afi-0d123e21abcc85abc</fpgaImageId>
        <loadPermissions>
            <item>
                <userId>123456789012</userId>
            </item>
        </loadPermissions>
    </fpgaImageAttribute>
</ModifyFpgaImageAttributeResponse>
```

## See Also
<a name="API_ModifyFpgaImageAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyFpgaImageAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyFpgaImageAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyFpgaImageAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyFpgaImageAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyFpgaImageAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyFpgaImageAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyFpgaImageAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyFpgaImageAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyFpgaImageAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyFpgaImageAttribute)
