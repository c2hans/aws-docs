---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_FileConfiguration.html
---

# FileConfiguration
<a name="API_connect-app-integrations_FileConfiguration"></a>

The configuration for what files should be pulled from the source.

## Contents
<a name="API_connect-app-integrations_FileConfiguration_Contents"></a>

 ** Folders **   <a name="connect-Type-connect-app-integrations_FileConfiguration-Folders"></a>
Identifiers for the source folders to pull all files from recursively.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.*\S.*`
Required: Yes

 ** Filters **   <a name="connect-Type-connect-app-integrations_FileConfiguration-Filters"></a>
Restrictions for what files should be pulled from the source.
Type: String to array of strings map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.*\S.*`
Array Members: Minimum number of 1 item. Maximum number of 2048 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: No

## See Also
<a name="API_connect-app-integrations_FileConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/FileConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/FileConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/FileConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
