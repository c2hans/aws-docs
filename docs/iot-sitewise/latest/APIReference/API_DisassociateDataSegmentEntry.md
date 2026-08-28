---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DisassociateDataSegmentEntry.html
---

# DisassociateDataSegmentEntry
<a name="API_DisassociateDataSegmentEntry"></a>

Contains information about a data segment entry to disassociate from a dataset.

## Contents
<a name="API_DisassociateDataSegmentEntry_Contents"></a>

 ** endTimestamp **   <a name="iotsitewise-Type-DisassociateDataSegmentEntry-endTimestamp"></a>
The nanosecond-precision end time of the data segment to disassociate.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** sourceDatasetId **   <a name="iotsitewise-Type-DisassociateDataSegmentEntry-sourceDatasetId"></a>
The ID of the source dataset that contains the data segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** startTimestamp **   <a name="iotsitewise-Type-DisassociateDataSegmentEntry-startTimestamp"></a>
The nanosecond-precision start time of the data segment to disassociate.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** timeSeriesId **   <a name="iotsitewise-Type-DisassociateDataSegmentEntry-timeSeriesId"></a>
The ID of the time series.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 73.
Required: Yes

## See Also
<a name="API_DisassociateDataSegmentEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DisassociateDataSegmentEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DisassociateDataSegmentEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DisassociateDataSegmentEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
