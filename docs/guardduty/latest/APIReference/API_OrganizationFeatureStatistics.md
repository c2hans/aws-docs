---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_OrganizationFeatureStatistics.html
---

# OrganizationFeatureStatistics
<a name="API_OrganizationFeatureStatistics"></a>

Information about the number of accounts that have enabled a specific feature.

## Contents
<a name="API_OrganizationFeatureStatistics_Contents"></a>

 ** additionalConfiguration **   <a name="guardduty-Type-OrganizationFeatureStatistics-additionalConfiguration"></a>
Name of the additional configuration.
Type: Array of [OrganizationFeatureStatisticsAdditionalConfiguration](API_OrganizationFeatureStatisticsAdditionalConfiguration.md) objects
Required: No

 ** enabledAccountsCount **   <a name="guardduty-Type-OrganizationFeatureStatistics-enabledAccountsCount"></a>
Total number of accounts that have enabled a specific feature.
Type: Integer
Required: No

 ** name **   <a name="guardduty-Type-OrganizationFeatureStatistics-name"></a>
Name of the feature.
Type: String
Valid Values: `S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | RUNTIME_MONITORING | AI_PROTECTION`
Required: No

## See Also
<a name="API_OrganizationFeatureStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/OrganizationFeatureStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/OrganizationFeatureStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/OrganizationFeatureStatistics)
