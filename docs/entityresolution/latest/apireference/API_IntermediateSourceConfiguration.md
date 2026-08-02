---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IntermediateSourceConfiguration.html
---

# IntermediateSourceConfiguration
<a name="API_IntermediateSourceConfiguration"></a>

The Amazon S3 location that temporarily stores your data while it processes. Your information won't be saved permanently.

## Contents
<a name="API_IntermediateSourceConfiguration_Contents"></a>

 ** intermediateS3Path **   <a name="API-Type-IntermediateSourceConfiguration-intermediateS3Path"></a>
The Amazon S3 location (bucket and prefix). For example: `s3://provider_bucket/DOC-EXAMPLE-BUCKET`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

## See Also
<a name="API_IntermediateSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/IntermediateSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/IntermediateSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/IntermediateSourceConfiguration)
