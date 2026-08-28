---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReadAuthenticationMetadata.html
---

# ReadAuthenticationMetadata
<a name="API_ReadAuthenticationMetadata"></a>

Read-only authentication metadata union containing non-sensitive configuration details for different authentication types.

## Contents
<a name="API_ReadAuthenticationMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ApiKeyConnectionMetadata **   <a name="QS-Type-ReadAuthenticationMetadata-ApiKeyConnectionMetadata"></a>
Read-only metadata for API key authentication configuration.
Type: [ReadAPIKeyConnectionMetadata](API_ReadAPIKeyConnectionMetadata.md) object
Required: No

 ** AuthorizationCodeGrantMetadata **   <a name="QS-Type-ReadAuthenticationMetadata-AuthorizationCodeGrantMetadata"></a>
Read-only metadata for OAuth2 authorization code grant flow configuration.
Type: [ReadAuthorizationCodeGrantMetadata](API_ReadAuthorizationCodeGrantMetadata.md) object
Required: No

 ** BasicAuthConnectionMetadata **   <a name="QS-Type-ReadAuthenticationMetadata-BasicAuthConnectionMetadata"></a>
Read-only metadata for basic authentication configuration.
Type: [ReadBasicAuthConnectionMetadata](API_ReadBasicAuthConnectionMetadata.md) object
Required: No

 ** ClientCredentialsGrantMetadata **   <a name="QS-Type-ReadAuthenticationMetadata-ClientCredentialsGrantMetadata"></a>
Read-only metadata for OAuth2 client credentials grant flow configuration.
Type: [ReadClientCredentialsGrantMetadata](API_ReadClientCredentialsGrantMetadata.md) object
Required: No

 ** IamConnectionMetadata **   <a name="QS-Type-ReadAuthenticationMetadata-IamConnectionMetadata"></a>
Read-only metadata for IAM-based authentication configuration.
Type: [ReadIamConnectionMetadata](API_ReadIamConnectionMetadata.md) object
Required: No

 ** NoneConnectionMetadata **   <a name="QS-Type-ReadAuthenticationMetadata-NoneConnectionMetadata"></a>
Read-only metadata for connections that do not require authentication.
Type: [ReadNoneConnectionMetadata](API_ReadNoneConnectionMetadata.md) object
Required: No

## See Also
<a name="API_ReadAuthenticationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReadAuthenticationMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReadAuthenticationMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReadAuthenticationMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
