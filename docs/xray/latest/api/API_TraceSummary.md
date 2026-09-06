---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_TraceSummary.html
---

# TraceSummary
<a name="API_TraceSummary"></a>

Metadata generated from the segment documents in a trace.

## Contents
<a name="API_TraceSummary_Contents"></a>

 ** Annotations **   <a name="xray-Type-TraceSummary-Annotations"></a>
Annotations from the trace's segment documents.
Type: String to array of [ValueWithServiceIds](API_ValueWithServiceIds.md) objects map
Required: No

 ** AvailabilityZones **   <a name="xray-Type-TraceSummary-AvailabilityZones"></a>
A list of Availability Zones for any zone corresponding to the trace segments.
Type: Array of [AvailabilityZoneDetail](API_AvailabilityZoneDetail.md) objects
Required: No

 ** Duration **   <a name="xray-Type-TraceSummary-Duration"></a>
 The length of time in seconds between the start time of the earliest segment that started and the end time of the last segment that completed.
Type: Double
Required: No

 ** EntryPoint **   <a name="xray-Type-TraceSummary-EntryPoint"></a>
The root of a trace.
Type: [ServiceId](API_ServiceId.md) object
Required: No

 ** ErrorRootCauses **   <a name="xray-Type-TraceSummary-ErrorRootCauses"></a>
A collection of ErrorRootCause structures corresponding to the trace segments.
Type: Array of [ErrorRootCause](API_ErrorRootCause.md) objects
Required: No

 ** FaultRootCauses **   <a name="xray-Type-TraceSummary-FaultRootCauses"></a>
A collection of FaultRootCause structures corresponding to the trace segments.
Type: Array of [FaultRootCause](API_FaultRootCause.md) objects
Required: No

 ** HasError **   <a name="xray-Type-TraceSummary-HasError"></a>
The root segment document has a 400 series error.
Type: Boolean
Required: No

 ** HasFault **   <a name="xray-Type-TraceSummary-HasFault"></a>
The root segment document has a 500 series error.
Type: Boolean
Required: No

 ** HasThrottle **   <a name="xray-Type-TraceSummary-HasThrottle"></a>
One or more of the segment documents has a 429 throttling error.
Type: Boolean
Required: No

 ** Http **   <a name="xray-Type-TraceSummary-Http"></a>
Information about the HTTP request served by the trace.
Type: [Http](API_Http.md) object
Required: No

 ** Id **   <a name="xray-Type-TraceSummary-Id"></a>
The unique identifier for the request that generated the trace's segments and subsegments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 35.
Required: No

 ** InstanceIds **   <a name="xray-Type-TraceSummary-InstanceIds"></a>
A list of EC2 instance IDs for any instance corresponding to the trace segments.
Type: Array of [InstanceIdDetail](API_InstanceIdDetail.md) objects
Required: No

 ** IsPartial **   <a name="xray-Type-TraceSummary-IsPartial"></a>
One or more of the segment documents is in progress.
Type: Boolean
Required: No

 ** MatchedEventTime **   <a name="xray-Type-TraceSummary-MatchedEventTime"></a>
The matched time stamp of a defined event.
Type: Timestamp
Required: No

 ** ResourceARNs **   <a name="xray-Type-TraceSummary-ResourceARNs"></a>
A list of resource ARNs for any resource corresponding to the trace segments.
Type: Array of [ResourceARNDetail](API_ResourceARNDetail.md) objects
Required: No

 ** ResponseTime **   <a name="xray-Type-TraceSummary-ResponseTime"></a>
The length of time in seconds between the start and end times of the root segment. If the service performs work asynchronously, the response time measures the time before the response is sent to the user, while the duration measures the amount of time before the last traced activity completes.
Type: Double
Required: No

 ** ResponseTimeRootCauses **   <a name="xray-Type-TraceSummary-ResponseTimeRootCauses"></a>
A collection of ResponseTimeRootCause structures corresponding to the trace segments.
Type: Array of [ResponseTimeRootCause](API_ResponseTimeRootCause.md) objects
Required: No

 ** Revision **   <a name="xray-Type-TraceSummary-Revision"></a>
The revision number of a trace.
Type: Integer
Required: No

 ** ServiceIds **   <a name="xray-Type-TraceSummary-ServiceIds"></a>
Service IDs from the trace's segment documents.
Type: Array of [ServiceId](API_ServiceId.md) objects
Required: No

 ** StartTime **   <a name="xray-Type-TraceSummary-StartTime"></a>
The start time of a trace, based on the earliest trace segment start time.
Type: Timestamp
Required: No

 ** Users **   <a name="xray-Type-TraceSummary-Users"></a>
Users from the trace's segment documents.
Type: Array of [TraceUser](API_TraceUser.md) objects
Required: No

## See Also
<a name="API_TraceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/TraceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/TraceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/TraceSummary)
