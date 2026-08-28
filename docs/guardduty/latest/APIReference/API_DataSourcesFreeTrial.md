---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DataSourcesFreeTrial.html
---

# DataSourcesFreeTrial
<a name="API_DataSourcesFreeTrial"></a>

Contains information about which data sources are enabled for the GuardDuty member account.

## Contents
<a name="API_DataSourcesFreeTrial_Contents"></a>

 ** cloudTrail **   <a name="guardduty-Type-DataSourcesFreeTrial-cloudTrail"></a>
Describes whether any AWS CloudTrail management event logs are enabled as data sources.
Type: [DataSourceFreeTrial](API_DataSourceFreeTrial.md) object
Required: No

 ** dnsLogs **   <a name="guardduty-Type-DataSourcesFreeTrial-dnsLogs"></a>
Describes whether any DNS logs are enabled as data sources.
Type: [DataSourceFreeTrial](API_DataSourceFreeTrial.md) object
Required: No

 ** flowLogs **   <a name="guardduty-Type-DataSourcesFreeTrial-flowLogs"></a>
Describes whether any VPC Flow logs are enabled as data sources.
Type: [DataSourceFreeTrial](API_DataSourceFreeTrial.md) object
Required: No

 ** kubernetes **   <a name="guardduty-Type-DataSourcesFreeTrial-kubernetes"></a>
Describes whether any Kubernetes logs are enabled as data sources.
Type: [KubernetesDataSourceFreeTrial](API_KubernetesDataSourceFreeTrial.md) object
Required: No

 ** malwareProtection **   <a name="guardduty-Type-DataSourcesFreeTrial-malwareProtection"></a>
Describes whether Malware Protection is enabled as a data source.
Type: [MalwareProtectionDataSourceFreeTrial](API_MalwareProtectionDataSourceFreeTrial.md) object
Required: No

 ** s3Logs **   <a name="guardduty-Type-DataSourcesFreeTrial-s3Logs"></a>
Describes whether any S3 data event logs are enabled as data sources.
Type: [DataSourceFreeTrial](API_DataSourceFreeTrial.md) object
Required: No

## See Also
<a name="API_DataSourcesFreeTrial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DataSourcesFreeTrial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DataSourcesFreeTrial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DataSourcesFreeTrial)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
