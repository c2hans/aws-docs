---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-deployment-associatedpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Deployment AssociatedPolicy
<a name="aws-properties-networksecuritymanager-deployment-associatedpolicy"></a>

References a policy that a deployment applies. Use the `AssociatedPolicyList` property of the `AWS::NetworkSecurityManager::Deployment` resource to associate policies with a deployment.

## Syntax
<a name="aws-properties-networksecuritymanager-deployment-associatedpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-deployment-associatedpolicy-syntax.json"></a>

```
{
  "[PolicyArn](#cfn-networksecuritymanager-deployment-associatedpolicy-policyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-deployment-associatedpolicy-syntax.yaml"></a>

```
  [PolicyArn](#cfn-networksecuritymanager-deployment-associatedpolicy-policyarn): {{String}}
```

## Properties
<a name="aws-properties-networksecuritymanager-deployment-associatedpolicy-properties"></a>

`PolicyArn`  <a name="cfn-networksecuritymanager-deployment-associatedpolicy-policyarn"></a>
The Amazon Resource Name (ARN) of the policy to apply. To pin the deployment to a specific published version of the policy, append the version qualifier to the ARN, for example `arn:aws:network-security-manager:us-east-1:123456789012:policy:a1b2c3d4e5f6:3`. If you omit the version qualifier, the deployment uses the latest published version of the policy.
To get this value from a policy defined in the same template, use `Fn::GetAtt` with the [AWS::NetworkSecurityManager::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-policy.html) resource.
*Required*: Yes
*Type*: String
*Pattern*: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
*Minimum*: `20`
*Maximum*: `1010`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
