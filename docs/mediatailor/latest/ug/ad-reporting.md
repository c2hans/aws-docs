---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting.html
---

# Reporting ad tracking data
<a name="ad-reporting"></a>

MediaTailor provides two options for tracking and reporting on how much of an ad a viewer has watched. In the server-side ad reporting approach, MediaTailor tracks the ad and sends beacons (tracking signals) directly to the ad server. Alternatively, in the client-side tracking approach, the client player (the user's device) tracks the ad and sends the beacons to the ad server. The type of ad reporting used in a playback session depends on the specific request the player makes to initiate the session in MediaTailor.

For information about passing session and player data to the ad server using dynamic variables, see [MediaTailor dynamic ad variables for ADS requests](variables.md). For details about session initialization parameters, see [MediaTailor manifest query parameters](manifest-query-parameters.md).

**Topics**
+ [MediaTailor server-side ad tracking and reporting](ad-reporting-server-side.md)
+ [Client-side ad tracking](ad-reporting-client-side.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
