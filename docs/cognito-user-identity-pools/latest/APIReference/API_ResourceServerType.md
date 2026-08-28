---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ResourceServerType.html
---

# ResourceServerType
<a name="API_ResourceServerType"></a>

The details of a resource server configuration and associated custom scopes in a user pool.

This data type is a request parameter of [CreateResourceServer](API_CreateResourceServer.md) and a response parameter of [DescribeResourceServer](API_DescribeResourceServer.md).

## Contents
<a name="API_ResourceServerType_Contents"></a>

 ** Identifier **   <a name="CognitoUserPools-Type-ResourceServerType-Identifier"></a>
A unique resource server identifier for the resource server. The identifier can be an API friendly name like `solar-system-data`. You can also set an API URL like `https://solar-system-data-api.example.com` as your identifier.
Amazon Cognito represents scopes in the access token in the format `$resource-server-identifier/$scope`. Longer scope-identifier strings increase the size of your access tokens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
Required: No

 ** Name **   <a name="CognitoUserPools-Type-ResourceServerType-Name"></a>
The name of the resource server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\s+=,.@-]+`
Required: No

 ** Scopes **   <a name="CognitoUserPools-Type-ResourceServerType-Scopes"></a>
A list of scopes that are defined for the resource server.
Type: Array of [ResourceServerScopeType](API_ResourceServerScopeType.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** UserPoolId **   <a name="CognitoUserPools-Type-ResourceServerType-UserPoolId"></a>
The ID of the user pool that contains the resource server configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

## See Also
<a name="API_ResourceServerType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ResourceServerType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ResourceServerType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ResourceServerType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
