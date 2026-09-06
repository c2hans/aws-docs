---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ParametricCloudWatchMonitoringConfiguration.html
---

# ParametricCloudWatchMonitoringConfiguration
<a name="API_ParametricCloudWatchMonitoringConfiguration"></a>

 A configuration for CloudWatch monitoring. You can configure your jobs to send log information to CloudWatch Logs. This data type allows job template parameters to be specified within.

## Contents
<a name="API_ParametricCloudWatchMonitoringConfiguration_Contents"></a>

 ** logGroupName **   <a name="emroneks-Type-ParametricCloudWatchMonitoringConfiguration-logGroupName"></a>
 The name of the log group for log publishing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9\$\{\}]+`
Required: No

 ** logStreamNamePrefix **   <a name="emroneks-Type-ParametricCloudWatchMonitoringConfiguration-logStreamNamePrefix"></a>
 The specified name prefix for log streams.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ParametricCloudWatchMonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ParametricCloudWatchMonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ParametricCloudWatchMonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ParametricCloudWatchMonitoringConfiguration)
