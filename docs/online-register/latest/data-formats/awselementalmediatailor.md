---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awselementalmediatailor.html
---

# Data retrieval APIs for AWS Elemental MediaTailor
<a name="awselementalmediatailor"></a>

AWS Elemental MediaTailor provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="mediatailor-DescribeChannel"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname.html) | Retrieve the channel with the specified channel name | Read |
| <a name="mediatailor-DescribeLiveSource"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesource-livesourcename.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesource-livesourcename.html) | Retrieve the live source with the specified live source name on the source location with the specified source location name | Read |
| <a name="mediatailor-DescribeProgram"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-program-programname.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-program-programname.html) | Retrieve the program with the specified program name on the channel with the specified channel name | Read |
| <a name="mediatailor-DescribeSourceLocation"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname.html) | Retrieve the source location with the specified source location name | Read |
| <a name="mediatailor-DescribeVodSource"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsource-vodsourcename.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsource-vodsourcename.html) | Retrieve the VOD source with the specified VOD source name on the source location with the specified source location name | Read |
| <a name="mediatailor-GetChannelPolicy"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-policy.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-policy.html) | Read the IAM policy on the channel with the specified channel name | Read |
| <a name="mediatailor-GetChannelSchedule"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-schedule.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-schedule.html) | Retrieve the schedule of programs on the channel with the specified channel name | Read |
| <a name="mediatailor-GetPlaybackConfiguration"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfiguration-name.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfiguration-name.html) | Retrieve the configuration for the specified name | Read |
| <a name="mediatailor-GetPrefetchSchedule"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname-name.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname-name.html) | Retrieve prefetch schedule for a playback configuration with the specified prefetch schedule name | Read |
| <a name="mediatailor-ListAlerts"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/alerts.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/alerts.html) | Retrieve the list of alerts on a resource | Read |
| <a name="mediatailor-ListChannels"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/channels.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/channels.html) | Retrieve the list of existing channels | Read |
| <a name="mediatailor-ListLiveSources"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesources.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesources.html) | Retrieve the list of existing live sources on the source location with the specified source location name | Read |
| <a name="mediatailor-ListPlaybackConfigurations"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfigurations.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfigurations.html) | Retrieve the list of available configurations | List |
| <a name="mediatailor-ListPrefetchSchedules"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname.html) | Retrieve the list of prefetch schedules for a playback configuration | List |
| <a name="mediatailor-ListSourceLocations"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocations.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocations.html) | Retrieve the list of existing source locations | Read |
| <a name="mediatailor-ListTagsForResource"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/tags-resourcearn.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/tags-resourcearn.html) | List the tags assigned to the specified playback configuration resource | Read |
| <a name="mediatailor-ListVodSources"></a>[https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsources.html](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsources.html) | Retrieve the list of existing VOD sources on the source location with the specified source location name | Read |
