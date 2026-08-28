---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_UpdateConnectorEgressConfig.html
---

# UpdateConnectorEgressConfig
<a name="API_UpdateConnectorEgressConfig"></a>

Structure for updating the egress configuration of an existing connector. Allows modification of how traffic is routed from the connector to the SFTP server, including VPC\_LATTICE settings.

## Contents
<a name="API_UpdateConnectorEgressConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** VpcLattice **   <a name="TransferFamily-Type-UpdateConnectorEgressConfig-VpcLattice"></a>
VPC\_LATTICE configuration updates for the connector. Use this to modify the Resource Configuration ARN or port number for VPC-based connectivity.
Type: [UpdateConnectorVpcLatticeEgressConfig](API_UpdateConnectorVpcLatticeEgressConfig.md) object
Required: No

## See Also
<a name="API_UpdateConnectorEgressConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/UpdateConnectorEgressConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/UpdateConnectorEgressConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/UpdateConnectorEgressConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
