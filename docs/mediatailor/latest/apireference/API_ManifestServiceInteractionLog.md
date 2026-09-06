---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ManifestServiceInteractionLog.html
---

# ManifestServiceInteractionLog
<a name="API_ManifestServiceInteractionLog"></a>

Settings for customizing what events are included in logs for interactions with the origin server.

For more information about manifest service logs, including descriptions of the event types, see [MediaTailor manifest logs description and event types](https://docs.aws.amazon.com/mediatailor/latest/ug/log-types.html) in AWS Elemental MediaTailor User Guide.

## Contents
<a name="API_ManifestServiceInteractionLog_Contents"></a>

 ** ExcludeEventTypes **   <a name="mediatailor-Type-ManifestServiceInteractionLog-ExcludeEventTypes"></a>
Indicates that MediaTailor won't emit the selected events in the logs for playback sessions that are initialized with this configuration.
Type: Array of strings
Valid Values: `GENERATED_MANIFEST | ORIGIN_MANIFEST | SESSION_INITIALIZED | TRACKING_RESPONSE | CONFIG_SYNTAX_ERROR | CONFIG_SECURITY_ERROR | UNKNOWN_HOST | TIMEOUT_ERROR | CONNECTION_ERROR | IO_ERROR | UNKNOWN_ERROR | HOST_DISALLOWED | PARSING_ERROR | MANIFEST_ERROR | NO_MASTER_OR_MEDIA_PLAYLIST | NO_MASTER_PLAYLIST | NO_MEDIA_PLAYLIST | INCOMPATIBLE_HLS_VERSION | SCTE35_PARSING_ERROR | INVALID_SINGLE_PERIOD_DASH_MANIFEST | UNSUPPORTED_SINGLE_PERIOD_DASH_MANIFEST | LAST_PERIOD_MISSING_AUDIO | LAST_PERIOD_MISSING_AUDIO_WARNING | ERROR_ORIGIN_PREFIX_INTERPOLATION | ERROR_ADS_INTERPOLATION | ERROR_LIVE_PRE_ROLL_ADS_INTERPOLATION | ERROR_CDN_AD_SEGMENT_INTERPOLATION | ERROR_CDN_CONTENT_SEGMENT_INTERPOLATION | ERROR_SLATE_AD_URL_INTERPOLATION | ERROR_PROFILE_NAME_INTERPOLATION | ERROR_BUMPER_START_INTERPOLATION | ERROR_BUMPER_END_INTERPOLATION | PRE_SESSION_INIT_HOOK_ERROR | PRE_SESSION_INIT_FUNCTION_ERROR`
Required: No

 ** PublishOptInEventTypes **   <a name="mediatailor-Type-ManifestServiceInteractionLog-PublishOptInEventTypes"></a>
Indicates that MediaTailor will emit the selected events in the logs for playback sessions that are initialized with this configuration. These events are not emitted by default and must be explicitly opted in.
Type: Array of strings
Valid Values: `PRE_SESSION_INIT_HOOK_SUMMARY | PRE_SESSION_INIT_FUNCTION_COMPLETED`
Required: No

## See Also
<a name="API_ManifestServiceInteractionLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ManifestServiceInteractionLog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ManifestServiceInteractionLog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ManifestServiceInteractionLog)
