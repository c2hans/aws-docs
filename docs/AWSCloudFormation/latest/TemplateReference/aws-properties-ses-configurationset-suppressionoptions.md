---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationset-suppressionoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSet SuppressionOptions
<a name="aws-properties-ses-configurationset-suppressionoptions"></a>

An object that contains information about the suppression list preferences for your account.

## Syntax
<a name="aws-properties-ses-configurationset-suppressionoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationset-suppressionoptions-syntax.json"></a>

```
{
  "[SuppressedReasons](#cfn-ses-configurationset-suppressionoptions-suppressedreasons)" : {{[ String, ... ]}},
  "[ValidationOptions](#cfn-ses-configurationset-suppressionoptions-validationoptions)" : {{ValidationOptions}}
}
```

### YAML
<a name="aws-properties-ses-configurationset-suppressionoptions-syntax.yaml"></a>

```
  [SuppressedReasons](#cfn-ses-configurationset-suppressionoptions-suppressedreasons): {{
    - String}}
  [ValidationOptions](#cfn-ses-configurationset-suppressionoptions-validationoptions): {{
    ValidationOptions}}
```

## Properties
<a name="aws-properties-ses-configurationset-suppressionoptions-properties"></a>

`SuppressedReasons`  <a name="cfn-ses-configurationset-suppressionoptions-suppressedreasons"></a>
A list that contains the reasons that email addresses are automatically added to the suppression list for your account. This list can contain any or all of the following:
+ `COMPLAINT` – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a complaint.
+ `BOUNCE` – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a hard bounce.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidationOptions`  <a name="cfn-ses-configurationset-suppressionoptions-validationoptions"></a>
The configuration settings for email automatic validation.
*Required*: No
*Type*: [ValidationOptions](aws-properties-ses-configurationset-validationoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
