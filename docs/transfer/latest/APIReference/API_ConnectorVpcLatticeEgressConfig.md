---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ConnectorVpcLatticeEgressConfig.html
---

# ConnectorVpcLatticeEgressConfig
<a name="API_ConnectorVpcLatticeEgressConfig"></a>

VPC\_LATTICE egress configuration that specifies the Resource Configuration ARN and port for connecting to SFTP servers through customer VPCs. Requires a valid Resource Configuration with appropriate network access.

## Contents
<a name="API_ConnectorVpcLatticeEgressConfig_Contents"></a>

 ** ResourceConfigurationArn **   <a name="TransferFamily-Type-ConnectorVpcLatticeEgressConfig-ResourceConfigurationArn"></a>
ARN of the VPC\_LATTICE Resource Configuration that defines the target SFTP server location. Must point to a valid Resource Configuration in the customer's VPC with appropriate network connectivity to the SFTP server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}`
Required: Yes

 ** PortNumber **   <a name="TransferFamily-Type-ConnectorVpcLatticeEgressConfig-PortNumber"></a>
Port number for connecting to the SFTP server through VPC\_LATTICE. Defaults to 22 if not specified. Must match the port on which the target SFTP server is listening.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_ConnectorVpcLatticeEgressConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ConnectorVpcLatticeEgressConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ConnectorVpcLatticeEgressConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ConnectorVpcLatticeEgressConfig)
