---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_InputFileConfig.html
---

# InputFileConfig
<a name="API_InputFileConfig"></a>

A list of parameters that specify the input channels, type of input data, and where it is located.

## Contents
<a name="API_InputFileConfig_Contents"></a>

 ** channelName **   <a name="braket-Type-InputFileConfig-channelName"></a>
A named input source that an Amazon Braket hybrid job can consume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\.\-_]+`
Required: Yes

 ** dataSource **   <a name="braket-Type-InputFileConfig-dataSource"></a>
The location of the input data.
Type: [DataSource](API_DataSource.md) object
Required: Yes

 ** contentType **   <a name="braket-Type-InputFileConfig-contentType"></a>
The MIME type of the data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_InputFileConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/InputFileConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/InputFileConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/InputFileConfig)
