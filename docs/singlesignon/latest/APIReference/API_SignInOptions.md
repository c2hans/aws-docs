---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_SignInOptions.html
---

# SignInOptions
<a name="API_SignInOptions"></a>

A structure that describes the sign-in options for an application portal.

## Contents
<a name="API_SignInOptions_Contents"></a>

 ** Origin **   <a name="singlesignon-Type-SignInOptions-Origin"></a>
This determines how IAM Identity Center navigates the user to the target application. It can be one of the following values:
+  `APPLICATION`: IAM Identity Center redirects the customer to the configured `ApplicationUrl`.
+  `IDENTITY_CENTER`: IAM Identity Center uses SAML identity-provider initiated authentication to sign the customer directly into a SAML-based application.
Type: String
Valid Values: `IDENTITY_CENTER | APPLICATION`
Required: Yes

 ** ApplicationUrl **   <a name="singlesignon-Type-SignInOptions-ApplicationUrl"></a>
The URL that accepts authentication requests for an application. This is a required parameter if the `Origin` parameter is `APPLICATION`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `http(s)?:\/\/[-a-zA-Z0-9+&@#\/%?=~_|!:,.;]*[-a-zA-Z0-9+&bb@#\/%?=~_|]`
Required: No

## See Also
<a name="API_SignInOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/SignInOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/SignInOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/SignInOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
