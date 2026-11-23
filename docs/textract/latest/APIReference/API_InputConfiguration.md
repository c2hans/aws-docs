---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_InputConfiguration.html
---

# InputConfiguration

The Amazon S3 location of the input document for a document insights job.

## Contents
<a name="API_InputConfiguration_Contents"></a>

 ** S3Uri **   <a name="Textract-Type-InputConfiguration-S3Uri"></a>
The Amazon S3 URI of the input document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
Required: Yes

## See Also
<a name="API_InputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/InputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/InputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/InputConfiguration)
