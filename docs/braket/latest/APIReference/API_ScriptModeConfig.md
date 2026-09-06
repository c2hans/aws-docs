---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_ScriptModeConfig.html
---

# ScriptModeConfig
<a name="API_ScriptModeConfig"></a>

Contains information about algorithm scripts used for the Amazon Braket hybrid job.

## Contents
<a name="API_ScriptModeConfig_Contents"></a>

 ** entryPoint **   <a name="braket-Type-ScriptModeConfig-entryPoint"></a>
The entry point in the algorithm scripts from where the execution begins in the hybrid job.
Type: String
Required: Yes

 ** s3Uri **   <a name="braket-Type-ScriptModeConfig-s3Uri"></a>
The URI that specifies the S3 path to the algorithm scripts used by an Amazon Braket hybrid job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** compressionType **   <a name="braket-Type-ScriptModeConfig-compressionType"></a>
The type of compression used to store the algorithm scripts in Amazon S3 storage.
Type: String
Valid Values: `NONE | GZIP`
Required: No

## See Also
<a name="API_ScriptModeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/ScriptModeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/ScriptModeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/ScriptModeConfig)
