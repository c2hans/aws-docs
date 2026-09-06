---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_SampleDataSource.html
---

# SampleDataSource
<a name="API_SampleDataSource"></a>

Identifies a sample data file in Amazon S3 to use as the source when creating a data transformation profile. Valid only when the source format is Comma-separated values (CSV).

## Contents
<a name="API_SampleDataSource_Contents"></a>

 ** S3Uri **   <a name="HealthLake-Type-SampleDataSource-S3Uri"></a>
The Amazon S3 URI of the sample data file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9](/.*)?`
Required: Yes

## See Also
<a name="API_SampleDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/SampleDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/SampleDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/SampleDataSource)
