---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_S3Config.html
---

# S3Config
<a name="API_S3Config"></a>

The configuration for publishing Internet Monitor internet measurements to Amazon S3. The configuration includes the bucket name and (optionally) prefix for the S3 bucket to store the measurements, and the delivery status. The delivery status is `ENABLED` or `DISABLED`, depending on whether you choose to deliver internet measurements to S3 logs.

## Contents
<a name="API_S3Config_Contents"></a>

 ** BucketName **   <a name="internetmonitor-Type-S3Config-BucketName"></a>
The Amazon S3 bucket name.
Type: String
Length Constraints: Minimum length of 3.
Required: No

 ** BucketPrefix **   <a name="internetmonitor-Type-S3Config-BucketPrefix"></a>
The Amazon S3 bucket prefix.
Type: String
Required: No

 ** LogDeliveryStatus **   <a name="internetmonitor-Type-S3Config-LogDeliveryStatus"></a>
The status of publishing Internet Monitor internet measurements to an Amazon S3 bucket.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_S3Config_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/S3Config)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/S3Config)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/S3Config)
