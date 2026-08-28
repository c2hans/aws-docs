---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Crawler.html
---

# Crawler
<a name="API_Crawler"></a>

Specifies a crawler program that examines a data source and uses classifiers to try to determine its schema. If successful, the crawler records metadata concerning the data source in the AWS Glue Data Catalog.

## Contents
<a name="API_Crawler_Contents"></a>

 ** Classifiers **   <a name="Glue-Type-Crawler-Classifiers"></a>
A list of UTF-8 strings that specify the custom classifiers that are associated with the crawler.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Configuration **   <a name="Glue-Type-Crawler-Configuration"></a>
Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior. For more information, see [Setting crawler configuration options](https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html).
Type: String
Required: No

 ** CrawlElapsedTime **   <a name="Glue-Type-Crawler-CrawlElapsedTime"></a>
If the crawler is running, contains the total time elapsed since the last crawl began.
Type: Long
Required: No

 ** CrawlerSecurityConfiguration **   <a name="Glue-Type-Crawler-CrawlerSecurityConfiguration"></a>
The name of the `SecurityConfiguration` structure to be used by this crawler.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** CreationTime **   <a name="Glue-Type-Crawler-CreationTime"></a>
The time that the crawler was created.
Type: Timestamp
Required: No

 ** DatabaseName **   <a name="Glue-Type-Crawler-DatabaseName"></a>
The name of the database in which the crawler's output is stored.
Type: String
Required: No

 ** Description **   <a name="Glue-Type-Crawler-Description"></a>
A description of the crawler.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LakeFormationConfiguration **   <a name="Glue-Type-Crawler-LakeFormationConfiguration"></a>
Specifies whether the crawler should use AWS Lake Formation credentials for the crawler instead of the IAM role credentials.
Type: [LakeFormationConfiguration](API_LakeFormationConfiguration.md) object
Required: No

 ** LastCrawl **   <a name="Glue-Type-Crawler-LastCrawl"></a>
The status of the last crawl, and potentially error information if an error occurred.
Type: [LastCrawlInfo](API_LastCrawlInfo.md) object
Required: No

 ** LastUpdated **   <a name="Glue-Type-Crawler-LastUpdated"></a>
The time that the crawler was last updated.
Type: Timestamp
Required: No

 ** LineageConfiguration **   <a name="Glue-Type-Crawler-LineageConfiguration"></a>
A configuration that specifies whether data lineage is enabled for the crawler.
Type: [LineageConfiguration](API_LineageConfiguration.md) object
Required: No

 ** Name **   <a name="Glue-Type-Crawler-Name"></a>
The name of the crawler.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RecrawlPolicy **   <a name="Glue-Type-Crawler-RecrawlPolicy"></a>
A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.
Type: [RecrawlPolicy](API_RecrawlPolicy.md) object
Required: No

 ** Role **   <a name="Glue-Type-Crawler-Role"></a>
The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.
Type: String
Required: No

 ** Schedule **   <a name="Glue-Type-Crawler-Schedule"></a>
For scheduled crawlers, the schedule when the crawler runs.
Type: [Schedule](API_Schedule.md) object
Required: No

 ** SchemaChangePolicy **   <a name="Glue-Type-Crawler-SchemaChangePolicy"></a>
The policy that specifies update and delete behaviors for the crawler.
Type: [SchemaChangePolicy](API_SchemaChangePolicy.md) object
Required: No

 ** State **   <a name="Glue-Type-Crawler-State"></a>
Indicates whether the crawler is running, or whether a run is pending.
Type: String
Valid Values: `READY | RUNNING | STOPPING`
Required: No

 ** TablePrefix **   <a name="Glue-Type-Crawler-TablePrefix"></a>
The prefix added to the names of tables that are created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** Targets **   <a name="Glue-Type-Crawler-Targets"></a>
A collection of targets to crawl.
Type: [CrawlerTargets](API_CrawlerTargets.md) object
Required: No

 ** Version **   <a name="Glue-Type-Crawler-Version"></a>
The version of the crawler.
Type: Long
Required: No

## See Also
<a name="API_Crawler_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Crawler)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Crawler)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Crawler)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
