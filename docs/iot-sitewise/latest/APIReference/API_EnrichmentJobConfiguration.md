---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_EnrichmentJobConfiguration.html
---

# EnrichmentJobConfiguration
<a name="API_EnrichmentJobConfiguration"></a>

Configuration for the enrichment job defining which analysis type to perform on video time-series data. Currently supports event detection enrichment. Exactly one member must be specified.

## Contents
<a name="API_EnrichmentJobConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** eventDetection **   <a name="iotsitewise-Type-EnrichmentJobConfiguration-eventDetection"></a>
Event detection configuration that generates embeddings from video time-series data enabling natural language similarity search on events. The service processes video data and creates embeddings stored in IoT SiteWise for semantic querying.
Type: [EventDetection](API_EventDetection.md) object
Required: No

## See Also
<a name="API_EnrichmentJobConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/EnrichmentJobConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/EnrichmentJobConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/EnrichmentJobConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
