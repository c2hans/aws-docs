---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSecurityGroup.html
---

# DeleteSecurityGroup
<a name="API_DeleteSecurityGroup"></a>

Deletes a security group.

If you attempt to delete a security group that is associated with an instance or network interface, is referenced by another security group in the same VPC, or has a VPC association, the operation fails with `DependencyViolation`.

## Request Parameters
<a name="API_DeleteSecurityGroup_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **GroupId**
The ID of the security group.
Type: String
Required: No

 **GroupName**
[Default VPC] The name of the security group. You can specify either the security group name or the security group ID. For security groups in a nondefault VPC, you must specify the security group ID.
Type: String
Required: No

## Response Elements
<a name="API_DeleteSecurityGroup_ResponseElements"></a>

The following elements are returned by the service.

 **groupId**
The ID of the deleted security group.
Type: String

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, returns an error.
Type: Boolean

## Errors
<a name="API_DeleteSecurityGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteSecurityGroup_Examples"></a>

### Example
<a name="API_DeleteSecurityGroup_Example_1"></a>

This example deletes the specified security group.

#### Sample Request
<a name="API_DeleteSecurityGroup_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteSecurityGroup
&GroupId=sg-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteSecurityGroup_Example_1_Response"></a>

```
<DeleteSecurityGroupResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <return>true</return>
</DeleteSecurityGroupResponse>
```

## See Also
<a name="API_DeleteSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteSecurityGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteSecurityGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteSecurityGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteSecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteSecurityGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteSecurityGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteSecurityGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteSecurityGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteSecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteSecurityGroup)
