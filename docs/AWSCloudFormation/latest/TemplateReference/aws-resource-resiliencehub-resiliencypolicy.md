---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-resiliencehub-resiliencypolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHub::ResiliencyPolicy
<a name="aws-resource-resiliencehub-resiliencypolicy"></a>

Defines a resiliency policy.

**Note**
AWS Resilience Hub allows you to provide a value of zero for `rtoInSecs` and `rpoInSecs` of your resiliency policy. But, while assessing your application, the lowest possible assessment result is near zero. Hence, if you provide value zero for `rtoInSecs` and `rpoInSecs`, the estimated workload RTO and estimated workload RPO result will be near zero and the **Compliance status** for your application will be set to **Policy breached**.

## Syntax
<a name="aws-resource-resiliencehub-resiliencypolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-resiliencehub-resiliencypolicy-syntax.json"></a>

```
{
  "Type" : "AWS::ResilienceHub::ResiliencyPolicy",
  "Properties" : {
      "[DataLocationConstraint](#cfn-resiliencehub-resiliencypolicy-datalocationconstraint)" : {{String}},
      "[Policy](#cfn-resiliencehub-resiliencypolicy-policy)" : {{PolicyMap}},
      "[PolicyDescription](#cfn-resiliencehub-resiliencypolicy-policydescription)" : {{String}},
      "[PolicyName](#cfn-resiliencehub-resiliencypolicy-policyname)" : {{String}},
      "[Tags](#cfn-resiliencehub-resiliencypolicy-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Tier](#cfn-resiliencehub-resiliencypolicy-tier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-resiliencehub-resiliencypolicy-syntax.yaml"></a>

```
Type: AWS::ResilienceHub::ResiliencyPolicy
Properties:
  [DataLocationConstraint](#cfn-resiliencehub-resiliencypolicy-datalocationconstraint): {{String}}
  [Policy](#cfn-resiliencehub-resiliencypolicy-policy): {{
    PolicyMap}}
  [PolicyDescription](#cfn-resiliencehub-resiliencypolicy-policydescription): {{String}}
  [PolicyName](#cfn-resiliencehub-resiliencypolicy-policyname): {{String}}
  [Tags](#cfn-resiliencehub-resiliencypolicy-tags): {{
    {{Key}}: {{Value}}}}
  [Tier](#cfn-resiliencehub-resiliencypolicy-tier): {{String}}
```

## Properties
<a name="aws-resource-resiliencehub-resiliencypolicy-properties"></a>

`DataLocationConstraint`  <a name="cfn-resiliencehub-resiliencypolicy-datalocationconstraint"></a>
Specifies a high-level geographical location constraint for where your resilience policy data can be stored.
*Required*: No
*Type*: String
*Allowed values*: `AnyLocation | SameContinent | SameCountry`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Policy`  <a name="cfn-resiliencehub-resiliencypolicy-policy"></a>
The resiliency policy.
*Required*: Yes
*Type*: [PolicyMap](aws-properties-resiliencehub-resiliencypolicy-policymap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyDescription`  <a name="cfn-resiliencehub-resiliencypolicy-policydescription"></a>
Description of the resiliency policy.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyName`  <a name="cfn-resiliencehub-resiliencypolicy-policyname"></a>
The name of the policy
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-resiliencehub-resiliencypolicy-tags"></a>
Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,128}`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tier`  <a name="cfn-resiliencehub-resiliencypolicy-tier"></a>
The tier for this resiliency policy, ranging from the highest severity (`MissionCritical`) to lowest (`NonCritical`).
*Required*: Yes
*Type*: String
*Allowed values*: `MissionCritical | Critical | Important | CoreServices | NonCritical`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-resiliencehub-resiliencypolicy-return-values"></a>

### Ref
<a name="aws-resource-resiliencehub-resiliencypolicy-return-values-ref"></a>

The returned Amazon Resource Name (ARN) for the resiliency policy.

### Fn::GetAtt
<a name="aws-resource-resiliencehub-resiliencypolicy-return-values-fn--getatt"></a>

Amazon Resource Name (ARN) for the resiliency policy.

####
<a name="aws-resource-resiliencehub-resiliencypolicy-return-values-fn--getatt-fn--getatt"></a>

`PolicyArn`  <a name="PolicyArn-fn::getatt"></a>
Amazon Resource Name (ARN) of the resiliency policy.
