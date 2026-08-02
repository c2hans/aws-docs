---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_TransformationInputDataConfig.html
---

# TransformationInputDataConfig
<a name="API_TransformationInputDataConfig"></a>

The Amazon S3 location and source format configuration for input data in a transformation job.

## Contents
<a name="API_TransformationInputDataConfig_Contents"></a>

 ** S3Uri **   <a name="HealthLake-Type-TransformationInputDataConfig-S3Uri"></a>
The Amazon S3 URI of the input data to transform.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 2048.
Pattern: `s3://[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9](/.+)?`
Required: Yes

 ** SourceFormat **   <a name="HealthLake-Type-TransformationInputDataConfig-SourceFormat"></a>
The format of the source data files (C-CDA or CSV).
Type: String
Valid Values: `CCDA | CSV`
Required: No

## See Also
<a name="API_TransformationInputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/TransformationInputDataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/TransformationInputDataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/TransformationInputDataConfig)
