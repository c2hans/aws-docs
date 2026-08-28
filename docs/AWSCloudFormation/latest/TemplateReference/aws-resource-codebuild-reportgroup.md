---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-reportgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::ReportGroup
<a name="aws-resource-codebuild-reportgroup"></a>

Represents a report group. A report group contains a collection of reports.

## Syntax
<a name="aws-resource-codebuild-reportgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codebuild-reportgroup-syntax.json"></a>

```
{
  "Type" : "AWS::CodeBuild::ReportGroup",
  "Properties" : {
      "[DeleteReports](#cfn-codebuild-reportgroup-deletereports)" : {{Boolean}},
      "[ExportConfig](#cfn-codebuild-reportgroup-exportconfig)" : {{ReportExportConfig}},
      "[Name](#cfn-codebuild-reportgroup-name)" : {{String}},
      "[Tags](#cfn-codebuild-reportgroup-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-codebuild-reportgroup-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-codebuild-reportgroup-syntax.yaml"></a>

```
Type: AWS::CodeBuild::ReportGroup
Properties:
  [DeleteReports](#cfn-codebuild-reportgroup-deletereports): {{Boolean}}
  [ExportConfig](#cfn-codebuild-reportgroup-exportconfig): {{
    ReportExportConfig}}
  [Name](#cfn-codebuild-reportgroup-name): {{String}}
  [Tags](#cfn-codebuild-reportgroup-tags): {{
    - Tag}}
  [Type](#cfn-codebuild-reportgroup-type): {{String}}
```

## Properties
<a name="aws-resource-codebuild-reportgroup-properties"></a>

`DeleteReports`  <a name="cfn-codebuild-reportgroup-deletereports"></a>
When deleting a report group, specifies if reports within the report group should be deleted.
true
Deletes any reports that belong to the report group before deleting the report group.
false
You must delete any reports in the report group. This is the default value. If you delete a report group that contains one or more reports, an exception is thrown.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportConfig`  <a name="cfn-codebuild-reportgroup-exportconfig"></a>
Information about the destination where the raw data of this `ReportGroup` is exported.
*Required*: Yes
*Type*: [ReportExportConfig](aws-properties-codebuild-reportgroup-reportexportconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-codebuild-reportgroup-name"></a>
The name of the `ReportGroup`.
*Required*: No
*Type*: String
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-codebuild-reportgroup-tags"></a>
A list of tag key and value pairs associated with this report group.
These tags are available for use by AWS services that support AWS CodeBuild report group tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-codebuild-reportgroup-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-codebuild-reportgroup-type"></a>
The type of the `ReportGroup`. This can be one of the following values:
CODE\_COVERAGE
The report group contains code coverage reports.
TEST
The report group contains test reports.
*Required*: Yes
*Type*: String
*Allowed values*: `TEST | CODE_COVERAGE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-codebuild-reportgroup-return-values"></a>

### Ref
<a name="aws-resource-codebuild-reportgroup-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, `Ref` returns the ARN of the AWS CodeBuild report group, such as `arn:aws:codebuild:region:123456789012:report-group/myReportGroupName`.

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-codebuild-reportgroup-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values. For more information about using `Fn::GetAtt`, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-codebuild-reportgroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the AWS CodeBuild report group, such as `arn:aws:codebuild:region:123456789012:report-group/myReportGroupName`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
