---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WindowsConfiguration.html
---

# WindowsConfiguration
<a name="API_WindowsConfiguration"></a>

Windows-specific configuration settings for an ISO import, including the edition to install from a multi-edition Windows ISO file.

## Contents
<a name="API_WindowsConfiguration_Contents"></a>

 ** imageIndex **   <a name="imagebuilder-Type-WindowsConfiguration-imageIndex"></a>
The 1-based index that specifies which Windows edition to install from a multi-edition Windows ISO file. A Windows ISO can contain a `.wim` file with multiple image indexes, each representing a different edition.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 4294967295.
Required: Yes

## See Also
<a name="API_WindowsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/WindowsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/WindowsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/WindowsConfiguration)
