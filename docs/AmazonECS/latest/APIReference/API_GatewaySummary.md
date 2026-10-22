---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewaySummary.html
---

# GatewaySummary
<a name="API_GatewaySummary"></a>

A summary of a gateway that is returned by the `ListGateways` operation.

## Contents
<a name="API_GatewaySummary_Contents"></a>

 ** createdAt **   <a name="ECS-Type-GatewaySummary-createdAt"></a>
The Unix timestamp for the time when the gateway was created.
Type: Timestamp
Required: No

 ** gatewayArn **   <a name="ECS-Type-GatewaySummary-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.
Type: String
Required: No

 ** name **   <a name="ECS-Type-GatewaySummary-name"></a>
The name of the gateway.
Type: String
Required: No

 ** status **   <a name="ECS-Type-GatewaySummary-status"></a>
The status of the gateway.
Type: String
Valid Values: `ACTIVE | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | DELETED`
Required: No

## See Also
<a name="API_GatewaySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewaySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewaySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewaySummary)
