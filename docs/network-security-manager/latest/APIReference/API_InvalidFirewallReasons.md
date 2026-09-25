---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_InvalidFirewallReasons.html
---

# InvalidFirewallReasons
<a name="API_InvalidFirewallReasons"></a>

Details about the ways in which a firewall's configuration differs from the intended configuration.

## Contents
<a name="API_InvalidFirewallReasons_Contents"></a>

 ** incorrectAppendableConfigurationOrder **   <a name="networksecuritymanager-Type-InvalidFirewallReasons-incorrectAppendableConfigurationOrder"></a>
Appendable configuration values that are present but in the wrong order.
Type: Array of [ConfigurationIssue](API_ConfigurationIssue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** incorrectSingleValueConfigurations **   <a name="networksecuritymanager-Type-InvalidFirewallReasons-incorrectSingleValueConfigurations"></a>
Single-value configuration settings whose values do not match the expected values.
Type: Array of [ConfigurationIssue](API_ConfigurationIssue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** missingAppendableConfigurationValues **   <a name="networksecuritymanager-Type-InvalidFirewallReasons-missingAppendableConfigurationValues"></a>
Appendable configuration values that are expected but missing.
Type: Array of [ConfigurationIssue](API_ConfigurationIssue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** missingMergeableConfigurationValues **   <a name="networksecuritymanager-Type-InvalidFirewallReasons-missingMergeableConfigurationValues"></a>
Mergeable configuration values that are expected but missing.
Type: Array of [ConfigurationIssue](API_ConfigurationIssue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** unexpectedAppendableConfigurationValues **   <a name="networksecuritymanager-Type-InvalidFirewallReasons-unexpectedAppendableConfigurationValues"></a>
Appendable configuration values that are present but not expected.
Type: Array of [ConfigurationIssue](API_ConfigurationIssue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** unexpectedMergeableConfigurationValues **   <a name="networksecuritymanager-Type-InvalidFirewallReasons-unexpectedMergeableConfigurationValues"></a>
Mergeable configuration values that are present but not expected.
Type: Array of [ConfigurationIssue](API_ConfigurationIssue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_InvalidFirewallReasons_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/InvalidFirewallReasons)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/InvalidFirewallReasons)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/InvalidFirewallReasons)
