---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CustomAuthCredentials.html
---

# CustomAuthCredentials
<a name="API_CustomAuthCredentials"></a>

The custom credentials required for custom authentication.

## Contents
<a name="API_CustomAuthCredentials_Contents"></a>

 ** customAuthenticationType **   <a name="appflow-Type-CustomAuthCredentials-customAuthenticationType"></a>
The custom authentication type that the connector uses.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** credentialsMap **   <a name="appflow-Type-CustomAuthCredentials-credentialsMap"></a>
A map that holds custom authentication credentials.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w]+`
Value Length Constraints: Maximum length of 2048.
Value Pattern: `\S+`
Required: No

## See Also
<a name="API_CustomAuthCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/CustomAuthCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/CustomAuthCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/CustomAuthCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
