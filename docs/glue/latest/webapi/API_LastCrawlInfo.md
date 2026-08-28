---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_LastCrawlInfo.html
---

# LastCrawlInfo
<a name="API_LastCrawlInfo"></a>

Status and error information about the most recent crawl.

## Contents
<a name="API_LastCrawlInfo_Contents"></a>

 ** ErrorMessage **   <a name="Glue-Type-LastCrawlInfo-ErrorMessage"></a>
If an error occurred, the error information about the last crawl.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LogGroup **   <a name="Glue-Type-LastCrawlInfo-LogGroup"></a>
The log group for the last crawl.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** LogStream **   <a name="Glue-Type-LastCrawlInfo-LogStream"></a>
The log stream for the last crawl.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** MessagePrefix **   <a name="Glue-Type-LastCrawlInfo-MessagePrefix"></a>
The prefix for a message about this crawl.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StartTime **   <a name="Glue-Type-LastCrawlInfo-StartTime"></a>
The time at which the crawl started.
Type: Timestamp
Required: No

 ** Status **   <a name="Glue-Type-LastCrawlInfo-Status"></a>
Status of the last crawl.
Type: String
Valid Values: `SUCCEEDED | CANCELLED | FAILED`
Required: No

## See Also
<a name="API_LastCrawlInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/LastCrawlInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/LastCrawlInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/LastCrawlInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
