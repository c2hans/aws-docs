---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-ownershipsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space OwnershipSettings
<a name="aws-properties-sagemaker-space-ownershipsettings"></a>

The collection of ownership settings for a space.

## Syntax
<a name="aws-properties-sagemaker-space-ownershipsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-ownershipsettings-syntax.json"></a>

```
{
  "[OwnerUserProfileName](#cfn-sagemaker-space-ownershipsettings-owneruserprofilename)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-ownershipsettings-syntax.yaml"></a>

```
  [OwnerUserProfileName](#cfn-sagemaker-space-ownershipsettings-owneruserprofilename): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-space-ownershipsettings-properties"></a>

`OwnerUserProfileName`  <a name="cfn-sagemaker-space-ownershipsettings-owneruserprofilename"></a>
The user profile who is the owner of the space.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
