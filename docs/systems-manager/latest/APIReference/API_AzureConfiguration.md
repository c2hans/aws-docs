---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AzureConfiguration.html
---

# AzureConfiguration
<a name="API_AzureConfiguration"></a>

The access details and targets for connecting to a Microsoft Azure tenant, including the application registration used for authentication and the subscriptions to target.

## Contents
<a name="API_AzureConfiguration_Contents"></a>

 ** ApplicationId **   <a name="systemsmanager-Type-AzureConfiguration-ApplicationId"></a>
The ID of the Azure application registration used for authentication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

 ** TenantId **   <a name="systemsmanager-Type-AzureConfiguration-TenantId"></a>
The ID of the Azure tenant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

 ** ApplicationDisplayName **   <a name="systemsmanager-Type-AzureConfiguration-ApplicationDisplayName"></a>
The display name of the Azure application registration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
Required: No

 ** Targets **   <a name="systemsmanager-Type-AzureConfiguration-Targets"></a>
The target Azure subscriptions for the cloud connector.
Type: [ConfigurationTargets](API_ConfigurationTargets.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** TenantDisplayName **   <a name="systemsmanager-Type-AzureConfiguration-TenantDisplayName"></a>
The display name of the Azure tenant.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
Required: No

## See Also
<a name="API_AzureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AzureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AzureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AzureConfiguration)
