---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ComputeCapacityStatus.html
---

# ComputeCapacityStatus
<a name="API_ComputeCapacityStatus"></a>

Describes the capacity status for a fleet.

## Contents
<a name="API_ComputeCapacityStatus_Contents"></a>

 ** Desired **   <a name="WorkSpacesApplications-Type-ComputeCapacityStatus-Desired"></a>
The desired number of streaming instances.
Type: Integer
Required: Yes

 ** ActiveUserSessions **   <a name="WorkSpacesApplications-Type-ComputeCapacityStatus-ActiveUserSessions"></a>
The number of user sessions currently being used for streaming sessions. This only applies to multi-session fleets.
Type: Integer
Required: No

 ** ActualUserSessions **   <a name="WorkSpacesApplications-Type-ComputeCapacityStatus-ActualUserSessions"></a>
The total number of session slots that are available for streaming or are currently streaming.
ActualUserSessionCapacity = AvailableUserSessionCapacity \+ ActiveUserSessions
This only applies to multi-session fleets.
Type: Integer
Required: No

 ** Available **   <a name="WorkSpacesApplications-Type-ComputeCapacityStatus-Available"></a>
The number of currently available instances that can be used to stream sessions.
Type: Integer
Required: No

 ** AvailableUserSessions **   <a name="WorkSpacesApplications-Type-ComputeCapacityStatus-AvailableUserSessions"></a>
The number of idle session slots currently available for user sessions.
AvailableUserSessionCapacity = ActualUserSessionCapacity - ActiveUserSessions
This only applies to multi-session fleets.
Type: Integer
Required: No

 ** DesiredUserSessions **   <a name="WorkSpacesApplications-Type-ComputeCapacityStatus-DesiredUserSessions"></a>
The total number of sessions slots that are either running or pending. This represents the total number of concurrent streaming sessions your fleet can support in a steady state.
DesiredUserSessionCapacity = ActualUserSessionCapacity \+ PendingUserSessionCapacity
This only applies to multi-session fleets.
Type: Integer
Required: No

 ** Draining **   <a name="WorkSpacesApplications-Type-ComputeCapacityStatus-Draining"></a>
The number of instances in drain mode. This only applies to multi-session fleets.
Type: Integer
Required: No

 ** DrainModeActiveUserSessions **   <a name="WorkSpacesApplications-Type-ComputeCapacityStatus-DrainModeActiveUserSessions"></a>
The number of active user sessions on instances in drain mode. This only applies to multi-session fleets.
Type: Integer
Required: No

 ** DrainModeUnusedUserSessions **   <a name="WorkSpacesApplications-Type-ComputeCapacityStatus-DrainModeUnusedUserSessions"></a>
The number of unused session slots on instances in drain mode that cannot be used for user session provisioning. This only applies to multi-session fleets.
Type: Integer
Required: No

 ** InUse **   <a name="WorkSpacesApplications-Type-ComputeCapacityStatus-InUse"></a>
The number of instances in use for streaming.
Type: Integer
Required: No

 ** Running **   <a name="WorkSpacesApplications-Type-ComputeCapacityStatus-Running"></a>
The total number of simultaneous streaming instances that are running.
Type: Integer
Required: No

## See Also
<a name="API_ComputeCapacityStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ComputeCapacityStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ComputeCapacityStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ComputeCapacityStatus)
