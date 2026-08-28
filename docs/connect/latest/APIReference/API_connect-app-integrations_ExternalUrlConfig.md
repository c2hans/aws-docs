---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_ExternalUrlConfig.html
---

# ExternalUrlConfig
<a name="API_connect-app-integrations_ExternalUrlConfig"></a>

The external URL source for the application.

## Contents
<a name="API_connect-app-integrations_ExternalUrlConfig_Contents"></a>

 ** AccessUrl **   <a name="connect-Type-connect-app-integrations_ExternalUrlConfig-AccessUrl"></a>
The URL to access the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^\w+\:\/\/.*$`
Required: Yes

 ** ApprovedOrigins **   <a name="connect-Type-connect-app-integrations_ExternalUrlConfig-ApprovedOrigins"></a>
Additional URLs to allow list if different than the access URL.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^\w+\:\/\/.*$`
Required: No

## See Also
<a name="API_connect-app-integrations_ExternalUrlConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/ExternalUrlConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/ExternalUrlConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/ExternalUrlConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
