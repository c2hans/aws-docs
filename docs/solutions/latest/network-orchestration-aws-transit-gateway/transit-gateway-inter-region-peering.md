---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/transit-gateway-inter-region-peering.html
---

# Transit Gateway inter-Region peering
<a name="transit-gateway-inter-region-peering"></a>

You can use Transit Gateway peering to directly route traffic between two transit gateways in the same AWS Region or across Regions. This section provides information about how this solution supports peering.

 **Architecture diagram of AWS resources deployed to support Transit Gateway inter-Region peering.**

![inter region architecture](http://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/images/inter-region-architecture.png)

1. When you [tag the transit gateway](tgw-peering-attachments.md#add-tags-to-transit-gateway), an EventBridge event initiates. The target for this event is the transit gateway peering attachment Lambda function in the hub account.

1. The `tgw-peering` Lambda function creates the peering attachment between the transit gateways based on the tag key and value. The peering attachment state transitions from `InitializingRequest` to `PendingAcceptance`.

1. The Lambda function accepts the peering attachment request in the remote Region.

1. The solution sets the peering attachment state to `Available`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Network Orchestration for AWS Transit Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
