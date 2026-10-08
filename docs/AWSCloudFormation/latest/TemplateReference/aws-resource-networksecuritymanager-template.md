---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-template.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Template
<a name="aws-resource-networksecuritymanager-template"></a>

The `AWS::NetworkSecurityManager::Template` resource specifies an AWS Network Security Manager template. A template groups one or more rules so that you can reuse the same set of protections across policies. You can also associate rules with a policy directly, without using a template.

You reference a template from a policy, then roll the protections out to the accounts and resources selected by a scope. Templates created with this resource are always published in `ACTIVE` state; CloudFormation does not create templates in `DRAFT` state.

For conceptual information and guidance on writing rule configurations, see the [AWS Network Security Manager Developer Guide](https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html). For the default quotas that apply to your account, see [Quotas](https://docs.aws.amazon.com/network-security-manager/latest/devguide/quotas.html).

## Syntax
<a name="aws-resource-networksecuritymanager-template-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networksecuritymanager-template-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkSecurityManager::Template",
  "Properties" : {
      "[AssociatedRuleList](#cfn-networksecuritymanager-template-associatedrulelist)" : {{[ AssociatedRule, ... ]}},
      "[FirewallType](#cfn-networksecuritymanager-template-firewalltype)" : {{String}},
      "[Tags](#cfn-networksecuritymanager-template-tags)" : {{[ Tag, ... ]}},
      "[TemplateDescription](#cfn-networksecuritymanager-template-templatedescription)" : {{String}},
      "[TemplateName](#cfn-networksecuritymanager-template-templatename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-networksecuritymanager-template-syntax.yaml"></a>

```
Type: AWS::NetworkSecurityManager::Template
Properties:
  [AssociatedRuleList](#cfn-networksecuritymanager-template-associatedrulelist): {{
    - AssociatedRule}}
  [FirewallType](#cfn-networksecuritymanager-template-firewalltype): {{String}}
  [Tags](#cfn-networksecuritymanager-template-tags): {{
    - Tag}}
  [TemplateDescription](#cfn-networksecuritymanager-template-templatedescription): {{String}}
  [TemplateName](#cfn-networksecuritymanager-template-templatename): {{String}}
```

## Properties
<a name="aws-resource-networksecuritymanager-template-properties"></a>

`AssociatedRuleList`  <a name="cfn-networksecuritymanager-template-associatedrulelist"></a>
The rules associated with the template.
This property is required when you create a template. You must associate at least one rule; AWS Network Security Manager rejects a template that has no associated rules.
*Required*: Conditional
*Type*: Array of [AssociatedRule](aws-properties-networksecuritymanager-template-associatedrule.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallType`  <a name="cfn-networksecuritymanager-template-firewalltype"></a>
The type of firewall that the template configures. `WAF` specifies an AWS WAF template. All rules that you associate with the template must use the same firewall type.
This property is required when you create a template. You can't change the firewall type after you create the template.
*Required*: Conditional
*Type*: String
*Allowed values*: `WAF | NETWORK_FIREWALL | NETWORK_FIREWALL_V2 | IGW_FIREWALL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-networksecuritymanager-template-tags"></a>
The tags to assign to the template. Each tag is a key-value pair. You can add tags when you create the template and change them afterward without replacing the template. You can assign up to 200 tags to a template.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-networksecuritymanager-template-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateDescription`  <a name="cfn-networksecuritymanager-template-templatedescription"></a>
A description of the template.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9 _.:/=+\-@]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateName`  <a name="cfn-networksecuritymanager-template-templatename"></a>
The name of the template.
You can't change the name of a template after you create it.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-networksecuritymanager-template-return-values"></a>

### Ref
<a name="aws-resource-networksecuritymanager-template-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the template. For example:

 `{ "Ref": "myTemplate" }`

For a template named `common-waf-baseline`, `Ref` returns a value similar to `arn:aws:network-security-manager:us-east-1:123456789012:template:a1b2c3d4e5f6`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-networksecuritymanager-template-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-networksecuritymanager-template-return-values-fn--getatt-fn--getatt"></a>

`Status`  <a name="Status-fn::getatt"></a>
The current status of the template. Templates created with this resource are always published, so this value is always `ACTIVE`.
*Allowed Values*: `DRAFT` \| `ACTIVE`

`TemplateArn`  <a name="TemplateArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the template.

`TemplateId`  <a name="TemplateId-fn::getatt"></a>
The service-generated id of the template.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time when the resource was last updated. For a snapshot, this is the time when the snapshot was created.

`Version`  <a name="Version-fn::getatt"></a>
The version of the template. AWS Network Security Manager assigns version `1` when it publishes the template and increments the version each time the template is published again, including each time CloudFormation updates it.

## Examples
<a name="aws-resource-networksecuritymanager-template--examples"></a>

### Group a rule into a reusable template
<a name="aws-resource-networksecuritymanager-template--examples--Group_a_rule_into_a_reusable_template"></a>

#### YAML
<a name="aws-resource-networksecuritymanager-template--examples--Group_a_rule_into_a_reusable_template--yaml"></a>

```
                AWSTemplateFormatVersion: "2010-09-09"
                Description: Groups Network Security Manager rules into a reusable template.
                Resources:
                  AllowByDefaultRule:
                    Type: AWS::NetworkSecurityManager::Rule
                    Properties:
                      RuleName: allow-by-default
                      FirewallType: WAF
                      RuleType: CONFIGURATION
                      Configuration: '{"DefaultAction":{"Allow":{}}}'

                  BaselineTemplate:
                    Type: AWS::NetworkSecurityManager::Template
                    Properties:
                      TemplateName: waf-baseline
                      TemplateDescription: Baseline web ACL settings for every account.
                      FirewallType: WAF
                      AssociatedRuleList:
                        - RuleArn: !GetAtt AllowByDefaultRule.RuleArn
                Outputs:
                  TemplateArn:
                    Value: !GetAtt BaselineTemplate.TemplateArn
```
