---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/accessibility-captions.html
---

# Settings for accessibility captions
<a name="accessibility-captions"></a>

When you create an HLS or CMAF HLS output and include an ISMC or WebVTT captions track, you can add accessibility attributes for captions to your output manifest. MediaConvert adds these attributes according to sections 4.5 and 4.6 of the [HLS authoring specification for Apple devices](https://developer.apple.com/documentation/http_live_streaming/hls_authoring_specification_for_apple_devices).

When you set **Accessibility subtitles** (`accessibility`) to **Enabled** (`ENABLED`), MediaConvert adds the following attributes to the captions track in the manifest under `EXT-X-MEDIA`: `CHARACTERISTICS="public.accessibility.describes-spoken-dialog,public.accessibility.describes-music-and-sound"` and `AUTOSELECT="YES"`.

Keep the default value, **Disabled** (`DISABLED`), if the captions track is not intended to provide such accessibility. MediaConvert will not add the attributes from the previous paragraph.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
