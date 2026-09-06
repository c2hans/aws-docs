---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CapacityStatus.html
---

# CapacityStatus
<a name="API_CapacityStatus"></a>

Describes the capacity status for a pool of WorkSpaces.

## Contents
<a name="API_CapacityStatus_Contents"></a>

 ** ActiveUserSessions **   <a name="WorkSpaces-Type-CapacityStatus-ActiveUserSessions"></a>
The number of user sessions currently being used for your pool.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** ActualUserSessions **   <a name="WorkSpaces-Type-CapacityStatus-ActualUserSessions"></a>
The total number of user sessions that are available for streaming or are currently streaming in your pool.
ActualUserSessions = AvailableUserSessions \+ ActiveUserSessions
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** AvailableUserSessions **   <a name="WorkSpaces-Type-CapacityStatus-AvailableUserSessions"></a>
The number of user sessions currently available for streaming from your pool.
AvailableUserSessions = ActualUserSessions - ActiveUserSessions
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** DesiredUserSessions **   <a name="WorkSpaces-Type-CapacityStatus-DesiredUserSessions"></a>
The total number of sessions slots that are either running or pending. This represents the total number of concurrent streaming sessions your pool can support in a steady state.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_CapacityStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CapacityStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CapacityStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CapacityStatus)
