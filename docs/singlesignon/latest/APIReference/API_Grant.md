---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_Grant.html
---

# Grant
<a name="API_Grant"></a>

The Grant union represents the set of possible configuration options for the selected grant type. Exactly one member of the union must be specified, and must match the grant type selected.

## Contents
<a name="API_Grant_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AuthorizationCode **   <a name="singlesignon-Type-Grant-AuthorizationCode"></a>
Configuration options for the `authorization_code` grant type.
Type: [AuthorizationCodeGrant](API_AuthorizationCodeGrant.md) object
Required: No

 ** JwtBearer **   <a name="singlesignon-Type-Grant-JwtBearer"></a>
Configuration options for the `urn:ietf:params:oauth:grant-type:jwt-bearer` grant type.
Type: [JwtBearerGrant](API_JwtBearerGrant.md) object
Required: No

 ** RefreshToken **   <a name="singlesignon-Type-Grant-RefreshToken"></a>
Configuration options for the `refresh_token` grant type.
Type: [RefreshTokenGrant](API_RefreshTokenGrant.md) object
Required: No

 ** TokenExchange **   <a name="singlesignon-Type-Grant-TokenExchange"></a>
Configuration options for the `urn:ietf:params:oauth:grant-type:token-exchange` grant type.
Type: [TokenExchangeGrant](API_TokenExchangeGrant.md) object
Required: No

## See Also
<a name="API_Grant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/Grant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/Grant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/Grant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
