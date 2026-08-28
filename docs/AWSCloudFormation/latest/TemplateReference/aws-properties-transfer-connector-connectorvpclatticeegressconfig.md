---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-connector-connectorvpclatticeegressconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Connector ConnectorVpcLatticeEgressConfig
<a name="aws-properties-transfer-connector-connectorvpclatticeegressconfig"></a>

VPC\_LATTICE egress configuration that specifies the Resource Configuration ARN and port for connecting to SFTP servers through customer VPCs. Requires a valid Resource Configuration with appropriate network access.

## Syntax
<a name="aws-properties-transfer-connector-connectorvpclatticeegressconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-connector-connectorvpclatticeegressconfig-syntax.json"></a>

```
{
  "[PortNumber](#cfn-transfer-connector-connectorvpclatticeegressconfig-portnumber)" : {{Integer}},
  "[ResourceConfigurationArn](#cfn-transfer-connector-connectorvpclatticeegressconfig-resourceconfigurationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-connector-connectorvpclatticeegressconfig-syntax.yaml"></a>

```
  [PortNumber](#cfn-transfer-connector-connectorvpclatticeegressconfig-portnumber): {{Integer}}
  [ResourceConfigurationArn](#cfn-transfer-connector-connectorvpclatticeegressconfig-resourceconfigurationarn): {{String}}
```

## Properties
<a name="aws-properties-transfer-connector-connectorvpclatticeegressconfig-properties"></a>

`PortNumber`  <a name="cfn-transfer-connector-connectorvpclatticeegressconfig-portnumber"></a>
Port number for connecting to the SFTP server through VPC\_LATTICE. Defaults to 22 if not specified. Must match the port on which the target SFTP server is listening.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceConfigurationArn`  <a name="cfn-transfer-connector-connectorvpclatticeegressconfig-resourceconfigurationarn"></a>
ARN of the VPC\_LATTICE Resource Configuration that defines the target SFTP server location. Must point to a valid Resource Configuration in the customer's VPC with appropriate network connectivity to the SFTP server.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
