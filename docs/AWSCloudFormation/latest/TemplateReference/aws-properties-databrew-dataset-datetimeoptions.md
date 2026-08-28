---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-dataset-datetimeoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Dataset DatetimeOptions
<a name="aws-properties-databrew-dataset-datetimeoptions"></a>

Represents additional options for correct interpretation of datetime parameters used in the Amazon S3 path of a dataset.

## Syntax
<a name="aws-properties-databrew-dataset-datetimeoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-dataset-datetimeoptions-syntax.json"></a>

```
{
  "[Format](#cfn-databrew-dataset-datetimeoptions-format)" : {{String}},
  "[LocaleCode](#cfn-databrew-dataset-datetimeoptions-localecode)" : {{String}},
  "[TimezoneOffset](#cfn-databrew-dataset-datetimeoptions-timezoneoffset)" : {{String}}
}
```

### YAML
<a name="aws-properties-databrew-dataset-datetimeoptions-syntax.yaml"></a>

```
  [Format](#cfn-databrew-dataset-datetimeoptions-format): {{String}}
  [LocaleCode](#cfn-databrew-dataset-datetimeoptions-localecode): {{String}}
  [TimezoneOffset](#cfn-databrew-dataset-datetimeoptions-timezoneoffset): {{String}}
```

## Properties
<a name="aws-properties-databrew-dataset-datetimeoptions-properties"></a>

`Format`  <a name="cfn-databrew-dataset-datetimeoptions-format"></a>
Required option, that defines the datetime format used for a date parameter in the Amazon S3 path. Should use only supported datetime specifiers and separation characters, all litera a-z or A-Z character should be escaped with single quotes. E.g. "MM.dd.yyyy-'at'-HH:mm".
*Required*: Yes
*Type*: String
*Minimum*: `2`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocaleCode`  <a name="cfn-databrew-dataset-datetimeoptions-localecode"></a>
Optional value for a non-US locale code, needed for correct interpretation of some date formats.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_\.#@\-]+$`
*Minimum*: `2`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimezoneOffset`  <a name="cfn-databrew-dataset-datetimeoptions-timezoneoffset"></a>
Optional value for a timezone offset of the datetime parameter value in the Amazon S3 path. Shouldn't be used if Format for this parameter includes timezone fields. If no offset specified, UTC is assumed.
*Required*: No
*Type*: String
*Pattern*: `^(Z|[-+](\d|\d{2}|\d{2}:?\d{2}))$`
*Minimum*: `1`
*Maximum*: `6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
