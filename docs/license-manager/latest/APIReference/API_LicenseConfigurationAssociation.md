---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseConfigurationAssociation.html
---

# LicenseConfigurationAssociation
<a name="API_LicenseConfigurationAssociation"></a>

Describes an association with a license configuration.

## Contents
<a name="API_LicenseConfigurationAssociation_Contents"></a>

 ** AmiAssociationScope **   <a name="licensemanager-Type-LicenseConfigurationAssociation-AmiAssociationScope"></a>
Scope of AMI associations. The possible value is `cross-account`.
Type: String
Required: No

 ** AssociationTime **   <a name="licensemanager-Type-LicenseConfigurationAssociation-AssociationTime"></a>
Time when the license configuration was associated with the resource.
Type: Timestamp
Required: No

 ** ResourceArn **   <a name="licensemanager-Type-LicenseConfigurationAssociation-ResourceArn"></a>
Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** ResourceOwnerId **   <a name="licensemanager-Type-LicenseConfigurationAssociation-ResourceOwnerId"></a>
ID of the AWS account that owns the resource consuming licenses.
Type: String
Required: No

 ** ResourceType **   <a name="licensemanager-Type-LicenseConfigurationAssociation-ResourceType"></a>
Type of server resource.
Type: String
Valid Values: `EC2_INSTANCE | EC2_HOST | EC2_AMI | RDS | SYSTEMS_MANAGER_MANAGED_INSTANCE`
Required: No

## See Also
<a name="API_LicenseConfigurationAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/LicenseConfigurationAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/LicenseConfigurationAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/LicenseConfigurationAssociation)
