---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BrowserExtensionConfiguration.html
---

# BrowserExtensionConfiguration
<a name="API_BrowserExtensionConfiguration"></a>

The container for browser extension configuration for an Amazon Q Business web experience.

## Contents
<a name="API_BrowserExtensionConfiguration_Contents"></a>

 ** enabledBrowserExtensions **   <a name="qbusiness-Type-BrowserExtensionConfiguration-enabledBrowserExtensions"></a>
Specify the browser extensions allowed for your Amazon Q web experience.
+  `CHROME` — Enables the extension for Chromium-based browsers (Google Chrome, Microsoft Edge, Opera, etc.).
+  `FIREFOX` — Enables the extension for Mozilla Firefox.
+  `CHROME` and `FIREFOX` — Enable the extension for Chromium-based browsers and Mozilla Firefox.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `FIREFOX | CHROME`
Required: Yes

## See Also
<a name="API_BrowserExtensionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/BrowserExtensionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/BrowserExtensionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/BrowserExtensionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
