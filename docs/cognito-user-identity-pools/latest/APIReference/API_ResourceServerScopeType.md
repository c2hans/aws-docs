---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ResourceServerScopeType.html
---

# ResourceServerScopeType
<a name="API_ResourceServerScopeType"></a>

One custom scope associated with a user pool resource server. This data type is a member of `ResourceServerScopeType`. For more information, see [ Scopes, M2M, and API authorization with resource servers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html).

This data type is a request parameter of [CreateResourceServer](API_CreateResourceServer.md) and a response parameter of [DescribeResourceServer](API_DescribeResourceServer.md).

## Contents
<a name="API_ResourceServerScopeType_Contents"></a>

 ** ScopeDescription **   <a name="CognitoUserPools-Type-ResourceServerScopeType-ScopeDescription"></a>
A friendly description of a custom scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ScopeName **   <a name="CognitoUserPools-Type-ResourceServerScopeType-ScopeName"></a>
The name of the scope. Amazon Cognito renders custom scopes in the format `resourceServerIdentifier/ScopeName`. For example, if this parameter is `exampleScope` in the resource server with the identifier `exampleResourceServer`, you request and receive the scope `exampleResourceServer/exampleScope`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x21\x23-\x2E\x30-\x5B\x5D-\x7E]+`
Required: Yes

## See Also
<a name="API_ResourceServerScopeType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ResourceServerScopeType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ResourceServerScopeType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ResourceServerScopeType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
