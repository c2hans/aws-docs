---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ClientCredentialsGrantDetails.html
---

# ClientCredentialsGrantDetails
<a name="API_ClientCredentialsGrantDetails"></a>

Configuration details for OAuth2 client credentials grant flow, including client ID, client secret, token endpoint, and optional scopes.

## Contents
<a name="API_ClientCredentialsGrantDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClientId **   <a name="QS-Type-ClientCredentialsGrantDetails-ClientId"></a>
The client identifier issued to the client during the registration process with the authorization server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** ClientSecret **   <a name="QS-Type-ClientCredentialsGrantDetails-ClientSecret"></a>
The client secret issued to the client during the registration process with the authorization server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: Yes

 ** TokenEndpoint **   <a name="QS-Type-ClientCredentialsGrantDetails-TokenEndpoint"></a>
The authorization server endpoint used to obtain access tokens via the client credentials grant flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

## See Also
<a name="API_ClientCredentialsGrantDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ClientCredentialsGrantDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ClientCredentialsGrantDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ClientCredentialsGrantDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
