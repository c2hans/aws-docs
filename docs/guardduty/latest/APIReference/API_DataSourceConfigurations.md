---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DataSourceConfigurations.html
---

# DataSourceConfigurations
<a name="API_DataSourceConfigurations"></a>

Contains information about which data sources are enabled.

## Contents
<a name="API_DataSourceConfigurations_Contents"></a>

 ** kubernetes **   <a name="guardduty-Type-DataSourceConfigurations-kubernetes"></a>
Describes whether any Kubernetes logs are enabled as data sources.
Type: [KubernetesConfiguration](API_KubernetesConfiguration.md) object
Required: No

 ** malwareProtection **   <a name="guardduty-Type-DataSourceConfigurations-malwareProtection"></a>
Describes whether Malware Protection is enabled as a data source.
Type: [MalwareProtectionConfiguration](API_MalwareProtectionConfiguration.md) object
Required: No

 ** s3Logs **   <a name="guardduty-Type-DataSourceConfigurations-s3Logs"></a>
Describes whether S3 data event logs are enabled as a data source.
Type: [S3LogsConfiguration](API_S3LogsConfiguration.md) object
Required: No

## See Also
<a name="API_DataSourceConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DataSourceConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DataSourceConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DataSourceConfigurations)
