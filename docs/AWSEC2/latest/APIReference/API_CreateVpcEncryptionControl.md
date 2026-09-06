---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEncryptionControl.html
---

# CreateVpcEncryptionControl
<a name="API_CreateVpcEncryptionControl"></a>

Creates a VPC Encryption Control configuration for a specified VPC. VPC Encryption Control enables you to enforce encryption for all data in transit within and between VPCs to meet compliance requirements for standards like HIPAA, FedRAMP, and PCI DSS.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateVpcEncryptionControl_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TagSpecification.N**
The tags to apply to the VPC Encryption Control resource.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VpcId**
The ID of the VPC for which to create the encryption control configuration.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateVpcEncryptionControl_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **vpcEncryptionControl**
Information about the VPC Encryption Control configuration.
Type: [VpcEncryptionControl](API_VpcEncryptionControl.md) object

## Errors
<a name="API_CreateVpcEncryptionControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateVpcEncryptionControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVpcEncryptionControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVpcEncryptionControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVpcEncryptionControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVpcEncryptionControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVpcEncryptionControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVpcEncryptionControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVpcEncryptionControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVpcEncryptionControl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVpcEncryptionControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVpcEncryptionControl)
