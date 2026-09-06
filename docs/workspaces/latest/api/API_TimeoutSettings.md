---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_TimeoutSettings.html
---

# TimeoutSettings
<a name="API_TimeoutSettings"></a>

Describes the timeout settings for a pool of WorkSpaces.

## Contents
<a name="API_TimeoutSettings_Contents"></a>

 ** DisconnectTimeoutInSeconds **   <a name="WorkSpaces-Type-TimeoutSettings-DisconnectTimeoutInSeconds"></a>
Specifies the amount of time, in seconds, that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within the time set, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 36000.
Required: No

 ** IdleDisconnectTimeoutInSeconds **   <a name="WorkSpaces-Type-TimeoutSettings-IdleDisconnectTimeoutInSeconds"></a>
The amount of time in seconds a connection will stay active while idle.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 36000.
Required: No

 ** MaxUserDurationInSeconds **   <a name="WorkSpaces-Type-TimeoutSettings-MaxUserDurationInSeconds"></a>
Specifies the maximum amount of time, in seconds, that a streaming session can remain active. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.
Type: Integer
Valid Range: Minimum value of 600. Maximum value of 432000.
Required: No

## See Also
<a name="API_TimeoutSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/TimeoutSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/TimeoutSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/TimeoutSettings)
