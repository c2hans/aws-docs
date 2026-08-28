---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/voice-analytics.html
---

# Using Amazon Chime SDK voice analytics
<a name="voice-analytics"></a>

The Amazon Chime SDK voice analytics feature enables you to implement speaker search and voice tone analysis. You use speaker search to identify and enroll new callers, and to identify repeat callers and assign a confidence score to those identifications. You use voice tone analysis to predict a caller's sentiment as `negative`, `neutral`, or `positive`.

You run voice analytics as an optional component of an Amazon Chime SDK call analytics session.

Voice analytics works with media insights pipelines or Amazon Chime SDK Voice Connectors calls. We recommend using the [ Media Pipelines SDK](media-pipelines.md) and invoking tasks on a media insights pipeline for finer grained control over, and information about, the tasks.

You can use Voice Connectors to ensure backward compatibility, but we only update the media insights pipeline APIs with new features.

For more information about creating and using Voice Connectors, see [ Managing Amazon Chime SDK Voice Connectors ](https://docs.aws.amazon.com/chime-sdk/latest/ag/voice-connectors.html) in the *Amazon Chime SDK Administrator Guide*.

Voice analytics also provides:
+ Asynchronous task processing. Tasks run independently from each other.
+ Control over when you process insights.

You can initiate voice analytics by calling the [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartSpeakerSearchTask.html) and [StartVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartVoiceToneAnalysisTask.html) APIs.

The following topics explain how to use voice analytics.

**Topics**
+ [Understanding voice analytics architecture for the Amazon Chime SDK](va-architecture.md)
+ [Understanding speaker search workflow for the Amazon Chime SDK](va-data-flow.md)
+ [Sample voice tone analysis workflow for the Amazon Chime SDK](va-tone-flow.md)
+ [Polling for task results for the Amazon Chime SDK](va-task-result-poll.md)
+ [Understanding notifications for the Amazon Chime SDK](va-notification-targets.md)
+ [Understanding data storage, opt-out, and data-retention policies for the Amazon Chime SDK](va-opt-out.md)
+ [Using voice APIs to run voice analytics for the Amazon Chime SDK](va-in-voice-namespace.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
