---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AuthorizationCodeGrantMetadata.html
---

# AuthorizationCodeGrantMetadata
<a name="API_AuthorizationCodeGrantMetadata"></a>

Metadata for OAuth 2.0 authorization code grant authentication.

## Contents
<a name="API_AuthorizationCodeGrantMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BaseEndpoint **   <a name="QS-Type-AuthorizationCodeGrantMetadata-BaseEndpoint"></a>
The base URL endpoint for the external service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** RedirectUrl **   <a name="QS-Type-AuthorizationCodeGrantMetadata-RedirectUrl"></a>
The redirect URL for the OAuth authorization flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** AuthorizationCodeGrantCredentialsDetails **   <a name="QS-Type-AuthorizationCodeGrantMetadata-AuthorizationCodeGrantCredentialsDetails"></a>
The detailed credentials configuration for authorization code grant.
Type: [AuthorizationCodeGrantCredentialsDetails](API_AuthorizationCodeGrantCredentialsDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** AuthorizationCodeGrantCredentialsSource **   <a name="QS-Type-AuthorizationCodeGrantMetadata-AuthorizationCodeGrantCredentialsSource"></a>
The source of the authorization code grant credentials.
Type: String
Valid Values: `PLAIN_CREDENTIALS`
Required: No

## See Also
<a name="API_AuthorizationCodeGrantMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AuthorizationCodeGrantMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AuthorizationCodeGrantMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AuthorizationCodeGrantMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
