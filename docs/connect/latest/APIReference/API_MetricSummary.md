---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MetricSummary.html
---

# MetricSummary
<a name="API_MetricSummary"></a>

Contains summary information about a metric.

## Contents
<a name="API_MetricSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-MetricSummary-Arn"></a>
The Amazon Resource Name (ARN) of the metric.
Type: String
Required: Yes

 ** Id **   <a name="connect-Type-MetricSummary-Id"></a>
The identifier of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: Yes

 ** Name **   <a name="connect-Type-MetricSummary-Name"></a>
The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Status **   <a name="connect-Type-MetricSummary-Status"></a>
The publish status of the metric.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: Yes

 ** Type **   <a name="connect-Type-MetricSummary-Type"></a>
The type of the metric.
Type: String
Valid Values: `AWS_MANAGED | CUSTOMER_MANAGED`
Required: Yes

 ** LastModifiedRegion **   <a name="connect-Type-MetricSummary-LastModifiedRegion"></a>
The region where the metric was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-MetricSummary-LastModifiedTime"></a>
The timestamp of when the metric was last modified.
Type: Timestamp
Required: No

## See Also
<a name="API_MetricSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MetricSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MetricSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MetricSummary)
