---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseConfiguration.html
---

# LicenseConfiguration
<a name="API_LicenseConfiguration"></a>

A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated Instance, Dedicated Host, or all of these), host affinity (how long a VM must be associated with a host), and the number of licenses purchased and used.

## Contents
<a name="API_LicenseConfiguration_Contents"></a>

 ** AutomatedDiscoveryInformation **   <a name="licensemanager-Type-LicenseConfiguration-AutomatedDiscoveryInformation"></a>
Automated discovery information.
Type: [AutomatedDiscoveryInformation](API_AutomatedDiscoveryInformation.md) object
Required: No

 ** ConsumedLicenses **   <a name="licensemanager-Type-LicenseConfiguration-ConsumedLicenses"></a>
Number of licenses consumed.
Type: Long
Required: No

 ** ConsumedLicenseSummaryList **   <a name="licensemanager-Type-LicenseConfiguration-ConsumedLicenseSummaryList"></a>
Summaries for licenses consumed by various resources.
Type: Array of [ConsumedLicenseSummary](API_ConsumedLicenseSummary.md) objects
Required: No

 ** Description **   <a name="licensemanager-Type-LicenseConfiguration-Description"></a>
Description of the license configuration.
Type: String
Required: No

 ** DisassociateWhenNotFound **   <a name="licensemanager-Type-LicenseConfiguration-DisassociateWhenNotFound"></a>
When true, disassociates a resource when software is uninstalled.
Type: Boolean
Required: No

 ** LicenseConfigurationArn **   <a name="licensemanager-Type-LicenseConfiguration-LicenseConfigurationArn"></a>
Amazon Resource Name (ARN) of the license configuration.
Type: String
Required: No

 ** LicenseConfigurationId **   <a name="licensemanager-Type-LicenseConfiguration-LicenseConfigurationId"></a>
Unique ID of the license configuration.
Type: String
Required: No

 ** LicenseCount **   <a name="licensemanager-Type-LicenseConfiguration-LicenseCount"></a>
Number of licenses managed by the license configuration.
Type: Long
Required: No

 ** LicenseCountHardLimit **   <a name="licensemanager-Type-LicenseConfiguration-LicenseCountHardLimit"></a>
Number of available licenses as a hard limit.
Type: Boolean
Required: No

 ** LicenseCountingType **   <a name="licensemanager-Type-LicenseConfiguration-LicenseCountingType"></a>
Dimension to use to track the license inventory.
Type: String
Valid Values: `vCPU | Instance | Core | Socket`
Required: No

 ** LicenseExpiry **   <a name="licensemanager-Type-LicenseConfiguration-LicenseExpiry"></a>
License configuration expiry time in Unix timestamp format.
Type: Long
Required: No

 ** LicenseRules **   <a name="licensemanager-Type-LicenseConfiguration-LicenseRules"></a>
License rules.
Type: Array of strings
Required: No

 ** ManagedResourceSummaryList **   <a name="licensemanager-Type-LicenseConfiguration-ManagedResourceSummaryList"></a>
Summaries for managed resources.
Type: Array of [ManagedResourceSummary](API_ManagedResourceSummary.md) objects
Required: No

 ** Name **   <a name="licensemanager-Type-LicenseConfiguration-Name"></a>
Name of the license configuration.
Type: String
Required: No

 ** OwnerAccountId **   <a name="licensemanager-Type-LicenseConfiguration-OwnerAccountId"></a>
Account ID of the license configuration's owner.
Type: String
Required: No

 ** ProductInformationList **   <a name="licensemanager-Type-LicenseConfiguration-ProductInformationList"></a>
Product information.
Type: Array of [ProductInformation](API_ProductInformation.md) objects
Required: No

 ** Status **   <a name="licensemanager-Type-LicenseConfiguration-Status"></a>
Status of the license configuration.
Type: String
Required: No

## See Also
<a name="API_LicenseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/LicenseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/LicenseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/LicenseConfiguration)
