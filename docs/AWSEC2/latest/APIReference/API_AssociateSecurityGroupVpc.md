---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateSecurityGroupVpc.html
---

# AssociateSecurityGroupVpc
<a name="API_AssociateSecurityGroupVpc"></a>

Associates a security group with another VPC in the same Region. This enables you to use the same security group with network interfaces and instances in the specified VPC.

**Note**
The VPC you want to associate the security group with must be in the same Region.
You can associate the security group with another VPC if your account owns the VPC or if the VPC was shared with you.
You must own the security group.
You cannot use this feature with default security groups.
You cannot use this feature with the default VPC.

## Request Parameters
<a name="API_AssociateSecurityGroupVpc_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **GroupId**
A security group ID.
Type: String
Required: Yes

 **VpcId**
A VPC ID.
Type: String
Required: Yes

## Response Elements
<a name="API_AssociateSecurityGroupVpc_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **state**
The state of the association.
Type: String
Valid Values: `associating | associated | association-failed | disassociating | disassociated | disassociation-failed`

## Errors
<a name="API_AssociateSecurityGroupVpc_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_AssociateSecurityGroupVpc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateSecurityGroupVpc)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateSecurityGroupVpc)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateSecurityGroupVpc)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateSecurityGroupVpc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateSecurityGroupVpc)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateSecurityGroupVpc)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateSecurityGroupVpc)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateSecurityGroupVpc)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateSecurityGroupVpc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateSecurityGroupVpc)
