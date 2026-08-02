---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetricsConfiguration.html
---

# MetricsConfiguration
<a name="API_MetricsConfiguration"></a>

Specifies a metrics configuration for the CloudWatch request metrics (specified by the metrics configuration ID) from an Amazon S3 bucket. If you're updating an existing metrics configuration, note that this is a full replacement of the existing metrics configuration. If you don't include the elements you want to keep, they are erased. For more information, see [PutBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTMetricConfiguration.html).

## Contents
<a name="API_MetricsConfiguration_Contents"></a>

 ** Id **   <a name="AmazonS3-Type-MetricsConfiguration-Id"></a>
The ID used to identify the metrics configuration. The ID has a 64 character limit and can only contain letters, numbers, periods, dashes, and underscores.
Type: String
Required: Yes

 ** Filter **   <a name="AmazonS3-Type-MetricsConfiguration-Filter"></a>
Specifies a metrics configuration filter. The metrics configuration will only include objects that meet the filter's criteria. A filter must be a prefix, an object tag, an access point ARN, or a conjunction (MetricsAndOperator).
Metrics configurations for directory buckets do not support tag filters.
Type: [MetricsFilter](API_MetricsFilter.md) data type
Required: No

## See Also
<a name="API_MetricsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/MetricsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/MetricsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/MetricsConfiguration)
