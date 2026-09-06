---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedConnectorVpcLatticeEgressConfig.html
---

# DescribedConnectorVpcLatticeEgressConfig
<a name="API_DescribedConnectorVpcLatticeEgressConfig"></a>

VPC\_LATTICE egress configuration details in the response, containing the Resource Configuration ARN and port number currently configured for the connector.

## Contents
<a name="API_DescribedConnectorVpcLatticeEgressConfig_Contents"></a>

 ** ResourceConfigurationArn **   <a name="TransferFamily-Type-DescribedConnectorVpcLatticeEgressConfig-ResourceConfigurationArn"></a>
ARN of the VPC\_LATTICE Resource Configuration currently used by the connector. This Resource Configuration defines the network path to the SFTP server through the customer's VPC.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}`
Required: Yes

 ** PortNumber **   <a name="TransferFamily-Type-DescribedConnectorVpcLatticeEgressConfig-PortNumber"></a>
Port number currently configured for SFTP connections through VPC\_LATTICE. Shows the port on which the connector attempts to connect to the target SFTP server.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_DescribedConnectorVpcLatticeEgressConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedConnectorVpcLatticeEgressConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedConnectorVpcLatticeEgressConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedConnectorVpcLatticeEgressConfig)
