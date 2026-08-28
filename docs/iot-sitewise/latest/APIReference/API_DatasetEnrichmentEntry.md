---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DatasetEnrichmentEntry.html
---

# DatasetEnrichmentEntry
<a name="API_DatasetEnrichmentEntry"></a>

Contains enrichment status information for a specific data type in a dataset.

## Contents
<a name="API_DatasetEnrichmentEntry_Contents"></a>

 ** status **   <a name="iotsitewise-Type-DatasetEnrichmentEntry-status"></a>
The enrichment status of the data type in the dataset.
Type: String
Valid Values: `FULLY_ENRICHED | PARTIALLY_ENRICHED | NOT_ENRICHED`
Required: Yes

 ** lastEnrichedAt **   <a name="iotsitewise-Type-DatasetEnrichmentEntry-lastEnrichedAt"></a>
The date the data was last enriched, in Unix epoch time.
Type: Timestamp
Required: No

## See Also
<a name="API_DatasetEnrichmentEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DatasetEnrichmentEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DatasetEnrichmentEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DatasetEnrichmentEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
