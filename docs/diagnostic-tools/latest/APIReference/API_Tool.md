---
source_url: https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Tool.html
---

# Tool
<a name="API_Tool"></a>

Information about a Diagnostic Tool.

## Contents
<a name="API_Tool_Contents"></a>

 ** id **   <a name="diagnostictools-Type-Tool-id"></a>
Unique Identifier for Diagnostic Tool .
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `\w+`
Required: Yes

 ** latestVersionId **   <a name="diagnostictools-Type-Tool-latestVersionId"></a>
Field specifying the latest available version of the artifact associated with the Diagnostic Tool.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 17.
Pattern: `[0-9]{1,5}.[0-9]{1,5}.[0-9]{1,5}`
Required: Yes

 ** name **   <a name="diagnostictools-Type-Tool-name"></a>
Describes the Diagnostic Tool Name.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 256.
Pattern: `[\ \w]+`
Required: Yes

 ** versions **   <a name="diagnostictools-Type-Tool-versions"></a>
Array of versions object associated with the Tool.
Type: Array of [ToolVersion](API_ToolVersion.md) objects
Required: Yes

## See Also
<a name="API_Tool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/troubleshooting-2023-01-01/Tool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/troubleshooting-2023-01-01/Tool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/troubleshooting-2023-01-01/Tool)
