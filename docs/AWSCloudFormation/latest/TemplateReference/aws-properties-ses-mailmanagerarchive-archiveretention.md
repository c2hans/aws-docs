---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerarchive-archiveretention.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerArchive ArchiveRetention
<a name="aws-properties-ses-mailmanagerarchive-archiveretention"></a>

The retention policy for an email archive that specifies how long emails are kept before being automatically deleted.

## Syntax
<a name="aws-properties-ses-mailmanagerarchive-archiveretention-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerarchive-archiveretention-syntax.json"></a>

```
{
  "[RetentionPeriod](#cfn-ses-mailmanagerarchive-archiveretention-retentionperiod)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerarchive-archiveretention-syntax.yaml"></a>

```
  [RetentionPeriod](#cfn-ses-mailmanagerarchive-archiveretention-retentionperiod): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerarchive-archiveretention-properties"></a>

`RetentionPeriod`  <a name="cfn-ses-mailmanagerarchive-archiveretention-retentionperiod"></a>
The enum value sets the period for retaining emails in an archive.
*Required*: Yes
*Type*: String
*Allowed values*: `THREE_MONTHS | SIX_MONTHS | NINE_MONTHS | ONE_YEAR | EIGHTEEN_MONTHS | TWO_YEARS | THIRTY_MONTHS | THREE_YEARS | FOUR_YEARS | FIVE_YEARS | SIX_YEARS | SEVEN_YEARS | EIGHT_YEARS | NINE_YEARS | TEN_YEARS | PERMANENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
