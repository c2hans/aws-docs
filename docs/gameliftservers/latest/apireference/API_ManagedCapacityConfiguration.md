---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ManagedCapacityConfiguration.html
---

# ManagedCapacityConfiguration
<a name="API_ManagedCapacityConfiguration"></a>

Use ManagedCapacityConfiguration with the "SCALE\_TO\_AND\_FROM\_ZERO" ZeroCapacityStrategy to enable Amazon GameLift Servers to fully manage the MinSize value, switching between 0 and 1 based on game session activity. This is ideal for eliminating compute costs during periods of no game activity. It is particularly beneficial during development when you're away from your desk, iterating on builds for extended periods, in production environments serving low-traffic locations, or for games with long, predictable downtime windows. By automatically managing capacity between 0 and 1 instances, you avoid paying for idle instances while maintaining the ability to serve game sessions when demand arrives. Note that while scale-out is triggered immediately upon receiving a game session request, actual game session availability depends on your server process startup time, so this approach works best with multi-location Fleets where cold-start latency is tolerable. With a "MANUAL" ZeroCapacityStrategy Amazon GameLift Servers will not modify Fleet MinSize values automatically and will not scale out from zero instances in response to game sessions.

## Contents
<a name="API_ManagedCapacityConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ScaleInAfterInactivityMinutes **   <a name="gameliftservers-Type-ManagedCapacityConfiguration-ScaleInAfterInactivityMinutes"></a>
Length of time, in minutes, that Amazon GameLift Servers will wait before scaling in your MinSize and DesiredInstances to 0 after a period with no game session activity. Default: 30 minutes.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1440.
Required: No

 ** ZeroCapacityStrategy **   <a name="gameliftservers-Type-ManagedCapacityConfiguration-ZeroCapacityStrategy"></a>
The strategy Amazon GameLift Servers will use to automatically scale your capacity to and from zero instances in response to game session activity. Game session activity refers to any active running sessions or game session requests.
Possible ZeroCapacityStrategy types include:
+  **MANUAL** -- (default value) Amazon GameLift Servers will not update capacity to and from zero on your behalf.
+  **SCALE\_TO\_AND\_FROM\_ZERO** -- Amazon GameLift Servers will automatically scale out MinSize and DesiredInstances from 0 to 1 in response to a game session request, and will scale in MinSize and DesiredInstances to 0 after a period with no game session activity. The duration of this scale in period can be configured using ScaleInAfterInactivityMinutes.
Type: String
Valid Values: `MANUAL | SCALE_TO_AND_FROM_ZERO`
Required: No

## See Also
<a name="API_ManagedCapacityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ManagedCapacityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ManagedCapacityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ManagedCapacityConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
