---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_PrincipalSearchResult.html
---

# PrincipalSearchResult
<a name="API_PrincipalSearchResult"></a>

A user or group matched by SearchPrincipals.

## Contents
<a name="API_PrincipalSearchResult_Contents"></a>

 ** displayName **   <a name="cloudwatchomni-Type-PrincipalSearchResult-displayName"></a>
The display name of the principal.
Type: String
Required: Yes

 ** principalId **   <a name="cloudwatchomni-Type-PrincipalSearchResult-principalId"></a>
The unique ID of the principal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9:/_+=,.@-]*`
Required: Yes

 ** principalType **   <a name="cloudwatchomni-Type-PrincipalSearchResult-principalType"></a>
Whether the principal is a user or a group.
Type: String
Valid Values: `USER | GROUP`
Required: Yes

 ** description **   <a name="cloudwatchomni-Type-PrincipalSearchResult-description"></a>
An optional description of the principal.
Type: String
Required: No

 ** userName **   <a name="cloudwatchomni-Type-PrincipalSearchResult-userName"></a>
The user name of the principal. Present for users only.
Type: String
Required: No

## See Also
<a name="API_PrincipalSearchResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/PrincipalSearchResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/PrincipalSearchResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/PrincipalSearchResult)
