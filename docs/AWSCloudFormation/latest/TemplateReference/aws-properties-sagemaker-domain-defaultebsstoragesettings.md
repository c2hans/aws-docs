---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-defaultebsstoragesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain DefaultEbsStorageSettings
<a name="aws-properties-sagemaker-domain-defaultebsstoragesettings"></a>

A collection of default EBS storage settings that apply to spaces created within a domain or user profile.

## Syntax
<a name="aws-properties-sagemaker-domain-defaultebsstoragesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-defaultebsstoragesettings-syntax.json"></a>

```
{
  "[DefaultEbsVolumeSizeInGb](#cfn-sagemaker-domain-defaultebsstoragesettings-defaultebsvolumesizeingb)" : {{Integer}},
  "[MaximumEbsVolumeSizeInGb](#cfn-sagemaker-domain-defaultebsstoragesettings-maximumebsvolumesizeingb)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-defaultebsstoragesettings-syntax.yaml"></a>

```
  [DefaultEbsVolumeSizeInGb](#cfn-sagemaker-domain-defaultebsstoragesettings-defaultebsvolumesizeingb): {{Integer}}
  [MaximumEbsVolumeSizeInGb](#cfn-sagemaker-domain-defaultebsstoragesettings-maximumebsvolumesizeingb): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-domain-defaultebsstoragesettings-properties"></a>

`DefaultEbsVolumeSizeInGb`  <a name="cfn-sagemaker-domain-defaultebsstoragesettings-defaultebsvolumesizeingb"></a>
The default size of the EBS storage volume for a space.
*Required*: Yes
*Type*: Integer
*Minimum*: `5`
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumEbsVolumeSizeInGb`  <a name="cfn-sagemaker-domain-defaultebsstoragesettings-maximumebsvolumesizeingb"></a>
The maximum size of the EBS storage volume for a space.
*Required*: Yes
*Type*: Integer
*Minimum*: `5`
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
