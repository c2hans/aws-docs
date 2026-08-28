---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3files-filesystem-expirationdatarule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Files::FileSystem ExpirationDataRule
<a name="aws-properties-s3files-filesystem-expirationdatarule"></a>

Specifies a rule that controls when cached data expires from the file system based on last access time.

## Syntax
<a name="aws-properties-s3files-filesystem-expirationdatarule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3files-filesystem-expirationdatarule-syntax.json"></a>

```
{
  "[DaysAfterLastAccess](#cfn-s3files-filesystem-expirationdatarule-daysafterlastaccess)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3files-filesystem-expirationdatarule-syntax.yaml"></a>

```
  [DaysAfterLastAccess](#cfn-s3files-filesystem-expirationdatarule-daysafterlastaccess): {{Integer}}
```

## Properties
<a name="aws-properties-s3files-filesystem-expirationdatarule-properties"></a>

`DaysAfterLastAccess`  <a name="cfn-s3files-filesystem-expirationdatarule-daysafterlastaccess"></a>
The number of days after last access before cached data expires from the file system.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `365`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
