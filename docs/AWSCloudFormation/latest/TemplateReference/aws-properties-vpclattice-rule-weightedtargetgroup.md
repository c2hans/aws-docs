---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-rule-weightedtargetgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Rule WeightedTargetGroup
<a name="aws-properties-vpclattice-rule-weightedtargetgroup"></a>

Describes the weight of a target group.

## Syntax
<a name="aws-properties-vpclattice-rule-weightedtargetgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-rule-weightedtargetgroup-syntax.json"></a>

```
{
  "[TargetGroupIdentifier](#cfn-vpclattice-rule-weightedtargetgroup-targetgroupidentifier)" : {{String}},
  "[Weight](#cfn-vpclattice-rule-weightedtargetgroup-weight)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-vpclattice-rule-weightedtargetgroup-syntax.yaml"></a>

```
  [TargetGroupIdentifier](#cfn-vpclattice-rule-weightedtargetgroup-targetgroupidentifier): {{String}}
  [Weight](#cfn-vpclattice-rule-weightedtargetgroup-weight): {{Integer}}
```

## Properties
<a name="aws-properties-vpclattice-rule-weightedtargetgroup-properties"></a>

`TargetGroupIdentifier`  <a name="cfn-vpclattice-rule-weightedtargetgroup-targetgroupidentifier"></a>
The ID of the target group.
*Required*: Yes
*Type*: String
*Pattern*: `^((tg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}))$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-vpclattice-rule-weightedtargetgroup-weight"></a>
Only required if you specify multiple target groups for a forward action. The weight determines how requests are distributed to the target group. For example, if you specify two target groups, each with a weight of 10, each target group receives half the requests. If you specify two target groups, one with a weight of 10 and the other with a weight of 20, the target group with a weight of 20 receives twice as many requests as the other target group. If there's only one target group specified, then the default value is 100.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `999`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
