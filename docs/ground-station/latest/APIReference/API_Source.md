---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_Source.html
---

# Source
<a name="API_Source"></a>

Dataflow details for the source side.

## Contents
<a name="API_Source_Contents"></a>

 ** configDetails **   <a name="groundstation-Type-Source-configDetails"></a>
Additional details for a `Config`, if type is `dataflow-endpoint` or `antenna-downlink-demod-decode`
Type: [ConfigDetails](API_ConfigDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** configId **   <a name="groundstation-Type-Source-configId"></a>
UUID of a `Config`.
Type: String
Required: No

 ** configType **   <a name="groundstation-Type-Source-configType"></a>
Type of a `Config`.
Type: String
Valid Values: `antenna-downlink | antenna-downlink-demod-decode | tracking | dataflow-endpoint | antenna-uplink | uplink-echo | s3-recording | telemetry-sink`
Required: No

 ** dataflowSourceRegion **   <a name="groundstation-Type-Source-dataflowSourceRegion"></a>
Region of a dataflow source.
Type: String
Required: No

## See Also
<a name="API_Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/Source)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/Source)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/Source)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
