---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_OAuthClientCredentials.html
---

# OAuthClientCredentials
<a name="API_OAuthClientCredentials"></a>

The OAuth 2.0 client credentials used for authenticating a data source connection. Use this structure to provide a client ID, client secret, and username directly instead of referencing a secret stored in Amazon Secrets Manager. This structure supports data sources that use two-legged OAuth (2LO) authentication, such as Snowflake.

## Contents
<a name="API_OAuthClientCredentials_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClientId **   <a name="QS-Type-OAuthClientCredentials-ClientId"></a>
The client ID of the OAuth 2.0 application that is registered with the data source provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\p{Cc}]+`
Required: No

 ** ClientSecret **   <a name="QS-Type-OAuthClientCredentials-ClientSecret"></a>
The client secret of the OAuth 2.0 application that is registered with the data source provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\p{Cc}]+`
Required: No

 ** Username **   <a name="QS-Type-OAuthClientCredentials-Username"></a>
The username of the account that is used for OAuth 2.0 client credentials authentication with the data source provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_OAuthClientCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/OAuthClientCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/OAuthClientCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/OAuthClientCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
