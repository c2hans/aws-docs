---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup OnPremisesTagSetListObject
<a name="aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject"></a>

 The `OnPremisesTagSetListObject` property type specifies lists of on-premises instance tag groups. In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

`OnPremisesTagSetListObject` is a property of the [CodeDeploy DeploymentGroup OnPremisesTagSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html) property type.

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject-syntax.json"></a>

```
{
  "[OnPremisesTagGroup](#cfn-codedeploy-deploymentgroup-onpremisestagsetlistobject-onpremisestaggroup)" : {{[ TagFilter, ... ]}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject-syntax.yaml"></a>

```
  [OnPremisesTagGroup](#cfn-codedeploy-deploymentgroup-onpremisestagsetlistobject-onpremisestaggroup): {{
    - TagFilter}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject-properties"></a>

`OnPremisesTagGroup`  <a name="cfn-codedeploy-deploymentgroup-onpremisestagsetlistobject-onpremisestaggroup"></a>
Information about groups of on-premises instance tags.
*Required*: No
*Type*: Array of [TagFilter](aws-properties-codedeploy-deploymentgroup-tagfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
