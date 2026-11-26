---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_JobSubmitPlugin.html
---

# JobSubmitPlugin

A job submit plugin configuration, including its name, runtime language, and script source.

## Contents
<a name="API_JobSubmitPlugin_Contents"></a>

 ** name **   <a name="PCS-Type-JobSubmitPlugin-name"></a>
A unique name for the plugin. The name can be up to 64 characters long. Valid characters are letters, numbers, underscores (`_`), and hyphens (`-`). The first character must be a letter or a number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9_-]*`
Required: Yes

 ** scriptSource **   <a name="PCS-Type-JobSubmitPlugin-scriptSource"></a>
The source location and integrity information for the script.
Type: [JobSubmitScriptSource](API_JobSubmitScriptSource.md) object
Required: Yes

 ** type **   <a name="PCS-Type-JobSubmitPlugin-type"></a>
The runtime language used to execute the custom script. Valid values:
+  `STARLARK` – The script uses Starlark syntax.
Type: String
Valid Values: `STARLARK`
Required: Yes

## See Also
<a name="API_JobSubmitPlugin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/JobSubmitPlugin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/JobSubmitPlugin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/JobSubmitPlugin)
