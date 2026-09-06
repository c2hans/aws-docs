---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rtbfabric-linkroutingrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::LinkRoutingRule
<a name="aws-resource-rtbfabric-linkroutingrule"></a>

<a name="aws-resource-rtbfabric-linkroutingrule-description"></a>The `AWS::RTBFabric::LinkRoutingRule` resource Property description not available. for RTBFabric.

## Syntax
<a name="aws-resource-rtbfabric-linkroutingrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rtbfabric-linkroutingrule-syntax.json"></a>

```
{
  "Type" : "AWS::RTBFabric::LinkRoutingRule",
  "Properties" : {
      "[Conditions](#cfn-rtbfabric-linkroutingrule-conditions)" : {{RuleCondition}},
      "[GatewayId](#cfn-rtbfabric-linkroutingrule-gatewayid)" : {{String}},
      "[LinkId](#cfn-rtbfabric-linkroutingrule-linkid)" : {{String}},
      "[Priority](#cfn-rtbfabric-linkroutingrule-priority)" : {{Integer}},
      "[Tags](#cfn-rtbfabric-linkroutingrule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rtbfabric-linkroutingrule-syntax.yaml"></a>

```
Type: AWS::RTBFabric::LinkRoutingRule
Properties:
  [Conditions](#cfn-rtbfabric-linkroutingrule-conditions): {{
    RuleCondition}}
  [GatewayId](#cfn-rtbfabric-linkroutingrule-gatewayid): {{String}}
  [LinkId](#cfn-rtbfabric-linkroutingrule-linkid): {{String}}
  [Priority](#cfn-rtbfabric-linkroutingrule-priority): {{Integer}}
  [Tags](#cfn-rtbfabric-linkroutingrule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rtbfabric-linkroutingrule-properties"></a>

`Conditions`  <a name="cfn-rtbfabric-linkroutingrule-conditions"></a>
The conditions for the routing rule.
*Required*: Yes
*Type*: [RuleCondition](aws-properties-rtbfabric-linkroutingrule-rulecondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GatewayId`  <a name="cfn-rtbfabric-linkroutingrule-gatewayid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^rtb-gw-[a-z0-9-]{1,25}$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LinkId`  <a name="cfn-rtbfabric-linkroutingrule-linkid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^link-[a-z0-9-]{1,25}$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Priority`  <a name="cfn-rtbfabric-linkroutingrule-priority"></a>
The priority of the routing rule.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-rtbfabric-linkroutingrule-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-rtbfabric-linkroutingrule-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rtbfabric-linkroutingrule-return-values"></a>

### Ref
<a name="aws-resource-rtbfabric-linkroutingrule-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rtbfabric-linkroutingrule-return-values-fn--getatt"></a>

####
<a name="aws-resource-rtbfabric-linkroutingrule-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
Property description not available.

`RuleId`  <a name="RuleId-fn::getatt"></a>
The unique identifier of the routing rule.

`Status`  <a name="Status-fn::getatt"></a>
The status of the routing rule.

`UpdatedTimestamp`  <a name="UpdatedTimestamp-fn::getatt"></a>
Property description not available.
