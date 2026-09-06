---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ConnectorEgressConfig.html
---

# ConnectorEgressConfig
<a name="API_ConnectorEgressConfig"></a>

Configuration structure that defines how traffic is routed from the connector to the SFTP server. Contains VPC Lattice settings when using VPC\_LATTICE egress type for private connectivity through customer VPCs.

## Contents
<a name="API_ConnectorEgressConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** VpcLattice **   <a name="TransferFamily-Type-ConnectorEgressConfig-VpcLattice"></a>
VPC\_LATTICE configuration for routing connector traffic through customer VPCs. Enables private connectivity to SFTP servers without requiring public internet access or complex network configurations.
Type: [ConnectorVpcLatticeEgressConfig](API_ConnectorVpcLatticeEgressConfig.md) object
Required: No

## See Also
<a name="API_ConnectorEgressConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ConnectorEgressConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ConnectorEgressConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ConnectorEgressConfig)
