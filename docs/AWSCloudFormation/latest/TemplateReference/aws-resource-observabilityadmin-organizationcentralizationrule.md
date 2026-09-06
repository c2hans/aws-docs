---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-observabilityadmin-organizationcentralizationrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule
<a name="aws-resource-observabilityadmin-organizationcentralizationrule"></a>

Defines how telemetry data should be centralized across an AWS Organization, including source and destination configurations.

## Syntax
<a name="aws-resource-observabilityadmin-organizationcentralizationrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-observabilityadmin-organizationcentralizationrule-syntax.json"></a>

```
{
  "Type" : "AWS::ObservabilityAdmin::OrganizationCentralizationRule",
  "Properties" : {
      "[Rule](#cfn-observabilityadmin-organizationcentralizationrule-rule)" : {{CentralizationRule}},
      "[RuleName](#cfn-observabilityadmin-organizationcentralizationrule-rulename)" : {{String}},
      "[Tags](#cfn-observabilityadmin-organizationcentralizationrule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-observabilityadmin-organizationcentralizationrule-syntax.yaml"></a>

```
Type: AWS::ObservabilityAdmin::OrganizationCentralizationRule
Properties:
  [Rule](#cfn-observabilityadmin-organizationcentralizationrule-rule): {{
    CentralizationRule}}
  [RuleName](#cfn-observabilityadmin-organizationcentralizationrule-rulename): {{String}}
  [Tags](#cfn-observabilityadmin-organizationcentralizationrule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-observabilityadmin-organizationcentralizationrule-properties"></a>

`Rule`  <a name="cfn-observabilityadmin-organizationcentralizationrule-rule"></a>
Property description not available.
*Required*: Yes
*Type*: [CentralizationRule](aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleName`  <a name="cfn-observabilityadmin-organizationcentralizationrule-rulename"></a>
The name of the organization centralization rule.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z-]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-observabilityadmin-organizationcentralizationrule-tags"></a>
 A key-value pair to filter resources based on tags associated with the resource. For more information about tags, see [What are tags?](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html)
*Required*: No
*Type*: Array of [Tag](aws-properties-observabilityadmin-organizationcentralizationrule-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-observabilityadmin-organizationcentralizationrule-return-values"></a>

### Ref
<a name="aws-resource-observabilityadmin-organizationcentralizationrule-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-observabilityadmin-organizationcentralizationrule-return-values-fn--getatt"></a>

####
<a name="aws-resource-observabilityadmin-organizationcentralizationrule-return-values-fn--getatt-fn--getatt"></a>

`RuleArn`  <a name="RuleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the organization centralization rule.
