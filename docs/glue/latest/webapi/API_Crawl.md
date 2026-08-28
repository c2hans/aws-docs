---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Crawl.html
---

# Crawl
<a name="API_Crawl"></a>

The details of a crawl in the workflow.

## Contents
<a name="API_Crawl_Contents"></a>

 ** CompletedOn **   <a name="Glue-Type-Crawl-CompletedOn"></a>
The date and time on which the crawl completed.
Type: Timestamp
Required: No

 ** ErrorMessage **   <a name="Glue-Type-Crawl-ErrorMessage"></a>
The error message associated with the crawl.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LogGroup **   <a name="Glue-Type-Crawl-LogGroup"></a>
The log group associated with the crawl.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** LogStream **   <a name="Glue-Type-Crawl-LogStream"></a>
The log stream associated with the crawl.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** StartedOn **   <a name="Glue-Type-Crawl-StartedOn"></a>
The date and time on which the crawl started.
Type: Timestamp
Required: No

 ** State **   <a name="Glue-Type-Crawl-State"></a>
The state of the crawler.
Type: String
Valid Values: `RUNNING | CANCELLING | CANCELLED | SUCCEEDED | FAILED | ERROR`
Required: No

## See Also
<a name="API_Crawl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Crawl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Crawl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Crawl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
