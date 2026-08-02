---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CustomPattern.html
---

# CustomPattern
<a name="API_CustomPattern"></a>

The pattern configuration for redacting custom data types in session.

## Contents
<a name="API_CustomPattern_Contents"></a>

 ** patternName **   <a name="workspacesweb-Type-CustomPattern-patternName"></a>
The pattern name for the custom pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[_\-\d\w]+`
Required: Yes

 ** patternRegex **   <a name="workspacesweb-Type-CustomPattern-patternRegex"></a>
The pattern regex for the customer pattern. The format must follow JavaScript regex format. The pattern must be enclosed between slashes, and can have flags behind the second slash. For example: “/ab\+c/gi”.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `\/((?:[^\n])+)\/([gimsuyvd]{0,8})`
Required: Yes

 ** keywordRegex **   <a name="workspacesweb-Type-CustomPattern-keywordRegex"></a>
The keyword regex for the customer pattern. After there is a match to the pattern regex, the keyword regex is used to search within the proximity of the match. If there is a keyword match, then the match is confirmed. If no keyword regex is provided, the pattern regex match will automatically be confirmed. The format must follow JavaScript regex format. The pattern must be enclosed between slashes, and can have flags behind the second slash. For example, “/ab\+c/gi”
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `\/((?:[^\n])+)\/([gimsuyvd]{0,8})`
Required: No

 ** patternDescription **   <a name="workspacesweb-Type-CustomPattern-patternDescription"></a>
The pattern description for the customer pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ _\-\d\w]+`
Required: No

## See Also
<a name="API_CustomPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/CustomPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/CustomPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/CustomPattern)
