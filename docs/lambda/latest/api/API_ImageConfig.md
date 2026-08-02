---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ImageConfig.html
---

# ImageConfig
<a name="API_ImageConfig"></a>

Configuration values that override the container image Dockerfile settings. For more information, see [Container image settings](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms).

## Contents
<a name="API_ImageConfig_Contents"></a>

 ** Command **   <a name="lambda-Type-ImageConfig-Command"></a>
Specifies parameters that you want to pass in with ENTRYPOINT.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1500 items.
Required: No

 ** EntryPoint **   <a name="lambda-Type-ImageConfig-EntryPoint"></a>
Specifies the entry point to their application, which is typically the location of the runtime executable.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1500 items.
Required: No

 ** WorkingDirectory **   <a name="lambda-Type-ImageConfig-WorkingDirectory"></a>
Specifies the working directory.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_ImageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ImageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ImageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ImageConfig)
