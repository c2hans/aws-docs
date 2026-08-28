---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedConnectorEgressConfig.html
---

# DescribedConnectorEgressConfig
<a name="API_DescribedConnectorEgressConfig"></a>

Response structure containing the current egress configuration details for the connector. Shows how traffic is currently routed from the connector to the SFTP server.

## Contents
<a name="API_DescribedConnectorEgressConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** VpcLattice **   <a name="TransferFamily-Type-DescribedConnectorEgressConfig-VpcLattice"></a>
VPC\_LATTICE configuration details in the response, showing the current Resource Configuration ARN and port settings for VPC-based connectivity.
Type: [DescribedConnectorVpcLatticeEgressConfig](API_DescribedConnectorVpcLatticeEgressConfig.md) object
Required: No

## See Also
<a name="API_DescribedConnectorEgressConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedConnectorEgressConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedConnectorEgressConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedConnectorEgressConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
