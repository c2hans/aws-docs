---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_LocationConfiguration.html
---

# LocationConfiguration
<a name="API_LocationConfiguration"></a>

Configuration settings that define a stream group's stream capacity for a location. When configuring a location for the first time, you must specify a numeric value for at least one of the two capacity types. To update the capacity for an existing stream group, call [UpdateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html). To add a new location and specify its capacity, call [AddStreamGroupLocations](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AddStreamGroupLocations.html).

When you modify capacity for an existing location, always specify `AlwaysOnCapacity`, `MaximumCapacity`, and `TargetIdleCapacity` in the same request. If you omit one or more of these values, the service applies internal defaults for the missing values. These defaults might not match what you intend.

## Contents
<a name="API_LocationConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LocationName **   <a name="gameliftstreams-Type-LocationConfiguration-LocationName"></a>
 A location's name. For example, `us-east-1`. For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** AlwaysOnCapacity **   <a name="gameliftstreams-Type-LocationConfiguration-AlwaysOnCapacity"></a>
This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MaximumCapacity **   <a name="gameliftstreams-Type-LocationConfiguration-MaximumCapacity"></a>
This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** OnDemandCapacity **   <a name="gameliftstreams-Type-LocationConfiguration-OnDemandCapacity"></a>
This field is deprecated. Use `MaximumCapacity` instead. This parameter cannot be used with `MaximumCapacity` or `TargetIdleCapacity` in the same location configuration.
The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated. This offers a cost control measure at the expense of a greater startup time (typically under 5 minutes). Default is 0 when creating a stream group or adding a location.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TargetIdleCapacity **   <a name="gameliftstreams-Type-LocationConfiguration-TargetIdleCapacity"></a>
This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** VpcTransitConfiguration **   <a name="gameliftstreams-Type-LocationConfiguration-VpcTransitConfiguration"></a>
Configuration for connecting the stream group to resources in your Amazon VPC using AWS Transit Gateway. This setting is optional. If specified, Amazon GameLift Streams creates a Transit Gateway to enable private network connectivity between the service VPC and your VPC. The VPC ID cannot be changed after the stream group is created, but you can update the CIDR blocks by calling [UpdateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html).
Type: [VpcTransitConfiguration](API_VpcTransitConfiguration.md) object
Required: No

## See Also
<a name="API_LocationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/LocationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/LocationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/LocationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
