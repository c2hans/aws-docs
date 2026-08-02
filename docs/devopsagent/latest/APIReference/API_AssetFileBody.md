---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_AssetFileBody.html
---

# AssetFileBody
<a name="API_AssetFileBody"></a>

Content of an individual asset file

## Contents
<a name="API_AssetFileBody_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** bytes **   <a name="devopsagent-Type-AssetFileBody-bytes"></a>
Binary file content
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 6291456.
Required: No

 ** text **   <a name="devopsagent-Type-AssetFileBody-text"></a>
Text file content
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1572864.
Required: No

## See Also
<a name="API_AssetFileBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/AssetFileBody)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/AssetFileBody)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/AssetFileBody)
