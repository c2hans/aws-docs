---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_OrganizationDataSourceConfigurationsResult.html
---

# OrganizationDataSourceConfigurationsResult
<a name="API_OrganizationDataSourceConfigurationsResult"></a>

An object that contains information on which data sources are automatically enabled for new members within the organization.

## Contents
<a name="API_OrganizationDataSourceConfigurationsResult_Contents"></a>

 ** s3Logs **   <a name="guardduty-Type-OrganizationDataSourceConfigurationsResult-s3Logs"></a>
Describes whether S3 data event logs are enabled as a data source.
Type: [OrganizationS3LogsConfigurationResult](API_OrganizationS3LogsConfigurationResult.md) object
Required: Yes

 ** kubernetes **   <a name="guardduty-Type-OrganizationDataSourceConfigurationsResult-kubernetes"></a>
Describes the configuration of Kubernetes data sources.
Type: [OrganizationKubernetesConfigurationResult](API_OrganizationKubernetesConfigurationResult.md) object
Required: No

 ** malwareProtection **   <a name="guardduty-Type-OrganizationDataSourceConfigurationsResult-malwareProtection"></a>
Describes the configuration of Malware Protection data source for an organization.
Type: [OrganizationMalwareProtectionConfigurationResult](API_OrganizationMalwareProtectionConfigurationResult.md) object
Required: No

## See Also
<a name="API_OrganizationDataSourceConfigurationsResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/OrganizationDataSourceConfigurationsResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/OrganizationDataSourceConfigurationsResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/OrganizationDataSourceConfigurationsResult)
