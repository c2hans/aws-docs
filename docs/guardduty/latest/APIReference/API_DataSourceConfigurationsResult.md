---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DataSourceConfigurationsResult.html
---

# DataSourceConfigurationsResult
<a name="API_DataSourceConfigurationsResult"></a>

Contains information on the status of data sources for the detector.

## Contents
<a name="API_DataSourceConfigurationsResult_Contents"></a>

 ** cloudTrail **   <a name="guardduty-Type-DataSourceConfigurationsResult-cloudTrail"></a>
An object that contains information on the status of CloudTrail as a data source.
Type: [CloudTrailConfigurationResult](API_CloudTrailConfigurationResult.md) object
Required: Yes

 ** dnsLogs **   <a name="guardduty-Type-DataSourceConfigurationsResult-dnsLogs"></a>
An object that contains information on the status of DNS logs as a data source.
Type: [DNSLogsConfigurationResult](API_DNSLogsConfigurationResult.md) object
Required: Yes

 ** flowLogs **   <a name="guardduty-Type-DataSourceConfigurationsResult-flowLogs"></a>
An object that contains information on the status of VPC flow logs as a data source.
Type: [FlowLogsConfigurationResult](API_FlowLogsConfigurationResult.md) object
Required: Yes

 ** s3Logs **   <a name="guardduty-Type-DataSourceConfigurationsResult-s3Logs"></a>
An object that contains information on the status of S3 Data event logs as a data source.
Type: [S3LogsConfigurationResult](API_S3LogsConfigurationResult.md) object
Required: Yes

 ** kubernetes **   <a name="guardduty-Type-DataSourceConfigurationsResult-kubernetes"></a>
An object that contains information on the status of all Kubernetes data sources.
Type: [KubernetesConfigurationResult](API_KubernetesConfigurationResult.md) object
Required: No

 ** malwareProtection **   <a name="guardduty-Type-DataSourceConfigurationsResult-malwareProtection"></a>
Describes the configuration of Malware Protection data sources.
Type: [MalwareProtectionConfigurationResult](API_MalwareProtectionConfigurationResult.md) object
Required: No

## See Also
<a name="API_DataSourceConfigurationsResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DataSourceConfigurationsResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DataSourceConfigurationsResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DataSourceConfigurationsResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
