---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ParametricS3MonitoringConfiguration.html
---

# ParametricS3MonitoringConfiguration
<a name="API_ParametricS3MonitoringConfiguration"></a>

 Amazon S3 configuration for monitoring log publishing. You can configure your jobs to send log information to Amazon S3. This data type allows job template parameters to be specified within.

## Contents
<a name="API_ParametricS3MonitoringConfiguration_Contents"></a>

 ** logUri **   <a name="emroneks-Type-ParametricS3MonitoringConfiguration-logUri"></a>
Amazon S3 destination URI for log publishing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_ParametricS3MonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ParametricS3MonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ParametricS3MonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ParametricS3MonitoringConfiguration)
