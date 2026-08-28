---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ComponentStatusData.html
---

# ComponentStatusData
<a name="API_ComponentStatusData"></a>

Data on the status of agent components.

## Contents
<a name="API_ComponentStatusData_Contents"></a>

 ** capabilityArn **   <a name="groundstation-Type-ComponentStatusData-capabilityArn"></a>
Capability ARN of the component.
Type: String
Required: Yes

 ** componentType **   <a name="groundstation-Type-ComponentStatusData-componentType"></a>
The Component type.
Type: String
Pattern: `[a-zA-Z0-9_]{1,64}`
Required: Yes

 ** dataflowId **   <a name="groundstation-Type-ComponentStatusData-dataflowId"></a>
Dataflow UUID associated with the component.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** status **   <a name="groundstation-Type-ComponentStatusData-status"></a>
Component status.
Type: String
Valid Values: `SUCCESS | FAILED | ACTIVE | INACTIVE`
Required: Yes

 ** bytesReceived **   <a name="groundstation-Type-ComponentStatusData-bytesReceived"></a>
Bytes received by the component.
Type: Long
Required: No

 ** bytesSent **   <a name="groundstation-Type-ComponentStatusData-bytesSent"></a>
Bytes sent by the component.
Type: Long
Required: No

 ** packetsDropped **   <a name="groundstation-Type-ComponentStatusData-packetsDropped"></a>
Packets dropped by component.
Type: Long
Required: No

## See Also
<a name="API_ComponentStatusData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ComponentStatusData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ComponentStatusData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ComponentStatusData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
