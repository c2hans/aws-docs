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
