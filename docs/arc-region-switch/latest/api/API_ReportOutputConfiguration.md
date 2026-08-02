---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ReportOutputConfiguration.html
---

# ReportOutputConfiguration
<a name="API_ReportOutputConfiguration"></a>

Configuration for report output destinations used in a Region switch plan.

## Contents
<a name="API_ReportOutputConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3Configuration **   <a name="regionswitch-Type-ReportOutputConfiguration-s3Configuration"></a>
Configuration for delivering reports to an Amazon S3 bucket.
Type: [S3ReportOutputConfiguration](API_S3ReportOutputConfiguration.md) object
Required: No

## See Also
<a name="API_ReportOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ReportOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ReportOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ReportOutputConfiguration)
