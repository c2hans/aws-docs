---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_InputDataConfig.html
---

# InputDataConfig
<a name="API_InputDataConfig"></a>

The input properties for an entities detection job. This includes the name of the S3 bucket and the path to the files to be analyzed.

## Contents
<a name="API_InputDataConfig_Contents"></a>

 ** S3Bucket **   <a name="comprehendmedical-Type-InputDataConfig-S3Bucket"></a>
The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[0-9a-z\.\-_]*(?!\.)$`
Required: Yes

 ** S3Key **   <a name="comprehendmedical-Type-InputDataConfig-S3Key"></a>
The path to the input data files in the S3 bucket.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_InputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/InputDataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/InputDataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/InputDataConfig)
