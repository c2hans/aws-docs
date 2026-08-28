---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ParametricMonitoringConfiguration.html
---

# ParametricMonitoringConfiguration
<a name="API_ParametricMonitoringConfiguration"></a>

 Configuration setting for monitoring. This data type allows job template parameters to be specified within.

## Contents
<a name="API_ParametricMonitoringConfiguration_Contents"></a>

 ** cloudWatchMonitoringConfiguration **   <a name="emroneks-Type-ParametricMonitoringConfiguration-cloudWatchMonitoringConfiguration"></a>
 Monitoring configurations for CloudWatch.
Type: [ParametricCloudWatchMonitoringConfiguration](API_ParametricCloudWatchMonitoringConfiguration.md) object
Required: No

 ** persistentAppUI **   <a name="emroneks-Type-ParametricMonitoringConfiguration-persistentAppUI"></a>
 Monitoring configurations for the persistent application UI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9\$\{\}]+`
Required: No

 ** s3MonitoringConfiguration **   <a name="emroneks-Type-ParametricMonitoringConfiguration-s3MonitoringConfiguration"></a>
 Amazon S3 configuration for monitoring log publishing.
Type: [ParametricS3MonitoringConfiguration](API_ParametricS3MonitoringConfiguration.md) object
Required: No

## See Also
<a name="API_ParametricMonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ParametricMonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ParametricMonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ParametricMonitoringConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
