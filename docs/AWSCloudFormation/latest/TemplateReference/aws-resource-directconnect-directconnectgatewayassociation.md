---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directconnect-directconnectgatewayassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DirectConnect::DirectConnectGatewayAssociation
<a name="aws-resource-directconnect-directconnectgatewayassociation"></a>

Creates an association between a Direct Connect gateway and a virtual private gateway. The virtual private gateway must be attached to a VPC and must not be associated with another Direct Connect gateway.

If creating a Direct Connect gateway association between resources in separate AWS accounts, the CloudFormation stack account must own the virtual private gateway. The other account must own the Direct Connect gateway, and must have a role allowing the stack account to accept Direct Connect gateway association proposals.

For more information, see [Direct Connect gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html) in the * Direct Connect User Guide *.

## Syntax
<a name="aws-resource-directconnect-directconnectgatewayassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-directconnect-directconnectgatewayassociation-syntax.json"></a>

```
{
  "Type" : "AWS::DirectConnect::DirectConnectGatewayAssociation",
  "Properties" : {
      "[AcceptDirectConnectGatewayAssociationProposalRoleArn](#cfn-directconnect-directconnectgatewayassociation-acceptdirectconnectgatewayassociationproposalrolearn)" : {{String}},
      "[AllowedPrefixesToDirectConnectGateway](#cfn-directconnect-directconnectgatewayassociation-allowedprefixestodirectconnectgateway)" : {{[ String, ... ]}},
      "[AssociatedGatewayId](#cfn-directconnect-directconnectgatewayassociation-associatedgatewayid)" : {{String}},
      "[DirectConnectGatewayId](#cfn-directconnect-directconnectgatewayassociation-directconnectgatewayid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-directconnect-directconnectgatewayassociation-syntax.yaml"></a>

```
Type: AWS::DirectConnect::DirectConnectGatewayAssociation
Properties:
  [AcceptDirectConnectGatewayAssociationProposalRoleArn](#cfn-directconnect-directconnectgatewayassociation-acceptdirectconnectgatewayassociationproposalrolearn): {{String}}
  [AllowedPrefixesToDirectConnectGateway](#cfn-directconnect-directconnectgatewayassociation-allowedprefixestodirectconnectgateway): {{
    - String}}
  [AssociatedGatewayId](#cfn-directconnect-directconnectgatewayassociation-associatedgatewayid): {{String}}
  [DirectConnectGatewayId](#cfn-directconnect-directconnectgatewayassociation-directconnectgatewayid): {{String}}
```

## Properties
<a name="aws-resource-directconnect-directconnectgatewayassociation-properties"></a>

`AcceptDirectConnectGatewayAssociationProposalRoleArn`  <a name="cfn-directconnect-directconnectgatewayassociation-acceptdirectconnectgatewayassociationproposalrolearn"></a>
The Amazon Resource Name (ARN) of the role in a separate account to accept the Direct Connect Gateway association proposal. The role needs to have `directconnect:AcceptDirectConnectGatewayAssociationProposal` permissions.
This should only be used when creating an association with a Direct Connect gateway in a separate AWS account.
*Required*: Conditional
*Type*: String
*Pattern*: `^arn:aws[a-z-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AllowedPrefixesToDirectConnectGateway`  <a name="cfn-directconnect-directconnectgatewayassociation-allowedprefixestodirectconnectgateway"></a>
The Amazon VPC prefixes to advertise to the Direct Connect gateway.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssociatedGatewayId`  <a name="cfn-directconnect-directconnectgatewayassociation-associatedgatewayid"></a>
The ID or ARN of the associated gateway.
*Required*: Yes
*Type*: String
*Pattern*: `^((arn:aws[a-z-]*:ec2:[a-z0-9-]+:[0-9]{12}:(vpn-gateway/vgw|transit-gateway/tgw))|(vgw|tgw))-[a-zA-Z0-9]{8,32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DirectConnectGatewayId`  <a name="cfn-directconnect-directconnectgatewayassociation-directconnectgatewayid"></a>
The ID or ARN of the Direct Connect gateway.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws[a-z-]*:directconnect::[0-9]{12}:dx-gateway/)?[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-directconnect-directconnectgatewayassociation-return-values"></a>

### Ref
<a name="aws-resource-directconnect-directconnectgatewayassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the Direct Connect gateway association.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-directconnect-directconnectgatewayassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-directconnect-directconnectgatewayassociation-return-values-fn--getatt-fn--getatt"></a>

`AssociationId`  <a name="AssociationId-fn::getatt"></a>
The ID of the Direct Connect gateway association.

## Examples
<a name="aws-resource-directconnect-directconnectgatewayassociation--examples"></a>

### Direct Connect gateway association with a virtual private gateway in the same account
<a name="aws-resource-directconnect-directconnectgatewayassociation--examples--Direct_Connect_gateway_association_with_a_virtual_private_gateway_in_the_same_account"></a>

This example shows a basic Direct Connect gateway association with a virtual private gateway.

#### JSON
<a name="aws-resource-directconnect-directconnectgatewayassociation--examples--Direct_Connect_gateway_association_with_a_virtual_private_gateway_in_the_same_account--json"></a>

```
{
  "Resources": {
    "myDirectConnectGateway": {
      "Type": "AWS::DirectConnect::DirectConnectGateway",
      "Properties": {
        "DirectConnectGatewayName": "cfn-directconnectgateway-example",
        "AmazonSideAsn": "65412"
      }
    },
    "myDirectConnectGatewayAssociation": {
      "Type": "AWS::DirectConnect::DirectConnectGatewayAssociation",
      "Properties": {
        "AssociatedGatewayId": "vgw-aba37db6",
        "DirectConnectGatewayId": {
          "Ref": "myDirectConnectGateway"
        },
        "AllowedPrefixesToDirectConnectGateway": [
          "10.0.0.0/24"
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-directconnect-directconnectgatewayassociation--examples--Direct_Connect_gateway_association_with_a_virtual_private_gateway_in_the_same_account--yaml"></a>

```
Resources:
  myDirectConnectGateway:
    Type: AWS::DirectConnect::DirectConnectGateway
    Properties:
      DirectConnectGatewayName: cfn-directconnectgateway-example
      AmazonSideAsn: '65412'
  myDirectConnectGatewayAssociation:
    Type: AWS::DirectConnect::DirectConnectGatewayAssociation
    Properties:
      AssociationGatewayId: vgw-aba37db6
      DirectConnectGatewayId: !Ref myDirectConnectGateway
      AllowedPrefixesToDirectConnectGateway:
      - 10.0.0.0/24
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
