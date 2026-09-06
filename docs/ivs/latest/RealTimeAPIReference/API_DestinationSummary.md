---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DestinationSummary.html
---

# DestinationSummary
<a name="API_DestinationSummary"></a>

Summary information about a Destination.

## Contents
<a name="API_DestinationSummary_Contents"></a>

 ** id **   <a name="ivsrealtimeeapireference-Type-DestinationSummary-id"></a>
Unique identifier for this destination, assigned by IVS.
Type: String
Required: Yes

 ** state **   <a name="ivsrealtimeeapireference-Type-DestinationSummary-state"></a>
State of the Composition Destination.
Type: String
Valid Values: `STARTING | ACTIVE | STOPPING | RECONNECTING | FAILED | STOPPED`
Required: Yes

 ** endTime **   <a name="ivsrealtimeeapireference-Type-DestinationSummary-endTime"></a>
UTC time of the destination end. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

 ** startTime **   <a name="ivsrealtimeeapireference-Type-DestinationSummary-startTime"></a>
UTC time of the destination start. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

## See Also
<a name="API_DestinationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/DestinationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/DestinationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/DestinationSummary)
