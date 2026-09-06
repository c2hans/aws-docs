---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcTenancy.html
---

# ModifyVpcTenancy
<a name="API_ModifyVpcTenancy"></a>

Modifies the instance tenancy attribute of the specified VPC. You can change the instance tenancy attribute of a VPC to `default` only. You cannot change the instance tenancy attribute to `dedicated`.

After you modify the tenancy of the VPC, any new instances that you launch into the VPC have a tenancy of `default`, unless you specify otherwise during launch. The tenancy of any existing instances in the VPC is not affected.

For more information, see [Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_ModifyVpcTenancy_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceTenancy**
The instance tenancy attribute for the VPC.
Type: String
Valid Values: `default`
Required: Yes

 **VpcId**
The ID of the VPC.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyVpcTenancy_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, returns an error.
Type: Boolean

## Errors
<a name="API_ModifyVpcTenancy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyVpcTenancy_Examples"></a>

### Example
<a name="API_ModifyVpcTenancy_Example_1"></a>

This example modifies the tenancy of `vpc-1a2b3c4d` to `default`.

#### Sample Request
<a name="API_ModifyVpcTenancy_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVpcTenancy
&VpcId=vpc-1a2b3c4d
&InstanceTenancy=default
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyVpcTenancy_Example_1_Response"></a>

```
<ModifyVpcTenancyResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <return>true</return>
    <requestId>125acea6-ba5c-4c6e-8e17-example</requestId>
</ModifyVpcTenancyResponse>
```

## See Also
<a name="API_ModifyVpcTenancy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVpcTenancy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVpcTenancy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVpcTenancy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVpcTenancy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVpcTenancy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVpcTenancy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVpcTenancy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVpcTenancy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVpcTenancy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVpcTenancy)
