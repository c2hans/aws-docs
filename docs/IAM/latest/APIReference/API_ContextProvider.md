---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ContextProvider.html
---

# ContextProvider

Contains the trusted identity propagation context provider configuration for a SAML or OpenID Connect (OIDC) identity provider. The context provider defines how the subject is derived and how keys from the external identity provider's assertion or token are mapped into trusted context keys.

This data type is used as a request parameter in the [CreateOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html), [UpdateOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateOpenIDConnectProvider.html), [CreateSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateSAMLProvider.html), and [UpdateSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateSAMLProvider.html) operations, and as a response element in the [GetOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOpenIDConnectProvider.html) and [GetSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSAMLProvider.html) operations.

## Contents
<a name="API_ContextProvider_Contents"></a>

 ** SubjectSourceKey **
The source key that is used to derive the subject for the injected trusted context. This value identifies the claim or attribute in the external identity provider's assertion or token that supplies the subject.
The key can contain only ASCII letters (A-Z, a-z), numbers (0-9), single spaces, and the following characters: `_ . : / = + - @ #`. It can't start or end with a space or contain two spaces in a row.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** KeyDefinitionList.member.N **
A list of source-to-target key mappings that define how keys from the external identity provider's assertion or token are mapped into trusted context keys. You can specify from 0 to 10 mappings.
Type: Array of [ContextProviderKeyDefinition](API_ContextProviderKeyDefinition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** SubjectTypeSourceKey **
The source key that supplies the subject type from the external identity provider's assertion or token.
The key can contain only ASCII letters (A-Z, a-z), numbers (0-9), single spaces, and the following characters: `_ . : / = + - @ #`. It can't start or end with a space or contain two spaces in a row.
This parameter is mutually exclusive with `SubjectTypeValue`. Specify either `SubjectTypeSourceKey` or `SubjectTypeValue`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SubjectTypeValue **
A static value for the subject type, such as `user` or `workload`.
This parameter is optional and is mutually exclusive with `SubjectTypeSourceKey`. Specify either `SubjectTypeValue` or `SubjectTypeSourceKey`, but not both.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_ContextProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ContextProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ContextProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ContextProvider)
