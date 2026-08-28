---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyAccountVpcEncryptionControl.html
---

# ModifyAccountVpcEncryptionControl
<a name="API_ModifyAccountVpcEncryptionControl"></a>

Modifies the account-level VPC Encryption Control configuration. This sets the encryption control mode and resource exclusions that apply to the VPCs in your account. VPC Encryption Control enables you to enforce encryption for all data in transit within and between VPCs to meet compliance requirements.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_ModifyAccountVpcEncryptionControl_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EgressOnlyInternetGateway**
Specifies whether to exclude egress-only internet gateway resource from account-level encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 **ElasticFileSystem**
Specifies whether to exclude Elastic File System service from account-level encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 **InternetGateway**
Specifies whether to exclude internet gateway resource from account-level encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 **Lambda**
Specifies whether to exclude Lambda service from account-level encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 **Mode**
The encryption mode for the account encryption control configuration.
Type: String
Valid Values: `unmanaged | attempt-monitor | attempt-enforce`
Required: No

 **NatGateway**
Specifies whether to exclude NAT gateway resource from account-level encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 **VirtualPrivateGateway**
Specifies whether to exclude virtual private gateway resource from account-level encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 **VpcLattice**
Specifies whether to exclude VPC Lattice service from account-level encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

 **VpcPeering**
Specifies whether to exclude VPC peering connection resource from account-level encryption enforcement.
Type: String
Valid Values: `enable | disable`
Required: No

## Response Elements
<a name="API_ModifyAccountVpcEncryptionControl_ResponseElements"></a>

The following elements are returned by the service.

 **accountVpcEncryptionControl**
Information about the account-level VPC Encryption Control configuration.
Type: [AccountVpcEncryptionControl](API_AccountVpcEncryptionControl.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyAccountVpcEncryptionControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyAccountVpcEncryptionControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyAccountVpcEncryptionControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyAccountVpcEncryptionControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyAccountVpcEncryptionControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyAccountVpcEncryptionControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyAccountVpcEncryptionControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyAccountVpcEncryptionControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyAccountVpcEncryptionControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyAccountVpcEncryptionControl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyAccountVpcEncryptionControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyAccountVpcEncryptionControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
