---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AuthorizationCodeGrantDetails.html
---

# AuthorizationCodeGrantDetails
<a name="API_AuthorizationCodeGrantDetails"></a>

Configuration details for OAuth 2.0 authorization code grant flow.

## Contents
<a name="API_AuthorizationCodeGrantDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AuthorizationEndpoint **   <a name="QS-Type-AuthorizationCodeGrantDetails-AuthorizationEndpoint"></a>
The authorization endpoint URL for the OAuth flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** ClientId **   <a name="QS-Type-AuthorizationCodeGrantDetails-ClientId"></a>
The client ID for the OAuth application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** ClientSecret **   <a name="QS-Type-AuthorizationCodeGrantDetails-ClientSecret"></a>
The client secret for the OAuth application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: Yes

 ** TokenEndpoint **   <a name="QS-Type-AuthorizationCodeGrantDetails-TokenEndpoint"></a>
The token endpoint URL for obtaining access tokens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

## See Also
<a name="API_AuthorizationCodeGrantDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AuthorizationCodeGrantDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AuthorizationCodeGrantDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AuthorizationCodeGrantDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
