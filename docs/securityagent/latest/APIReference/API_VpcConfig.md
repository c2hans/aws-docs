---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_VpcConfig.html
---

# VpcConfig
<a name="API_VpcConfig"></a>

The VPC configuration for a pentest, specifying the VPC, security groups, and subnets to use during testing.

## Contents
<a name="API_VpcConfig_Contents"></a>

 ** securityGroupArns **   <a name="securityagent-Type-VpcConfig-securityGroupArns"></a>
The Amazon Resource Names (ARNs) of the security groups for the VPC configuration.
Type: Array of strings
Required: No

 ** subnetArns **   <a name="securityagent-Type-VpcConfig-subnetArns"></a>
The Amazon Resource Names (ARNs) of the subnets for the VPC configuration.
Type: Array of strings
Required: No

 ** vpcArn **   <a name="securityagent-Type-VpcConfig-vpcArn"></a>
The Amazon Resource Name (ARN) of the VPC.
Type: String
Required: No

## See Also
<a name="API_VpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/VpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/VpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/VpcConfig)
