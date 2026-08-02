---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CrawlsFilter.html
---

# CrawlsFilter
<a name="API_CrawlsFilter"></a>

A list of fields, comparators and value that you can use to filter the crawler runs for a specified crawler.

## Contents
<a name="API_CrawlsFilter_Contents"></a>

 ** FieldName **   <a name="Glue-Type-CrawlsFilter-FieldName"></a>
A key used to filter the crawler runs for a specified crawler. Valid values for each of the field names are:
+  `CRAWL_ID`: A string representing the UUID identifier for a crawl.
+  `STATE`: A string representing the state of the crawl.
+  `START_TIME` and `END_TIME`: The epoch timestamp in milliseconds.
+  `DPU_HOUR`: The number of data processing unit (DPU) hours used for the crawl.
Type: String
Valid Values: `CRAWL_ID | STATE | START_TIME | END_TIME | DPU_HOUR`
Required: No

 ** FieldValue **   <a name="Glue-Type-CrawlsFilter-FieldValue"></a>
The value provided for comparison on the crawl field.
Type: String
Required: No

 ** FilterOperator **   <a name="Glue-Type-CrawlsFilter-FilterOperator"></a>
A defined comparator that operates on the value. The available operators are:
+  `GT`: Greater than.
+  `GE`: Greater than or equal to.
+  `LT`: Less than.
+  `LE`: Less than or equal to.
+  `EQ`: Equal to.
+  `NE`: Not equal to.
Type: String
Valid Values: `GT | GE | LT | LE | EQ | NE`
Required: No

## See Also
<a name="API_CrawlsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CrawlsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CrawlsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CrawlsFilter)
