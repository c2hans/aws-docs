---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterOutput.html
---

# RouterOutput
<a name="API_RouterOutput"></a>

A router output in AWS Elemental MediaConnect. A router output is a destination for media content that can receive input from one or more router inputs.

## Contents
<a name="API_RouterOutput_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-RouterOutput-arn"></a>
The Amazon Resource Name (ARN) of the router output.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerOutput:[a-z0-9]{12}`
Required: Yes

 ** availabilityZone **   <a name="mediaconnect-Type-RouterOutput-availabilityZone"></a>
The Availability Zone of the router output.
Type: String
Required: Yes

 ** configuration **   <a name="mediaconnect-Type-RouterOutput-configuration"></a>
The configuration settings for a router output.
Type: [RouterOutputConfiguration](API_RouterOutputConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** createdAt **   <a name="mediaconnect-Type-RouterOutput-createdAt"></a>
The timestamp when the router output was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="mediaconnect-Type-RouterOutput-id"></a>
The unique identifier of the router output.
Type: String
Required: Yes

 ** maintenanceConfiguration **   <a name="mediaconnect-Type-RouterOutput-maintenanceConfiguration"></a>
The maintenance configuration settings applied to this router output.
Type: [MaintenanceConfiguration](API_MaintenanceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** maintenanceType **   <a name="mediaconnect-Type-RouterOutput-maintenanceType"></a>
The type of maintenance configuration applied to this router output.
Type: String
Valid Values: `PREFERRED_DAY_TIME | DEFAULT`
Required: Yes

 ** maximumBitrate **   <a name="mediaconnect-Type-RouterOutput-maximumBitrate"></a>
The maximum bitrate for the router output.
Type: Long
Required: Yes

 ** messages **   <a name="mediaconnect-Type-RouterOutput-messages"></a>
The messages associated with the router output.
Type: Array of [RouterOutputMessage](API_RouterOutputMessage.md) objects
Required: Yes

 ** name **   <a name="mediaconnect-Type-RouterOutput-name"></a>
The name of the router output.
Type: String
Required: Yes

 ** outputType **   <a name="mediaconnect-Type-RouterOutput-outputType"></a>
The type of the router output.
Type: String
Valid Values: `STANDARD | MEDIACONNECT_FLOW | MEDIALIVE_INPUT`
Required: Yes

 ** regionName **   <a name="mediaconnect-Type-RouterOutput-regionName"></a>
The AWS Region where the router output is located.
Type: String
Required: Yes

 ** routedState **   <a name="mediaconnect-Type-RouterOutput-routedState"></a>
The current state of the association between the router output and its input.
Type: String
Valid Values: `ROUTED | ROUTING | UNROUTED`
Required: Yes

 ** routingScope **   <a name="mediaconnect-Type-RouterOutput-routingScope"></a>
Indicates whether the router output is configured for Regional or global routing.
Type: String
Valid Values: `REGIONAL | GLOBAL`
Required: Yes

 ** state **   <a name="mediaconnect-Type-RouterOutput-state"></a>
The overall state of the router output.
Type: String
Valid Values: `CREATING | STANDBY | STARTING | ACTIVE | STOPPING | DELETING | UPDATING | ERROR | RECOVERING | MIGRATING`
Required: Yes

 ** streamDetails **   <a name="mediaconnect-Type-RouterOutput-streamDetails"></a>
Information about the router output's stream, including connection state and destination details. The specific details provided vary based on the router output type.
Type: [RouterOutputStreamDetails](API_RouterOutputStreamDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** tags **   <a name="mediaconnect-Type-RouterOutput-tags"></a>
Key-value pairs that can be used to tag and organize this router output.
Type: String to string map
Required: Yes

 ** tier **   <a name="mediaconnect-Type-RouterOutput-tier"></a>
The tier level of the router output.
Type: String
Valid Values: `OUTPUT_100 | OUTPUT_50 | OUTPUT_20`
Required: Yes

 ** updatedAt **   <a name="mediaconnect-Type-RouterOutput-updatedAt"></a>
The timestamp when the router output was last updated.
Type: Timestamp
Required: Yes

 ** ipAddress **   <a name="mediaconnect-Type-RouterOutput-ipAddress"></a>
The IP address of the router output.
Type: String
Required: No

 ** maintenanceSchedule **   <a name="mediaconnect-Type-RouterOutput-maintenanceSchedule"></a>
The current maintenance schedule details for this router output.
Type: [MaintenanceSchedule](API_MaintenanceSchedule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** maintenanceScheduleType **   <a name="mediaconnect-Type-RouterOutput-maintenanceScheduleType"></a>
The type of maintenance schedule currently in effect for this router output.
Type: String
Valid Values: `WINDOW`
Required: No

 ** routedInputArn **   <a name="mediaconnect-Type-RouterOutput-routedInputArn"></a>
The Amazon Resource Name (ARN) of the router input associated with the output.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerInput:[a-z0-9]{12}`
Required: No

## See Also
<a name="API_RouterOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterOutput)
