---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_AssetFileContent.html
---

# AssetFileContent
<a name="API_AssetFileContent"></a>

A single file with path and content

## Contents
<a name="API_AssetFileContent_Contents"></a>

 ** body **   <a name="devopsagent-Type-AssetFileContent-body"></a>
The file content
Type: [AssetFileBody](API_AssetFileBody.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** path **   <a name="devopsagent-Type-AssetFileContent-path"></a>
The path of the file within the asset
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9_./ ()-]+`
Required: Yes

 ** metadata **   <a name="devopsagent-Type-AssetFileContent-metadata"></a>
Optional metadata for this file
Type: JSON value
Required: No

## See Also
<a name="API_AssetFileContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/AssetFileContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/AssetFileContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/AssetFileContent)
