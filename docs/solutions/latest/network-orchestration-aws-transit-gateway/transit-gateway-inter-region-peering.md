---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/transit-gateway-inter-region-peering.html
---

# Transit Gateway inter-Region peering
<a name="transit-gateway-inter-region-peering"></a>

You can use Transit Gateway peering to directly route traffic between two transit gateways in the same AWS Region or across Regions. This section provides information about how this Guidance supports peering.

 **Architecture diagram of AWS resources deployed to support Transit Gateway inter-Region peering.**

![inter region architecture](https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/images/inter-region-architecture.png)

1. When you [tag the transit gateway](tgw-peering-attachments.md#add-tags-to-transit-gateway), an EventBridge event initiates. The target for this event is the transit gateway peering attachment Lambda function in the hub account.

1. The `tgw-peering` Lambda function creates the peering attachment between the transit gateways based on the tag key and value. The peering attachment state transitions from `InitializingRequest` to `PendingAcceptance`.

1. The Lambda function accepts the peering attachment request in the remote Region.

1. The Lambda function sets the peering attachment state to `Available`.
