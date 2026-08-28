---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ReportGroup.html
---

# ReportGroup
<a name="API_ReportGroup"></a>

A series of reports. Each report contains information about the results from running a series of test cases. You specify the test cases for a report group in the buildspec for a build project using one or more paths to the test case files.

## Contents
<a name="API_ReportGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="CodeBuild-Type-ReportGroup-arn"></a>
The ARN of the `ReportGroup`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** created **   <a name="CodeBuild-Type-ReportGroup-created"></a>
The date and time this `ReportGroup` was created.
Type: Timestamp
Required: No

 ** exportConfig **   <a name="CodeBuild-Type-ReportGroup-exportConfig"></a>
Information about the destination where the raw data of this `ReportGroup` is exported.
Type: [ReportExportConfig](API_ReportExportConfig.md) object
Required: No

 ** lastModified **   <a name="CodeBuild-Type-ReportGroup-lastModified"></a>
The date and time this `ReportGroup` was last modified.
Type: Timestamp
Required: No

 ** name **   <a name="CodeBuild-Type-ReportGroup-name"></a>
The name of the `ReportGroup`.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Required: No

 ** status **   <a name="CodeBuild-Type-ReportGroup-status"></a>
The status of the report group. This property is read-only.
This can be one of the following values:
ACTIVE
The report group is active.
DELETING
The report group is in the process of being deleted.
Type: String
Valid Values: `ACTIVE | DELETING`
Required: No

 ** tags **   <a name="CodeBuild-Type-ReportGroup-tags"></a>
A list of tag key and value pairs associated with this report group.
These tags are available for use by AWS services that support AWS CodeBuild report group tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** type **   <a name="CodeBuild-Type-ReportGroup-type"></a>
The type of the `ReportGroup`. This can be one of the following values:
CODE\_COVERAGE
The report group contains code coverage reports.
TEST
The report group contains test reports.
Type: String
Valid Values: `TEST | CODE_COVERAGE`
Required: No

## See Also
<a name="API_ReportGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ReportGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ReportGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ReportGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
