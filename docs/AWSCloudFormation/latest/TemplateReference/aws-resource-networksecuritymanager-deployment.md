---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-deployment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Deployment
<a name="aws-resource-networksecuritymanager-deployment"></a>

The `AWS::NetworkSecurityManager::Deployment` resource specifies an AWS Network Security Manager deployment. A deployment is the object that puts protections into effect: it ties one or more *policies*, which describe the protections to apply, to a single *scope*, which selects the accounts and resources to apply them to.

Because a deployment only references policies and scopes, you create those resources first. A policy in turn references a template or a rule, so a complete stack builds the objects in this order: [AWS::NetworkSecurityManager::Rule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-rule.html), [AWS::NetworkSecurityManager::Template](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-template.html), [AWS::NetworkSecurityManager::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-policy.html), [AWS::NetworkSecurityManager::Scope](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-scope.html), and then `AWS::NetworkSecurityManager::Deployment`. Use `Fn::GetAtt` to pass each policy and scope ARN into the deployment so that CloudFormation infers this order for you.

Deployments that CloudFormation creates are always published, so the deployment begins applying its policies as soon as the stack operation completes. For conceptual information about deployments, see [What is AWS Network Security Manager?](https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html) in the *AWS Network Security Manager Developer Guide*.

**Note**
Network Security Manager uses optimistic concurrency control on deployments. If the deployment is modified outside of CloudFormation between the time CloudFormation reads it and the time CloudFormation writes to it, the stack operation fails with a conflict error. Manage a deployment either through CloudFormation or through the console and API, not both.

## Syntax
<a name="aws-resource-networksecuritymanager-deployment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networksecuritymanager-deployment-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkSecurityManager::Deployment",
  "Properties" : {
      "[AssociatedPolicyList](#cfn-networksecuritymanager-deployment-associatedpolicylist)" : {{[ AssociatedPolicy, ... ]}},
      "[AssociatedScopeList](#cfn-networksecuritymanager-deployment-associatedscopelist)" : {{[ AssociatedScope, ... ]}},
      "[DeploymentConfiguration](#cfn-networksecuritymanager-deployment-deploymentconfiguration)" : {{DeploymentConfiguration}},
      "[DeploymentDescription](#cfn-networksecuritymanager-deployment-deploymentdescription)" : {{String}},
      "[DeploymentName](#cfn-networksecuritymanager-deployment-deploymentname)" : {{String}},
      "[Tags](#cfn-networksecuritymanager-deployment-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-networksecuritymanager-deployment-syntax.yaml"></a>

```
Type: AWS::NetworkSecurityManager::Deployment
Properties:
  [AssociatedPolicyList](#cfn-networksecuritymanager-deployment-associatedpolicylist): {{
    - AssociatedPolicy}}
  [AssociatedScopeList](#cfn-networksecuritymanager-deployment-associatedscopelist): {{
    - AssociatedScope}}
  [DeploymentConfiguration](#cfn-networksecuritymanager-deployment-deploymentconfiguration): {{
    DeploymentConfiguration}}
  [DeploymentDescription](#cfn-networksecuritymanager-deployment-deploymentdescription): {{String}}
  [DeploymentName](#cfn-networksecuritymanager-deployment-deploymentname): {{String}}
  [Tags](#cfn-networksecuritymanager-deployment-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-networksecuritymanager-deployment-properties"></a>

`AssociatedPolicyList`  <a name="cfn-networksecuritymanager-deployment-associatedpolicylist"></a>
The policies that the deployment applies. Specify one or two policies. Each entry references an [AWS::NetworkSecurityManager::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-policy.html) resource by ARN.
This property is required when you create a deployment. Network Security Manager rejects a deployment that has no associated policy.
*Required*: Conditional
*Type*: Array of [AssociatedPolicy](aws-properties-networksecuritymanager-deployment-associatedpolicy.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssociatedScopeList`  <a name="cfn-networksecuritymanager-deployment-associatedscopelist"></a>
The scope that selects the accounts and resources the deployment protects. A deployment has exactly one scope, so specify a list with a single entry that references an [AWS::NetworkSecurityManager::Scope](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-scope.html) resource by ARN.
This property is required when you create a deployment. Network Security Manager rejects a deployment that has no associated scope.
*Required*: Conditional
*Type*: Array of [AssociatedScope](aws-properties-networksecuritymanager-deployment-associatedscope.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeploymentConfiguration`  <a name="cfn-networksecuritymanager-deployment-deploymentconfiguration"></a>
The configuration settings for the deployment.
*Required*: No
*Type*: [DeploymentConfiguration](aws-properties-networksecuritymanager-deployment-deploymentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeploymentDescription`  <a name="cfn-networksecuritymanager-deployment-deploymentdescription"></a>
A description of the deployment.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9 _.:/=+\-@]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeploymentName`  <a name="cfn-networksecuritymanager-deployment-deploymentname"></a>
The name of the deployment. The name must be unique within your AWS account and Region.
You can't change the name of a deployment after you create it. Specifying a different name replaces the deployment, which removes the protections applied by the original deployment while the replacement is created.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-networksecuritymanager-deployment-tags"></a>
The tags to assign to the deployment. Each tag is a key-value pair. You can add tags when you create the deployment and change them afterward without replacing the deployment.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-networksecuritymanager-deployment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-networksecuritymanager-deployment-return-values"></a>

### Ref
<a name="aws-resource-networksecuritymanager-deployment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the deployment. For example:

 `{ "Ref": "myDeployment" }`

For a deployment whose logical ID is `myDeployment`, `Ref` returns a value similar to `arn:aws:network-security-manager:us-east-1:123456789012:deployment:a1b2c3d4e5f6`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-networksecuritymanager-deployment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-networksecuritymanager-deployment-return-values-fn--getatt-fn--getatt"></a>

`DeploymentArn`  <a name="DeploymentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the deployment. For example: `arn:aws:network-security-manager:us-east-1:123456789012:deployment:a1b2c3d4e5f6`.
This is also the value returned by `Ref` for this resource.

`DeploymentId`  <a name="DeploymentId-fn::getatt"></a>
The unique identifier that Network Security Manager generates for the deployment. This value is unique within your AWS account and Region. For example: `a1b2c3d4e5f6`.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the deployment. Deployments that CloudFormation manages are always published, so this attribute returns `ACTIVE`.
*Allowed Values*: `DRAFT` \| `ACTIVE`

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time when the resource was last updated. For a snapshot, this is the time when the snapshot was created.

`Version`  <a name="Version-fn::getatt"></a>
The version of the deployment. Network Security Manager assigns version `1` when the deployment is created and increments it each time the deployment is published again, including on stack updates. For example: `3`.

## Examples
<a name="aws-resource-networksecuritymanager-deployment--examples"></a>

### Put a policy into effect against a scope
<a name="aws-resource-networksecuritymanager-deployment--examples--Put_a_policy_into_effect_against_a_scope"></a>

#### YAML
<a name="aws-resource-networksecuritymanager-deployment--examples--Put_a_policy_into_effect_against_a_scope--yaml"></a>

```
                AWSTemplateFormatVersion: "2010-09-09"
                Description: >-
                  Puts Network Security Manager protections into effect by tying a policy to a scope.
                  CloudFormation builds the resources in dependency order: rule, template, policy, scope, deployment.
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
                      FirewallType: WAF
                      Priority: 100
                      AssociatedTemplateAndRuleList:
                        - TemplateArn: !GetAtt BaselineTemplate.TemplateArn
                      PolicyConfiguration:
                        RemediationEnabled: true
                        ResourcesCleanUp: false
                        WafConfig:
                          ExistingCustomerWebACLResolution: RETROFIT
                          ConflictResolution: MERGE_WHERE_APPLICABLE

                  AllDistributionsScope:
                    Type: AWS::NetworkSecurityManager::Scope
                    Properties:
                      ScopeName: all-cloudfront-distributions
                      ScopeConfiguration: '{"AccountFilter":{"IncludeAll":true},"ResourceScopes":{"AWS::CloudFront::Distribution":{"IncludeAll":true}}}'

                  BaselineDeployment:
                    Type: AWS::NetworkSecurityManager::Deployment
                    Properties:
                      DeploymentName: waf-baseline-deployment
                      DeploymentDescription: Applies the baseline policy to every CloudFront distribution.
                      AssociatedPolicyList:
                        - PolicyArn: !GetAtt BaselinePolicy.PolicyArn
                      AssociatedScopeList:
                        - ScopeArn: !GetAtt AllDistributionsScope.ScopeArn
                      DeploymentConfiguration:
                        EnableCrossAccountVisibility: true
                Outputs:
                  DeploymentArn:
                    Value: !GetAtt BaselineDeployment.DeploymentArn
```
