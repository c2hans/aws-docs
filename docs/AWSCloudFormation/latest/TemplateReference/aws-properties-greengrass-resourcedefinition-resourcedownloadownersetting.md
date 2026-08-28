---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ResourceDefinition ResourceDownloadOwnerSetting
<a name="aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting"></a>

The owner setting for a downloaded machine learning resource. For more information, see [Access Machine Learning Resources from Lambda Functions](https://docs.aws.amazon.com/greengrass/v1/developerguide/access-ml-resources.html) in the * AWS IoT Greengrass Version 1 Developer Guide *.

<a name="aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting-inheritance"></a> In an CloudFormation template, `ResourceDownloadOwnerSetting` is the property type of the `OwnerSetting` property for the [`S3MachineLearningModelResourceData`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html) and [`SageMakerMachineLearningModelResourceData`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html) property types.

## Syntax
<a name="aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting-syntax.json"></a>

```
{
  "[GroupOwner](#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-groupowner)" : {{String}},
  "[GroupPermission](#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-grouppermission)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting-syntax.yaml"></a>

```
  [GroupOwner](#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-groupowner): {{String}}
  [GroupPermission](#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-grouppermission): {{String}}
```

## Properties
<a name="aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting-properties"></a>

`GroupOwner`  <a name="cfn-greengrass-resourcedefinition-resourcedownloadownersetting-groupowner"></a>
The group owner of the machine learning resource. This is the group ID (GID) of an existing Linux OS group on the system. The group's permissions are added to the Lambda process.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroupPermission`  <a name="cfn-greengrass-resourcedefinition-resourcedownloadownersetting-grouppermission"></a>
The permissions that the group owner has to the machine learning resource. Valid values are `rw` (read-write) or `ro` (read-only).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
