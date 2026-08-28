---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AuthenticationMetadata.html
---

# AuthenticationMetadata
<a name="API_AuthenticationMetadata"></a>

Union type containing authentication metadata for different authentication methods.

## Contents
<a name="API_AuthenticationMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ApiKeyConnectionMetadata **   <a name="QS-Type-AuthenticationMetadata-ApiKeyConnectionMetadata"></a>
API key authentication metadata.
Type: [APIKeyConnectionMetadata](API_APIKeyConnectionMetadata.md) object
Required: No

 ** AuthorizationCodeGrantMetadata **   <a name="QS-Type-AuthenticationMetadata-AuthorizationCodeGrantMetadata"></a>
OAuth 2.0 authorization code grant authentication metadata.
Type: [AuthorizationCodeGrantMetadata](API_AuthorizationCodeGrantMetadata.md) object
Required: No

 ** BasicAuthConnectionMetadata **   <a name="QS-Type-AuthenticationMetadata-BasicAuthConnectionMetadata"></a>
Basic authentication metadata using username and password.
Type: [BasicAuthConnectionMetadata](API_BasicAuthConnectionMetadata.md) object
Required: No

 ** ClientCredentialsGrantMetadata **   <a name="QS-Type-AuthenticationMetadata-ClientCredentialsGrantMetadata"></a>
OAuth 2.0 client credentials grant authentication metadata.
Type: [ClientCredentialsGrantMetadata](API_ClientCredentialsGrantMetadata.md) object
Required: No

 ** IamConnectionMetadata **   <a name="QS-Type-AuthenticationMetadata-IamConnectionMetadata"></a>
IAM role-based authentication metadata for AWS services.
Type: [IAMConnectionMetadata](API_IAMConnectionMetadata.md) object
Required: No

 ** NoneConnectionMetadata **   <a name="QS-Type-AuthenticationMetadata-NoneConnectionMetadata"></a>
No authentication metadata for services that don't require authentication.
Type: [NoneConnectionMetadata](API_NoneConnectionMetadata.md) object
Required: No

## See Also
<a name="API_AuthenticationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AuthenticationMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AuthenticationMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AuthenticationMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
