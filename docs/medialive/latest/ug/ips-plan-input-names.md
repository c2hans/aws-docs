---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/ips-plan-input-names.html
---

# Plan the input and input attachment names
<a name="ips-plan-input-names"></a>

You should plan the names for the input and the input attachment. Here are some tips:
+ Use the same name for the input and input attachments.
+ Include an indicator of whether the entity is static or dynamic.
+ For a static input, include either the name of the video source or a description of the video source.
+ For a dynamic input, include an indicator of its characteristics, which you determined in step 2. Doing so ensures that you do not attach an unsuitable video source when you specify the URI in the input switch action.

For example, for a static input:
+ `static-filler`
+ `static-live-studio-feed`

For example, for a dynamic input:
+ `dynamic-s3-preroll-bucket-embedded-EN-FR-ES-DE`
+ `dynamic-s3-preroll-bucket-embedded-FR-ES-DE-EN`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
