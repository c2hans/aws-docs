---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListedRouterOutput.html
---

# ListedRouterOutput
<a name="API_ListedRouterOutput"></a>

A summary of a router output, including its name, type, ARN, ID, state, routed state, and other key details. This structure is used in the response of the ListRouterOutputs operation.

## Contents
<a name="API_ListedRouterOutput_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-ListedRouterOutput-arn"></a>
The Amazon Resource Name (ARN) of the router output.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerOutput:[a-z0-9]{12}`
Required: Yes

 ** availabilityZone **   <a name="mediaconnect-Type-ListedRouterOutput-availabilityZone"></a>
The Availability Zone of the router output.
Type: String
Required: Yes

 ** createdAt **   <a name="mediaconnect-Type-ListedRouterOutput-createdAt"></a>
The timestamp when the router output was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="mediaconnect-Type-ListedRouterOutput-id"></a>
The unique identifier of the router output.
Type: String
Required: Yes

 ** maximumBitrate **   <a name="mediaconnect-Type-ListedRouterOutput-maximumBitrate"></a>
The maximum bitrate of the router output.
Type: Long
Required: Yes

 ** messageCount **   <a name="mediaconnect-Type-ListedRouterOutput-messageCount"></a>
The number of messages associated with the router output.
Type: Integer
Required: Yes

 ** name **   <a name="mediaconnect-Type-ListedRouterOutput-name"></a>
The name of the router output.
Type: String
Required: Yes

 ** outputType **   <a name="mediaconnect-Type-ListedRouterOutput-outputType"></a>
The type of the router output.
Type: String
Valid Values: `STANDARD | MEDIACONNECT_FLOW | MEDIALIVE_INPUT`
Required: Yes

 ** regionName **   <a name="mediaconnect-Type-ListedRouterOutput-regionName"></a>
The AAWS Region where the router output is located.
Type: String
Required: Yes

 ** routedState **   <a name="mediaconnect-Type-ListedRouterOutput-routedState"></a>
The current state of the association between the router output and its input.
Type: String
Valid Values: `ROUTED | ROUTING | UNROUTED`
Required: Yes

 ** routingScope **   <a name="mediaconnect-Type-ListedRouterOutput-routingScope"></a>
Indicates whether the router output is configured for Regional or global routing.
Type: String
Valid Values: `REGIONAL | GLOBAL`
Required: Yes

 ** state **   <a name="mediaconnect-Type-ListedRouterOutput-state"></a>
The overall state of the router output.
Type: String
Valid Values: `CREATING | STANDBY | STARTING | ACTIVE | STOPPING | DELETING | UPDATING | ERROR | RECOVERING | MIGRATING`
Required: Yes

 ** updatedAt **   <a name="mediaconnect-Type-ListedRouterOutput-updatedAt"></a>
The timestamp when the router output was last updated.
Type: Timestamp
Required: Yes

 ** maintenanceSchedule **   <a name="mediaconnect-Type-ListedRouterOutput-maintenanceSchedule"></a>
The details of the maintenance schedule for the listed router output.
Type: [MaintenanceSchedule](API_MaintenanceSchedule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** maintenanceScheduleType **   <a name="mediaconnect-Type-ListedRouterOutput-maintenanceScheduleType"></a>
The type of maintenance schedule currently associated with the listed router output.
Type: String
Valid Values: `WINDOW`
Required: No

 ** networkInterfaceArn **   <a name="mediaconnect-Type-ListedRouterOutput-networkInterfaceArn"></a>
The ARN of the network interface associated with the router output.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: No

 ** routedInputArn **   <a name="mediaconnect-Type-ListedRouterOutput-routedInputArn"></a>
The ARN of the router input associated with the output.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerInput:[a-z0-9]{12}`
Required: No

## See Also
<a name="API_ListedRouterOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListedRouterOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListedRouterOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListedRouterOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
