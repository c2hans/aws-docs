---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ExportErrorReportLocation.html
---

# ExportErrorReportLocation
<a name="API_ExportErrorReportLocation"></a>

Contains the location where error reports will be written on failure.

## Contents
<a name="API_ExportErrorReportLocation_Contents"></a>

 ** s3Uri **   <a name="iotsitewise-Type-ExportErrorReportLocation-s3Uri"></a>
The S3 URI prefix for the error report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.+`
Required: Yes

## See Also
<a name="API_ExportErrorReportLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ExportErrorReportLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ExportErrorReportLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ExportErrorReportLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
