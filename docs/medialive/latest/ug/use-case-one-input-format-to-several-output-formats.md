---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-input-format-to-several-output-formats.html
---

# Use case C: One input format converted to different formats, one format for each output
<a name="use-case-one-input-format-to-several-output-formats"></a>

In this use case for including captions in a MediaLive output, the input is set up with one format of captions and two or more languages. Assume that you want to produce several different types of output, and that in each output you want to convert the captions to a different format but include all the languages.

For example, the input has Teletext captions in Czech and Polish. You want to produce a Microsoft Smooth output and an HLS output. In the Microsoft Smooth output, you want to convert both captions to TTML. In the HLS output, you want to convert both captions to WebVTT.

![Flowchart showing input captions conversion to output captions for different streaming formats.](http://docs.aws.amazon.com/medialive/latest/ug/images/captions_INttext_OUT_OPmss_hls.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
