---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkfirewall-firewallpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::FirewallPolicy
<a name="aws-resource-networkfirewall-firewallpolicy"></a>

Use the firewall policy to define the stateless and stateful network traffic filtering behavior for your firewall. You can use one firewall policy for multiple firewalls.

## Syntax
<a name="aws-resource-networkfirewall-firewallpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkfirewall-firewallpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkFirewall::FirewallPolicy",
  "Properties" : {
      "[Description](#cfn-networkfirewall-firewallpolicy-description)" : {{String}},
      "[FirewallPolicy](#cfn-networkfirewall-firewallpolicy-firewallpolicy)" : {{FirewallPolicy}},
      "[FirewallPolicyName](#cfn-networkfirewall-firewallpolicy-firewallpolicyname)" : {{String}},
      "[Tags](#cfn-networkfirewall-firewallpolicy-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-networkfirewall-firewallpolicy-syntax.yaml"></a>

```
Type: AWS::NetworkFirewall::FirewallPolicy
Properties:
  [Description](#cfn-networkfirewall-firewallpolicy-description): {{String}}
  [FirewallPolicy](#cfn-networkfirewall-firewallpolicy-firewallpolicy): {{
    FirewallPolicy}}
  [FirewallPolicyName](#cfn-networkfirewall-firewallpolicy-firewallpolicyname): {{String}}
  [Tags](#cfn-networkfirewall-firewallpolicy-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-networkfirewall-firewallpolicy-properties"></a>

`Description`  <a name="cfn-networkfirewall-firewallpolicy-description"></a>
A description of the firewall policy.
*Required*: No
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallPolicy`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicy"></a>
The traffic filtering behavior of a firewall policy, defined in a collection of stateless and stateful rule groups and other settings.
*Required*: Yes
*Type*: [FirewallPolicy](aws-properties-networkfirewall-firewallpolicy-firewallpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallPolicyName`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicyname"></a>
The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-networkfirewall-firewallpolicy-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-networkfirewall-firewallpolicy-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-networkfirewall-firewallpolicy-return-values"></a>

### Ref
<a name="aws-resource-networkfirewall-firewallpolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the firewall policy. For example:

 `{ "Ref": "arn:aws:network-firewall:us-east-1:012345678901:firewall-policy/myFirewallPolicyName" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-networkfirewall-firewallpolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-networkfirewall-firewallpolicy-return-values-fn--getatt-fn--getatt"></a>

`FirewallPolicyArn`  <a name="FirewallPolicyArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the firewall policy.

`FirewallPolicyId`  <a name="FirewallPolicyId-fn::getatt"></a>
The unique ID of the firewall policy resource.

## Examples
<a name="aws-resource-networkfirewall-firewallpolicy--examples"></a>

### Create a firewall policy
<a name="aws-resource-networkfirewall-firewallpolicy--examples--Create_a_firewall_policy"></a>

The following shows example firewall policy specifications.

#### JSON
<a name="aws-resource-networkfirewall-firewallpolicy--examples--Create_a_firewall_policy--json"></a>

```
"SampleFirewallPolicy": {
    "Type": "AWS::NetworkFirewall::FirewallPolicy",
    "Properties": {
        "FirewallPolicyName": "SampleFirewallPolicyName",
        "FirewallPolicy": {
            "StatelessDefaultActions": [
                "aws:pass"
            ],
            "StatelessFragmentDefaultActions": [
                "aws:drop"
            ],
            "StatefulRuleGroupReferences": [
                {
                    "ResourceArn": {
                        "Ref": "SampleStatefulRuleGroup"
                    }
                }
            ],
            "StatelessRuleGroupReferences": [
                {
                    "ResourceArn": {
                        "Ref": "SampleStatelessRuleGroup"
                    },
                    "Priority": 100
                }
            ]
        },
        "Description": "FirewallPolicy description goes here",
        "Tags": [
            {
                "Key": "Foo",
                "Value": "Bar"
            }
        ]
    }
}
```

#### YAML
<a name="aws-resource-networkfirewall-firewallpolicy--examples--Create_a_firewall_policy--yaml"></a>

```
SampleFirewallPolicy:
  Type: 'AWS::NetworkFirewall::FirewallPolicy'
  Properties:
    FirewallPolicyName: SampleFirewallPolicyName
    FirewallPolicy:
      StatelessDefaultActions:
        - 'aws:pass'
      StatelessFragmentDefaultActions:
        - 'aws:drop'
      StatefulRuleGroupReferences:
        - ResourceArn: !Ref SampleStatefulRuleGroup1
      StatelessRuleGroupReferences:
        - ResourceArn: !Ref SampleStatelessRuleGroup
          Priority: 100
    Description: FirewallPolicy description goes here
    Tags:
      - Key: Foo
        Value: Bar
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
