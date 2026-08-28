---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconvert-jobtemplate-accelerationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConvert::JobTemplate AccelerationSettings
<a name="aws-properties-mediaconvert-jobtemplate-accelerationsettings"></a>

Accelerated transcoding can significantly speed up jobs with long, visually complex content. Outputs that use this feature incur pro-tier pricing. For information about feature limitations, For more information, see [Job Limitations for Accelerated Transcoding in AWS Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/job-requirements.html) in the *AWS Elemental MediaConvert User Guide*.

## Syntax
<a name="aws-properties-mediaconvert-jobtemplate-accelerationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconvert-jobtemplate-accelerationsettings-syntax.json"></a>

```
{
  "[Mode](#cfn-mediaconvert-jobtemplate-accelerationsettings-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconvert-jobtemplate-accelerationsettings-syntax.yaml"></a>

```
  [Mode](#cfn-mediaconvert-jobtemplate-accelerationsettings-mode): {{String}}
```

## Properties
<a name="aws-properties-mediaconvert-jobtemplate-accelerationsettings-properties"></a>

`Mode`  <a name="cfn-mediaconvert-jobtemplate-accelerationsettings-mode"></a>
Specify the conditions when the service will run your job with accelerated transcoding.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
