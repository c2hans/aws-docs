---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Destination.html
---

# Destination
<a name="API_Destination"></a>

Object specifying the status of a Destination.

## Contents
<a name="API_Destination_Contents"></a>

 ** configuration **   <a name="ivsrealtimeeapireference-Type-Destination-configuration"></a>
Configuration used to create this destination.
Type: [DestinationConfiguration](API_DestinationConfiguration.md) object
Required: Yes

 ** id **   <a name="ivsrealtimeeapireference-Type-Destination-id"></a>
Unique identifier for this destination, assigned by IVS.
Type: String
Required: Yes

 ** state **   <a name="ivsrealtimeeapireference-Type-Destination-state"></a>
State of the Composition Destination.
Type: String
Valid Values: `STARTING | ACTIVE | STOPPING | RECONNECTING | FAILED | STOPPED`
Required: Yes

 ** detail **   <a name="ivsrealtimeeapireference-Type-Destination-detail"></a>
Optional details regarding the status of the destination.
Type: [DestinationDetail](API_DestinationDetail.md) object
Required: No

 ** endTime **   <a name="ivsrealtimeeapireference-Type-Destination-endTime"></a>
UTC time of the destination end. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

 ** startTime **   <a name="ivsrealtimeeapireference-Type-Destination-startTime"></a>
UTC time of the destination start. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/Destination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
