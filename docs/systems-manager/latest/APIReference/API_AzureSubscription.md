---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AzureSubscription.html
---

# AzureSubscription
<a name="API_AzureSubscription"></a>

Information about an Azure subscription targeted by the cloud connector.

## Contents
<a name="API_AzureSubscription_Contents"></a>

 ** Id **   <a name="systemsmanager-Type-AzureSubscription-Id"></a>
The ID of the Azure subscription.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

 ** DisplayName **   <a name="systemsmanager-Type-AzureSubscription-DisplayName"></a>
The display name of the Azure subscription.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
Required: No

## See Also
<a name="API_AzureSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AzureSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AzureSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AzureSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
