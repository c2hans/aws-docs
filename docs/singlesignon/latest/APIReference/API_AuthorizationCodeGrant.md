---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AuthorizationCodeGrant.html
---

# AuthorizationCodeGrant
<a name="API_AuthorizationCodeGrant"></a>

A structure that defines configuration settings for an application that supports the OAuth 2.0 Authorization Code Grant.

## Contents
<a name="API_AuthorizationCodeGrant_Contents"></a>

 ** RedirectUris **   <a name="singlesignon-Type-AuthorizationCodeGrant-RedirectUris"></a>
A list of URIs that are valid locations to redirect a user's browser after the user is authorized.
RedirectUris is required when the grant type is `authorization_code`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_AuthorizationCodeGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/AuthorizationCodeGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/AuthorizationCodeGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/AuthorizationCodeGrant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
