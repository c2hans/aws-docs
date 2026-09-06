---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_InternetMeasurementsLogDelivery.html
---

# InternetMeasurementsLogDelivery
<a name="API_InternetMeasurementsLogDelivery"></a>

Publish internet measurements to an Amazon S3 bucket in addition to CloudWatch Logs.

## Contents
<a name="API_InternetMeasurementsLogDelivery_Contents"></a>

 ** S3Config **   <a name="internetmonitor-Type-InternetMeasurementsLogDelivery-S3Config"></a>
The configuration information for publishing Internet Monitor internet measurements to Amazon S3. The configuration includes the bucket name and (optionally) prefix for the S3 bucket to store the measurements, and the delivery status. The delivery status is `ENABLED` or `DISABLED`, depending on whether you choose to deliver internet measurements to S3 logs.
Type: [S3Config](API_S3Config.md) object
Required: No

## See Also
<a name="API_InternetMeasurementsLogDelivery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/InternetMeasurementsLogDelivery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/InternetMeasurementsLogDelivery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/InternetMeasurementsLogDelivery)
