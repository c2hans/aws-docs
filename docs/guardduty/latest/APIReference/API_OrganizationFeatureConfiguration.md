---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_OrganizationFeatureConfiguration.html
---

# OrganizationFeatureConfiguration
<a name="API_OrganizationFeatureConfiguration"></a>

A list of features which will be configured for the organization.

## Contents
<a name="API_OrganizationFeatureConfiguration_Contents"></a>

 ** additionalConfiguration **   <a name="guardduty-Type-OrganizationFeatureConfiguration-additionalConfiguration"></a>
The additional information that will be configured for the organization.
Type: Array of [OrganizationAdditionalConfiguration](API_OrganizationAdditionalConfiguration.md) objects
Required: No

 ** autoEnable **   <a name="guardduty-Type-OrganizationFeatureConfiguration-autoEnable"></a>
Describes the status of the feature that is configured for the member accounts within the organization. One of the following values is the status for the entire organization:
+  `NEW`: Indicates that when a new account joins the organization, they will have the feature enabled automatically.
+  `ALL`: Indicates that all accounts in the organization have the feature enabled automatically. This includes `NEW` accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.

  It may take up to 24 hours to update the configuration for all the member accounts.
+  `NONE`: Indicates that the feature will not be automatically enabled for any account in the organization. The administrator must manage the feature for each account individually.
Type: String
Valid Values: `NEW | NONE | ALL`
Required: No

 ** name **   <a name="guardduty-Type-OrganizationFeatureConfiguration-name"></a>
The name of the feature that will be configured for the organization.
Type: String
Valid Values: `S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | RUNTIME_MONITORING | AI_PROTECTION`
Required: No

## See Also
<a name="API_OrganizationFeatureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/OrganizationFeatureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/OrganizationFeatureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/OrganizationFeatureConfiguration)
