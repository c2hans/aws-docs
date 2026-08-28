---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_Destination.html
---

# Destination
<a name="API_Destination"></a>

Dataflow details for the destination side.

## Contents
<a name="API_Destination_Contents"></a>

 ** configDetails **   <a name="groundstation-Type-Destination-configDetails"></a>
Additional details for a `Config`, if type is dataflow endpoint or antenna demod decode.
Type: [ConfigDetails](API_ConfigDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** configId **   <a name="groundstation-Type-Destination-configId"></a>
UUID of a `Config`.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** configType **   <a name="groundstation-Type-Destination-configType"></a>
Type of a `Config`.
Type: String
Valid Values: `antenna-downlink | antenna-downlink-demod-decode | tracking | dataflow-endpoint | antenna-uplink | uplink-echo | s3-recording | telemetry-sink`
Required: No

 ** dataflowDestinationRegion **   <a name="groundstation-Type-Destination-dataflowDestinationRegion"></a>
Region of a dataflow destination.
Type: String
Required: No

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/Destination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
