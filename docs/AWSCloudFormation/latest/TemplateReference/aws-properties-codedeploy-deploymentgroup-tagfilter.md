---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-tagfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup TagFilter
<a name="aws-properties-codedeploy-deploymentgroup-tagfilter"></a>

`TagFilter` is a property type of the [AWS::CodeDeploy::DeploymentGroup ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html) resource that specifies which on-premises instances to associate with the deployment group. To register on-premise instances with AWS CodeDeploy, see [Configure Existing On-Premises Instances by Using AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-on-premises.html) in the *AWS CodeDeploy User Guide*.

For more information about using tags and tag groups to help manage your Amazon EC2 instances and on-premises instances, see [Tagging Instances for Deployment Groups in AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-tagging.html) in the *AWS CodeDeploy User Guide*.

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-tagfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-tagfilter-syntax.json"></a>

```
{
  "[Key](#cfn-codedeploy-deploymentgroup-tagfilter-key)" : {{String}},
  "[Type](#cfn-codedeploy-deploymentgroup-tagfilter-type)" : {{String}},
  "[Value](#cfn-codedeploy-deploymentgroup-tagfilter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-tagfilter-syntax.yaml"></a>

```
  [Key](#cfn-codedeploy-deploymentgroup-tagfilter-key): {{String}}
  [Type](#cfn-codedeploy-deploymentgroup-tagfilter-type): {{String}}
  [Value](#cfn-codedeploy-deploymentgroup-tagfilter-value): {{String}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-tagfilter-properties"></a>

`Key`  <a name="cfn-codedeploy-deploymentgroup-tagfilter-key"></a>
The on-premises instance tag filter key.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-codedeploy-deploymentgroup-tagfilter-type"></a>
The on-premises instance tag filter type:
+ KEY\_ONLY: Key only.
+ VALUE\_ONLY: Value only.
+ KEY\_AND\_VALUE: Key and value.
*Required*: No
*Type*: String
*Allowed values*: `KEY_ONLY | VALUE_ONLY | KEY_AND_VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-codedeploy-deploymentgroup-tagfilter-value"></a>
The on-premises instance tag filter value.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
