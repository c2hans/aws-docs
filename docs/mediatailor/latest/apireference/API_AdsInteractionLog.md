---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdsInteractionLog.html
---

# AdsInteractionLog
<a name="API_AdsInteractionLog"></a>

Settings for customizing what events are included in logs for interactions with the ad decision server (ADS).

For more information about ADS logs, inlcuding descriptions of the event types, see [MediaTailor ADS logs description and event types](https://docs.aws.amazon.com/mediatailor/latest/ug/ads-log-format.html) in AWS Elemental MediaTailor User Guide.

## Contents
<a name="API_AdsInteractionLog_Contents"></a>

 ** ExcludeEventTypes **   <a name="mediatailor-Type-AdsInteractionLog-ExcludeEventTypes"></a>
Indicates that MediaTailor won't emit the selected events in the logs for playback sessions that are initialized with this configuration.
Type: Array of strings
Valid Values: `AD_MARKER_FOUND | NON_AD_MARKER_FOUND | MAKING_ADS_REQUEST | MODIFIED_TARGET_URL | VAST_REDIRECT | EMPTY_VAST_RESPONSE | EMPTY_VMAP_RESPONSE | VAST_RESPONSE | REDIRECTED_VAST_RESPONSE | FILLED_AVAIL | FILLED_OVERLAY_AVAIL | BEACON_FIRED | WARNING_NO_ADVERTISEMENTS | WARNING_VPAID_AD_DROPPED | WARNING_URL_VARIABLE_SUBSTITUTION_FAILED | ERROR_UNKNOWN | ERROR_UNKNOWN_HOST | ERROR_DISALLOWED_HOST | ERROR_ADS_IO | ERROR_ADS_TIMEOUT | ERROR_ADS_RESPONSE_PARSE | ERROR_ADS_RESPONSE_UNKNOWN_ROOT_ELEMENT | ERROR_ADS_INVALID_RESPONSE | ERROR_VAST_REDIRECT_EMPTY_RESPONSE | ERROR_VAST_REDIRECT_MULTIPLE_VAST | ERROR_VAST_REDIRECT_FAILED | ERROR_VAST_MISSING_MEDIAFILES | ERROR_VAST_MISSING_CREATIVES | ERROR_VAST_MISSING_OVERLAYS | ERROR_VAST_MISSING_IMPRESSION | ERROR_VAST_INVALID_VAST_AD_TAG_URI | ERROR_VAST_MULTIPLE_TRACKING_EVENTS | ERROR_VAST_MULTIPLE_LINEAR | ERROR_VAST_INVALID_MEDIA_FILE | ERROR_FIRING_BEACON_FAILED | ERROR_PERSONALIZATION_DISABLED | VOD_TIME_BASED_AVAIL_PLAN_VAST_RESPONSE_FOR_OFFSET | VOD_TIME_BASED_AVAIL_PLAN_SUCCESS | VOD_TIME_BASED_AVAIL_PLAN_WARNING_NO_ADVERTISEMENTS | INTERSTITIAL_VOD_SUCCESS | INTERSTITIAL_VOD_FAILURE | PRE_ADS_REQUEST_HOOK_ERROR | PRE_ADS_REQUEST_FUNCTION_ERROR`
Required: No

 ** PublishOptInEventTypes **   <a name="mediatailor-Type-AdsInteractionLog-PublishOptInEventTypes"></a>
Indicates that MediaTailor emits `RAW_ADS_RESPONSE` logs for playback sessions that are initialized with this configuration.
Type: Array of strings
Valid Values: `RAW_ADS_RESPONSE | RAW_ADS_REQUEST | PRE_ADS_REQUEST_HOOK_SUMMARY | PRE_ADS_REQUEST_FUNCTION_COMPLETED`
Required: No

## See Also
<a name="API_AdsInteractionLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/AdsInteractionLog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/AdsInteractionLog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/AdsInteractionLog)
