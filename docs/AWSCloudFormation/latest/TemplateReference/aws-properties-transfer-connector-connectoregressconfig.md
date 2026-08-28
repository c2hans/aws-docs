---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-connector-connectoregressconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Connector ConnectorEgressConfig
<a name="aws-properties-transfer-connector-connectoregressconfig"></a>

Configuration structure that defines how traffic is routed from the connector to the SFTP server. Contains VPC Lattice settings when using VPC\_LATTICE egress type for private connectivity through customer VPCs.

## Syntax
<a name="aws-properties-transfer-connector-connectoregressconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-connector-connectoregressconfig-syntax.json"></a>

```
{
  "[VpcLattice](#cfn-transfer-connector-connectoregressconfig-vpclattice)" : {{ConnectorVpcLatticeEgressConfig}}
}
```

### YAML
<a name="aws-properties-transfer-connector-connectoregressconfig-syntax.yaml"></a>

```
  [VpcLattice](#cfn-transfer-connector-connectoregressconfig-vpclattice): {{
    ConnectorVpcLatticeEgressConfig}}
```

## Properties
<a name="aws-properties-transfer-connector-connectoregressconfig-properties"></a>

`VpcLattice`  <a name="cfn-transfer-connector-connectoregressconfig-vpclattice"></a>
VPC\_LATTICE configuration for routing connector traffic through customer VPCs. Enables private connectivity to SFTP servers without requiring public internet access or complex network configurations.
*Required*: Yes
*Type*: [ConnectorVpcLatticeEgressConfig](aws-properties-transfer-connector-connectorvpclatticeegressconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
