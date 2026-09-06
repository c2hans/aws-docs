---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterInput.html
---

# RouterInput
<a name="API_RouterInput"></a>

A router input in AWS Elemental MediaConnect. A router input is a source of media content that can be routed to one or more router outputs.

## Contents
<a name="API_RouterInput_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-RouterInput-arn"></a>
The Amazon Resource Name (ARN) of the router input.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerInput:[a-z0-9]{12}`
Required: Yes

 ** availabilityZone **   <a name="mediaconnect-Type-RouterInput-availabilityZone"></a>
The Availability Zone of the router input.
Type: String
Required: Yes

 ** configuration **   <a name="mediaconnect-Type-RouterInput-configuration"></a>
The configuration settings for a router input.
Type: [RouterInputConfiguration](API_RouterInputConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** contentQualityAnalysisConfiguration **   <a name="mediaconnect-Type-RouterInput-contentQualityAnalysisConfiguration"></a>
The content quality analysis configuration for the router input.
Type: [RouterContentQualityAnalysisConfiguration](API_RouterContentQualityAnalysisConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** contentQualityAnalysisType **   <a name="mediaconnect-Type-RouterInput-contentQualityAnalysisType"></a>
The type of content quality analysis applied to the router input.
Type: String
Valid Values: `CONTENT_LEVEL`
Required: Yes

 ** createdAt **   <a name="mediaconnect-Type-RouterInput-createdAt"></a>
The timestamp when the router input was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="mediaconnect-Type-RouterInput-id"></a>
The unique identifier of the router input.
Type: String
Required: Yes

 ** inputType **   <a name="mediaconnect-Type-RouterInput-inputType"></a>
The type of the router input.
Type: String
Valid Values: `STANDARD | FAILOVER | MERGE | MEDIACONNECT_FLOW | MEDIALIVE_CHANNEL`
Required: Yes

 ** maintenanceConfiguration **   <a name="mediaconnect-Type-RouterInput-maintenanceConfiguration"></a>
The maintenance configuration settings applied to this router input.
Type: [MaintenanceConfiguration](API_MaintenanceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** maintenanceType **   <a name="mediaconnect-Type-RouterInput-maintenanceType"></a>
The type of maintenance configuration applied to this router input.
Type: String
Valid Values: `PREFERRED_DAY_TIME | DEFAULT`
Required: Yes

 ** maximumBitrate **   <a name="mediaconnect-Type-RouterInput-maximumBitrate"></a>
The maximum bitrate for the router input.
Type: Long
Required: Yes

 ** messages **   <a name="mediaconnect-Type-RouterInput-messages"></a>
The messages associated with the router input.
Type: Array of [RouterInputMessage](API_RouterInputMessage.md) objects
Required: Yes

 ** name **   <a name="mediaconnect-Type-RouterInput-name"></a>
The name of the router input.
Type: String
Required: Yes

 ** regionName **   <a name="mediaconnect-Type-RouterInput-regionName"></a>
The AWS Region where the router input is located.
Type: String
Required: Yes

 ** routedOutputs **   <a name="mediaconnect-Type-RouterInput-routedOutputs"></a>
The number of router outputs associated with the router input.
Type: Integer
Required: Yes

 ** routingScope **   <a name="mediaconnect-Type-RouterInput-routingScope"></a>
Indicates whether the router input is configured for Regional or global routing.
Type: String
Valid Values: `REGIONAL | GLOBAL`
Required: Yes

 ** state **   <a name="mediaconnect-Type-RouterInput-state"></a>
The current state of the router input.
Type: String
Valid Values: `CREATING | STANDBY | STARTING | ACTIVE | STOPPING | DELETING | UPDATING | ERROR | RECOVERING | MIGRATING`
Required: Yes

 ** streamDetails **   <a name="mediaconnect-Type-RouterInput-streamDetails"></a>
Configuration details for the router input stream.
Type: [RouterInputStreamDetails](API_RouterInputStreamDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** tags **   <a name="mediaconnect-Type-RouterInput-tags"></a>
Key-value pairs that can be used to tag and organize this router input.
Type: String to string map
Required: Yes

 ** tier **   <a name="mediaconnect-Type-RouterInput-tier"></a>
The tier level of the router input.
Type: String
Valid Values: `INPUT_100 | INPUT_50 | INPUT_20`
Required: Yes

 ** transitEncryption **   <a name="mediaconnect-Type-RouterInput-transitEncryption"></a>
The transit encryption settings for a router input.
Type: [RouterInputTransitEncryption](API_RouterInputTransitEncryption.md) object
Required: Yes

 ** updatedAt **   <a name="mediaconnect-Type-RouterInput-updatedAt"></a>
The timestamp when the router input was last updated.
Type: Timestamp
Required: Yes

 ** ipAddress **   <a name="mediaconnect-Type-RouterInput-ipAddress"></a>
The IP address of the router input.
Type: String
Required: No

 ** maintenanceSchedule **   <a name="mediaconnect-Type-RouterInput-maintenanceSchedule"></a>
The current maintenance schedule details for this router input.
Type: [MaintenanceSchedule](API_MaintenanceSchedule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** maintenanceScheduleType **   <a name="mediaconnect-Type-RouterInput-maintenanceScheduleType"></a>
The type of maintenance schedule currently in effect for this router input.
Type: String
Valid Values: `WINDOW`
Required: No

 ** maximumRoutedOutputs **   <a name="mediaconnect-Type-RouterInput-maximumRoutedOutputs"></a>
The maximum number of outputs that can be simultaneously routed to this input.
Type: Integer
Required: No

## See Also
<a name="API_RouterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterInput)
