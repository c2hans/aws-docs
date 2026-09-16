---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_S3DeliveryConfiguration.html
---

# S3DeliveryConfiguration
<a name="API_S3DeliveryConfiguration"></a>

This structure contains delivery configurations that apply only when the delivery destination resource is an S3 bucket.

## Contents
<a name="API_S3DeliveryConfiguration_Contents"></a>

 ** enableHiveCompatiblePath **   <a name="CWL-Type-S3DeliveryConfiguration-enableHiveCompatiblePath"></a>
This parameter causes the S3 objects that contain delivered logs to use a prefix structure that allows for integration with Apache Hive.
Type: Boolean
Required: No

 ** suffixPath **   <a name="CWL-Type-S3DeliveryConfiguration-suffixPath"></a>
This string allows re-configuring the S3 object prefix to contain either static or variable sections. The valid variables to use in the suffix path vary by log type. To find the values supported for the suffix path for each log type, use the [DescribeConfigurationTemplates](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.html) operation and check the `allowedSuffixPathFields` field in the response. For more information about how the destination prefix, suffix path, and Hive-compatible setting determine the Amazon S3 object key, see [Amazon S3 object key for V2 deliveries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.html#AWS-logs-infrastructure-V2-S3-object-key).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_S3DeliveryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/S3DeliveryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/S3DeliveryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/S3DeliveryConfiguration)
