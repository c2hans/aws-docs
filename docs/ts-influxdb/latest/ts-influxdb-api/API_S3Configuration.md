---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_S3Configuration.html
---

# S3Configuration
<a name="API_S3Configuration"></a>

Configuration for S3 bucket log delivery.

## Contents
<a name="API_S3Configuration_Contents"></a>

 ** bucketName **   <a name="tsinfluxdb-Type-S3Configuration-bucketName"></a>
The name of the S3 bucket to deliver logs to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+`
Required: Yes

 ** enabled **   <a name="tsinfluxdb-Type-S3Configuration-enabled"></a>
Indicates whether log delivery to the S3 bucket is enabled.
Type: Boolean
Required: Yes

## See Also
<a name="API_S3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/S3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/S3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/S3Configuration)
