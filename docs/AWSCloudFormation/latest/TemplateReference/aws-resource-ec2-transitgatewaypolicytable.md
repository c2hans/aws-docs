---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewaypolicytable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayPolicyTable
<a name="aws-resource-ec2-transitgatewaypolicytable"></a>

Describes a transit gateway policy table.

## Syntax
<a name="aws-resource-ec2-transitgatewaypolicytable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewaypolicytable-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayPolicyTable",
  "Properties" : {
      "[Tags](#cfn-ec2-transitgatewaypolicytable-tags)" : {{[ Tag, ... ]}},
      "[TransitGatewayId](#cfn-ec2-transitgatewaypolicytable-transitgatewayid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewaypolicytable-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayPolicyTable
Properties:
  [Tags](#cfn-ec2-transitgatewaypolicytable-tags): {{
    - Tag}}
  [TransitGatewayId](#cfn-ec2-transitgatewaypolicytable-transitgatewayid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewaypolicytable-properties"></a>

`Tags`  <a name="cfn-ec2-transitgatewaypolicytable-tags"></a>
he key-value pairs associated with the transit gateway policy table.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-transitgatewaypolicytable-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitGatewayId`  <a name="cfn-ec2-transitgatewaypolicytable-transitgatewayid"></a>
The ID of the transit gateway.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewaypolicytable-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewaypolicytable-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-transitgatewaypolicytable-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-transitgatewaypolicytable-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The timestamp when the transit gateway policy table was created.

`State`  <a name="State-fn::getatt"></a>
The state of the transit gateway policy table

`TransitGatewayPolicyTableId`  <a name="TransitGatewayPolicyTableId-fn::getatt"></a>
The ID of the transit gateway policy table.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
