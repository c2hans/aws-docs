---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnalyticsConfiguration.html
---

# AnalyticsConfiguration
<a name="API_AnalyticsConfiguration"></a>

Specifies the configuration and any analyses for the analytics filter of an Amazon S3 bucket.

## Contents
<a name="API_AnalyticsConfiguration_Contents"></a>

 ** Id **   <a name="AmazonS3-Type-AnalyticsConfiguration-Id"></a>
The ID that identifies the analytics configuration.
Type: String
Required: Yes

 ** StorageClassAnalysis **   <a name="AmazonS3-Type-AnalyticsConfiguration-StorageClassAnalysis"></a>
 Contains data related to access patterns to be collected and made available to analyze the tradeoffs between different storage classes.
Type: [StorageClassAnalysis](API_StorageClassAnalysis.md) data type
Required: Yes

 ** Filter **   <a name="AmazonS3-Type-AnalyticsConfiguration-Filter"></a>
The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.
Type: [AnalyticsFilter](API_AnalyticsFilter.md) data type
Required: No

## See Also
<a name="API_AnalyticsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AnalyticsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AnalyticsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AnalyticsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
