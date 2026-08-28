---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ReportExportConfig.html
---

# ReportExportConfig
<a name="API_ReportExportConfig"></a>

 Information about the location where the run of a report is exported.

## Contents
<a name="API_ReportExportConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** exportConfigType **   <a name="CodeBuild-Type-ReportExportConfig-exportConfigType"></a>
 The export configuration type. Valid values are:
+  `S3`: The report results are exported to an S3 bucket.
+  `NO_EXPORT`: The report results are not exported.
Type: String
Valid Values: `S3 | NO_EXPORT`
Required: No

 ** s3Destination **   <a name="CodeBuild-Type-ReportExportConfig-s3Destination"></a>
 A `S3ReportExportConfig` object that contains information about the S3 bucket where the run of a report is exported.
Type: [S3ReportExportConfig](API_S3ReportExportConfig.md) object
Required: No

## See Also
<a name="API_ReportExportConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ReportExportConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ReportExportConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ReportExportConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
