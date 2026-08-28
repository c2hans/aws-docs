---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-stack-applicationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack ApplicationSettings
<a name="aws-properties-appstream-stack-applicationsettings"></a>

The persistent application settings for users of a stack.

## Syntax
<a name="aws-properties-appstream-stack-applicationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-stack-applicationsettings-syntax.json"></a>

```
{
  "[Enabled](#cfn-appstream-stack-applicationsettings-enabled)" : {{Boolean}},
  "[SettingsGroup](#cfn-appstream-stack-applicationsettings-settingsgroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-stack-applicationsettings-syntax.yaml"></a>

```
  [Enabled](#cfn-appstream-stack-applicationsettings-enabled): {{Boolean}}
  [SettingsGroup](#cfn-appstream-stack-applicationsettings-settingsgroup): {{String}}
```

## Properties
<a name="aws-properties-appstream-stack-applicationsettings-properties"></a>

`Enabled`  <a name="cfn-appstream-stack-applicationsettings-enabled"></a>
Enables or disables persistent application settings for users during their streaming sessions.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SettingsGroup`  <a name="cfn-appstream-stack-applicationsettings-settingsgroup"></a>
The path prefix for the S3 bucket where users’ persistent application settings are stored. You can allow the same persistent application settings to be used across multiple stacks by specifying the same settings group for each stack.
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
