---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-hybrid-mode.html
---

# Hybrid mode with server-side ad beacons
<a name="ad-reporting-hybrid-mode"></a>

MediaTailor supports a hybrid mode for session tracking. In this mode, the service emits playback-related ad-tracking events, but makes the complete client-side tracking payload available for the session

To enable hybrid tracking using playback prefixes, from the player initialize a new MediaTailor playback session using a request in one of the following formats, according to your protocol:

**Example : HLS format**

```
POST master.m3u8
    {
        "adsParams": {
           "deviceType": "ipad"
       },
       "reportingMode":"server"
    }
```

**Example : DASH format**

```
POST manifest.mpd
    {
        "adsParams": {
           "deviceType": "ipad"
       },
       "reportingMode":"server"
    }
```

MediaTailor maintains the following tracking events in hybrid mode:
+ Impression
+ Start
+ First quartile
+ Midpoint
+ Third quartile
+ Complete
+ `breakStart` (vmap)
+ `breakEnd` (vmap)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
