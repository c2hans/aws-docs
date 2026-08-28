---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_LocationState.html
---

# LocationState
<a name="API_LocationState"></a>

Represents a location and its corresponding stream capacity and status.

## Contents
<a name="API_LocationState_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllocatedCapacity **   <a name="gameliftstreams-Type-LocationState-AllocatedCapacity"></a>
This value is the stream capacity that Amazon GameLift Streams has provisioned in a stream group that can respond immediately to stream requests. It includes resources that are currently streaming and resources that are idle and ready to respond to stream requests. When target-idle capacity is configured, the idle resources include the capacity buffer maintained beyond ongoing sessions. You pay for this capacity whether it's in use or not. After making changes to capacity, it can take a few minutes for the allocated capacity count to reflect the change while compute resources are allocated or deallocated. Similarly, when allocated on-demand capacity is no longer needed, it can take a few minutes for Amazon GameLift Streams to spin down the allocated capacity.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** AlwaysOnCapacity **   <a name="gameliftstreams-Type-LocationState-AlwaysOnCapacity"></a>
This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** IdleCapacity **   <a name="gameliftstreams-Type-LocationState-IdleCapacity"></a>
This value is the amount of allocated capacity that is not currently streaming. It represents the stream group's ability to respond immediately to new stream requests with near-instant startup time.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** InternalVpcIpv4CidrBlock **   <a name="gameliftstreams-Type-LocationState-InternalVpcIpv4CidrBlock"></a>
The CIDR block of the service VPC for this location. Add this CIDR block to your VPC route table to enable traffic routing through the Transit Gateway.
Type: String
Pattern: `(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])/([0-9]|[1-2][0-9]|3[0-2])`
Required: No

 ** LocationName **   <a name="gameliftstreams-Type-LocationState-LocationName"></a>
 A location's name. For example, `us-east-1`. For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** MaximumCapacity **   <a name="gameliftstreams-Type-LocationState-MaximumCapacity"></a>
This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** OnDemandCapacity **   <a name="gameliftstreams-Type-LocationState-OnDemandCapacity"></a>
The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated. This offers a cost control measure at the expense of a greater startup time (typically under 5 minutes). Default is 0 when creating a stream group or adding a location.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** RequestedCapacity **   <a name="gameliftstreams-Type-LocationState-RequestedCapacity"></a>
This value is the always-on capacity that you most recently requested for a stream group. You request capacity separately for each location in a stream group. In response to an increase in requested capacity, Amazon GameLift Streams attempts to provision compute resources to make the stream group's allocated capacity meet requested capacity. When always-on capacity is decreased, it can take a few minutes to deprovision allocated capacity to match the requested capacity.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Status **   <a name="gameliftstreams-Type-LocationState-Status"></a>
This value is set of locations, including their name, current status, and capacities.
A location can be in one of the following states:
+  `ACTIVATING`: Amazon GameLift Streams is preparing the location. You cannot stream from, scale the capacity of, or remove this location yet.
+  `ACTIVE`: The location is provisioned with initial capacity. You can now stream from, scale the capacity of, or remove this location.
+  `ERROR`: Amazon GameLift Streams failed to set up this location. The `StatusReason` field describes the error. You can remove this location and try to add it again.
+  `REMOVING`: Amazon GameLift Streams is working to remove this location. This will release all provisioned capacity for this location in this stream group.
Type: String
Valid Values: `ACTIVATING | ACTIVE | ERROR | REMOVING`
Required: No

 ** TargetIdleCapacity **   <a name="gameliftstreams-Type-LocationState-TargetIdleCapacity"></a>
This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** VpcTransitConfiguration **   <a name="gameliftstreams-Type-LocationState-VpcTransitConfiguration"></a>
The VPC transit configuration for this location, including the Transit Gateway details needed to complete the VPC attachment setup.
Type: [VpcTransitConfigurationResponse](API_VpcTransitConfigurationResponse.md) object
Required: No

## See Also
<a name="API_LocationState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/LocationState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/LocationState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/LocationState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
