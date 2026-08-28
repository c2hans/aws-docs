---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-reportgroup-reportexportconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::ReportGroup ReportExportConfig
<a name="aws-properties-codebuild-reportgroup-reportexportconfig"></a>

 Information about the location where the run of a report is exported.

## Syntax
<a name="aws-properties-codebuild-reportgroup-reportexportconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-reportgroup-reportexportconfig-syntax.json"></a>

```
{
  "[ExportConfigType](#cfn-codebuild-reportgroup-reportexportconfig-exportconfigtype)" : {{String}},
  "[S3Destination](#cfn-codebuild-reportgroup-reportexportconfig-s3destination)" : {{S3ReportExportConfig}}
}
```

### YAML
<a name="aws-properties-codebuild-reportgroup-reportexportconfig-syntax.yaml"></a>

```
  [ExportConfigType](#cfn-codebuild-reportgroup-reportexportconfig-exportconfigtype): {{String}}
  [S3Destination](#cfn-codebuild-reportgroup-reportexportconfig-s3destination): {{
    S3ReportExportConfig}}
```

## Properties
<a name="aws-properties-codebuild-reportgroup-reportexportconfig-properties"></a>

`ExportConfigType`  <a name="cfn-codebuild-reportgroup-reportexportconfig-exportconfigtype"></a>
 The export configuration type. Valid values are:
+ `S3`: The report results are exported to an S3 bucket.
+ `NO_EXPORT`: The report results are not exported.
*Required*: Yes
*Type*: String
*Allowed values*: `S3 | NO_EXPORT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Destination`  <a name="cfn-codebuild-reportgroup-reportexportconfig-s3destination"></a>
 A `S3ReportExportConfig` object that contains information about the S3 bucket where the run of a report is exported.
*Required*: No
*Type*: [S3ReportExportConfig](aws-properties-codebuild-reportgroup-s3reportexportconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
