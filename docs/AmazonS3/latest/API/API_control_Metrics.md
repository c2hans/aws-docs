---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Metrics.html
---

# Metrics
<a name="API_control_Metrics"></a>

A container that specifies replication metrics-related settings.

## Contents
<a name="API_control_Metrics_Contents"></a>

 ** Status **   <a name="AmazonS3-Type-control_Metrics-Status"></a>
Specifies whether replication metrics are enabled.
Type: String
Valid Values: `Enabled | Disabled`
Required: Yes

 ** EventThreshold **   <a name="AmazonS3-Type-control_Metrics-EventThreshold"></a>
A container that specifies the time threshold for emitting the `s3:Replication:OperationMissedThreshold` event.
This is not supported by Amazon S3 on Outposts buckets.
Type: [ReplicationTimeValue](API_control_ReplicationTimeValue.md) data type
Required: No

## See Also
<a name="API_control_Metrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Metrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Metrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Metrics)
