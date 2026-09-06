---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedQueryS3OutputConfiguration.html
---

# ProtectedQueryS3OutputConfiguration
<a name="API_ProtectedQueryS3OutputConfiguration"></a>

Contains the configuration to write the query results to S3.

## Contents
<a name="API_ProtectedQueryS3OutputConfiguration_Contents"></a>

 ** bucket **   <a name="API-Type-ProtectedQueryS3OutputConfiguration-bucket"></a>
The S3 bucket to unload the protected query results.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `.*(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$).*`
Required: Yes

 ** resultFormat **   <a name="API-Type-ProtectedQueryS3OutputConfiguration-resultFormat"></a>
Intended file format of the result.
Type: String
Valid Values: `CSV | PARQUET`
Required: Yes

 ** keyPrefix **   <a name="API-Type-ProtectedQueryS3OutputConfiguration-keyPrefix"></a>
The S3 prefix to unload the protected query results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[\w!.=*/-]*`
Required: No

 ** singleFileOutput **   <a name="API-Type-ProtectedQueryS3OutputConfiguration-singleFileOutput"></a>
Indicates whether files should be output as a single file (`TRUE`) or output as multiple files (`FALSE`). This parameter is only supported for analyses with the Spark analytics engine.
Type: Boolean
Required: No

## See Also
<a name="API_ProtectedQueryS3OutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedQueryS3OutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedQueryS3OutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedQueryS3OutputConfiguration)
