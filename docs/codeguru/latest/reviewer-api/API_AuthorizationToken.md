---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_AuthorizationToken.html
---

# AuthorizationToken
<a name="API_AuthorizationToken"></a>

Contains authorization information for accessing third-party repositories.

## Contents
<a name="API_AuthorizationToken_Contents"></a>

 ** CreationTime **   <a name="reviewer-Type-AuthorizationToken-CreationTime"></a>
The time when the authorization token was created.
Type: Timestamp
Required: Yes

 ** Scopes **   <a name="reviewer-Type-AuthorizationToken-Scopes"></a>
The access scopes granted by the authorization token.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** Token **   <a name="reviewer-Type-AuthorizationToken-Token"></a>
The authorization token value.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 2048.
Pattern: `\S+`
Required: Yes

 ** User **   <a name="reviewer-Type-AuthorizationToken-User"></a>
The user associated with the authorization token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: Yes

## See Also
<a name="API_AuthorizationToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/AuthorizationToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/AuthorizationToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/AuthorizationToken)
