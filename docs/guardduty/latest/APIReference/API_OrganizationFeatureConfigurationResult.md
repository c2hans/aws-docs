---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_OrganizationFeatureConfigurationResult.html
---

# OrganizationFeatureConfigurationResult
<a name="API_OrganizationFeatureConfigurationResult"></a>

A list of features which will be configured for the organization.

## Contents
<a name="API_OrganizationFeatureConfigurationResult_Contents"></a>

 ** additionalConfiguration **   <a name="guardduty-Type-OrganizationFeatureConfigurationResult-additionalConfiguration"></a>
The additional configuration that is configured for the member accounts within the organization.
Type: Array of [OrganizationAdditionalConfigurationResult](API_OrganizationAdditionalConfigurationResult.md) objects
Required: No

 ** autoEnable **   <a name="guardduty-Type-OrganizationFeatureConfigurationResult-autoEnable"></a>
Describes the status of the feature that is configured for the member accounts within the organization.
+  `NEW`: Indicates that when a new account joins the organization, they will have the feature enabled automatically.
+  `ALL`: Indicates that all accounts in the organization have the feature enabled automatically. This includes `NEW` accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.
+  `NONE`: Indicates that the feature will not be automatically enabled for any account in the organization. In this case, each account will be managed individually by the administrator.
Type: String
Valid Values: `NEW | NONE | ALL`
Required: No

 ** name **   <a name="guardduty-Type-OrganizationFeatureConfigurationResult-name"></a>
The name of the feature that is configured for the member accounts within the organization.
Type: String
Valid Values: `S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | RUNTIME_MONITORING | AI_PROTECTION`
Required: No

## See Also
<a name="API_OrganizationFeatureConfigurationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/OrganizationFeatureConfigurationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/OrganizationFeatureConfigurationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/OrganizationFeatureConfigurationResult)
