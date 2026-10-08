---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Rule
<a name="aws-resource-networksecuritymanager-rule"></a>

The `AWS::NetworkSecurityManager::Rule` resource specifies an AWS Network Security Manager rule. A rule defines a network security configuration to enforce, such as an AWS WAF rule group or a single web ACL setting.

You reference a rule from a template or a policy, then roll the protections out to the accounts and resources selected by a scope. Rules created with this resource are always published in `ACTIVE` state; CloudFormation does not create rules in `DRAFT` state.

For conceptual information and guidance on writing rule configurations, see the [AWS Network Security Manager Developer Guide](https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html).

## Syntax
<a name="aws-resource-networksecuritymanager-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networksecuritymanager-rule-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkSecurityManager::Rule",
  "Properties" : {
      "[Configuration](#cfn-networksecuritymanager-rule-configuration)" : {{String}},
      "[FirewallType](#cfn-networksecuritymanager-rule-firewalltype)" : {{String}},
      "[RuleDescription](#cfn-networksecuritymanager-rule-ruledescription)" : {{String}},
      "[RuleName](#cfn-networksecuritymanager-rule-rulename)" : {{String}},
      "[RuleType](#cfn-networksecuritymanager-rule-ruletype)" : {{String}},
      "[Tags](#cfn-networksecuritymanager-rule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-networksecuritymanager-rule-syntax.yaml"></a>

```
Type: AWS::NetworkSecurityManager::Rule
Properties:
  [Configuration](#cfn-networksecuritymanager-rule-configuration): {{String}}
  [FirewallType](#cfn-networksecuritymanager-rule-firewalltype): {{String}}
  [RuleDescription](#cfn-networksecuritymanager-rule-ruledescription): {{String}}
  [RuleName](#cfn-networksecuritymanager-rule-rulename): {{String}}
  [RuleType](#cfn-networksecuritymanager-rule-ruletype): {{String}}
  [Tags](#cfn-networksecuritymanager-rule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-networksecuritymanager-rule-properties"></a>

`Configuration`  <a name="cfn-networksecuritymanager-rule-configuration"></a>
The firewall configuration for the rule, as a JSON string. The structure depends on the values of `FirewallType` and `RuleType`. For an AWS WAF`INSPECTION` rule, provide an AWS WAF rule group. For an AWS WAF`CONFIGURATION` rule, provide a single web ACL setting, such as `DefaultAction` or `VisibilityConfig`.
This property is a JSON string, not a JSON object. In a template, supply the configuration as a quoted string, or generate it with the [Fn::ToJsonString](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-tojsonstring.html) intrinsic function.
This property is required when you create a rule.
For the schema of each setting and complete examples, see [Writing rule configurations](https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html) in the *AWS Network Security Manager Developer Guide*.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallType`  <a name="cfn-networksecuritymanager-rule-firewalltype"></a>
The type of firewall that the rule configures. `WAF` specifies an AWS WAF rule.
This property is required when you create a rule. You can't change the firewall type after you create the rule.
*Required*: Conditional
*Type*: String
*Allowed values*: `WAF`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RuleDescription`  <a name="cfn-networksecuritymanager-rule-ruledescription"></a>
A description of the rule.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9 _.:/=+\-@]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleName`  <a name="cfn-networksecuritymanager-rule-rulename"></a>
The name of the rule.
You can't change the name of a rule after you create it.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RuleType`  <a name="cfn-networksecuritymanager-rule-ruletype"></a>
The type of the rule. `CONFIGURATION` rules contain firewall settings, and `INSPECTION` rules contain rule groups.
This property is required when you create a rule, and when you update `Configuration`. You can't change the rule type after you create the rule.
*Required*: Conditional
*Type*: String
*Allowed values*: `CONFIGURATION | INSPECTION`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-networksecuritymanager-rule-tags"></a>
The tags to assign to the rule. Each tag is a key-value pair. You can add tags when you create the rule and change them afterward without replacing the rule.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-networksecuritymanager-rule-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-networksecuritymanager-rule-return-values"></a>

### Ref
<a name="aws-resource-networksecuritymanager-rule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the rule. For example:

 `{ "Ref": "myRule" }`

For a rule named `block-known-bad-ips`, `Ref` returns a value similar to `arn:aws:network-security-manager:us-east-1:123456789012:rule:a1b2c3d4e5f6`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-networksecuritymanager-rule-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-networksecuritymanager-rule-return-values-fn--getatt-fn--getatt"></a>

`RuleArn`  <a name="RuleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the rule. For example: `arn:aws:network-security-manager:us-east-1:123456789012:rule:a1b2c3d4e5f6`.

`RuleId`  <a name="RuleId-fn::getatt"></a>
The service-generated identifier of the rule. For example: `a1b2c3d4e5f6`.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the rule. Rules managed with CloudFormation are always published, so this attribute returns `ACTIVE`.
*Allowed Values*: `DRAFT` \| `ACTIVE`

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time when the resource was last updated. For a snapshot, this is the time when the snapshot was created.

`Version`  <a name="Version-fn::getatt"></a>
The version of the resource.

## Examples
<a name="aws-resource-networksecuritymanager-rule--examples"></a>

### Create a rule that sets the default action of a web ACL
<a name="aws-resource-networksecuritymanager-rule--examples--Create_a_rule_that_sets_the_default_action_of_a_web_ACL"></a>

#### YAML
<a name="aws-resource-networksecuritymanager-rule--examples--Create_a_rule_that_sets_the_default_action_of_a_web_ACL--yaml"></a>

```
                AWSTemplateFormatVersion: "2010-09-09"
                Description: Creates a Network Security Manager rule that sets the default action of a web ACL.
                Resources:
                  AllowByDefaultRule:
                    Type: AWS::NetworkSecurityManager::Rule
                    Properties:
                      RuleName: allow-by-default
                      RuleDescription: Allows requests that no rule group blocks.
                      FirewallType: WAF
                      RuleType: CONFIGURATION
                      Configuration: '{"DefaultAction":{"Allow":{}}}'
                      Tags:
                        - Key: Owner
                          Value: network-security
                Outputs:
                  RuleArn:
                    Description: The ARN of the rule, for use in a template or policy.
                    Value: !GetAtt AllowByDefaultRule.RuleArn
```
