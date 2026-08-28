---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-workflow-s3filelocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Workflow S3FileLocation
<a name="aws-properties-transfer-workflow-s3filelocation"></a>

Specifies the S3 details for the file being used, such as bucket, ETag, and so forth.

## Syntax
<a name="aws-properties-transfer-workflow-s3filelocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-workflow-s3filelocation-syntax.json"></a>

```
{
  "[S3FileLocation](#cfn-transfer-workflow-s3filelocation-s3filelocation)" : {{S3InputFileLocation}}
}
```

### YAML
<a name="aws-properties-transfer-workflow-s3filelocation-syntax.yaml"></a>

```
  [S3FileLocation](#cfn-transfer-workflow-s3filelocation-s3filelocation): {{
    S3InputFileLocation}}
```

## Properties
<a name="aws-properties-transfer-workflow-s3filelocation-properties"></a>

`S3FileLocation`  <a name="cfn-transfer-workflow-s3filelocation-s3filelocation"></a>
 Specifies the details for the file location for the file that's being used in the workflow. Only applicable if you are using Amazon S3 storage.
*Required*: No
*Type*: [S3InputFileLocation](aws-properties-transfer-workflow-s3inputfilelocation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
