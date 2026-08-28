---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RecrawlPolicy.html
---

# RecrawlPolicy
<a name="API_RecrawlPolicy"></a>

When crawling an Amazon S3 data source after the first crawl is complete, specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run. For more information, see [Incremental Crawls in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/incremental-crawls.html) in the developer guide.

## Contents
<a name="API_RecrawlPolicy_Contents"></a>

 ** RecrawlBehavior **   <a name="Glue-Type-RecrawlPolicy-RecrawlBehavior"></a>
Specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run.
A value of `CRAWL_EVERYTHING` specifies crawling the entire dataset again.
A value of `CRAWL_NEW_FOLDERS_ONLY` specifies crawling only folders that were added since the last crawler run.
A value of `CRAWL_EVENT_MODE` specifies crawling only the changes identified by Amazon S3 events.
Type: String
Valid Values: `CRAWL_EVERYTHING | CRAWL_NEW_FOLDERS_ONLY | CRAWL_EVENT_MODE`
Required: No

## See Also
<a name="API_RecrawlPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RecrawlPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RecrawlPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RecrawlPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
