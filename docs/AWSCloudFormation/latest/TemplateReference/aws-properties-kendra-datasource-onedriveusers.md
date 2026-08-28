---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-onedriveusers.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource OneDriveUsers
<a name="aws-properties-kendra-datasource-onedriveusers"></a>

User accounts whose documents should be indexed.

## Syntax
<a name="aws-properties-kendra-datasource-onedriveusers-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-onedriveusers-syntax.json"></a>

```
{
  "[OneDriveUserList](#cfn-kendra-datasource-onedriveusers-onedriveuserlist)" : {{[ String, ... ]}},
  "[OneDriveUserS3Path](#cfn-kendra-datasource-onedriveusers-onedriveusers3path)" : {{S3Path}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-onedriveusers-syntax.yaml"></a>

```
  [OneDriveUserList](#cfn-kendra-datasource-onedriveusers-onedriveuserlist): {{
    - String}}
  [OneDriveUserS3Path](#cfn-kendra-datasource-onedriveusers-onedriveusers3path): {{
    S3Path}}
```

## Properties
<a name="aws-properties-kendra-datasource-onedriveusers-properties"></a>

`OneDriveUserList`  <a name="cfn-kendra-datasource-onedriveusers-onedriveuserlist"></a>
A list of users whose documents should be indexed. Specify the user names in email format, for example, `username@tenantdomain`. If you need to index the documents of more than 10 users, use the `OneDriveUserS3Path` field to specify the location of a file containing a list of users.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OneDriveUserS3Path`  <a name="cfn-kendra-datasource-onedriveusers-onedriveusers3path"></a>
The S3 bucket location of a file containing a list of users whose documents should be indexed.
*Required*: No
*Type*: [S3Path](aws-properties-kendra-datasource-s3path.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
