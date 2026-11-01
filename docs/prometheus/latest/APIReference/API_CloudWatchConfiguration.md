---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CloudWatchConfiguration.html
---

# CloudWatchConfiguration
<a name="API_CloudWatchConfiguration"></a>

The configuration identifies the CloudWatch dataset used as a scraper destination.

## Contents
<a name="API_CloudWatchConfiguration_Contents"></a>

 ** datasetArn **   <a name="prometheus-Type-CloudWatchConfiguration-datasetArn"></a>
The Amazon Resource Name (ARN) of the CloudWatch dataset. To use the default dataset, specify `arn:aws:cloudwatch:<region>:<account-id>:dataset/default`.
Type: String
Pattern: `arn:aws[-a-z]*:cloudwatch:[-a-z0-9]+:[0-9]{12}:dataset\/.+`
Required: Yes

## See Also
<a name="API_CloudWatchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/CloudWatchConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/CloudWatchConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/CloudWatchConfiguration)
