---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ExecuteCommandSessionConfiguration.html
---

# ExecuteCommandSessionConfiguration
<a name="API_ExecuteCommandSessionConfiguration"></a>

Information about the commands that will be run on a Dev Environment when an SSH session begins.

## Contents
<a name="API_ExecuteCommandSessionConfiguration_Contents"></a>

 ** command **   <a name="codecatalyst-Type-ExecuteCommandSessionConfiguration-command"></a>
The command used at the beginning of the SSH session to a Dev Environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** arguments **   <a name="codecatalyst-Type-ExecuteCommandSessionConfiguration-arguments"></a>
An array of arguments containing arguments and members.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_ExecuteCommandSessionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/ExecuteCommandSessionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/ExecuteCommandSessionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/ExecuteCommandSessionConfiguration)
