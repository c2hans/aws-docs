---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_UpdateConnectorVpcLatticeEgressConfig.html
---

# UpdateConnectorVpcLatticeEgressConfig
<a name="API_UpdateConnectorVpcLatticeEgressConfig"></a>

VPC\_LATTICE egress configuration updates for modifying how the connector routes traffic through customer VPCs. Changes to these settings may require connector restart to take effect.

## Contents
<a name="API_UpdateConnectorVpcLatticeEgressConfig_Contents"></a>

 ** PortNumber **   <a name="TransferFamily-Type-UpdateConnectorVpcLatticeEgressConfig-PortNumber"></a>
Updated port number for SFTP connections through VPC\_LATTICE. Change this if the target SFTP server port has been modified or if connecting to a different server endpoint.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** ResourceConfigurationArn **   <a name="TransferFamily-Type-UpdateConnectorVpcLatticeEgressConfig-ResourceConfigurationArn"></a>
Updated ARN of the VPC\_LATTICE Resource Configuration. Use this to change the target SFTP server location or modify the network path through the customer's VPC infrastructure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}`
Required: No

## See Also
<a name="API_UpdateConnectorVpcLatticeEgressConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/UpdateConnectorVpcLatticeEgressConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/UpdateConnectorVpcLatticeEgressConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/UpdateConnectorVpcLatticeEgressConfig)
