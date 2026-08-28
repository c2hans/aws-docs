---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-managedresourcedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ManagedResourceDetails
<a name="aws-properties-bedrockagentcore-gatewaytarget-managedresourcedetails"></a>

Details of a resource created and managed by the gateway for private endpoint connectivity.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-managedresourcedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-managedresourcedetails-syntax.json"></a>

```
{
  "[Domain](#cfn-bedrockagentcore-gatewaytarget-managedresourcedetails-domain)" : {{String}},
  "[ResourceAssociationArn](#cfn-bedrockagentcore-gatewaytarget-managedresourcedetails-resourceassociationarn)" : {{String}},
  "[ResourceGatewayArn](#cfn-bedrockagentcore-gatewaytarget-managedresourcedetails-resourcegatewayarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-managedresourcedetails-syntax.yaml"></a>

```
  [Domain](#cfn-bedrockagentcore-gatewaytarget-managedresourcedetails-domain): {{String}}
  [ResourceAssociationArn](#cfn-bedrockagentcore-gatewaytarget-managedresourcedetails-resourceassociationarn): {{String}}
  [ResourceGatewayArn](#cfn-bedrockagentcore-gatewaytarget-managedresourcedetails-resourcegatewayarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-managedresourcedetails-properties"></a>

`Domain`  <a name="cfn-bedrockagentcore-gatewaytarget-managedresourcedetails-domain"></a>
The domain associated with this managed resource.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAssociationArn`  <a name="cfn-bedrockagentcore-gatewaytarget-managedresourcedetails-resourceassociationarn"></a>
The ARN of the service network resource association.
*Required*: No
*Type*: String
*Pattern*: `^(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkresourceassociation/)?snra-[0-9a-f]{17}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceGatewayArn`  <a name="cfn-bedrockagentcore-gatewaytarget-managedresourcedetails-resourcegatewayarn"></a>
The ARN of the VPC Lattice resource gateway created in your account.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
