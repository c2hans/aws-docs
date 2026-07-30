---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-ec2tagset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup EC2TagSet
<a name="aws-properties-codedeploy-deploymentgroup-ec2tagset"></a>

 The `EC2TagSet` property type specifies information about groups of tags applied to Amazon EC2 instances. The deployment group includes only Amazon EC2 instances identified by all the tag groups. `EC2TagSet` cannot be used in the same template as `EC2TagFilter`.

 For information about using tags and tag groups to help manage your Amazon EC2 instances and on-premises instances, see [Tagging Instances for Deployment Groups in AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-tagging.html).

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-ec2tagset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-ec2tagset-syntax.json"></a>

```
{
  "[Ec2TagSetList](#cfn-codedeploy-deploymentgroup-ec2tagset-ec2tagsetlist)" : {{[ EC2TagSetListObject, ... ]}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-ec2tagset-syntax.yaml"></a>

```
  [Ec2TagSetList](#cfn-codedeploy-deploymentgroup-ec2tagset-ec2tagsetlist): {{
    - EC2TagSetListObject}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-ec2tagset-properties"></a>

`Ec2TagSetList`  <a name="cfn-codedeploy-deploymentgroup-ec2tagset-ec2tagsetlist"></a>
 The Amazon EC2 tags that are already applied to Amazon EC2 instances that you want to include in the deployment group. CodeDeploy includes all Amazon EC2 instances identified by any of the tags you specify in this deployment group.
 Duplicates are not allowed.
*Required*: No
*Type*: Array of [EC2TagSetListObject](aws-properties-codedeploy-deploymentgroup-ec2tagsetlistobject.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-codedeploy-deploymentgroup-ec2tagset--seealso"></a>
+ [EC2TagSet](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_EC2TagSet.html) in the *AWS CodeDeploy API Reference*.
