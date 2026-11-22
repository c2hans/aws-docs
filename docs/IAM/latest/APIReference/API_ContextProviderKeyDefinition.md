---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ContextProviderKeyDefinition.html
---

# ContextProviderKeyDefinition

Defines a single mapping from a source key in the external identity provider's assertion or token to a target trusted context key.

This data type is used as a member of the [ContextProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ContextProvider.html) data type.

## Contents
<a name="API_ContextProviderKeyDefinition_Contents"></a>

 ** SourceKey **
The key in the external identity provider's assertion or token to read the value from.
The key can contain only ASCII letters (A-Z, a-z), numbers (0-9), single spaces, and the following characters: `_ . : / = + - @ #`. It can't start or end with a space or contain two spaces in a row.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** TargetKey **
The trusted context key to map the source value into.
The key can contain only ASCII letters (A-Z, a-z), numbers (0-9), single spaces, and the following characters: `_ . : / = + - @ #`. It can't start or end with a space or contain two spaces in a row.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ContextProviderKeyDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ContextProviderKeyDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ContextProviderKeyDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ContextProviderKeyDefinition)
