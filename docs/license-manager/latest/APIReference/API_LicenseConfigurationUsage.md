---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseConfigurationUsage.html
---

# LicenseConfigurationUsage
<a name="API_LicenseConfigurationUsage"></a>

Details about the usage of a resource associated with a license configuration.

## Contents
<a name="API_LicenseConfigurationUsage_Contents"></a>

 ** AssociationTime **   <a name="licensemanager-Type-LicenseConfigurationUsage-AssociationTime"></a>
Time when the license configuration was initially associated with the resource.
Type: Timestamp
Required: No

 ** ConsumedLicenses **   <a name="licensemanager-Type-LicenseConfigurationUsage-ConsumedLicenses"></a>
Number of licenses consumed by the resource.
Type: Long
Required: No

 ** ResourceArn **   <a name="licensemanager-Type-LicenseConfigurationUsage-ResourceArn"></a>
Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** ResourceOwnerId **   <a name="licensemanager-Type-LicenseConfigurationUsage-ResourceOwnerId"></a>
ID of the account that owns the resource.
Type: String
Required: No

 ** ResourceStatus **   <a name="licensemanager-Type-LicenseConfigurationUsage-ResourceStatus"></a>
Status of the resource.
Type: String
Required: No

 ** ResourceType **   <a name="licensemanager-Type-LicenseConfigurationUsage-ResourceType"></a>
Type of resource.
Type: String
Valid Values: `EC2_INSTANCE | EC2_HOST | EC2_AMI | RDS | SYSTEMS_MANAGER_MANAGED_INSTANCE`
Required: No

## See Also
<a name="API_LicenseConfigurationUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/LicenseConfigurationUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/LicenseConfigurationUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/LicenseConfigurationUsage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
