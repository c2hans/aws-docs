---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CrawlerHistory.html
---

# CrawlerHistory
<a name="API_CrawlerHistory"></a>

Contains the information for a run of a crawler.

## Contents
<a name="API_CrawlerHistory_Contents"></a>

 ** CrawlId **   <a name="Glue-Type-CrawlerHistory-CrawlId"></a>
A UUID identifier for each crawl.
Type: String
Required: No

 ** DPUHour **   <a name="Glue-Type-CrawlerHistory-DPUHour"></a>
The number of data processing units (DPU) used in hours for the crawl.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** EndTime **   <a name="Glue-Type-CrawlerHistory-EndTime"></a>
The date and time on which the crawl ended.
Type: Timestamp
Required: No

 ** ErrorMessage **   <a name="Glue-Type-CrawlerHistory-ErrorMessage"></a>
If an error occurred, the error message associated with the crawl.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LogGroup **   <a name="Glue-Type-CrawlerHistory-LogGroup"></a>
The log group associated with the crawl.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** LogStream **   <a name="Glue-Type-CrawlerHistory-LogStream"></a>
The log stream associated with the crawl.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** MessagePrefix **   <a name="Glue-Type-CrawlerHistory-MessagePrefix"></a>
The prefix for a CloudWatch message about this crawl.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StartTime **   <a name="Glue-Type-CrawlerHistory-StartTime"></a>
The date and time on which the crawl started.
Type: Timestamp
Required: No

 ** State **   <a name="Glue-Type-CrawlerHistory-State"></a>
The state of the crawl.
Type: String
Valid Values: `RUNNING | COMPLETED | FAILED | STOPPED`
Required: No

 ** Summary **   <a name="Glue-Type-CrawlerHistory-Summary"></a>
A run summary for the specific crawl in JSON. Contains the catalog tables and partitions that were added, updated, or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_CrawlerHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CrawlerHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CrawlerHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CrawlerHistory)
