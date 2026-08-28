---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReadAuthorizationCodeGrantDetails.html
---

# ReadAuthorizationCodeGrantDetails
<a name="API_ReadAuthorizationCodeGrantDetails"></a>

Read-only configuration details for OAuth2 authorization code grant flow, including endpoints and client information.

## Contents
<a name="API_ReadAuthorizationCodeGrantDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AuthorizationEndpoint **   <a name="QS-Type-ReadAuthorizationCodeGrantDetails-AuthorizationEndpoint"></a>
The authorization server endpoint used to obtain authorization codes from the resource owner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** ClientId **   <a name="QS-Type-ReadAuthorizationCodeGrantDetails-ClientId"></a>
The client identifier for the OAuth2 authorization code grant flow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** TokenEndpoint **   <a name="QS-Type-ReadAuthorizationCodeGrantDetails-TokenEndpoint"></a>
The authorization server endpoint used to obtain access tokens via the authorization code grant flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

## See Also
<a name="API_ReadAuthorizationCodeGrantDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReadAuthorizationCodeGrantDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReadAuthorizationCodeGrantDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReadAuthorizationCodeGrantDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
