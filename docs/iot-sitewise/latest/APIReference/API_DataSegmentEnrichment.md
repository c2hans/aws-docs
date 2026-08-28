---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DataSegmentEnrichment.html
---

# DataSegmentEnrichment
<a name="API_DataSegmentEnrichment"></a>

Contains enrichment status information for a data segment.

## Contents
<a name="API_DataSegmentEnrichment_Contents"></a>

 ** status **   <a name="iotsitewise-Type-DataSegmentEnrichment-status"></a>
The enrichment status of the data segment.
Type: String
Valid Values: `ENRICHED | NOT_ENRICHED`
Required: Yes

 ** lastEnrichedAt **   <a name="iotsitewise-Type-DataSegmentEnrichment-lastEnrichedAt"></a>
The date the data segment was last enriched, in Unix epoch time.
Type: Timestamp
Required: No

## See Also
<a name="API_DataSegmentEnrichment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DataSegmentEnrichment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DataSegmentEnrichment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DataSegmentEnrichment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
