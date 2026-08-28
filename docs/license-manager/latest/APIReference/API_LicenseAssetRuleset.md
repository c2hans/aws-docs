---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseAssetRuleset.html
---

# LicenseAssetRuleset
<a name="API_LicenseAssetRuleset"></a>

License asset ruleset.

## Contents
<a name="API_LicenseAssetRuleset_Contents"></a>

 ** LicenseAssetRulesetArn **   <a name="licensemanager-Type-LicenseAssetRuleset-LicenseAssetRulesetArn"></a>
Amazon Resource Name (ARN) of the license asset ruleset.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** Name **   <a name="licensemanager-Type-LicenseAssetRuleset-Name"></a>
License asset ruleset name.
Type: String
Required: Yes

 ** Rules **   <a name="licensemanager-Type-LicenseAssetRuleset-Rules"></a>
License asset rules.
Type: Array of [LicenseAssetRule](API_LicenseAssetRule.md) objects
Required: Yes

 ** Description **   <a name="licensemanager-Type-LicenseAssetRuleset-Description"></a>
License asset ruleset description.
Type: String
Required: No

## See Also
<a name="API_LicenseAssetRuleset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/LicenseAssetRuleset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/LicenseAssetRuleset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/LicenseAssetRuleset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
