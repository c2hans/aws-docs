---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseAssetGroup.html
---

# LicenseAssetGroup
<a name="API_LicenseAssetGroup"></a>

License asset group.

## Contents
<a name="API_LicenseAssetGroup_Contents"></a>

 ** AssociatedLicenseAssetRulesetARNs **   <a name="licensemanager-Type-LicenseAssetGroup-AssociatedLicenseAssetRulesetARNs"></a>
ARNs of associated license asset rulesets.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** LicenseAssetGroupArn **   <a name="licensemanager-Type-LicenseAssetGroup-LicenseAssetGroupArn"></a>
Amazon Resource Name (ARN) of the license asset group.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** Name **   <a name="licensemanager-Type-LicenseAssetGroup-Name"></a>
License asset group name.
Type: String
Required: Yes

 ** Status **   <a name="licensemanager-Type-LicenseAssetGroup-Status"></a>
License asset group status.
Type: String
Valid Values: `ACTIVE | DISABLED | DELETED`
Required: Yes

 ** Description **   <a name="licensemanager-Type-LicenseAssetGroup-Description"></a>
License asset group description.
Type: String
Required: No

 ** LatestResourceDiscoveryTime **   <a name="licensemanager-Type-LicenseAssetGroup-LatestResourceDiscoveryTime"></a>
Latest resource discovery time.
Type: Timestamp
Required: No

 ** LatestUsageAnalysisTime **   <a name="licensemanager-Type-LicenseAssetGroup-LatestUsageAnalysisTime"></a>
Latest usage analysis time.
Type: Timestamp
Required: No

 ** LicenseAssetGroupConfigurations **   <a name="licensemanager-Type-LicenseAssetGroup-LicenseAssetGroupConfigurations"></a>
License asset group configurations.
Type: Array of [LicenseAssetGroupConfiguration](API_LicenseAssetGroupConfiguration.md) objects
Required: No

 ** Properties **   <a name="licensemanager-Type-LicenseAssetGroup-Properties"></a>
License asset group properties.
Type: Array of [LicenseAssetGroupProperty](API_LicenseAssetGroupProperty.md) objects
Required: No

 ** StatusMessage **   <a name="licensemanager-Type-LicenseAssetGroup-StatusMessage"></a>
License asset group status message.
Type: String
Required: No

## See Also
<a name="API_LicenseAssetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/LicenseAssetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/LicenseAssetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/LicenseAssetGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
