---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListedRouterInput.html
---

# ListedRouterInput
<a name="API_ListedRouterInput"></a>

A summary of a router input, including its name, type, ARN, ID, state, and other key details. This structure is used in the response of the ListRouterInputs operation.

## Contents
<a name="API_ListedRouterInput_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-ListedRouterInput-arn"></a>
The Amazon Resource Name (ARN) of the router input.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerInput:[a-z0-9]{12}`
Required: Yes

 ** availabilityZone **   <a name="mediaconnect-Type-ListedRouterInput-availabilityZone"></a>
The Availability Zone of the router input.
Type: String
Required: Yes

 ** createdAt **   <a name="mediaconnect-Type-ListedRouterInput-createdAt"></a>
The timestamp when the router input was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="mediaconnect-Type-ListedRouterInput-id"></a>
The unique identifier of the router input.
Type: String
Required: Yes

 ** inputType **   <a name="mediaconnect-Type-ListedRouterInput-inputType"></a>
The type of the router input.
Type: String
Valid Values: `STANDARD | FAILOVER | MERGE | MEDIACONNECT_FLOW | MEDIALIVE_CHANNEL`
Required: Yes

 ** maximumBitrate **   <a name="mediaconnect-Type-ListedRouterInput-maximumBitrate"></a>
The maximum bitrate of the router input.
Type: Long
Required: Yes

 ** messageCount **   <a name="mediaconnect-Type-ListedRouterInput-messageCount"></a>
The number of messages associated with the router input.
Type: Integer
Required: Yes

 ** name **   <a name="mediaconnect-Type-ListedRouterInput-name"></a>
The name of the router input.
Type: String
Required: Yes

 ** regionName **   <a name="mediaconnect-Type-ListedRouterInput-regionName"></a>
The AWS Region where the router input is located.
Type: String
Required: Yes

 ** routedOutputs **   <a name="mediaconnect-Type-ListedRouterInput-routedOutputs"></a>
The number of router outputs that are associated with this router input.
Type: Integer
Required: Yes

 ** routingScope **   <a name="mediaconnect-Type-ListedRouterInput-routingScope"></a>
Indicates whether the router input is configured for Regional or global routing.
Type: String
Valid Values: `REGIONAL | GLOBAL`
Required: Yes

 ** state **   <a name="mediaconnect-Type-ListedRouterInput-state"></a>
The overall state of the router input.
Type: String
Valid Values: `CREATING | STANDBY | STARTING | ACTIVE | STOPPING | DELETING | UPDATING | ERROR | RECOVERING | MIGRATING`
Required: Yes

 ** updatedAt **   <a name="mediaconnect-Type-ListedRouterInput-updatedAt"></a>
The timestamp when the router input was last updated.
Type: Timestamp
Required: Yes

 ** maintenanceSchedule **   <a name="mediaconnect-Type-ListedRouterInput-maintenanceSchedule"></a>
The details of the maintenance schedule for the listed router input.
Type: [MaintenanceSchedule](API_MaintenanceSchedule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** maintenanceScheduleType **   <a name="mediaconnect-Type-ListedRouterInput-maintenanceScheduleType"></a>
The type of maintenance schedule currently associated with the listed router input.
Type: String
Valid Values: `WINDOW`
Required: No

 ** networkInterfaceArn **   <a name="mediaconnect-Type-ListedRouterInput-networkInterfaceArn"></a>
The ARN of the network interface associated with the router input.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: No

## See Also
<a name="API_ListedRouterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListedRouterInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListedRouterInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListedRouterInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
