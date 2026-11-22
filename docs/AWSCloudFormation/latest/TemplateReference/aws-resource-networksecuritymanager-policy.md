---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-policy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Policy

The `AWS::NetworkSecurityManager::Policy` resource specifies an AWS Network Security Manager policy. A policy combines templates and rules with enforcement settings for a single firewall type: AWS WAF, AWS Shield Advanced, or the AWS Network Firewall automated internet firewall.

A policy does not protect anything on its own. It takes effect when you associate it with an `AWS::NetworkSecurityManager::Deployment` resource, which supplies the accounts and resources that the policy applies to.

**Note**
Policies that you create with CloudFormation are always published. The `Status` attribute of a CloudFormation-managed policy is `ACTIVE`, never `DRAFT`.

## Syntax
<a name="aws-resource-networksecuritymanager-policy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networksecuritymanager-policy-syntax.json"></a>

```json
{
  "Type" : "AWS::NetworkSecurityManager::Policy",
  "Properties" : {
      "[AssociatedTemplateAndRuleList](#cfn-networksecuritymanager-policy-associatedtemplateandrulelist)" : {{[ AssociatedTemplateAndRule, ... ]}},
      "[FirewallType](#cfn-networksecuritymanager-policy-firewalltype)" : {{String}},
      "[PolicyConfiguration](#cfn-networksecuritymanager-policy-policyconfiguration)" : {{PolicyConfiguration}},
      "[PolicyDescription](#cfn-networksecuritymanager-policy-policydescription)" : {{String}},
      "[PolicyName](#cfn-networksecuritymanager-policy-policyname)" : {{String}},
      "[Priority](#cfn-networksecuritymanager-policy-priority)" : {{Integer}},
      "[Tags](#cfn-networksecuritymanager-policy-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-networksecuritymanager-policy-syntax.yaml"></a>

```yaml
Type: AWS::NetworkSecurityManager::Policy
Properties:
  [AssociatedTemplateAndRuleList](#cfn-networksecuritymanager-policy-associatedtemplateandrulelist): {{
    - AssociatedTemplateAndRule}}
  [FirewallType](#cfn-networksecuritymanager-policy-firewalltype): {{String}}
  [PolicyConfiguration](#cfn-networksecuritymanager-policy-policyconfiguration): {{
    PolicyConfiguration}}
  [PolicyDescription](#cfn-networksecuritymanager-policy-policydescription): {{String}}
  [PolicyName](#cfn-networksecuritymanager-policy-policyname): {{String}}
  [Priority](#cfn-networksecuritymanager-policy-priority): {{Integer}}
  [Tags](#cfn-networksecuritymanager-policy-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-networksecuritymanager-policy-properties"></a>

`AssociatedTemplateAndRuleList`  <a name="cfn-networksecuritymanager-policy-associatedtemplateandrulelist"></a>
The templates and rules to associate with the policy. Each entry in the list must specify exactly one of `TemplateArn` or `RuleArn`. An entry that sets both, or neither, causes the stack operation to fail.
For AWS WAF and `IGW_FIREWALL` policies, specify 1 to 100 templates or rules, of which at most 2 can be templates. Every template and rule must use the same firewall type as the policy. For AWS Shield Advanced policies, omit this property or specify an empty list.
*Required*: No
*Type*: Array of [AssociatedTemplateAndRule](aws-properties-networksecuritymanager-policy-associatedtemplateandrule.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallType`  <a name="cfn-networksecuritymanager-policy-firewalltype"></a>
The type of firewall that the policy configures. Specify `WAF` for an AWS WAF policy, `SHIELD_ADVANCED` for an AWS Shield Advanced policy, or `IGW_FIREWALL` for an AWS Network Firewall automated internet firewall policy.
You can't change the firewall type of a policy after you create it. To use a different firewall type, you must replace the policy.
*Required*: Yes
*Type*: String
*Allowed values*: `WAF | SHIELD_ADVANCED | IGW_FIREWALL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyConfiguration`  <a name="cfn-networksecuritymanager-policy-policyconfiguration"></a>
The configuration settings that control how the policy behaves, including whether remediation is enabled and settings specific to the firewall type.
*Required*: Yes
*Type*: [PolicyConfiguration](aws-properties-networksecuritymanager-policy-policyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyDescription`  <a name="cfn-networksecuritymanager-policy-policydescription"></a>
A description of the policy.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9 _.:/=+\-@]*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyName`  <a name="cfn-networksecuritymanager-policy-policyname"></a>
The name of the policy. The name must be unique within your AWS account and AWS Region.
You can't change the name of a policy after you create it. To use a different name, you must replace the policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Priority`  <a name="cfn-networksecuritymanager-policy-priority"></a>
The priority of the policy. A lower number indicates a higher priority. When more than one policy applies to the same resource, Network Security Manager uses the settings of the highest-priority policy to resolve conflicts.
Each priority can be used by only one policy in an AWS account and AWS Region. Creating a policy with a priority that is already in use fails.
For `IGW_FIREWALL` policies, only the highest-priority policy that applies to a resource takes effect. Settings from lower-priority policies aren't merged in.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networksecuritymanager-policy-tags"></a>
The tags to add to the resource when it is created.
*Required*: No
*Type*: Array of [Tag](aws-properties-networksecuritymanager-policy-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-networksecuritymanager-policy-return-values"></a>

### Ref
<a name="aws-resource-networksecuritymanager-policy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the policy. For example:

 `{ "Ref": "myPolicy" }`

For a policy with the logical ID `myPolicy`, `Ref` returns a value such as `arn:aws:network-security-manager:us-east-1:123456789012:policy:a1b2c3d4e5f6`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-networksecuritymanager-policy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-networksecuritymanager-policy-return-values-fn--getatt-fn--getatt"></a>

`PolicyArn`  <a name="PolicyArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the policy.

`PolicyId`  <a name="PolicyId-fn::getatt"></a>
The service-generated ID of the policy. For example: `a1b2c3d4e5f6`.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the policy. Policies that CloudFormation manages are always published, so this attribute returns `ACTIVE`.
*Allowed Values*: `DRAFT` \| `ACTIVE`

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the policy was last updated, in ISO 8601 format. For example: `2026-11-19T21:42:56Z`.

`Version`  <a name="Version-fn::getatt"></a>
The version of the policy. Network Security Manager increments this value each time the policy is published. For example: `3`.

## Examples
<a name="aws-resource-networksecuritymanager-policy--examples"></a>

**Topics**
+ [Apply a template with automatic remediation](#aws-resource-networksecuritymanager-policy--examples--Apply_a_template_with_automatic_remediation)
+ [Create an internet firewall policy with a subnet connectivity override](#aws-resource-networksecuritymanager-policy--examples--Create_an_internet_firewall_policy_with_a_subnet_connectivity_override)

### Apply a template with automatic remediation
<a name="aws-resource-networksecuritymanager-policy--examples--Apply_a_template_with_automatic_remediation"></a>

#### YAML
<a name="aws-resource-networksecuritymanager-policy--examples--Apply_a_template_with_automatic_remediation--yaml"></a>

```yaml
                AWSTemplateFormatVersion: "2010-09-09"
                Description: Combines a Network Security Manager template with enforcement settings.
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
                      FirewallType: WAF
                      AssociatedRuleList:
                        - RuleArn: !GetAtt AllowByDefaultRule.RuleArn

                  BaselinePolicy:
                    Type: AWS::NetworkSecurityManager::Policy
                    Properties:
                      PolicyName: waf-baseline-policy
                      PolicyDescription: Applies the baseline template and remediates resources automatically.
                      FirewallType: WAF
                      Priority: 100
                      AssociatedTemplateAndRuleList:
                        - TemplateArn: !GetAtt BaselineTemplate.TemplateArn
                      PolicyConfiguration:
                        RemediationEnabled: true
                        ResourcesCleanUp: true
                        WafConfig:
                          ExistingCustomerWebACLResolution: RETROFIT
                          ConflictResolution: MERGE_WHERE_APPLICABLE
                Outputs:
                  PolicyArn:
                    Value: !GetAtt BaselinePolicy.PolicyArn
```

### Create an internet firewall policy with a subnet connectivity override
<a name="aws-resource-networksecuritymanager-policy--examples--Create_an_internet_firewall_policy_with_a_subnet_connectivity_override"></a>

#### YAML
<a name="aws-resource-networksecuritymanager-policy--examples--Create_an_internet_firewall_policy_with_a_subnet_connectivity_override--yaml"></a>

```yaml
                AWSTemplateFormatVersion: "2010-09-09"
                Description: Creates a Network Firewall automated internet firewall policy that excludes isolated subnets.
                Resources:
                  EnforceModeRule:
                    Type: AWS::NetworkSecurityManager::Rule
                    Properties:
                      RuleName: igw-enforce-mode
                      FirewallType: IGW_FIREWALL
                      RuleType: INSPECTION
                      Configuration: '{"PolicyMode":"ENFORCE"}'

                  InternetFirewallTemplate:
                    Type: AWS::NetworkSecurityManager::Template
                    Properties:
                      TemplateName: igw-baseline
                      FirewallType: IGW_FIREWALL
                      AssociatedRuleList:
                        - RuleArn: !GetAtt EnforceModeRule.RuleArn

                  IsolatedSubnetsScope:
                    Type: AWS::NetworkSecurityManager::Scope
                    Properties:
                      ScopeName: isolated-subnets
                      SpecializedScopeType: IGW_FIREWALL_SUBNET_CONNECTIVITY_OVERRIDE
                      ScopeConfiguration: '{"ResourceScopes":{"AWS::EC2::Subnet":{"Include":{"Expression":{"Criteria":{"Tags":{"network-zone":"isolated"}}}}}}}'

                  InternetFirewallPolicy:
                    Type: AWS::NetworkSecurityManager::Policy
                    Properties:
                      PolicyName: igw-baseline-policy
                      PolicyDescription: Inspects internet traffic and excludes isolated subnets.
                      FirewallType: IGW_FIREWALL
                      Priority: 200
                      AssociatedTemplateAndRuleList:
                        - TemplateArn: !GetAtt InternetFirewallTemplate.TemplateArn
                      PolicyConfiguration:
                        RemediationEnabled: true
                        ResourcesCleanUp: true
                        IgwFirewallConfig:
                          DefaultSubnetConnectivity: flexible
                          SubnetConnectivityOverrides:
                            - ConnectivityType: exclude
                              Scopes:
                                - !GetAtt IsolatedSubnetsScope.ScopeArn
                Outputs:
                  PolicyArn:
                    Value: !GetAtt InternetFirewallPolicy.PolicyArn
```
