---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CrawlerMetrics.html
---

# CrawlerMetrics
<a name="API_CrawlerMetrics"></a>

Metrics for a specified crawler.

## Contents
<a name="API_CrawlerMetrics_Contents"></a>

 ** CrawlerName **   <a name="Glue-Type-CrawlerMetrics-CrawlerName"></a>
The name of the crawler.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** LastRuntimeSeconds **   <a name="Glue-Type-CrawlerMetrics-LastRuntimeSeconds"></a>
The duration of the crawler's most recent run, in seconds.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** MedianRuntimeSeconds **   <a name="Glue-Type-CrawlerMetrics-MedianRuntimeSeconds"></a>
The median duration of this crawler's runs, in seconds.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** StillEstimating **   <a name="Glue-Type-CrawlerMetrics-StillEstimating"></a>
True if the crawler is still estimating how long it will take to complete this run.
Type: Boolean
Required: No

 ** TablesCreated **   <a name="Glue-Type-CrawlerMetrics-TablesCreated"></a>
The number of tables created by this crawler.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TablesDeleted **   <a name="Glue-Type-CrawlerMetrics-TablesDeleted"></a>
The number of tables deleted by this crawler.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TablesUpdated **   <a name="Glue-Type-CrawlerMetrics-TablesUpdated"></a>
The number of tables updated by this crawler.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TimeLeftSeconds **   <a name="Glue-Type-CrawlerMetrics-TimeLeftSeconds"></a>
The estimated time left to complete a running crawl.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

## See Also
<a name="API_CrawlerMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CrawlerMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CrawlerMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CrawlerMetrics)
