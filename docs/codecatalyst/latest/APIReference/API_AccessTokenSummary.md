---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_AccessTokenSummary.html
---

# AccessTokenSummary
<a name="API_AccessTokenSummary"></a>

Information about a specified personal access token (PAT).

## Contents
<a name="API_AccessTokenSummary_Contents"></a>

 ** id **   <a name="codecatalyst-Type-AccessTokenSummary-id"></a>
The system-generated ID of the personal access token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** name **   <a name="codecatalyst-Type-AccessTokenSummary-name"></a>
The friendly name of the personal access token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** expiresTime **   <a name="codecatalyst-Type-AccessTokenSummary-expiresTime"></a>
The date and time when the personal access token will expire, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp
Required: No

## See Also
<a name="API_AccessTokenSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/AccessTokenSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/AccessTokenSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/AccessTokenSummary)
