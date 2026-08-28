---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CapacityReservationSpecification.html
---

# CapacityReservationSpecification
<a name="API_CapacityReservationSpecification"></a>

The Capacity Reservation targeting option for the instances.

## Contents
<a name="API_CapacityReservationSpecification_Contents"></a>

 ** capacityReservationPreference **   <a name="bedrockagentcorecontrol-Type-CapacityReservationSpecification-capacityReservationPreference"></a>
The Capacity Reservation preference for the instances.
Type: String
Valid Values: `capacity-reservations-only | open | none`
Required: No

 ** capacityReservationTarget **   <a name="bedrockagentcorecontrol-Type-CapacityReservationSpecification-capacityReservationTarget"></a>
The target Capacity Reservation or Capacity Reservation group for the instances.
Type: [CapacityReservationTarget](API_CapacityReservationTarget.md) object
Required: No

## See Also
<a name="API_CapacityReservationSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CapacityReservationSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CapacityReservationSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CapacityReservationSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
