---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_OrganizationConfiguration.html
---

# OrganizationConfiguration
<a name="API_OrganizationConfiguration"></a>

 Provides information about the way an organization is configured in AWS Security Hub CSPM.

## Contents
<a name="API_OrganizationConfiguration_Contents"></a>

 ** ConfigurationType **   <a name="securityhub-Type-OrganizationConfiguration-ConfigurationType"></a>
 Indicates whether the organization uses local or central configuration.
If you use local configuration, the Security Hub CSPM delegated administrator can set `AutoEnable` to `true` and `AutoEnableStandards` to `DEFAULT`. This automatically enables Security Hub CSPM and default security standards in new organization accounts. These new account settings must be set separately in each AWS Region, and settings may be different in each Region.
 If you use central configuration, the delegated administrator can create configuration policies. Configuration policies can be used to configure Security Hub CSPM, security standards, and security controls in multiple accounts and Regions. If you want new organization accounts to use a specific configuration, you can create a configuration policy and associate it with the root or specific organizational units (OUs). New accounts will inherit the policy from the root or their assigned OU.
Type: String
Valid Values: `CENTRAL | LOCAL`
Required: No

 ** Status **   <a name="securityhub-Type-OrganizationConfiguration-Status"></a>
 Describes whether central configuration could be enabled as the `ConfigurationType` for the organization. If your `ConfigurationType` is local configuration, then the value of `Status` is always `ENABLED`.
Type: String
Valid Values: `PENDING | ENABLED | FAILED`
Required: No

 ** StatusMessage **   <a name="securityhub-Type-OrganizationConfiguration-StatusMessage"></a>
 Provides an explanation if the value of `Status` is equal to `FAILED` when `ConfigurationType` is equal to `CENTRAL`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_OrganizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/OrganizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/OrganizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/OrganizationConfiguration)
