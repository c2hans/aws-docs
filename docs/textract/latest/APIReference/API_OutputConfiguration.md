---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_OutputConfiguration.html
---

# OutputConfiguration

The Amazon S3 location where the results of a document insights job are written.

## Contents
<a name="API_OutputConfiguration_Contents"></a>

 ** S3Uri **   <a name="Textract-Type-OutputConfiguration-S3Uri"></a>
The Amazon S3 URI where the analysis results are written.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
Required: Yes

## See Also
<a name="API_OutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/OutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/OutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/OutputConfiguration)
