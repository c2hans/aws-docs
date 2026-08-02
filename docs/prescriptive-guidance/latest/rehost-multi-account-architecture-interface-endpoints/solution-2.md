---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-multi-account-architecture-interface-endpoints/solution-2.html
---

# Solution 2: Creating VPC endpoints in a central networking account for multiple Regions
<a name="solution-2"></a>

## Use case
<a name="use-case.5f3a939d-4975-583f-90b7-4d533e690ac5"></a>

You want to migrate your applications or servers to different AWS target accounts in multiple AWS Regions, to keep them close to your users or to enable business continuity in disaster recovery scenarios. This is an extension of the [first use case](solution-1.md)*.*

## Challenge
<a name="challenge.ea6a8e03-bd94-5c80-abaa-a832ca6eb712"></a>

To achieve this over a private network, you would have to create multiple VPC interface endpoints in every target account. This gets even more complex in a multi-Region scenario and adds to administrative overhead and costs for maintaining multiple endpoints. (See [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/).)

## Solution
<a name="solution.03073ea0-050f-560f-b66c-d61ce9e192bc"></a>

Create VPC endpoints for each Region in a central networking account and enable cross-account access by using a peered transit gateway and Route 53.

## Architecture
<a name="architecture.a6e1d276-ed76-5602-89e2-e4629caa33d5"></a>

The following diagram illustrates the architecture for this solution.

![Traffic flow for rehosting multiple accounts in multiple Regions.](http://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-multi-account-architecture-interface-endpoints/images/guide-img/7711a996-1484-4997-8795-d06bd903a940/images/d66e80b7-111a-44ad-b96e-652f72537a21.png)

The traffic flow is the same as in [solution 1](solution-1.md), except that the accounts in the two Regions are connected by transit gateway peering.

## Implementation steps
<a name="implementation-steps.9913581b-1524-5a40-aac2-416633d3e66a"></a>

1. In the central networking account, create a VPC interface endpoint for each target AWS Region.

1. In the central networking account, create a private hosted zone for each endpoint in each Region, and associate the zone with the target application VPCs in the same Region.

1. In the central networking account, create a transit gateway for each target Region, and share the gateway with target accounts in same Region by using AWS RAM.

1. Connect transit gateways across Regions by using transit gateway peering, and update the transit gateway route tables as required.

1. In the central networking account, create resolver rules for each target Region, and share these rules with target accounts in the same Region by using AWS RAM.
