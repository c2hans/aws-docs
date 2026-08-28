---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_LinuxSubscriptionsDiscoverySettings.html
---

# LinuxSubscriptionsDiscoverySettings
<a name="API_LinuxSubscriptionsDiscoverySettings"></a>

Lists the settings defined for discovering Linux subscriptions.

## Contents
<a name="API_LinuxSubscriptionsDiscoverySettings_Contents"></a>

 ** OrganizationIntegration **   <a name="licensemanagerlinuxsubscriptions-Type-LinuxSubscriptionsDiscoverySettings-OrganizationIntegration"></a>
Details if you have enabled resource discovery across your accounts in AWS Organizations.
Type: String
Valid Values: `Enabled | Disabled`
Required: Yes

 ** SourceRegions **   <a name="licensemanagerlinuxsubscriptions-Type-LinuxSubscriptionsDiscoverySettings-SourceRegions"></a>
The Regions in which to discover data for Linux subscriptions.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## See Also
<a name="API_LinuxSubscriptionsDiscoverySettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/LinuxSubscriptionsDiscoverySettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/LinuxSubscriptionsDiscoverySettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/LinuxSubscriptionsDiscoverySettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager Linux Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-linux-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
