---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GlueOAuth2Credentials.html
---

# GlueOAuth2Credentials
<a name="API_GlueOAuth2Credentials"></a>

The GlueOAuth2 credentials of a connection.

## Contents
<a name="API_GlueOAuth2Credentials_Contents"></a>

 ** accessToken **   <a name="datazone-Type-GlueOAuth2Credentials-accessToken"></a>
The access token of a connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `[\x20-\x7E]*`
Required: No

 ** jwtToken **   <a name="datazone-Type-GlueOAuth2Credentials-jwtToken"></a>
The jwt token of the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8000.
Pattern: `([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_\-\+\/=]*)`
Required: No

 ** refreshToken **   <a name="datazone-Type-GlueOAuth2Credentials-refreshToken"></a>
The refresh token of the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `[\x20-\x7E]*`
Required: No

 ** userManagedClientApplicationClientSecret **   <a name="datazone-Type-GlueOAuth2Credentials-userManagedClientApplicationClientSecret"></a>
The user managed client application client secret of the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[\x20-\x7E]*`
Required: No

## See Also
<a name="API_GlueOAuth2Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GlueOAuth2Credentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GlueOAuth2Credentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GlueOAuth2Credentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
