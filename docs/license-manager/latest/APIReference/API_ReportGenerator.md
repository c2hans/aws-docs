---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ReportGenerator.html
---

# ReportGenerator
<a name="API_ReportGenerator"></a>

Describe the details of a report generator.

## Contents
<a name="API_ReportGenerator_Contents"></a>

 ** CreateTime **   <a name="licensemanager-Type-ReportGenerator-CreateTime"></a>
Time the report was created.
Type: String
Required: No

 ** Description **   <a name="licensemanager-Type-ReportGenerator-Description"></a>
Description of the report generator.
Type: String
Required: No

 ** LastReportGenerationTime **   <a name="licensemanager-Type-ReportGenerator-LastReportGenerationTime"></a>
Time the last report was generated at.
Type: String
Required: No

 ** LastRunFailureReason **   <a name="licensemanager-Type-ReportGenerator-LastRunFailureReason"></a>
Failure message for the last report generation attempt.
Type: String
Required: No

 ** LastRunStatus **   <a name="licensemanager-Type-ReportGenerator-LastRunStatus"></a>
Status of the last report generation attempt.
Type: String
Required: No

 ** LicenseManagerReportGeneratorArn **   <a name="licensemanager-Type-ReportGenerator-LicenseManagerReportGeneratorArn"></a>
Amazon Resource Name (ARN) of the report generator.
Type: String
Required: No

 ** ReportContext **   <a name="licensemanager-Type-ReportGenerator-ReportContext"></a>
License configuration type for this generator.
Type: [ReportContext](API_ReportContext.md) object
Required: No

 ** ReportCreatorAccount **   <a name="licensemanager-Type-ReportGenerator-ReportCreatorAccount"></a>
The AWS account ID used to create the report generator.
Type: String
Required: No

 ** ReportFrequency **   <a name="licensemanager-Type-ReportGenerator-ReportFrequency"></a>
Details about how frequently reports are generated.
Type: [ReportFrequency](API_ReportFrequency.md) object
Required: No

 ** ReportGeneratorName **   <a name="licensemanager-Type-ReportGenerator-ReportGeneratorName"></a>
Name of the report generator.
Type: String
Required: No

 ** ReportType **   <a name="licensemanager-Type-ReportGenerator-ReportType"></a>
Type of reports that are generated.
Type: Array of strings
Valid Values: `LicenseConfigurationSummaryReport | LicenseConfigurationUsageReport | LicenseAssetGroupUsageReport`
Required: No

 ** S3Location **   <a name="licensemanager-Type-ReportGenerator-S3Location"></a>
Details of the S3 bucket that report generator reports are published to.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** Tags **   <a name="licensemanager-Type-ReportGenerator-Tags"></a>
Tags associated with the report generator.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ReportGenerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ReportGenerator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ReportGenerator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ReportGenerator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
