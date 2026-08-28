---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_MonitoringConfiguration.html
---

# MonitoringConfiguration
<a name="API_MonitoringConfiguration"></a>

Configuration setting for monitoring.

## Contents
<a name="API_MonitoringConfiguration_Contents"></a>

 ** cloudWatchMonitoringConfiguration **   <a name="emroneks-Type-MonitoringConfiguration-cloudWatchMonitoringConfiguration"></a>
Monitoring configurations for CloudWatch.
Type: [CloudWatchMonitoringConfiguration](API_CloudWatchMonitoringConfiguration.md) object
Required: No

 ** containerLogRotationConfiguration **   <a name="emroneks-Type-MonitoringConfiguration-containerLogRotationConfiguration"></a>
Enable or disable container log rotation.
Type: [ContainerLogRotationConfiguration](API_ContainerLogRotationConfiguration.md) object
Required: No

 ** managedLogs **   <a name="emroneks-Type-MonitoringConfiguration-managedLogs"></a>
The entity that controls configuration for managed logs.
Type: [ManagedLogs](API_ManagedLogs.md) object
Required: No

 ** persistentAppUI **   <a name="emroneks-Type-MonitoringConfiguration-persistentAppUI"></a>
Monitoring configurations for the persistent application UI.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** s3MonitoringConfiguration **   <a name="emroneks-Type-MonitoringConfiguration-s3MonitoringConfiguration"></a>
Amazon S3 configuration for monitoring log publishing.
Type: [S3MonitoringConfiguration](API_S3MonitoringConfiguration.md) object
Required: No

## See Also
<a name="API_MonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/MonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/MonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/MonitoringConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
