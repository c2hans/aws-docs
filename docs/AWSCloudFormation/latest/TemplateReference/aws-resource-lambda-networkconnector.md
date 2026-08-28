---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-networkconnector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::NetworkConnector
<a name="aws-resource-lambda-networkconnector"></a>

The `AWS::Lambda::NetworkConnector` resource creates a network connector that enables Lambda MicroVMs to reach resources in a virtual private cloud (VPC). A network connector provisions elastic network interfaces (ENIs) in the subnets you specify, providing a managed network path to private resources such as databases, caches, and internal APIs.

## Syntax
<a name="aws-resource-lambda-networkconnector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-networkconnector-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::NetworkConnector",
  "Properties" : {
      "[Configuration](#cfn-lambda-networkconnector-configuration)" : {{Config}},
      "[Name](#cfn-lambda-networkconnector-name)" : {{String}},
      "[OperatorRole](#cfn-lambda-networkconnector-operatorrole)" : {{String}},
      "[Tags](#cfn-lambda-networkconnector-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lambda-networkconnector-syntax.yaml"></a>

```
Type: AWS::Lambda::NetworkConnector
Properties:
  [Configuration](#cfn-lambda-networkconnector-configuration): {{
    Config}}
  [Name](#cfn-lambda-networkconnector-name): {{String}}
  [OperatorRole](#cfn-lambda-networkconnector-operatorrole): {{String}}
  [Tags](#cfn-lambda-networkconnector-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lambda-networkconnector-properties"></a>

`Configuration`  <a name="cfn-lambda-networkconnector-configuration"></a>
The network configuration for the connector. Specify a `VpcEgressConfiguration` to enable outbound traffic routing through your VPC.
*Required*: Yes
*Type*: [Config](aws-properties-lambda-networkconnector-config.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-lambda-networkconnector-name"></a>
A unique name for the network connector within your account and Region. Must be 1 to 64 alphanumeric characters, hyphens, or underscores.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)|[a-zA-Z0-9_-]{1,64}$`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OperatorRole`  <a name="cfn-lambda-networkconnector-operatorrole"></a>
The ARN of the IAM role that Lambda assumes to manage elastic network interfaces in your VPC. This role must have permissions for `ec2:CreateNetworkInterface` and related describe operations.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `0`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-lambda-networkconnector-tags"></a>
A list of tags to apply to the network connector. Use tags to categorize network connectors for cost allocation, access control, or operational management.
*Required*: No
*Type*: Array of [Tag](aws-properties-lambda-networkconnector-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-networkconnector-return-values"></a>

### Ref
<a name="aws-resource-lambda-networkconnector-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the network connector.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-networkconnector-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lambda-networkconnector-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the network connector.

`State`  <a name="State-fn::getatt"></a>
Current state of the network connector. Valid values are `PENDING`, `ACTIVE`, `INACTIVE`, `FAILED`, `DELETING`, and `DELETE_FAILED`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
