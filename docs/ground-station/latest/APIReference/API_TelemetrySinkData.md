---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TelemetrySinkData.html
---

# TelemetrySinkData
<a name="API_TelemetrySinkData"></a>

Information about a telemetry sink.

## Contents
<a name="API_TelemetrySinkData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** kinesisDataStreamData **   <a name="groundstation-Type-TelemetrySinkData-kinesisDataStreamData"></a>
Information about a telemetry sink of type `KINESIS_DATA_STREAM`.
Type: [KinesisDataStreamData](API_KinesisDataStreamData.md) object
Required: No

## See Also
<a name="API_TelemetrySinkData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/TelemetrySinkData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/TelemetrySinkData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/TelemetrySinkData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
