---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-table-magneticstorerejecteddatalocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::Table MagneticStoreRejectedDataLocation
<a name="aws-properties-timestream-table-magneticstorerejecteddatalocation"></a>

The location to write error reports for records rejected, asynchronously, during magnetic store writes.

## Syntax
<a name="aws-properties-timestream-table-magneticstorerejecteddatalocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-table-magneticstorerejecteddatalocation-syntax.json"></a>

```
{
  "[S3Configuration](#cfn-timestream-table-magneticstorerejecteddatalocation-s3configuration)" : {{S3Configuration}}
}
```

### YAML
<a name="aws-properties-timestream-table-magneticstorerejecteddatalocation-syntax.yaml"></a>

```
  [S3Configuration](#cfn-timestream-table-magneticstorerejecteddatalocation-s3configuration): {{
    S3Configuration}}
```

## Properties
<a name="aws-properties-timestream-table-magneticstorerejecteddatalocation-properties"></a>

`S3Configuration`  <a name="cfn-timestream-table-magneticstorerejecteddatalocation-s3configuration"></a>
Configuration of an S3 location to write error reports for records rejected, asynchronously, during magnetic store writes.
*Required*: No
*Type*: [S3Configuration](aws-properties-timestream-table-s3configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
