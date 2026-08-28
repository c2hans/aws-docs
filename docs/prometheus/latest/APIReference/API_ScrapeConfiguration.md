---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ScrapeConfiguration.html
---

# ScrapeConfiguration
<a name="API_ScrapeConfiguration"></a>

A scrape configuration for a scraper, base 64 encoded. For more information, see [Scraper configuration](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration) in the *Amazon Managed Service for Prometheus User Guide*.

## Contents
<a name="API_ScrapeConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** configurationBlob **   <a name="prometheus-Type-ScrapeConfiguration-configurationBlob"></a>
The base 64 encoded scrape configuration file.
Type: Base64-encoded binary data object
Required: No

## See Also
<a name="API_ScrapeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/ScrapeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/ScrapeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/ScrapeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
