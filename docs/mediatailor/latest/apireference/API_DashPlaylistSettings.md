---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DashPlaylistSettings.html
---

# DashPlaylistSettings
<a name="API_DashPlaylistSettings"></a>

Dash manifest configuration parameters.

## Contents
<a name="API_DashPlaylistSettings_Contents"></a>

 ** ManifestWindowSeconds **   <a name="mediatailor-Type-DashPlaylistSettings-ManifestWindowSeconds"></a>
The total duration (in seconds) of each manifest. Minimum value: `30` seconds. Maximum value: `3600` seconds.
Type: Integer
Required: No

 ** MinBufferTimeSeconds **   <a name="mediatailor-Type-DashPlaylistSettings-MinBufferTimeSeconds"></a>
Minimum amount of content (measured in seconds) that a player must keep available in the buffer. Minimum value: `2` seconds. Maximum value: `60` seconds.
Type: Integer
Required: No

 ** MinUpdatePeriodSeconds **   <a name="mediatailor-Type-DashPlaylistSettings-MinUpdatePeriodSeconds"></a>
Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest. Minimum value: `2` seconds. Maximum value: `60` seconds.
Type: Integer
Required: No

 ** SuggestedPresentationDelaySeconds **   <a name="mediatailor-Type-DashPlaylistSettings-SuggestedPresentationDelaySeconds"></a>
Amount of time (in seconds) that the player should be from the live point at the end of the manifest. Minimum value: `2` seconds. Maximum value: `60` seconds.
Type: Integer
Required: No

## See Also
<a name="API_DashPlaylistSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DashPlaylistSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DashPlaylistSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DashPlaylistSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
