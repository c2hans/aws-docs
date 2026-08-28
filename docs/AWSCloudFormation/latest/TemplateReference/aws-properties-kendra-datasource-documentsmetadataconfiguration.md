---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-documentsmetadataconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource DocumentsMetadataConfiguration
<a name="aws-properties-kendra-datasource-documentsmetadataconfiguration"></a>

Document metadata files that contain information such as the document access control information, source URI, document author, and custom attributes. Each metadata file contains metadata about a single document.

## Syntax
<a name="aws-properties-kendra-datasource-documentsmetadataconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-documentsmetadataconfiguration-syntax.json"></a>

```
{
  "[S3Prefix](#cfn-kendra-datasource-documentsmetadataconfiguration-s3prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-documentsmetadataconfiguration-syntax.yaml"></a>

```
  [S3Prefix](#cfn-kendra-datasource-documentsmetadataconfiguration-s3prefix): {{String}}
```

## Properties
<a name="aws-properties-kendra-datasource-documentsmetadataconfiguration-properties"></a>

`S3Prefix`  <a name="cfn-kendra-datasource-documentsmetadataconfiguration-s3prefix"></a>
A prefix used to filter metadata configuration files in the AWS S3 bucket. The S3 bucket might contain multiple metadata files. Use `S3Prefix` to include only the desired metadata files.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
