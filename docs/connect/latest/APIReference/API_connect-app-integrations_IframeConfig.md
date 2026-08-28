---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_IframeConfig.html
---

# IframeConfig
<a name="API_connect-app-integrations_IframeConfig"></a>

The iframe configuration for the application.

## Contents
<a name="API_connect-app-integrations_IframeConfig_Contents"></a>

 ** Allow **   <a name="connect-Type-connect-app-integrations_IframeConfig-Allow"></a>
The list of features that are allowed in the iframe.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-z-]+$`
Required: No

 ** Sandbox **   <a name="connect-Type-connect-app-integrations_IframeConfig-Sandbox"></a>
The list of sandbox attributes for the iframe.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-z-]+$`
Required: No

## See Also
<a name="API_connect-app-integrations_IframeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/IframeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/IframeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/IframeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
