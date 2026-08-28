---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/sgai-ad-tracking.html
---

# Ad tracking with SGAI
<a name="sgai-ad-tracking"></a>

SGAI supports both server-side and client-side ad tracking. You set the reporting mode at session initialization. The mode cannot change during the session.

Server-side tracking (default)
MediaTailor fires VAST beacons automatically when the player requests ad segments. Ad URIs in the asset list contain encrypted beacon metadata (`awsBeaconData`, `awsBeaconDomain`, `awsConfigurationName`). The player must support HLS `#EXT-X-DEFINE:QUERYPARAM` variable substitution. The asset list response does not include a `TRACKING` section.
For details about how SGAI server-side beaconing works, see [Server-side tracking with server-guided ad insertion (SGAI)](ad-reporting-server-side-sgai.md).

Client-side tracking
Add `aws.reportingMode=CLIENT` to your session initialization request. The asset list response includes a `TRACKING` section with beacon URLs that the player fires during ad playback. The `GetTracking` API endpoint is *not* used for SGAI sessions. Instead, each asset list response includes tracking data directly. The tracking data uses the same JSON schema as the server-side ad insertion (SSAI) tracking response.
For details, see [Server-guided ad insertion](ad-reporting-client-side.md#ad-reporting-client-side-best-practices-sgai).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
