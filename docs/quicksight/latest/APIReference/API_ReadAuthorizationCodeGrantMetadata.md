---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReadAuthorizationCodeGrantMetadata.html
---

# ReadAuthorizationCodeGrantMetadata
<a name="API_ReadAuthorizationCodeGrantMetadata"></a>

Read-only metadata for OAuth2 authorization code grant authentication configuration.

## Contents
<a name="API_ReadAuthorizationCodeGrantMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BaseEndpoint **   <a name="QS-Type-ReadAuthorizationCodeGrantMetadata-BaseEndpoint"></a>
The base endpoint URL for the OAuth2 authorization code grant flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** RedirectUrl **   <a name="QS-Type-ReadAuthorizationCodeGrantMetadata-RedirectUrl"></a>
The redirect URL where the authorization server will send the user after authorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** AuthorizationCodeGrantCredentialsSource **   <a name="QS-Type-ReadAuthorizationCodeGrantMetadata-AuthorizationCodeGrantCredentialsSource"></a>
The source of credentials for the authorization code grant flow.
Type: String
Valid Values: `PLAIN_CREDENTIALS`
Required: No

 ** ReadAuthorizationCodeGrantCredentialsDetails **   <a name="QS-Type-ReadAuthorizationCodeGrantMetadata-ReadAuthorizationCodeGrantCredentialsDetails"></a>
The read-only credentials details for the authorization code grant flow.
Type: [ReadAuthorizationCodeGrantCredentialsDetails](API_ReadAuthorizationCodeGrantCredentialsDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ReadAuthorizationCodeGrantMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReadAuthorizationCodeGrantMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReadAuthorizationCodeGrantMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReadAuthorizationCodeGrantMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
