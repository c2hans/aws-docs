---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-stackset-autodeployment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::StackSet AutoDeployment
<a name="aws-properties-cloudformation-stackset-autodeployment"></a>

Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organization or organizational unit (OU). For more information, see [Enable or disable automatic deployments for StackSets in AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-auto-deployment.html) in the *CloudFormation User Guide*.

## Syntax
<a name="aws-properties-cloudformation-stackset-autodeployment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-stackset-autodeployment-syntax.json"></a>

```
{
  "[DependsOn](#cfn-cloudformation-stackset-autodeployment-dependson)" : {{[ String, ... ]}},
  "[Enabled](#cfn-cloudformation-stackset-autodeployment-enabled)" : {{Boolean}},
  "[RetainStacksOnAccountRemoval](#cfn-cloudformation-stackset-autodeployment-retainstacksonaccountremoval)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cloudformation-stackset-autodeployment-syntax.yaml"></a>

```
  [DependsOn](#cfn-cloudformation-stackset-autodeployment-dependson): {{
    - String}}
  [Enabled](#cfn-cloudformation-stackset-autodeployment-enabled): {{Boolean}}
  [RetainStacksOnAccountRemoval](#cfn-cloudformation-stackset-autodeployment-retainstacksonaccountremoval): {{Boolean}}
```

## Properties
<a name="aws-properties-cloudformation-stackset-autodeployment-properties"></a>

`DependsOn`  <a name="cfn-cloudformation-stackset-autodeployment-dependson"></a>
A list of StackSet ARNs that this StackSet depends on for auto-deployment operations. When auto-deployment is triggered, operations will be sequenced to ensure all dependencies complete successfully before this StackSet's operation begins.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-cloudformation-stackset-autodeployment-enabled"></a>
If set to `true`, StackSets automatically deploys additional stack instances to AWS Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetainStacksOnAccountRemoval`  <a name="cfn-cloudformation-stackset-autodeployment-retainstacksonaccountremoval"></a>
If set to `true`, stack resources are retained when an account is removed from a target organization or OU. If set to `false`, stack resources are deleted. Specify only if `Enabled` is set to `True`.
*Required*: Conditional
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
